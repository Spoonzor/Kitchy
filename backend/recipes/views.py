from rest_framework import generics, permissions
from django.db.models import Q
from .models import Recipe, FavoriteRecipe
from .serializers import RecipeSerializer, FavoriteRecipeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import get_recipe_recommendations_enhanced

class RecipeListCreateView(generics.ListCreateAPIView):
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Recipe.objects.filter(Q(is_public=True) | Q(created_by=self.request.user))

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class RecipeDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Recipe.objects.all()

class FavoriteRecipeListCreateView(generics.ListCreateAPIView):
    serializer_class = FavoriteRecipeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return FavoriteRecipe.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        recipe_id = self.request.data.get('recipe')
        from recipes.models import Recipe
        recipe = Recipe.objects.get(id=recipe_id)
        serializer.save(user=self.request.user, recipe=recipe)

class FavoriteRecipeDetailView(generics.DestroyAPIView):
    serializer_class = FavoriteRecipeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return FavoriteRecipe.objects.filter(user=self.request.user)

class RecipeRecommendationView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        recommendations = get_recipe_recommendations_enhanced(request.user)
        data = [{
            "recipe": {
                "id": rec["recipe"].id,
                "title": rec["recipe"].title,
                "description": rec["recipe"].description,
            },
            "match_percentage": rec["match_percentage"],
            "missing_ingredients": rec["missing_ingredients"]
        } for rec in recommendations]
        return Response(data)
