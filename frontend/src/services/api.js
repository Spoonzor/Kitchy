import axios from 'axios';

const API_URL = 'http://localhost:8000/api';

export const getInventory = () => axios.get(`${API_URL}/inventory/`, {
  headers: { Authorization: 'Bearer ' + localStorage.getItem('token') }
});

// Ajoutez ici d'autres fonctions pour recettes, shopping, etc.
