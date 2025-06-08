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
    path('registro-GET', RegistroGetViewSet.as_view()),
    path('registro-POST', RegistroPostViewSet.as_view()),
    path('registro-UPTADE', RegistroUpdateViewSet.as_view()),
    path('registro-DELETE', RegistroDeleteViewSet.as_view()),


    path('Inicio-Sesion-GET', iniciaSecioViewSet.as_view()),
    path('Inicio-Sesion-POST', iniciaSecioPostViewSet.as_view()),
    path('Inicio-Sesion-UPDATE', iniciaSecioUpdateViewSet.as_view()),
    path('Inicio-Sesion-DELETE', iniciaSecioDeleteViewSet.as_view()),

    path('Inventario-GET', AdminInventarioViewSet.as_view()),
    path('Inventario-POST', AdminInventarioPostViewSet.as_view()),
    path('Inventario-UPDATE', AdminInventarioUpdateViewSet.as_view()),
    path('Inventario-DELETE', AdminInventarioDeleteViewSet.as_view()),

    path('Gestion-GET', AdminGestionViewSet.as_view()),
    path('Gestion-POST', AdminGestionPostViewSet.as_view()),
    path('Gestion-UPDATE', AdminGestionUpdateViewSet.as_view()),
    path('Gestion-DELETE', AdminGestionDeleteViewSet.as_view()),

    path('Perdidas-GET', AdminPerdidasViewSet.as_view()),
    path('Perdidas-PORT', AdminPerdidasPostViewSet.as_view()),
    path('Perdidas-UPDATE', AdminPerdidasUpdateViewSet.as_view()),
    path('Perdidas-DELETE', AdminPerdidasDeleteViewSet.as_view()),

    path('Cosecha-GET', InventarioCosechaViewSet.as_view()),
    path('Cosecha-POST', InventarioCosechaPostViewSet.as_view()),
    path('Cosecha-UPDATE', InventarioCosechaUpdateViewSet.as_view()),
    path('Cosecha-DELETE', InventarioCosechaDeleteViewSet.as_view()),

    path('Reportes-GET', ReporteAdminViewSet.as_view()),
    path('Reportes-POST', ReporteAdminPostViewSet.as_view()),
    path('Reportes-UPDATE', ReporteAdminUpdateViewSet.as_view()),
    path('Reportes-DELETE', ReporteAdminDeleteViewSet.as_view()),

    path('Semillas-GET', SemillaViewSet.as_view()),
    path('Semillas-POST', SemillaPostViewSet.as_view()),
    path('Semillas-UPDATE', SemillaUpdateViewSet.as_view()),
    path('Semillas-DELETE', SemillaDeleteViewSet.as_view()),
]
