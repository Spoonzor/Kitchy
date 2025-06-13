from rest_framework import serializers
from .models import Recipe, FavoriteRecipe

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'
        read_only_fields = ('created_by', 'created_at', 'updated_at')

class FavoriteRecipeSerializer(serializers.ModelSerializer):
    recipe = RecipeSerializer(read_only=True)
    
    class Meta:
        model = FavoriteRecipe
        fields = '__all__'
        read_only_fields = ('user', 'created_at')
