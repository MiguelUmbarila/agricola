from django.shortcuts import render

from rest_framework import generics
from .models import Terreno, Dron, ParametroFertilizacion, Ruta, Ejecucion, Reporte
from .serializers import (
    TerrenoSerializer, DronSerializer,
    ParametroFertilizacionSerializer, RutaSerializer,
    EjecucionSerializer, ReporteSerializer
)


# Vistas para Terreno
class TerrenoList(generics.ListCreateAPIView):
    queryset = Terreno.objects.all()
    serializer_class = TerrenoSerializer

class TerrenoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Terreno.objects.all()
    serializer_class = TerrenoSerializer

# Vistas para Dron
class DronList(generics.ListCreateAPIView):
    queryset = Dron.objects.all()
    serializer_class = DronSerializer

class DronDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dron.objects.all()
    serializer_class = DronSerializer

# Vistas para ParametroFertilizacion
class ParametroFertilizacionList(generics.ListCreateAPIView):
    queryset = ParametroFertilizacion.objects.all()
    serializer_class = ParametroFertilizacionSerializer

class ParametroFertilizacionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ParametroFertilizacion.objects.all()
    serializer_class = ParametroFertilizacionSerializer

# Vistas para Ruta
class RutaList(generics.ListCreateAPIView):
    queryset = Ruta.objects.all()
    serializer_class = RutaSerializer

class RutaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ruta.objects.all()
    serializer_class = RutaSerializer

# Vistas para Ejecucion
class EjecucionList(generics.ListCreateAPIView):
    queryset = Ejecucion.objects.all()
    serializer_class = EjecucionSerializer

class EjecucionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ejecucion.objects.all()
    serializer_class = EjecucionSerializer

# Vistas para Reporte
class ReporteList(generics.ListCreateAPIView):
    queryset = Reporte.objects.all()
    serializer_class = ReporteSerializer

class ReporteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reporte.objects.all()
    serializer_class = ReporteSerializer