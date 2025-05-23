from rest_framework import serializers
from .models import Registro, Agricultor, Administrador

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registro
        fields = '__all__'

class AgricultorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agricultor
        fields = '__all__'

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrador
        fields = '__all__'