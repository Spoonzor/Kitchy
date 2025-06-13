from rest_framework import serializers
from accounts.models.household import Household, HouseholdMembership

class HouseholdMembershipSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = HouseholdMembership
        fields = ['id', 'user', 'role', 'status', 'invitation_token', 'invited_at', 'accepted_at']
        read_only_fields = ['invitation_token', 'invited_at', 'accepted_at', 'user']

class HouseholdSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)
    memberships = HouseholdMembershipSerializer(many=True, read_only=True)

    class Meta:
        model = Household
        fields = ['id', 'name', 'created_by', 'created_at', 'updated_at', 'memberships']
        read_only_fields = ['created_by', 'created_at', 'updated_at', 'memberships']
