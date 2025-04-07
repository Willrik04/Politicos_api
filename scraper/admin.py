from django.contrib import admin
from .models import Partido, Candidato, ResultadoElectoral

@admin.register(Partido)
class PartidoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'lista')
    search_fields = ('nombre', 'lista')

@admin.register(Candidato)
class CandidatoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cargo', 'partido')
    list_filter = ('cargo', 'partido')
    search_fields = ('nombre', 'cargo')

@admin.register(ResultadoElectoral)
class ResultadoElectoralAdmin(admin.ModelAdmin):
    list_display = ('candidato', 'provincia', 'votos', 'porcentaje', 'fecha_actualizacion')
    list_filter = ('provincia', 'candidato__partido')
    search_fields = ('candidato__nombre', 'provincia')