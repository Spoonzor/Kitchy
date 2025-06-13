from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone
from django.contrib.auth.models import User
from accounts.models.household import Household, HouseholdMembership
from accounts.serializers.household import HouseholdSerializer, HouseholdMembershipSerializer

class HouseholdCreateView(generics.CreateAPIView):
    serializer_class = HouseholdSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        household = serializer.save(created_by=self.request.user)
        HouseholdMembership.objects.create(
            household=household,
            user=self.request.user,
            role='owner',
            status='accepted'
        )

class HouseholdInviteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, household_id):
        email = request.data.get('email')
        if not email:
            return Response({"error": "L'email est requis pour l'invitation."},
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            invited_user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"error": "Utilisateur non trouvé pour cet email."},
                            status=status.HTTP_404_NOT_FOUND)
        
        try:
            membership = HouseholdMembership.objects.get(household_id=household_id, user=request.user)
            if membership.role not in ('owner', 'admin'):
                return Response({"error": "Vous n'avez pas les droits pour inviter."},
                                status=status.HTTP_403_FORBIDDEN)
        except HouseholdMembership.DoesNotExist:
            return Response({"error": "Vous n'êtes pas membre de ce foyer."},
                            status=status.HTTP_403_FORBIDDEN)

        membership_invite, created = HouseholdMembership.objects.update_or_create(
            household_id=household_id,
            user=invited_user,
            defaults={'role': 'member', 'status': 'invited'}
        )
        serializer = HouseholdMembershipSerializer(membership_invite)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class AcceptInvitationView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        token = request.data.get('invitation_token')
        if not token:
            return Response({"error": "Token d'invitation requis."},
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            membership = HouseholdMembership.objects.get(invitation_token=token, user=request.user)
            if membership.status == 'accepted':
                return Response({"message": "Invitation déjà acceptée."}, status=status.HTTP_200_OK)
            membership.status = 'accepted'
            membership.accepted_at = timezone.now()
            membership.save()
            return Response({"message": "Invitation acceptée avec succès."}, status=status.HTTP_200_OK)
        except HouseholdMembership.DoesNotExist:
            return Response({"error": "Invitation non trouvée ou non valide."},
                            status=status.HTTP_404_NOT_FOUND)

class HouseholdListView(generics.ListAPIView):
    """
    Retourne les households où l'utilisateur est membre et a accepté l'invitation.
    """
    serializer_class = HouseholdSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Household.objects.filter(
            memberships__user=self.request.user,
            memberships__status='accepted'
        )