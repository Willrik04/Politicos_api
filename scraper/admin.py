from django.contrib import admin
from .models import Candidato, Partido, Resultado

admin.site.register(Candidato)
admin.site.register(Partido)
admin.site.register(Resultado)