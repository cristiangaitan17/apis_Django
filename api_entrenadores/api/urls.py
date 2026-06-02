from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    EntrenadorViewSet,
    EntrenadorDocumentoViewSet,
    SolicitudEntrenadorViewSet,
)

router = DefaultRouter()

# Registro de endpoints del API
router.register(r'entrenadores', EntrenadorViewSet)
router.register(r'entrenador-documentos', EntrenadorDocumentoViewSet)
router.register(r'solicitudes-entrenador', SolicitudEntrenadorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
