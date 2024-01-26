from django.urls import path
from . import consumer



websocket_urlpatterns=[
    path('ws/asc/', consumer.MyAsyncConsumer.as_asgi()),
    path('ws/sc/', consumer.MySyncConsumer.as_asgi()),

]