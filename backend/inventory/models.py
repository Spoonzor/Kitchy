from django.db import models
from django.contrib.auth.models import User
from accounts.models.household import Household  # Assurez-vous que ce chemin est correct

class InventoryItem(models.Model):
    owner = models.ForeignKey(User, related_name='inventory_items', on_delete=models.CASCADE)
    household = models.ForeignKey(Household, related_name='inventory_items', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    quantity = models.IntegerField(default=1)
    expiration_date = models.DateField(null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    barcode = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
