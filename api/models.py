from django.db import models

# Create your models here.


class Registro(models.Model):
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    ROLE_CHOICES = [
        ('Agricultor', 'Agricultor'),
        ('Administrador', 'Administrador')
    ]
    NombreUsuario = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=15, unique=True)
    rol = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Seleccione su rol')
    def __str__(self):
        return f"{self.NombreUsuario} ({self.rol})"

class InicioSecion(models.Model):
    contraseña = models.CharField(max_length=20, unique=True)
    nombreUsuario = models.ForeignKey(Registro, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.nombreUsuario}"


class admingestion(models.Model):
    fechas = models.DateField()
    Cantidad_Productos = models.CharField(max_length=10)
    TIPO_COSECHA = [
        ('Papa', 'Papa'),
        ('Aguacate', 'Aguacate'),
        ('Cafe', 'Cafe'),
        ('Sandia', 'Sandia'),
    ]
    tipo_Cosecha = models.CharField(max_length=100, choices=TIPO_COSECHA)

    def __str__(self):
        return f"{self.fechas}, {self.Cantidad_Productos}"


class CantidadProducto(models.Model):
    Tipo_Producto = [
        ('Tractores','Tractores'),
        ('Insectisida','Insectisida'),
        ('Semillas','Semillas'),
        ('Maquinaria','Maquinaria'),
    ]

    producto = models.CharField(max_length=100, choices=Tipo_Producto)
    cantidadesproducto = models.CharField(max_length=100)
    # cosecha = models.ForeignKey(admingestion, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.producto}"


class GestioFechasAdmin(models.Model):
    Temporada = [
        ('Temporada 1','Temporada 1'),
        ('Temporada 2','Temporada 2'),
        ('Temporada 3','Temporada 3'),
        ('Temporada 4','Temporada 4'),
    ]

    temporadas = models.CharField(max_length=100, choices=Temporada)
    fecha = models.DateField()

    def __str__(self):
        return f"{self.temporadas}, {self.fecha}"


class adminventario(models.Model):
    Tipo_SEMILLA = [
        ('Alverja', 'Alverja'),
        ('Frijoles', 'Frijoles'),
        ('Cafe', 'Cafe'),
        ('Sandia', 'Sandia'),
        ('Papa', 'Papa'),
        ('Aguacate', 'Aguacate')
    ]

    Semillas = models.CharField(max_length=10, choices=Tipo_SEMILLA)
    CosechasRegistradas = models.CharField(max_length=10)
    PerdidasRegistradas = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.Semillas}"
    
class tipoCosecha(models.Model):
    TIPO_COSECHA = [
        ('Papa', 'Papa'),
        ('Aguacate', 'Aguacate'),
        ('Cafe', 'Cafe'),
        ('Sandia', 'Sandia'),
    ]
    tipo_cosecha = models.CharField(max_length=100, choices=TIPO_COSECHA)
    TEMPORADAS = [
        ('Temporada 1','Temporada 1'),
        ('Temporada 2','Temporada 2'),
        ('Temporada 3','Temporada 3'),
        ('Temporada 4','Temporada 4'),
    ]
    temporada = models.CharField(max_length=100, choices=TEMPORADAS)

    def __str__(self):
        return f"{self.tipo_cosecha}, {self.temporada}"
    

class reportesadministrador(models.Model):
    Activos_Registrados = models.BigIntegerField()
    Pasivos_Registrados = models.BigIntegerField()
    Gnanacias_Registradas = models.BigIntegerField()

    def __str__(self):
        return f"{self.Gnanacias_Registradas}"
    

class semillaTipo(models.Model):
    Tipo_SEMILLA = [
        ('Alverja', 'Alverja'),
        ('Frijoles', 'Frijoles'),
        ('Cafe', 'Cafe'),
        ('Sandia', 'Sandia')
    ]
    tipo_semilla = models.CharField(max_length=100, choices=Tipo_SEMILLA)
    cantidad = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.tipo_semilla}"