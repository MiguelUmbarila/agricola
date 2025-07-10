from django.db import models


class Cultivo(models.Model):  # crear tabla del cultivo
    tipo = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=255)
    fecha_siembra = models.DateField()

    def __str__(self):
        return str(self.tipo)


class DatoClimatico(models.Model):  # crear tabla datos climaticos
    temperatura = models.FloatField()
    humedad = models.FloatField()
    lluvia = models.FloatField()
    cultivo = models.ForeignKey(Cultivo, on_delete=models.CASCADE, related_name='datos_climaticos')
    fecha_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Dato climático: {self.temperatura}°C"


class ModeloPredictivo(models.Model):  # crear tabla de informacion de entrenamiento del modelo predictivo
    nombre_modelo = models.CharField(max_length=100)
    fecha_entrenamiento = models.DateField()
    cultivo = models.ForeignKey(Cultivo, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nombre_modelo)

    
class Alerta(models.Model):  # crear tabla alerta para almacenar la informacion de estas
    tipo_alerta = models.CharField(max_length=100)
    nivel_alerta = models.CharField(max_length=50)
    fecha_generacion = models.DateTimeField()
    modelo_predictivo = models.ForeignKey(ModeloPredictivo, on_delete=models.CASCADE, related_name='alertas')

    def __str__(self):
        return str(self.tipo_alerta)


class Recomendacion(models.Model): 
     # crear tabla para almacenar todas las recomendaciones hechas por el sistema
    contenido = models.TextField()
    fecha = models.DateField(auto_now_add=True)
    cultivo_asociado = models.ForeignKey(Cultivo, on_delete=models.CASCADE, related_name='recomendaciones')

    def __str__(self):
        return str(self.contenido)