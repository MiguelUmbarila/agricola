from django.urls import path
from .views import (
    TerrenoList, TerrenoDetail,
    DronList, DronDetail,
    ParametroFertilizacionList, ParametroFertilizacionDetail,
    RutaList, RutaDetail,
    EjecucionList, EjecucionDetail,
    ReporteList, ReporteDetail
)

urlpatterns = [
    # Terrenos
    path('terrenos/', TerrenoList.as_view()),
    path('terrenos/<int:pk>/', TerrenoDetail.as_view()),

    # Drones
    path('drones/', DronList.as_view()),
    path('drones/<int:pk>/', DronDetail.as_view()),

    # Parámetros de fertilización
    path('parametros-fertilizacion/', ParametroFertilizacionList.as_view()),
    path('parametros-fertilizacion/<int:pk>/', ParametroFertilizacionDetail.as_view()),

    # Rutas
    path('rutas/', RutaList.as_view()),
    path('rutas/<int:pk>/', RutaDetail.as_view()),

    # Ejecuciones
    path('ejecuciones/', EjecucionList.as_view()),
    path('ejecuciones/<int:pk>/', EjecucionDetail.as_view()),

    # Reportes
    path('reportes/', ReporteList.as_view()),
    path('reportes/<int:pk>/', ReporteDetail.as_view()),
]