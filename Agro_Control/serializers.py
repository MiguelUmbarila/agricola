from rest_framework import serializers
from .models import (
    Cultivo, DatoClimatico, ModeloPredictivo,
    Alerta, Recomendacion
)

# Serializer para Cultivo
class CultivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cultivo
        fields = '__all__'

# Serializer para DatoClimatico 
class DatoClimaticoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatoClimatico
        fields = '__all__'

# Serializer para ModeloPredictivo 
class ModeloPredictivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModeloPredictivo
        fields = '__all__'

    # Serializer para Alerta 
class AlertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alerta
        fields = '__all__'

        # Serializer para Recomendacion 
class RecomendacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recomendacion
        fields = '__all__'