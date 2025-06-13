// frontend/src/components/HouseholdManagement.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import HouseholdForm from './HouseholdForm';

const HouseholdManagement = () => {
  const [households, setHouseholds] = useState([]);
  const [message, setMessage] = useState('');
  const navigate = useNavigate();

  useEffect(() => {
    const token = localStorage.getItem('token');
    if (!token) {
      navigate('/auth');
    } else {
      fetchHouseholds();
    }
  }, [navigate]);

  const fetchHouseholds = async () => {
    const token = localStorage.getItem('token');
    if (!token) {
      navigate('/auth');
      return;
    }
    try {
      const res = await axios.get(
        'http://localhost:8000/api/accounts/household/',
        { headers: { Authorization: 'Bearer ' + token } }
      );
      setHouseholds(res.data);
    } catch (error) {
      if (error.response?.status === 401) {
        // Token invalide ou expiré
        localStorage.removeItem('token');
        navigate('/auth');
      } else {
        console.error("Erreur de récupération des foyers :", error);
        setMessage("Impossible de charger les foyers.");
      }
    }
  };

  const handleCreated = () => {
    fetchHouseholds();
  };

  return (
    <div style={{ padding: '20px' }}>
      <h2>Gestion du ménage</h2>
      {message && <p style={{ color: 'red' }}>{message}</p>}
      {households.length > 0 ? (
        <ul>
          {households.map(household => (
            <li key={household.id} style={{ marginBottom: '8px' }}>
              <strong>{household.name}</strong>
            </li>
          ))}
        </ul>
      ) : (
        <p>Vous n'êtes lié à aucun foyer pour le moment.</p>
      )}
      <HouseholdForm onCreate={handleCreated} />
    </div>
  );
};

export default HouseholdManagement;
