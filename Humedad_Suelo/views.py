from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import Medicion, Alerta, ConfiguracionRiego, SensorHumedad
from .serializers import MedicionSerializer, AlertaSerializer, ConfiSerializers, SensorSerializers

class MedicionList(generics.ListCreateAPIView):
    queryset = Medicion.objects.all()
    serializer_class = MedicionSerializer

class MedicionListDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Medicion.objects.all()
    serializer_class = MedicionSerializer

class AlertaList(generics.ListCreateAPIView):
    queryset = Alerta.objects.all()
    serializer_class = AlertaSerializer

class AlertaListDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Alerta.objects.all()
    serializer_class = AlertaSerializer

class ConfiViewList(generics.ListCreateAPIView):
    queryset = ConfiguracionRiego.objects.all()
    serializer_class = ConfiSerializers

class ConfiViewDelet(generics.RetrieveUpdateDestroyAPIView):
    queryset = ConfiguracionRiego.objects.all()
    serializer_class = ConfiSerializers

class SensorViewList(generics.ListCreateAPIView):
    queryset = SensorHumedad.objects.all()
    serializer_class = SensorSerializers

class SensorViewDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = SensorHumedad.objects.all()
    serializer_class = SensorSerializers