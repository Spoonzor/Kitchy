import React, { useEffect, useState } from 'react';

const NotificationListener = () => {
  const [notifications, setNotifications] = useState([]);

  useEffect(() => {
    const ws = new WebSocket('ws://localhost:8000/ws/notifications/');

    ws.onopen = () => {
      console.log('Connexion WebSocket établie');
    };

    ws.onmessage = event => {
      const data = JSON.parse(event.data);
      setNotifications(prev => [...prev, data.message]);
    };

    ws.onerror = error => {
      console.error('Erreur WebSocket', error);
    };

    return () => ws.close();
  }, []);

  return (
    <div className="notification-panel">
      <h4>Notifications</h4>
      <ul>
        {notifications.map((note, idx) => (
          <li key={idx}>{note}</li>
        ))}
      </ul>
    </div>
  );
};

export default NotificationListener;
