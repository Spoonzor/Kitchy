from django.urls import path
from .views import InventoryItemListCreateView, InventoryItemDetailView

urlpatterns = [
    path('', InventoryItemListCreateView.as_view(), name='inventory_list_create'),
    path('<int:pk>/', InventoryItemDetailView.as_view(), name='inventory_detail'),
]
