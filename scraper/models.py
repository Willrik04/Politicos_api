from django.db import models

class Partido(models.Model):
    nombre = models.CharField(max_length=100)
    siglas = models.CharField(max_length=20)
    logo_url = models.URLField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    fecha_fundacion = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Candidato(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    partido = models.ForeignKey(Partido, on_delete=models.CASCADE, related_name='candidatos')
    foto_url = models.URLField(blank=True, null=True)
    biografia = models.TextField(blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    cargo_actual = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Resultado(models.Model):
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE, related_name='resultados')
    eleccion = models.CharField(max_length=100)
    fecha = models.DateField()
    votos = models.IntegerField()
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.candidato} - {self.eleccion} ({self.fecha})"