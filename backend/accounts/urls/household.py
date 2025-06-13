# (si utilisé en include séparé, sinon tout est dans __init__.py)
from django.urls import path
from accounts.views.household import (
    HouseholdListView, HouseholdCreateView,
    HouseholdInviteView, AcceptInvitationView,
)
urlpatterns = [
  path('', HouseholdListView.as_view(), name='household_list'),
  path('create/', HouseholdCreateView.as_view(), name='household_create'),
  path('<int:household_id>/invite/', HouseholdInviteView.as_view(), name='household_invite'),
  path('accept/', AcceptInvitationView.as_view(), name='household_accept_invitation'),
]
