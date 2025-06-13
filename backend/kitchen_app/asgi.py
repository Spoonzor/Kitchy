import os
import django
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
import inventory.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kitchen_app.settings')
django.setup()

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            inventory.routing.websocket_urlpatterns
        )
    ),
})
