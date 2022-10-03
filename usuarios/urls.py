from rest_framework import routers
from .api import UserViewSet

router = routers.DefaultRouter()

router.register('api/usuario' , UserViewSet, 'usuario')

urlpatterns = router.urls