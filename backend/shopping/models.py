from django.db import models
from django.contrib.auth.models import User

class ShoppingList(models.Model):
    user = models.ForeignKey(User, related_name='shopping_lists', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, default="Ma liste d'épicerie")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class ShoppingListItem(models.Model):
    shopping_list = models.ForeignKey(ShoppingList, related_name='items', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    quantity = models.IntegerField(default=1)
    purchased = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name
