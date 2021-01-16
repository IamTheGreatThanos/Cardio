"""
ASGI config for Cardio project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os
import django
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf.urls import url
from CardioApp.consumers import PointerConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Cardio.settings')
django.setup()
application = get_asgi_application()
# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     # Just HTTP for now. (We can add other protocols later.)
#     "websocket": AuthMiddlewareStack(
#         URLRouter([
#             url(r"^chart/$", PointerConsumer.as_asgi()),
#         ])
#     ),
# })
