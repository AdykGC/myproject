# backend/api/urls.py

from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet, openai_message

router = DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('chat/openai/', openai_message, name='openai_message'),
]

# Добавляем маршруты из роутера (ItemViewSet)
urlpatterns += router.urls
