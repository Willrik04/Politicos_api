from django.db import models

class Partido(models.Model):
    nombre = models.CharField(max_length=200)
    lista = models.CharField(max_length=50)
    logo_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - Lista {self.lista}"

class Candidato(models.Model):
    nombre = models.CharField(max_length=200)
    cargo = models.CharField(max_length=200)
    partido = models.ForeignKey(Partido, on_delete=models.CASCADE, related_name='candidatos')
    foto_url = models.URLField(blank=True, null=True)
    biografia = models.TextField(blank=True, null=True)
    propuestas = models.TextField(blank=True, null=True)
    redes_sociales = models.JSONField(default=dict, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.cargo} ({self.partido.nombre})"

class ResultadoElectoral(models.Model):
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE, related_name='resultados')
    provincia = models.CharField(max_length=100)
    votos = models.IntegerField(default=0)
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.candidato.nombre} - {self.provincia}: {self.porcentaje}%"