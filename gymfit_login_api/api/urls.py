from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdministradorViewSet, UsuarioViewSet, LoginViewSet

router = DefaultRouter()

# Registro de endpoints del API
router.register(r'administradores', AdministradorViewSet)
router.register(r'usuarios', UsuarioViewSet)
router.register(r'login', LoginViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
