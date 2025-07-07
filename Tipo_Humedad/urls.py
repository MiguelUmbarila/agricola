from django.urls import path
from .views import HumedadViewSet, HumedadViewDelete

urlpatterns = [
    path ('humedad/', HumedadViewSet.as_view()),
    path ('humedad-delete/<int:pk>/', HumedadViewDelete.as_view())
    ]