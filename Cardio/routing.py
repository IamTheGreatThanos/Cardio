from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf.urls import url
from CardioApp.consumers import PointerConsumer

application = ProtocolTypeRouter({
    # Just HTTP for now. (We can add other protocols later.)
    "websocket": AuthMiddlewareStack(
        URLRouter([
            url(r"^chart/$", PointerConsumer.as_asgi()),
        ])
    ),
})