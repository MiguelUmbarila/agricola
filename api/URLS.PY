from rest_framework import routers
from .view import RegistroViewSet, iniciaSecioViewSet

router = routers.DefaultRouter()

router.register('registro', RegistroViewSet)
router.register('inicio-secion', iniciaSecioViewSet)

urlpatterns = router.urls