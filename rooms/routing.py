from django.urls import path, re_path
from . import consumer

websocket_urlpatterns = [
    re_path(r'ws/(?P<room_name>\w+)/$', consumer.ChatConsumer.as_asgi()),
]