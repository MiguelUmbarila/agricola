from .models import Registro, Administrador, Agricultor
from rest_framework import viewsets, permissions
from .serializers import UsuarioSerializer, AgricultorSerializer, AdminSerializer


class RegistroViewSet(viewsets.ModelViewSet):
    queryset = Registro.objects.all()
    # permission_classes = [permissions.AllowAny]
    serializer_class = UsuarioSerializer


class AdminViewSet(viewsets.ModelViewSet):
    queryset = Administrador.objects.all()
    serializer_class = AdminSerializer


class AgricultorViewSet(viewsets.ModelViewSet):
    queryset = Agricultor.objects.all()
    serializer_class = AgricultorSerializer