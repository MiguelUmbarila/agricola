from rest_framework import routers
from .api import RegistroViewSet, AdminViewSet, AgricultorViewSet

router = routers.DefaultRouter()

router.register('registro', RegistroViewSet)
router.register('agricultor', AdminViewSet)
router.register('administrador', AgricultorViewSet)

urlpatterns = router.urls