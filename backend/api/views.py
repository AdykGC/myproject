from django.shortcuts import render
from django.conf import settings
from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer

# for AI contact
import openai
from rest_framework.decorators import api_view
from rest_framework.response import Response
# for AI contact
import logging
import ollama


logger = logging.getLogger(__name__)


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


#  openai.api_key = settings.OPENAI_API_KEY
#  @api_view(['POST'])
#  def chatgpt_message(request):
#      message = request.data.get('message', '')
#      if not message:
#          return Response({'error': 'Message is required'}, status=400)
#      try:
#          response = openai.ChatCompletion.create(
#              model="gpt-3.5-turbo",
#              messages=[{"role": "user", "content": message}],
#          )
#          reply = response.choices[0].message.content
#          return Response({'reply': reply})
#      except Exception as e:
#          return Response({'error': str(e)}, status=500)


@api_view(['POST'])
def ollama_message(request):
    """
    Обработчик POST-запроса к локальной LLM через Ollama.
    Ожидает JSON с ключом 'message'.
    Возвращает ответ модели в формате JSON.
    """

    user_message = request.data.get('message')
    if not user_message:
        return Response({'error': 'Message is required'}, status=400)
    try:
        response = ollama.chat(
            model='gemma3:1b',
            messages=[
                {"role": "user", "content": user_message}
            ]
        )
        reply = response['message']['content'].strip()
        return Response({'reply': reply})
    except Exception as e:
        logger.error(f"Ошибка при запросе к Ollama: {e}")
        return Response({'error': str(e)}, status=500)