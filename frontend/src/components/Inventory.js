import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Inventory = () => {
  const [items, setItems] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/api/inventory/', {
      headers: { Authorization: 'Bearer ' + localStorage.getItem('token') }
    })
    .then(res => setItems(res.data))
    .catch(err => console.error("Erreur lors de la récupération de l'inventaire", err));
  }, []);

  return (
    <div>
      <h2>Inventaire</h2>
      <ul>
        {items.map(item => (
          <li key={item.id}>{item.name} - Quantité: {item.quantity}</li>
        ))}
      </ul>
    </div>
  );
};

export default Inventory;
