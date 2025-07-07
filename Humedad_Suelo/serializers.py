from rest_framework import serializers
from .models import SensorHumedad, Medicion, Alerta, ConfiguracionRiego

class MedicionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicion
        fields = '__all__'

class AlertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alerta
        fields = '__all__'

class SensorSerializers(serializers.ModelSerializer):
    class Meta:
        model = SensorHumedad
        fields = '__all__'

class ConfiSerializers(serializers.ModelSerializer):
    class Meta:
        model = ConfiguracionRiego
        fields = '__all__'