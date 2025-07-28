from django.shortcuts import render
from django.conf import settings
from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer

# for AI contact
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Logs, API
import os
import logging
import ollama
from openai import OpenAI


logger = logging.getLogger(__name__)
client = OpenAI(api_key=settings.OPENAI_API_KEY)

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer




@api_view(['POST'])
def openai_message(request):
    """
    Обработчик POST-запроса к OpenAI Chat API.
    Ожидает JSON с ключом 'message'.
    Возвращает ответ модели в формате JSON.
    """
    user_message = request.data.get('message')
    if not user_message:
        return Response({'error': 'Message is required'}, status=400)

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # или "gpt-3.5-turbo"
            messages=[
                {"role": "user", "content": user_message}
            ],
            temperature=0.7,
            max_tokens=1000,
        )
        reply = response.choices[0].message.content.strip()
        return Response({'reply': reply})
    except Exception as e:
        logger.error(f"OpenAI error: {e}")
        return Response({'error': str(e)}, status=500)