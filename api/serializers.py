from rest_framework import serializers
from .models import Registro, InicioSecion

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registro
        fields = '__all__'

class inicioSecionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InicioSecion
        fields = '__all__'