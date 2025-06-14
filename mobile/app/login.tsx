// mobile/app/login.tsx
import { useState } from 'react';
import { View, StyleSheet, Alert } from 'react-native';
import { TextInput, Button, Text } from 'react-native-paper';
import axios from 'axios';
import { router } from 'expo-router';

export default function LoginScreen() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = async () => {
    try {
      const res = await axios.post('http://192.168.X.X:8000/api/accounts/login/', {
        email,
        password,
      });
      Alert.alert("Connecté !");
      router.replace('/dashboard'); // redirige vers la page d'accueil
    } catch (err) {
      Alert.alert("Erreur", "Échec de la connexion");
    }
  };

  return (
    <View style={styles.container}>
      <Text variant="headlineMedium">Connexion</Text>
      <TextInput label="Email" value={email} onChangeText={setEmail} style={styles.input} />
      <TextInput label="Mot de passe" value={password} onChangeText={setPassword} secureTextEntry style={styles.input} />
      <Button mode="contained" onPress={handleLogin}>Se connecter</Button>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, padding: 20, justifyContent: 'center' },
  input: { marginBottom: 12 }
});
