from django.db import models

# Create your models here.


class Registro(models.Model):
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    ROLE_CHOICES = [
        ('Agricultor', 'Agricultor'),
        ('Administrador', 'Administrador'),
    ]
    NombreUsuario = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=15)
    rol = models.CharField(max_length=20, choices=ROLE_CHOICES )
    def __str__(self):
        return f"{self.NombreUsuario} ({self.rol})"

class InicioSecion(models.Model):
    contraseña = models.CharField(max_length=20, unique=True)
    nombreUsuario = models.ForeignKey(Registro, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.nombreUsuario}"
