import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { Tabs } from 'expo-router';
import { MaterialIcons } from '@expo/vector-icons';

export default function DashboardLayout() {
  return (
    <Tabs>
      <Tabs.Screen name="home" options={{ title: 'Ménage', tabBarIcon: ({ color, size }) => <MaterialIcons name="home" color={color} size={size} /> }} />
      <Tabs.Screen name="inventory" options={{ title: 'Inventaire', tabBarIcon: ({ color, size }) => <MaterialIcons name="inventory" color={color} size={size} /> }} />
      <Tabs.Screen name="scanner" options={{ title: 'Scan', tabBarIcon: ({ color, size }) => <MaterialIcons name="camera-alt" color={color} size={size} /> }} />
      <Tabs.Screen name="recipes" options={{ title: 'Recettes', tabBarIcon: ({ color, size }) => <MaterialIcons name="restaurant-menu" color={color} size={size} /> }} />
      <Tabs.Screen name="profile" options={{ title: 'Profil', tabBarIcon: ({ color, size }) => <MaterialIcons name="person" color={color} size={size} /> }} />
    </Tabs>
  );
}
