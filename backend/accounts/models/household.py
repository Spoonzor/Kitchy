import uuid
from django.db import models
from django.contrib.auth.models import User

ROLE_CHOICES = (
    ('owner', 'Propriétaire'),
    ('admin', 'Administrateur'),
    ('member', 'Membre'),
)

STATUS_CHOICES = (
    ('invited', 'Invité'),
    ('accepted', 'Accepté'),
    ('declined', 'Déclinée'),
)

class Household(models.Model):
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(
        User, related_name='created_households',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class HouseholdMembership(models.Model):
    household = models.ForeignKey(
        Household, related_name='memberships', on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User, related_name='household_memberships', on_delete=models.CASCADE
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='member')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='invited')
    invitation_token = models.UUIDField(default=uuid.uuid4, editable=False)
    invited_at = models.DateTimeField(auto_now_add=True)
    accepted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('household', 'user')

    def __str__(self):
        return f"{self.user.username} dans {self.household.name} ({self.role})"
