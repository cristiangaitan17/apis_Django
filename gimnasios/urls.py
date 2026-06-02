from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SedeGimnasioViewSet, GimnasioClaseViewSet, ResenaGimnasioViewSet

router = DefaultRouter()
router.register(r'sedes', SedeGimnasioViewSet)
router.register(r'clases', GimnasioClaseViewSet)
router.register(r'resenas', ResenaGimnasioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]