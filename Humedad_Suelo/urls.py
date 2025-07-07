from django.urls import path
from .views import MedicionList, AlertaList,MedicionListDelete, AlertaListDelete, ConfiViewList, ConfiViewDelet, SensorViewList, SensorViewDelete

urlpatterns = [
    path('mediciones/', MedicionList.as_view()),
    path('mediciones/<int:pk>/', MedicionListDelete.as_view()),

    path('alertas/', AlertaList.as_view()),
    path('alertas/<int:pk>/', AlertaListDelete.as_view()),

    path('Agregar-Configurar/', ConfiViewList.as_view()),
    path('Eliminar-Configurar/<int:pk>/', ConfiViewDelet.as_view()),

    path('Agregar-Sensor/', SensorViewList.as_view()),
    path('Agregar-Sensor/<int:pk>/', SensorViewDelete.as_view()),

]