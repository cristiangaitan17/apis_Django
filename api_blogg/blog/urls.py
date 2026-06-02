from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from .views import (
    CategoriaViewSet,
    NoticiaViewSet,
    ArticuloSeccionViewSet,
    NutricionViewSet,
    DietaComidaViewSet,
    ComentarioComunidadViewSet,
    RespuestaComentarioViewSet
)

# Configuración de Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="API Blog - The House Fit",
        default_version='v1',
        description="API para gestión de blog: categorías, noticias, nutrición y comentarios",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@thehousefit.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

# Router
router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'noticias', NoticiaViewSet)
router.register(r'articulos-secciones', ArticuloSeccionViewSet)
router.register(r'nutricion', NutricionViewSet)
router.register(r'dieta-comidas', DietaComidaViewSet)
router.register(r'comentarios', ComentarioComunidadViewSet)
router.register(r'respuestas', RespuestaComentarioViewSet)

urlpatterns = [
    # API routes (Browsable API de DRF)
    path('', include(router.urls)),  
    
    # Swagger documentation
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]