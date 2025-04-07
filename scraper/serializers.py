from rest_framework import serializers
from .models import Candidato, Partido, ResultadoElectoral

class PartidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partido
        fields = '__all__'

class ResultadoElectoralSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultadoElectoral
        fields = ['provincia', 'votos', 'porcentaje', 'fecha_actualizacion']

class CandidatoSerializer(serializers.ModelSerializer):
    partido = PartidoSerializer(read_only=True)
    resultados = ResultadoElectoralSerializer(many=True, read_only=True)

    class Meta:
        model = Candidato
        fields = ['id', 'nombre', 'cargo', 'partido', 'foto_url', 'biografia', 'propuestas', 'redes_sociales', 'resultados']

class CandidatoDetailSerializer(serializers.ModelSerializer):
    partido = PartidoSerializer(read_only=True)
    resultados = ResultadoElectoralSerializer(many=True, read_only=True)

    class Meta:
        model = Candidato
        fields = '__all__'