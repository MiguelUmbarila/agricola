from django.shortcuts import render

# Create your views here.

from .models import Registro, InicioSecion, admInventario, adminGestio, adminPerdidas, invetarioCosecha, reportesadministrador, semillaTipo
from rest_framework import generics
from .serializers import UsuarioSerializer, InisioSesionSerializer, AdminInventarioSerializer, AdminGestionSerializer, AdminPerdidasSerializer, InventarioCosechaSerializar, ReportesAdminSerializer, SemillaTipoSerializer


# ------Registro------
class RegistroGetViewSet(generics.ListAPIView):
    queryset = Registro.objects.all()
    serializer_class = UsuarioSerializer

class RegistroPostViewSet(generics.CreateAPIView):
    queryset = Registro.objects.all()
    serializer_class = UsuarioSerializer

class RegistroUpdateViewSet(generics.RetrieveUpdateAPIView):
    queryset = Registro.objects.all()
    serializer_class = UsuarioSerializer
    
class RegistroDeleteViewSet(generics.DestroyAPIView):
    queryset = Registro.objects.all()
    serializer_class = UsuarioSerializer



# ----Inicio Sesion----
class iniciaSecioViewSet(generics.ListAPIView):
    queryset = InicioSecion.objects.all() 
    serializer_class = InisioSesionSerializer
class iniciaSecioPostViewSet(generics.CreateAPIView):
    queryset = InicioSecion.objects.all()
    serializer_class = InisioSesionSerializer
class iniciaSecioUpdateViewSet(generics.RetrieveUpdateAPIView):
    queryset = InicioSecion.objects.all()
    serializer_class = InisioSesionSerializer
class iniciaSecioDeleteViewSet(generics.DestroyAPIView):
    queryset = InicioSecion.objects.all()
    serializer_class = InisioSesionSerializer


# ----Inventario de Administrador----
class AdminInventarioViewSet(generics.ListAPIView):
    queryset = admInventario.objects.all()
    serializer_class = AdminInventarioSerializer
class AdminInventarioPostViewSet(generics.CreateAPIView):
    queryset = admInventario.objects.all()
    serializer_class = AdminInventarioSerializer
class AdminInventarioUpdateViewSet(generics.RetrieveUpdateAPIView):
    queryset = admInventario.objects.all()
    serializer_class = AdminInventarioSerializer
class AdminInventarioDeleteViewSet(generics.DestroyAPIView):
    queryset = admInventario.objects.all()
    serializer_class = AdminInventarioSerializer



# ----Gestion de Administrador----
class AdminGestionViewSet(generics.ListAPIView):
    queryset = adminGestio.objects.all()
    serializer_class = AdminGestionSerializer
class AdminGestionPostViewSet(generics.CreateAPIView):
    queryset = adminGestio.objects.all()
    serializer_class = AdminGestionSerializer
class AdminGestionUpdateViewSet(generics.RetrieveUpdateAPIView):
    queryset = adminGestio.objects.all()
    serializer_class = AdminGestionSerializer
class AdminGestionDeleteViewSet(generics.DestroyAPIView):
    queryset = adminGestio.objects.all()
    serializer_class = AdminGestionSerializer



# ----Perdidas de Administrador----
class AdminPerdidasViewSet(generics.ListAPIView):
    queryset = adminPerdidas.objects.all()
    serializer_class = AdminPerdidasSerializer
class AdminPerdidasPostViewSet(generics.CreateAPIView):
    queryset = adminPerdidas.objects.all()
    serializer_class = AdminPerdidasSerializer
class AdminPerdidasUpdateViewSet(generics.RetrieveUpdateAPIView):
    queryset = adminPerdidas.objects.all()
    serializer_class = AdminPerdidasSerializer
class AdminPerdidasDeleteViewSet(generics.DestroyAPIView):
    queryset = adminPerdidas.objects.all()
    serializer_class = AdminPerdidasSerializer




# ----Inventario de Cosechas----
class InventarioCosechaViewSet(generics.ListAPIView):
    queryset = invetarioCosecha.objects.all()
    serializer_class = InventarioCosechaSerializar
class InventarioCosechaPostViewSet(generics.CreateAPIView):
    queryset = invetarioCosecha.objects.all()
    serializer_class = InventarioCosechaSerializar
class InventarioCosechaUpdateViewSet(generics.RetrieveUpdateAPIView):
    queryset = invetarioCosecha.objects.all()
    serializer_class = InventarioCosechaSerializar
class InventarioCosechaDeleteViewSet(generics.DestroyAPIView):
    queryset = invetarioCosecha.objects.all()
    serializer_class = InventarioCosechaSerializar



# ----Reporte de Administrador----
class ReporteAdminViewSet(generics.ListAPIView):
    queryset = reportesadministrador.objects.all()
    serializer_class = ReportesAdminSerializer
class ReporteAdminPostViewSet(generics.CreateAPIView):
    queryset = reportesadministrador.objects.all()
    serializer_class = ReportesAdminSerializer
class ReporteAdminUpdateViewSet(generics.RetrieveUpdateAPIView):
    queryset = reportesadministrador.objects.all()
    serializer_class = ReportesAdminSerializer
class ReporteAdminDeleteViewSet(generics.DestroyAPIView):
    queryset = reportesadministrador.objects.all()
    serializer_class = ReportesAdminSerializer



# ----Tipo de semilla----
class SemillaViewSet(generics.ListAPIView):
    queryset = semillaTipo.objects.all()
    serializer_class = SemillaTipoSerializer
class SemillaPostViewSet(generics.CreateAPIView):
    queryset = semillaTipo.objects.all()
    serializer_class = SemillaTipoSerializer
class SemillaUpdateViewSet(generics.RetrieveUpdateAPIView):
    queryset = semillaTipo.objects.all()
    serializer_class = SemillaTipoSerializer
class SemillaDeleteViewSet(generics.DestroyAPIView):
    queryset = semillaTipo.objects.all()
    serializer_class = SemillaTipoSerializer


