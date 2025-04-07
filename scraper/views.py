from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Candidato, Partido, Resultado
from .serializers import CandidatoSerializer, PartidoSerializer, ResultadoSerializer
import os
import requests

class CandidatoViewSet(viewsets.ModelViewSet):
    queryset = Candidato.objects.all()
    serializer_class = CandidatoSerializer

class PartidoViewSet(viewsets.ModelViewSet):
    queryset = Partido.objects.all()
    serializer_class = PartidoSerializer

class ResultadoViewSet(viewsets.ModelViewSet):
    queryset = Resultado.objects.all()
    serializer_class = ResultadoSerializer

class ChatGPTView(APIView):
    def post(self, request):
        try:
            # Obtener la pregunta del usuario
            pregunta = request.data.get('pregunta', '')

            # Configurar la API de OpenAI (o la API que estés usando)
            api_key = os.environ.get('OPENAI_API_KEY', '')

            # Realizar la consulta a la API
            headers = {
                'Authorization': f'Bearer {api_key}',
                'Content-Type': 'application/json'
            }

            data = {
                'model': 'gpt-3.5-turbo',
                'messages': [
                    {'role': 'system', 'content': 'Eres un asistente especializado en política ecuatoriana.'},
                    {'role': 'user', 'content': pregunta}
                ]
            }

            response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=data)
            response_data = response.json()

            # Extraer la respuesta
            respuesta = response_data['choices'][0]['message']['content']

            return Response({"respuesta": respuesta})
        except Exception as e:
            return Response({"error": str(e)}, status=500)