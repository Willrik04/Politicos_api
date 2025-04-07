from rest_framework import serializers
from .models import Candidato, Partido, Resultado

class PartidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partido
        fields = '__all__'

class CandidatoSerializer(serializers.ModelSerializer):
    partido_nombre = serializers.ReadOnlyField(source='partido.nombre')

    class Meta:
        model = Candidato
        fields = '__all__'

class ResultadoSerializer(serializers.ModelSerializer):
    candidato_nombre = serializers.ReadOnlyField(source='candidato.nombre')

    class Meta:
        model = Resultado
        fields = '__all__'