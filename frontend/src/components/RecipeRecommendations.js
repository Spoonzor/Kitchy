import React, { useEffect, useState } from 'react';
import axios from 'axios';

const RecipeRecommendations = () => {
  const [recommendations, setRecommendations] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/api/recipes/recommendations/', {
      headers: { Authorization: 'Bearer ' + localStorage.getItem('token') }
    })
    .then(res => setRecommendations(res.data))
    .catch(err => console.error("Erreur de récupération des recommandations", err));
  }, []);

  return (
    <div>
      <h3>Recettes Recommandées</h3>
      <ul>
        {recommendations.map((rec, index) => (
          <li key={index}>
            <strong>{rec.recipe.title}</strong> - Correspondance: {Math.round(rec.match_percentage)}%
            <br/>
            Ingrédients manquants: {rec.missing_ingredients.join(', ')}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default RecipeRecommendations;
