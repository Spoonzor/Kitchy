// mobile/app/index.tsx
import { Text, View, Button } from 'react-native';
import { router } from 'expo-router';

export default function Index() {
  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <Text>Bienvenue dans Kitchy</Text>
      <Button title="Connexion" onPress={() => router.push('/login')} />
      <Button title="Register" onPress={() => router.push('/register')} />
    </View>
  );
}
