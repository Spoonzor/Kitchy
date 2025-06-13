// frontend/src/components/AuthPage.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const AuthPage = () => {
  const [isRegister, setIsRegister] = useState(false);
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password1: '',
    password2: ''
  });
  const [message, setMessage] = useState('');
  const navigate = useNavigate();

  // Si déjà connecté, redirige vers l'accueil
  useEffect(() => {
    const token = localStorage.getItem('token');
    if (token) {
      navigate('/');
    }
  }, [navigate]);

  const toggleMode = () => {
    setIsRegister(!isRegister);
    setMessage('');
    setFormData({ username: '', email: '', password1: '', password2: '' });
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  const handleRegister = async (e) => {
    e.preventDefault();
    setMessage('');

    if (formData.password1 !== formData.password2) {
      setMessage("Les mots de passe ne correspondent pas.");
      return;
    }

    try {
      await axios.post(
        'http://localhost:8000/api/accounts/registration/',
        {
          username: formData.username,
          email: formData.email,
          password1: formData.password1,
          password2: formData.password2
        },
        { headers: { 'Content-Type': 'application/json' } }
      );
      setMessage('Inscription réussie ! Vous pouvez maintenant vous connecter.');
      setIsRegister(false);
    } catch (error) {
      const err = error.response?.data || error.message;
      console.error('Erreur d\'inscription :', err);
      setMessage('Erreur d\'inscription : ' + JSON.stringify(err));
    }
  };

  const handleLogin = async (e) => {
    e.preventDefault();
    setMessage('');

    try {
      const res = await axios.post(
        'http://localhost:8000/api/accounts/token/',
        { username: formData.username, password: formData.password1 },
        { headers: { 'Content-Type': 'application/json' } }
      );

      const token = res.data.access;
      localStorage.setItem('token', token);

      const houseRes = await axios.get(
        'http://localhost:8000/api/accounts/household/',
        { headers: { Authorization: 'Bearer ' + token } }
      );

      if (houseRes.data.length === 0) {
        navigate('/household');
      } else {
        navigate('/');
      }
    } catch (error) {
      const err = error.response?.data || error.message;
      console.error('Erreur de connexion :', err);
      setMessage('Erreur de connexion : ' + JSON.stringify(err));
    }
  };

  return (
    <div style={{ padding: '20px', maxWidth: '400px', margin: 'auto' }}>
      <h2>{isRegister ? 'Inscription' : 'Connexion'}</h2>
      <form onSubmit={isRegister ? handleRegister : handleLogin}>
        {isRegister && (
          <div>
            <label>Email :</label>
            <input
              type="email"
              name="email"
              value={formData.email}
              onChange={handleInputChange}
              required
            />
          </div>
        )}
        <div>
          <label>Nom d'utilisateur :</label>
          <input
            type="text"
            name="username"
            value={formData.username}
            onChange={handleInputChange}
            required
          />
        </div>
        <div>
          <label>Mot de passe :</label>
          <input
            type="password"
            name="password1"
            value={formData.password1}
            onChange={handleInputChange}
            required
          />
        </div>
        {isRegister && (
          <div>
            <label>Confirmer le mot de passe :</label>
            <input
              type="password"
              name="password2"
              value={formData.password2}
              onChange={handleInputChange}
              required
            />
          </div>
        )}
        <button type="submit" style={{ marginTop: '10px' }}>
          {isRegister ? "S'inscrire" : 'Se connecter'}
        </button>
      </form>

      {message && (
        <p style={{ marginTop: '10px', color: 'red' }}>{message}</p>
      )}

      <div style={{ marginTop: '10px' }}>
        <button onClick={toggleMode} style={{ fontSize: '0.9em' }}>
          {isRegister
            ? 'Déjà un compte ? Se connecter'
            : "Pas encore de compte ? S'inscrire"}
        </button>
      </div>
    </div>
  );
};

export default AuthPage;
