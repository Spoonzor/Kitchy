// frontend/src/components/Homepage.js
import React from 'react';
import { Link } from 'react-router-dom';

const Homepage = () => {
  return (
    <div style={styles.container}>
      <h1>Bienvenue sur Kitchen App</h1>
      <p>Sélectionnez une section pour commencer :</p>
      <div style={styles.cardsContainer}>
        <div style={styles.card}>
          <Link to="/inventory" style={styles.link}>Inventaire</Link>
        </div>
        <div style={styles.card}>
          <Link to="/recipes" style={styles.link}>Recettes</Link>
        </div>
        <div style={styles.card}>
          <Link to="/shopping" style={styles.link}>Épicerie</Link>
        </div>
        <div style={styles.card}>
          <Link to="/stores" style={styles.link}>Magasins & Rabais</Link>
        </div>
        <div style={styles.card}>
          <Link to="/household" style={styles.link}>Gestion du ménage</Link>
        </div>
      </div>
    </div>
  );
};

const styles = {
  container: {
    textAlign: 'center',
    padding: '20px'
  },
  cardsContainer: {
    display: 'flex',
    justifyContent: 'center',
    flexWrap: 'wrap',
    gap: '20px',
    marginTop: '20px'
  },
  card: {
    border: '1px solid #ccc',
    borderRadius: '8px',
    padding: '20px',
    width: '200px'
  },
  link: {
    textDecoration: 'none',
    color: '#333',
    fontWeight: 'bold'
  }
};

export default Homepage;
