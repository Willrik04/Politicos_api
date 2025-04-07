from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Candidato, Partido, ResultadoElectoral
from .serializers import CandidatoSerializer, PartidoSerializer, ResultadoElectoralSerializer, CandidatoDetailSerializer
import openai
import os

# Vista básica para pruebas
def index(request):
    return JsonResponse({"message": "API de candidatos políticos"})

# Vistas para Candidatos
class CandidatoListView(generics.ListAPIView):
    queryset = Candidato.objects.all()
    serializer_class = CandidatoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre', 'cargo', 'partido__nombre']

class CandidatoDetailView(generics.RetrieveAPIView):
    queryset = Candidato.objects.all()
    serializer_class = CandidatoDetailSerializer

# Vistas para Partidos
class PartidoListView(generics.ListAPIView):
    queryset = Partido.objects.all()
    serializer_class = PartidoSerializer

class PartidoDetailView(generics.RetrieveAPIView):
    queryset = Partido.objects.all()
    serializer_class = PartidoSerializer

# Vistas para Resultados Electorales
class ResultadoElectoralListView(generics.ListAPIView):
    queryset = ResultadoElectoral.objects.all()
    serializer_class = ResultadoElectoralSerializer

    def get_queryset(self):
        queryset = ResultadoElectoral.objects.all()
        candidato_id = self.request.query_params.get('candidato_id')
        if candidato_id:
            queryset = queryset.filter(candidato_id=candidato_id)
        return queryset

# Vista para ChatGPT
class ChatGPTView(APIView):
    def post(self, request):
        try:
            # Obtener la pregunta del usuario
            pregunta = request.data.get('pregunta', '')

            # Configurar la API de OpenAI
            openai.api_key = os.environ.get('OPENAI_API_KEY', 'tu-api-key-aqui')

            # Realizar la consulta a ChatGPT
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Eres un asistente especializado en política ecuatoriana."},
                    {"role": "user", "content": pregunta}
                ]
            )

            # Extraer la respuesta
            respuesta = response.choices[0].message.content

            return Response({"respuesta": respuesta})
        except Exception as e:
            return Response({"error": str(e)}, status=500)