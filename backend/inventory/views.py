from rest_framework import generics, permissions
from .models import InventoryItem
from .serializers import InventoryItemSerializer

class InventoryItemListCreateView(generics.ListCreateAPIView):
    serializer_class = InventoryItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        membership = self.request.user.household_memberships.filter(status='accepted').first()
        if membership:
            return InventoryItem.objects.filter(household=membership.household)
        return InventoryItem.objects.filter(owner=self.request.user)
    def perform_create(self, serializer):
        membership = self.request.user.household_memberships.filter(status='accepted').first()
        if membership:
            serializer.save(owner=self.request.user, household=membership.household)
        else:
            serializer.save(owner=self.request.user)

class InventoryItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InventoryItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        membership = self.request.user.household_memberships.filter(status='accepted').first()
        if membership:
            return InventoryItem.objects.filter(household=membership.household)
        return InventoryItem.objects.filter(owner=self.request.user)
