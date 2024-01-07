import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from home.consumer import *
from django.urls import path
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dch.settings')

application = get_asgi_application

ws_patterns = [
        path('test/', TestConsumera.as_asgi())

]

application = ProtocolTypeRouter({
    'websocket' : URLRouter(ws_patterns)
})

