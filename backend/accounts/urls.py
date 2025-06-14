# backend/accounts/urls.py
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('household/', include('accounts.urls.household')),
    # Vous pouvez ajouter d'autres endpoints (par exemple, d'inscription)
]
