def get_recipe_recommendations_enhanced(user, min_match_percentage=70):
    from recipes.models import Recipe
    from inventory.models import InventoryItem
    inventory_items = InventoryItem.objects.filter(owner=user)
    inventory_set = {item.name.lower() for item in inventory_items}
    
    recommendations = []
    recipes = Recipe.objects.filter()
    
    for recipe in recipes:
        ingredients = [ing.strip().lower() for ing in recipe.ingredients.split(',')]
        total = len(ingredients)
        if total == 0:
            continue
        present = sum(1 for ing in ingredients if ing in inventory_set)
        match_percentage = (present / total) * 100
        if match_percentage >= min_match_percentage:
            recommendations.append({
                "recipe": recipe,
                "match_percentage": match_percentage,
                "missing_ingredients": [ing for ing in ingredients if ing not in inventory_set]
            })
    
    recommendations.sort(key=lambda x: -x["match_percentage"])
    return recommendations
