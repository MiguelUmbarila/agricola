from django.db import models

# Create your models here.

class Humedad(models.Model):
    humedad_actual = models.CharField(max_length=10)
    humedad_maxima = models.CharField(max_length=10)
    humedad_minima = models.CharField(max_length=10)
    humedad_solicitada = models.CharField(max_length=10)

    def __str__(self):
        return self.humedad_actual
   
    