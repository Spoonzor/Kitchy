// frontend/src/components/InventoryManager.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';

const InventoryManager = () => {
  const [items, setItems] = useState([]);
  const [formData, setFormData] = useState({
    name: '',
    quantity: 1,
    expiration_date: '',
    category: '',
    location: '',
    barcode: ''
  });
  const [editingId, setEditingId] = useState(null); // Pour savoir quel item est en cours d'édition
  const [loading, setLoading] = useState(false);
  const token = localStorage.getItem('token');

  // Récupérer les items de l'inventaire
  const fetchInventory = async () => {
    setLoading(true);
    try {
      const res = await axios.get('http://localhost:8000/api/inventory/', {
        headers: { Authorization: 'Bearer ' + token }
      });
      setItems(res.data);
    } catch (error) {
      console.error("Erreur lors de la récupération de l'inventaire:", error);
    }
    setLoading(false);
  };

  useEffect(() => {
    fetchInventory();
  }, []);

  // Gérer la modification des champs du formulaire
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  // Ajouter un nouvel item
  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post('http://localhost:8000/api/inventory/', formData, {
        headers: { Authorization: 'Bearer ' + token }
      });
      setItems(prev => [...prev, res.data]);
      // Réinitialiser le formulaire
      setFormData({
        name: '',
        quantity: 1,
        expiration_date: '',
        category: '',
        location: '',
        barcode: ''
      });
    } catch (error) {
      console.error("Erreur lors de l'ajout de l'item:", error);
    }
  };

  // Initialiser le formulaire d'édition avec les données de l'item sélectionné
  const handleEdit = (item) => {
    setEditingId(item.id);
    setFormData({
      name: item.name,
      quantity: item.quantity,
      expiration_date: item.expiration_date || '',
      category: item.category || '',
      location: item.location || '',
      barcode: item.barcode || ''
    });
  };

  // Sauvegarder la modification
  const handleUpdate = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.put(`http://localhost:8000/api/inventory/${editingId}/`, formData, {
        headers: { Authorization: 'Bearer ' + token }
      });
      // Mettre à jour la liste des items
      setItems(prev => prev.map(item => (item.id === editingId ? res.data : item)));
      setEditingId(null);
      // Réinitialiser le formulaire
      setFormData({
        name: '',
        quantity: 1,
        expiration_date: '',
        category: '',
        location: '',
        barcode: ''
      });
    } catch (error) {
      console.error("Erreur lors de la mise à jour de l'item:", error);
    }
  };

  // Annuler l'édition
  const handleCancelEdit = () => {
    setEditingId(null);
    setFormData({
      name: '',
      quantity: 1,
      expiration_date: '',
      category: '',
      location: '',
      barcode: ''
    });
  };

  // Supprimer un item
  const handleDelete = async (id) => {
    try {
      await axios.delete(`http://localhost:8000/api/inventory/${id}/`, {
        headers: { Authorization: 'Bearer ' + token }
      });
      setItems(prev => prev.filter(item => item.id !== id));
    } catch (error) {
      console.error("Erreur lors de la suppression de l'item:", error);
    }
  };

  return (
    <div style={{ padding: '20px' }}>
      <h2>Gestion de l'Inventaire</h2>
      {editingId ? (
        <form onSubmit={handleUpdate} style={{ marginBottom: '20px' }}>
          <h3>Modification de l'item</h3>
          <div>
            <label>Nom de l'item :</label>
            <input
              type="text"
              name="name"
              placeholder="Nom de l'item"
              value={formData.name}
              onChange={handleInputChange}
              required
            />
          </div>
          <div>
            <label>Quantité :</label>
            <input
              type="number"
              name="quantity"
              placeholder="Quantité"
              value={formData.quantity}
              onChange={handleInputChange}
              required
            />
          </div>
          <div>
            <label>Date d'expiration :</label>
            <input
              type="date"
              name="expiration_date"
              value={formData.expiration_date}
              onChange={handleInputChange}
            />
          </div>
          <div>
            <label>Catégorie :</label>
            <input
              type="text"
              name="category"
              placeholder="Catégorie"
              value={formData.category}
              onChange={handleInputChange}
            />
          </div>
          <div>
            <label>Emplacement :</label>
            <input
              type="text"
              name="location"
              placeholder="Emplacement"
              value={formData.location}
              onChange={handleInputChange}
            />
          </div>
          <div>
            <label>Barcode :</label>
            <input
              type="text"
              name="barcode"
              placeholder="Barcode"
              value={formData.barcode}
              onChange={handleInputChange}
            />
          </div>
          <button type="submit">Enregistrer la modification</button>
          <button type="button" onClick={handleCancelEdit}>Annuler</button>
        </form>
      ) : (
        <form onSubmit={handleSubmit} style={{ marginBottom: '20px' }}>
          <h3>Ajouter un nouvel item</h3>
          <div>
            <label>Nom de l'item :</label>
            <input
              type="text"
              name="name"
              placeholder="Nom de l'item"
              value={formData.name}
              onChange={handleInputChange}
              required
            />
          </div>
          <div>
            <label>Quantité :</label>
            <input
              type="number"
              name="quantity"
              placeholder="Quantité"
              value={formData.quantity}
              onChange={handleInputChange}
              required
            />
          </div>
          <div>
            <label>Date d'expiration :</label>
            <input
              type="date"
              name="expiration_date"
              value={formData.expiration_date}
              onChange={handleInputChange}
            />
          </div>
          <div>
            <label>Catégorie :</label>
            <input
              type="text"
              name="category"
              placeholder="Catégorie"
              value={formData.category}
              onChange={handleInputChange}
            />
          </div>
          <div>
            <label>Emplacement :</label>
            <input
              type="text"
              name="location"
              placeholder="Emplacement"
              value={formData.location}
              onChange={handleInputChange}
            />
          </div>
          <div>
            <label>Barcode :</label>
            <input
              type="text"
              name="barcode"
              placeholder="Barcode"
              value={formData.barcode}
              onChange={handleInputChange}
            />
          </div>
          <button type="submit">Ajouter l'item</button>
        </form>
      )}

      {loading ? (
        <p>Chargement de l'inventaire...</p>
      ) : (
        <div>
          <h3>Liste des Items :</h3>
          {items.length === 0 ? (
            <p>Aucun item trouvé.</p>
          ) : (
            <ul>
              {items.map(item => (
                <li key={item.id} style={{ marginBottom: '10px' }}>
                  <strong>{item.name}</strong> - Quantité : {item.quantity}
                  {item.expiration_date && <span> - Expiration : {item.expiration_date}</span>}
                  <div style={{ marginTop: '5px' }}>
                    <button onClick={() => handleEdit(item)}>Modifier</button>
                    <button onClick={() => handleDelete(item.id)} style={{ marginLeft: '10px' }}>Supprimer</button>
                  </div>
                </li>
              ))}
            </ul>
          )}
        </div>
      )}
    </div>
  );
};

export default InventoryManager;
