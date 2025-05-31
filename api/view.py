from .models import Registro, InicioSecion
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from .serializers import UsuarioSerializer, inicioSecionSerializer
from rest_framework.decorators import api_view
from rest_framework.response import responses
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404


class RegistroViewSet(viewsets.ModelViewSet):
    queryset = Registro.objects.all()
    serializer_class = UsuarioSerializer


class iniciaSecioViewSet(viewsets.ModelViewSet):
    queryset = InicioSecion.objects.all()
    serializer_class = inicioSecionSerializer


# Inicio de secsion cuando el usuario ya esta registrado
@api_view(['POST'])
def registro(request):
    serializer = UsuarioSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()

        user = Registro.objects.get(username = serializer.data['nombreUsuario'])
        user.set_password(serializer.data['contraseña'])
        user.save()

        token = token.objects.create(user=user)
        return responses({'token:': token.key, "user": serializer.data})
    
    return responses(serializer.errors)


# Verificacion del usuario y contraseña 
@api_view(['POST'])
def iniciosesion(request):
    user = get_object_or_404 (InicioSecion, username=request.data['nombreUsuario'], password=request.data['contraseña'])

    if not user.check_password(request.data['contraseña']):
        return responses({"error": "Contraseña incorrecta"})
    
    token = token.objects.get_or_create(user=user)
    serialiser =  inicioSecionSerializer(isinstance=user)

    return responses({"token": token.key, "user": serialiser.data})
