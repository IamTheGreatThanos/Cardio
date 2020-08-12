from channels.routing import ProtocolTypeRouter
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.conf.urls import url
from CardioApp.consumers import EchoConsumer

application = ProtocolTypeRouter({
    # WebSocket chat handler
    "websocket": AuthMiddlewareStack(
        URLRouter([
            url(r"^/socket/$", EchoConsumer),
        ])
    )
})