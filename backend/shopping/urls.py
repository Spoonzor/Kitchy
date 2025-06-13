from django.urls import path
from .views import (
    ShoppingListListCreateView, 
    ShoppingListDetailView,
    ShoppingListItemListCreateView, 
    ShoppingListItemDetailView
)

urlpatterns = [
    path('', ShoppingListListCreateView.as_view(), name='shopping_list_list_create'),
    path('<int:pk>/', ShoppingListDetailView.as_view(), name='shopping_list_detail'),
    path('<int:list_id>/items/', ShoppingListItemListCreateView.as_view(), name='shopping_list_item_list_create'),
    path('items/<int:pk>/', ShoppingListItemDetailView.as_view(), name='shopping_list_item_detail'),
]
