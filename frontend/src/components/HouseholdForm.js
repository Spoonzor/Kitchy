// frontend/src/components/HouseholdForm.js
import React, { useState } from 'react';
import axios from 'axios';

const HouseholdForm = () => {
  const [name, setName] = useState('');
  const [message, setMessage] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setMessage('');

    // Récupération du token JWT
    const token = localStorage.getItem('token');
    if (!token) {
      setMessage("Vous devez être connecté pour créer un household.");
      return;
    }

    try {
      const res = await axios.post(
        'http://localhost:8000/api/accounts/household/create/',
        { name },
        {
          headers: {
            'Content-Type': 'application/json',
            Authorization: 'Bearer ' + token
          }
        }
      );
      setMessage('Household créé avec succès !');
      setName('');
    } catch (error) {
      // Gestion robuste de l'erreur
      const err = error.response?.data || error.message;
      console.error("Erreur lors de la création du household :", err);
      setMessage("Erreur lors de la création du household : " + JSON.stringify(err));
    }
  };

  return (
    <div style={{ padding: '20px' }}>
      <h2>Créer un Household</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Nom du Household :</label>
          <input
            type="text"
            value={name}
            onChange={e => setName(e.target.value)}
            required
          />
        </div>
        <button type="submit" style={{ marginTop: '10px' }}>
          Créer
        </button>
      </form>
      {message && <p style={{ marginTop: '10px' }}>{message}</p>}
    </div>
  );
};

export default HouseholdForm;
