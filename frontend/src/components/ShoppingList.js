import React, { useEffect, useState } from 'react';
import axios from 'axios';

const ShoppingList = () => {
  const [lists, setLists] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/api/shopping/', {
      headers: { Authorization: 'Bearer ' + localStorage.getItem('token') }
    })
    .then(res => setLists(res.data))
    .catch(err => console.error("Erreur lors de la récupération des listes", err));
  }, []);

  return (
    <div>
      <h2>Liste d’Épicerie</h2>
      <ul>
        {lists.map(list => (
          <li key={list.id}>{list.title}</li>
        ))}
      </ul>
    </div>
  );
};

export default ShoppingList;
