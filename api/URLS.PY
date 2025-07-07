from django.urls import path
from .views import (
    RegistroGetViewSet,
    RegistroPostViewSet,
    RegistroUpdateViewSet,
    RegistroDeleteViewSet,

    iniciaSecioViewSet,
    iniciaSecioPostViewSet,
    iniciaSecioUpdateViewSet,
    iniciaSecioDeleteViewSet,

    AdminInventarioViewSet,
    AdminInventarioPostViewSet,
    AdminInventarioUpdateViewSet,
    AdminInventarioDeleteViewSet,

    AdminGestionViewSet,
    AdminGestionPostViewSet,
    AdminGestionUpdateViewSet,
    AdminGestionDeleteViewSet,

    AdminPerdidasViewSet,
    AdminPerdidasPostViewSet,
    AdminPerdidasUpdateViewSet,
    AdminPerdidasDeleteViewSet,

    InventarioCosechaViewSet,
    InventarioCosechaPostViewSet,
    InventarioCosechaUpdateViewSet,
    InventarioCosechaDeleteViewSet,

    ReporteAdminViewSet,
    ReporteAdminPostViewSet,
    ReporteAdminUpdateViewSet,
    ReporteAdminDeleteViewSet,

    SemillaViewSet,
    SemillaPostViewSet,
    SemillaUpdateViewSet,
    SemillaDeleteViewSet

)

urlpatterns = [
    # ---Registro---
    path('registro-GET/', RegistroGetViewSet.as_view()),
    path('registro-POST/', RegistroPostViewSet.as_view()),
    path('registro-UPTADE/<int:pk>/', RegistroUpdateViewSet.as_view()),
    path('registro-DELETE/<int:pk>/', RegistroDeleteViewSet.as_view()),


    path('Inicio-Sesion-GET/', iniciaSecioViewSet.as_view()),
    path('Inicio-Sesion-POST/', iniciaSecioPostViewSet.as_view()),
    path('Inicio-Sesion-UPDATE/<int:pk>/', iniciaSecioUpdateViewSet.as_view()),
    path('Inicio-Sesion-DELETE/<int:pk>/', iniciaSecioDeleteViewSet.as_view()),

    path('Inventario-GET/', AdminInventarioViewSet.as_view()),
    path('Inventario-POST/', AdminInventarioPostViewSet.as_view()),
    path('Inventario-UPDATE/<int:pk>/', AdminInventarioUpdateViewSet.as_view()),
    path('Inventario-DELETE/<int:pk>/', AdminInventarioDeleteViewSet.as_view()),

    path('Gestion-GET/', AdminGestionViewSet.as_view()),
    path('Gestion-POST/', AdminGestionPostViewSet.as_view()),
    path('Gestion-UPDATE/<int:pk>/', AdminGestionUpdateViewSet.as_view()),
    path('Gestion-DELETE/<int:pk>/', AdminGestionDeleteViewSet.as_view()),

    path('Perdidas-GET/', AdminPerdidasViewSet.as_view()),
    path('Perdidas-PORT/', AdminPerdidasPostViewSet.as_view()),
    path('Perdidas-UPDATE/<int:pk>/', AdminPerdidasUpdateViewSet.as_view()),
    path('Perdidas-DELETE/<int:pk>/', AdminPerdidasDeleteViewSet.as_view()),

    path('Cosecha-GET/', InventarioCosechaViewSet.as_view()),
    path('Cosecha-POST/', InventarioCosechaPostViewSet.as_view()),
    path('Cosecha-UPDATE/<int:pk>/', InventarioCosechaUpdateViewSet.as_view()),
    path('Cosecha-DELETE/<int:pk>/', InventarioCosechaDeleteViewSet.as_view()),

    path('Reportes-GET/', ReporteAdminViewSet.as_view()),
    path('Reportes-POST/', ReporteAdminPostViewSet.as_view()),
    path('Reportes-UPDATE/<int:pk>/', ReporteAdminUpdateViewSet.as_view()),
    path('Reportes-DELETE/<int:pk>/', ReporteAdminDeleteViewSet.as_view()),

    path('Semillas-GET/', SemillaViewSet.as_view()),
    path('Semillas-POST/', SemillaPostViewSet.as_view()),
    path('Semillas-UPDATE/<int:pk>/', SemillaUpdateViewSet.as_view()),
    path('Semillas-DELETE/<int:pk>/', SemillaDeleteViewSet.as_view()),
]
