from django.contrib import admin
from django.urls import path, include
from kitchen_app.views.debug import debug_view

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api/accounts/', include('dj_rest_auth.urls'))
    path('api/accounts/', include('accounts.urls')),
    #path('api/accounts/registration/', include('dj_rest_auth.registration.urls')),
    path('api/inventory/', include('inventory.urls')),
    path('api/recipes/', include('recipes.urls')),
    path('api/shopping/', include('shopping.urls')),
    path('debug/', debug_view, name='debug'),
]