from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path, include
from utils.socket_room import TokenAuthMiddlewareStack

from CardioApp.consumers import PointerConsumer

application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path("api/setByte/<id:str>", PointerConsumer.as_asgi()),
        ])
        
    ),
})

# application = ProtocolTypeRouter({
#     "websocket": AllowedHostsOriginValidator(
#         TokenAuthMiddlewareStack(
#             URLRouter([
#                 path("api/setByte/", PointerConsumer.as_asgi()),
#             ])
#         )
#     )
# })