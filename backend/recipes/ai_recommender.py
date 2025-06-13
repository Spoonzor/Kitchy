from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from recipes.models import Recipe
from inventory.models import InventoryItem

def get_content_based_recommendations(user):
    recipes = Recipe.objects.all()
    inventory_items = InventoryItem.objects.filter(owner=user)
    inventory_text = ' '.join(item.name.lower() for item in inventory_items)
    
    recipe_texts = [recipe.ingredients for recipe in recipes]
    documents = recipe_texts + [inventory_text]
    
    vectorizer = TfidfVectorizer(stop_words='french')
    tfidf_matrix = vectorizer.fit_transform(documents)
    
    recipe_vectors = tfidf_matrix[:-1]
    inventory_vector = tfidf_matrix[-1]
    
    similarities = cosine_similarity(inventory_vector, recipe_vectors).flatten()
    
    recommendations = []
    for idx, similarity in enumerate(similarities):
        recommendations.append({
            "recipe": recipes[idx],
            "similarity": similarity
        })
    recommendations.sort(key=lambda x: -x["similarity"])
    return recommendations
