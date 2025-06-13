from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    ingredients = models.TextField(help_text="Liste des ingrédients séparés par des virgules")
    instructions = models.TextField(help_text="Étapes de préparation")
    created_by = models.ForeignKey(User, related_name='recipes', on_delete=models.CASCADE)
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class FavoriteRecipe(models.Model):
    user = models.ForeignKey(User, related_name='favorite_recipes', on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, related_name='favorited_by', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'recipe')
