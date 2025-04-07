from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Candidato, Partido, Resultado
from .serializers import CandidatoSerializer, PartidoSerializer, ResultadoSerializer
import os

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

            # Simulamos una respuesta para probar
            respuesta = f"Respuesta simulada a: {pregunta}"

            return Response({"respuesta": respuesta})
        except Exception as e:
            return Response({"error": str(e)}, status=500)