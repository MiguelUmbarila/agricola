from django.db import models

class EstandarCalidad(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    parametro = models.CharField(max_length=100)  # ejemplo: 'Humedad', 'Impurezas'
    valor_minimo = models.FloatField()
    valor_maximo = models.FloatField()

    def __str__(self):
        return f"{self.nombre} - {self.parametro}"

class LoteGrano(models.Model):
    codigo_lote = models.CharField(max_length=50, unique=True)
    fecha_registro = models.DateField(auto_now_add=True)
    tipo_grano = models.CharField(max_length=50)  # ejemplo: arroz, maíz

    def __str__(self):
        return f"Lote {self.codigo_lote} - {self.tipo_grano}"

class MedicionCalidad(models.Model):
    lote = models.ForeignKey(LoteGrano, on_delete=models.CASCADE)
    parametro = models.CharField(max_length=100)
    valor_medido = models.FloatField()
    cumple_estandar = models.BooleanField(null=True)

    def __str__(self):
        return f"{self.parametro} = {self.valor_medido}"