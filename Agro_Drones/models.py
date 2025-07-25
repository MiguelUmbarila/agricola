from django.db import models

# Create your models here.

class Terreno(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.TextField()  # Coordenadas 
    area = models.DecimalField(max_digits=6, decimal_places=2)  # Hectáreas
    tipo_suelo = models.CharField(max_length=100)

class Dron(models.Model):
    modelo = models.CharField(max_length=100)
    numero_serie = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)  # 'disponible', 'en_mision', 'mantenimiento'
    bateria = models.DecimalField(max_digits=5, decimal_places=2)  # Porcentaje
    conectado = models.BooleanField(default=False)

class ParametroFertilizacion(models.Model):
    terreno = models.ForeignKey(Terreno, on_delete=models.CASCADE)
    tipo_cultivo = models.CharField(max_length=100)
    tipo_fertilizante = models.CharField(max_length=100)
    dosis = models.CharField(max_length=50)  # Ej: '150 kg/ha'
    frecuencia = models.CharField(max_length=50)
    zonas = models.TextField()  # Zonas específicas del terreno

class Ruta(models.Model):
    terreno = models.ForeignKey(Terreno, on_delete=models.CASCADE)
    dron = models.ForeignKey(Dron, on_delete=models.SET_NULL, null=True)
    coordenadas = models.TextField()  # GeoJSON o similar
    fecha_programada = models.DateTimeField()
    activa = models.BooleanField(default=True)

class Ejecucion(models.Model):
    ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField(null=True, blank=True)
    fertilizante_usado = models.DecimalField(max_digits=6, decimal_places=2)  # Cantidad en kg
    observaciones = models.TextField(blank=True)

class Reporte(models.Model):
    ejecucion = models.ForeignKey(Ejecucion, on_delete=models.CASCADE)
    eficiencia = models.DecimalField(max_digits=5, decimal_places=2)  # Porcentaje
    area_cubierta = models.CharField(max_length=100)
    fecha_generado = models.DateTimeField(auto_now_add=True)