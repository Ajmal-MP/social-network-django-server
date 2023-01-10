from django.urls import path
from apps.chats.consumers import ChatConsumer, ChatNotificationConsumer
from apps.notifications.consumers import NotificationsConsumer

websocket_urlpatterns = [
    path("chats/<conversation_name>/", ChatConsumer.as_asgi()),
    path("notifications/chat/", ChatNotificationConsumer.as_asgi()),

    path("notifications/", NotificationsConsumer.as_asgi()),
]
