# backend/kitchen_app/views/debug.py

from django.http import JsonResponse
from django.contrib.auth.models import User
from inventory.models import InventoryItem
from recipes.models import Recipe

def debug_view(request):
    """
    Vue de debug qui retourne des informations de base sur l'état de l'application.
    """
    try:
        user_count = User.objects.count()
        inventory_count = InventoryItem.objects.count()
        recipe_count = Recipe.objects.count()
        db_status = "ok"
    except Exception as e:
        user_count = inventory_count = recipe_count = "error"
        db_status = str(e)
    
    data = {
        "status": "online",
        "db_status": db_status,
        "user_count": user_count,
        "inventory_count": inventory_count,
        "recipe_count": recipe_count,
        "message": "Page de debug. À ne pas déployer en production."
    }
    return JsonResponse(data)
