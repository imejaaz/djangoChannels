from django.urls import path
from . import consumer



websocket_urlpatterns=[
    path('ws/sc/', consumer.TestConsumer.as_asgi()),
    path('ws/sca/', consumer.TestConsumera.as_asgi()),

]