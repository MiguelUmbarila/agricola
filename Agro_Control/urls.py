from django.urls import path
from .views import (
    CultivoListCreateView, CultivoDetailView,
    DatoClimaticoListCreateView, DatoClimaticoDetailView,
    ModeloPredictivoListCreateView, ModeloPredictivoDetailView,
    AlertaListCreateView, AlertaDetailView,
    RecomendacionListCreateView, RecomendacionDetailView,
)

urlpatterns = [


    # Cultivo
    path('cultivos/', CultivoListCreateView.as_view()),
    path('cultivos/<int:pk>/', CultivoDetailView.as_view()),

    # DatoClimatico
    path('datos_climaticos/', DatoClimaticoListCreateView.as_view()),
    path('datos_climaticos/<int:pk>/', DatoClimaticoDetailView.as_view()),

    # ModeloPredictivo
    path('modelos_predictivos/', ModeloPredictivoListCreateView.as_view()),
    path('modelos_predictivos/<int:pk>/', ModeloPredictivoDetailView.as_view()),

    # Alerta
    path('alertas/', AlertaListCreateView.as_view()),
    path('alertas/<int:pk>/', AlertaDetailView.as_view()),

    # Recomendacion
    path('recomendaciones/', RecomendacionListCreateView.as_view()),
    path('recomendaciones/<int:pk>/', RecomendacionDetailView.as_view()),
]