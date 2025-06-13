import os
from pathlib import Path

# Répertoire de base du projet
BASE_DIR = Path(__file__).resolve().parent.parent

# Clé secrète (à modifier pour la production)
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'votre_secret_key')

# Mode debug (à désactiver en production)
DEBUG = True

# Liste des hôtes autorisés
ALLOWED_HOSTS = []

# Applications installées
INSTALLED_APPS = [
    'django.contrib.sites',  # Nécessaire pour django-allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',   # Pour Google
    'allauth.socialaccount.providers.facebook', # Pour Facebook
    'dj_rest_auth',
    'dj_rest_auth.registration',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'channels',
    'rest_framework.authtoken',
    'corsheaders',
    'accounts',     # Gestion des comptes et du partage familial
    'inventory',    # Module Inventaire
    'recipes',      # Module Recettes et Favoris
    'shopping',     # Module Liste d’Épicerie
    'core',         # (Optionnel) Application dédiée aux commandes ou autres fonctionnalités
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Configuration des URLs
ROOT_URLCONF = 'kitchen_app.urls'

# Templates (vous pouvez ajouter des répertoires de templates dans DIRS si besoin)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Par exemple : [BASE_DIR / 'templates']
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI et ASGI
WSGI_APPLICATION = 'kitchen_app.wsgi.application'
ASGI_APPLICATION = 'kitchen_app.asgi.application'

# Configuration de la base de données (ici PostgreSQL ; modifiez selon vos besoins)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'kitchenapp'),
        'USER': os.environ.get('DB_USER', 'postgres'),
        'PASSWORD': os.environ.get('DB_PASS', 'L33trainrirzor!-'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': '5432',
    }
}

# Configuration de Django Channels (pour les WebSocket)
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
    },
}

# Configuration de Django REST Framework avec JWT (via djangorestframework-simplejwt)
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

# Internationalisation
LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'Europe/Paris'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Fichiers statiques
STATIC_URL = '/static/'

# Configuration pour les clés primaires auto-créées
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SITE_ID = 1

ACCOUNT_EMAIL_VERIFICATION = "none"  # Pour simplifier en développement
ACCOUNT_AUTHENTICATION_METHOD = "username"  # Ou "email" selon vos préférences
ACCOUNT_EMAIL_REQUIRED = False

CORS_ALLOW_ALL_ORIGINS = True