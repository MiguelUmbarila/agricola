from django.shortcuts import render

from rest_framework import generics
from .models import LoteGrano, MedicionCalidad, EstandarCalidad
from .serializers import LoteGranoSerializer, MedicionCalidadSerializer, EstandarCalidadSerializer

class LoteGranoViewList(generics.ListCreateAPIView):
    queryset = LoteGrano.objects.all()
    serializer_class = LoteGranoSerializer

class LoteGranoViewDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = LoteGrano.objects.all()
    serializer_class = LoteGranoSerializer

class MedicionCalidadVieList(generics.ListCreateAPIView):
    queryset = MedicionCalidad.objects.all()
    serializer_class = MedicionCalidadSerializer

class MedicionCalidadViewDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = MedicionCalidad.objects.all()
    serializer_class = MedicionCalidadSerializer

class EstandarCalidadViewlist(generics.ListCreateAPIView):
    queryset = EstandarCalidad.objects.all()
    serializer_class = EstandarCalidadSerializer

class EstandarCalidadViewDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = EstandarCalidad.objects.all()
    serializer_class = EstandarCalidadSerializer