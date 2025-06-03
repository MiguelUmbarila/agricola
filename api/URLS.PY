from rest_framework import routers
from .view import RegistroViewSet, iniciaSecioViewSet, adminGestionViewSet, adminInventarioViewSet, cantidadProductoViewSet, cosechaTipoViewSet, gestioFechasViewSet, reportesAdminViewSet, semillaTipoViewSet

router = routers.DefaultRouter()

router.register('registro', RegistroViewSet)
router.register('Inicio_Secion', iniciaSecioViewSet)
router.register('Gestion', adminGestionViewSet)
router.register('Inventario', adminInventarioViewSet)
router.register('Productos', cantidadProductoViewSet)
router.register('Cosecha', cosechaTipoViewSet)
router.register('Gestion-Fechas', gestioFechasViewSet)
router.register('Reportes', reportesAdminViewSet)
router.register('Semillas', semillaTipoViewSet)


urlpatterns = router.urls