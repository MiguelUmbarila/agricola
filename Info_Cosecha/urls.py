from django.urls import path
from . import views

urlpatterns = [
    
    path('cultivos/', views.CultivoListCreateView.as_view()),
    path('cultivos/<int:pk>/', views.CultivoRetrieveUpdateDestroyView.as_view()),

    path('sensores/', views.SensorListCreateView.as_view()),
    path('sensores/<int:pk>/', views.SensorRetrieveUpdateDestroyView.as_view()),

    path('lecturas/', views.LecturaSensorListCreateView.as_view()),
    path('lecturas/<int:pk>/', views.LecturaSensorRetrieveUpdateDestroyView.as_view()),

    path('cosechas/', views.CosechaListCreateView.as_view()),
    path('cosechas/<int:pk>/', views.CosechaRetrieveUpdateDestroyView.as_view()),

    path('alertas/', views.AlertaListCreateView.as_view()),
    path('alertas/<int:pk>/', views.AlertaRetrieveUpdateDestroyView.as_view()),

    path('informes/', views.InformeListCreateView.as_view()),
    path('informes/<int:pk>/', views.InformeRetrieveUpdateDestroyView.as_view()),
]