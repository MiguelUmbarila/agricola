from rest_framework import serializers
from .models import Registro, InicioSecion, adminventario, admingestion, CantidadProducto, GestioFechasAdmin, reportesadministrador, semillaTipo, tipoCosecha

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registro
        fields = [
            'id',
            'Nombre',
            'Apellido',
            'NombreUsuario',
            'contraseña',
            'rol'
        ]

class inicioSecionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InicioSecion
        fields = '__all__'


class adminInventarioSerializer(serializers.ModelSerializer):
    class Meta: 
        model = adminventario
        fields = '__all__'


class adminGestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = admingestion
        fields = '__all__'


class cantidadProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CantidadProducto
        fields = '__all__'


class gestionFechasAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = GestioFechasAdmin
        fields = '__all__'


class reportesAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = reportesadministrador
        fields = '__all__'


class SemillaTipoSeralizer(serializers.ModelSerializer):
    class Meta:
        model = semillaTipo
        fields = '__all__'


class tipoCosechaSerializer(serializers.ModelSerializer):
    class Meta:
        model = tipoCosecha
        fields = '__all__'