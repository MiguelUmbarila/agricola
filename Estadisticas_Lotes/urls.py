from django.urls import path
from .views import EstandarCalidadViewlist, EstandarCalidadViewDelete, LoteGranoViewList, LoteGranoViewDelete, MedicionCalidadVieList, MedicionCalidadViewDelete

urlpatterns = [
    path('lotes/', LoteGranoViewList.as_view()),
    path('lotes-Delete/<int:pk>/', LoteGranoViewDelete.as_view()),

    path('mediciones/', MedicionCalidadVieList.as_view()),
    path('mediciones-delete/<int:pk>/', MedicionCalidadViewDelete.as_view()),

    path('estandares/', EstandarCalidadViewlist.as_view()),
     path('estandares/<int:pk>/', EstandarCalidadViewDelete.as_view()),
]