from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from accounts.views.household import (
    HouseholdCreateView,
    HouseholdInviteView,
    AcceptInvitationView,
    HouseholdListView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', include('dj_rest_auth.urls')),       # si vous utilisez dj-rest-auth
    path('registration/', include('dj_rest_auth.registration.urls')),

    path('household/', HouseholdListView.as_view(), name='household_list'),
    path('household/create/', HouseholdCreateView.as_view(), name='household_create'),
    path('household/<int:household_id>/invite/', HouseholdInviteView.as_view(), name='household_invite'),
    path('household/accept/', AcceptInvitationView.as_view(), name='household_accept_invitation'),
]
