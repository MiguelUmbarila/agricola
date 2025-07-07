from rest_framework import serializers
from .models import Humedad

class HumedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Humedad
        fields = [
            'id', 
            'humedad_actual', 
            'humedad_maxima', 
            'humedad_minima', 
            'humedad_solicitada']