from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import (
    Cultivo, DatoClimatico, ModeloPredictivo,
    Alerta, Recomendacion
)
from .serializers import (
    CultivoSerializer, DatoClimaticoSerializer, ModeloPredictivoSerializer,
    AlertaSerializer, RecomendacionSerializer
)

# Cultivo
class CultivoListCreateView(generics.ListCreateAPIView):
    queryset = Cultivo.objects.all()
    serializer_class = CultivoSerializer

class CultivoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cultivo.objects.all()
    serializer_class = CultivoSerializer

# DatoClimatico
class DatoClimaticoListCreateView(generics.ListCreateAPIView):
    queryset = DatoClimatico.objects.all()
    serializer_class = DatoClimaticoSerializer

class DatoClimaticoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DatoClimatico.objects.all()
    serializer_class = DatoClimaticoSerializer

# ModeloPredictivo
class ModeloPredictivoListCreateView(generics.ListCreateAPIView):
    queryset = ModeloPredictivo.objects.all()
    serializer_class = ModeloPredictivoSerializer

class ModeloPredictivoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ModeloPredictivo.objects.all()
    serializer_class = ModeloPredictivoSerializer

# Alerta
class AlertaListCreateView(generics.ListCreateAPIView):
    queryset = Alerta.objects.all()
    serializer_class = AlertaSerializer

class AlertaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Alerta.objects.all()
    serializer_class = AlertaSerializer

# Recomendacion
class RecomendacionListCreateView(generics.ListCreateAPIView):
    queryset = Recomendacion.objects.all()
    serializer_class = RecomendacionSerializer

class RecomendacionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recomendacion.objects.all()
    serializer_class = RecomendacionSerializer