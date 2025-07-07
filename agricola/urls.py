"""
URL configuration for agricola project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Agricola/', include('api.urls')),
    path('Agro-Control/', include('Agro_Control.urls')),
    path('Agro-Drones/', include('Agro_Drones.urls')),
    path('Estadistica-Lotes/', include('Estadisticas_Lotes.urls')),
    path('Humedad-Suelo/', include('Humedad_Suelo.urls')),
    path('Informacion-Cosecha/', include('Info_Cosecha.urls')),
    path('Riego-Automatizado/', include('Riego_Automatizado.urls')),
    path('Tipo-Humedad', include('Tipo_Humedad.urls')),
]
