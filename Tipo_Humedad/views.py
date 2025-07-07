from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Humedad
from .serializers import HumedadSerializer

# Create your views here.
class HumedadViewSet(generics.ListCreateAPIView):
    queryset = Humedad.objects.all()
    serializer_class = HumedadSerializer

class HumedadViewDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Humedad.objects.all()
    serializer_class = HumedadSerializer

