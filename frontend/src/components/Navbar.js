// frontend/src/components/Navbar.js
import React from 'react';
import { Link, useNavigate } from 'react-router-dom';

const Navbar = () => {
  const navigate = useNavigate();
  const token = localStorage.getItem('token');

  const handleLogout = () => {
    localStorage.removeItem('token');
    navigate('/'); // ou '/login' selon votre route
  };

  return (
    <nav style={{ padding: '10px', background: '#f0f0f0' }}>
      <ul style={{ display: 'flex', gap: '20px', listStyle: 'none', margin: 0 }}>
        <li><Link to="/">Accueil</Link></li>
        {token && <>
          <li><Link to="/inventory">Inventaire</Link></li>
          <li><Link to="/recipes">Recettes</Link></li>
          <li><Link to="/shopping">Épicerie</Link></li>
          <li><Link to="/stores">Magasins & Rabais</Link></li>
          <li><Link to="/household">Gestion du ménage</Link></li>
          <li>
            <button 
              onClick={handleLogout} 
              style={{
                background: 'transparent',
                border: 'none',
                cursor: 'pointer',
                color: '#007bff',
                textDecoration: 'underline',
                padding: 0
              }}
            >
              Se déconnecter
            </button>
          </li>
        </>}
        {!token && (
          <li><Link to="/login">Se connecter / S'inscrire</Link></li>
        )}
      </ul>
    </nav>
  );
};

export default Navbar;
