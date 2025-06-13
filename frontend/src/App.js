import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './components/Navbar';
import AuthPage from './components/AuthPage';
import Homepage from './components/Homepage';
import InventoryManager from './components/InventoryManager';
import RecipeRecommendations from './components/RecipeRecommendations';
import ShoppingList from './components/ShoppingList';
import StoresAndDiscounts from './components/StoresAndDiscounts';
import HouseholdManagement from './components/HouseholdManagement';

function App() {
  const token = localStorage.getItem('token');
  return (
    <Router>
      <Navbar />
      <Routes>
        {!token ? (
          <Route path="*" element={<AuthPage />} />
        ) : (
          <>
            <Route path="/" element={<Homepage />} />
            <Route path="/inventory" element={<InventoryManager />} />
            <Route path="/recipes" element={<RecipeRecommendations />} />
            <Route path="/shopping" element={<ShoppingList />} />
            <Route path="/stores" element={<StoresAndDiscounts />} />
            <Route path="/household" element={<HouseholdManagement />} />
          </>
        )}
      </Routes>
    </Router>
  );
}

export default App;
