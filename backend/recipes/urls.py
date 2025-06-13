from django.urls import path
from .views import (
    RecipeListCreateView, 
    RecipeDetailView, 
    FavoriteRecipeListCreateView, 
    FavoriteRecipeDetailView, 
    RecipeRecommendationView
)

urlpatterns = [
    path('', RecipeListCreateView.as_view(), name='recipe_list_create'),
    path('<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('favorites/', FavoriteRecipeListCreateView.as_view(), name='favorite_recipe_list_create'),
    path('favorites/<int:pk>/', FavoriteRecipeDetailView.as_view(), name='favorite_recipe_detail'),
    path('recommendations/', RecipeRecommendationView.as_view(), name='recipe_recommendations'),
]
