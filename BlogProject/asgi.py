import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BlogProject.settings')
import realtime_app.routing
application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket":URLRouter(
            realtime_app.routing.websocket_urlpatterns
        )
        # Just HTTP for now. (We can add other protocols later.)
    }
)