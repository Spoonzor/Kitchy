from rest_framework import generics, permissions
from .models import ShoppingList, ShoppingListItem
from .serializers import ShoppingListSerializer, ShoppingListItemSerializer
from .utils import send_shopping_notification

class ShoppingListListCreateView(generics.ListCreateAPIView):
    serializer_class = ShoppingListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ShoppingList.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ShoppingListDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ShoppingListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ShoppingList.objects.filter(user=self.request.user)

class ShoppingListItemListCreateView(generics.ListCreateAPIView):
    serializer_class = ShoppingListItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        list_id = self.kwargs.get('list_id')
        return ShoppingListItem.objects.filter(shopping_list__id=list_id, shopping_list__user=self.request.user)

    def perform_create(self, serializer):
        list_id = self.kwargs.get('list_id')
        from shopping.models import ShoppingList
        shopping_list = ShoppingList.objects.get(id=list_id, user=self.request.user)
        instance = serializer.save(shopping_list=shopping_list)
        send_shopping_notification(self.request.user.id, instance.product_name)

class ShoppingListItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ShoppingListItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ShoppingListItem.objects.filter(shopping_list__user=self.request.user)
