from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path, include, re_path
from utils.socket_room import TokenAuthMiddlewareStack

from CardioApp.consumers import PointerConsumer

application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path('api/setByte/', PointerConsumer.as_asgi()),
        ])
        
    ),
})

# application = ProtocolTypeRouter({
#     "websocket": 
#         TokenAuthMiddlewareStack(
#             URLRouter([
#                 re_path(r"api/setByte/(?P<wid>\w+)/$", PointerConsumer.as_asgi()),
#             ])
#         )
    
# })