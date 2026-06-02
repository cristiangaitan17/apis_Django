from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import (
    CategoriaViewSet, 
    ProductoViewSet, 
    ResenaViewSet,
    CarritoViewSet, 
    CarritoItemViewSet, 
    PedidoViewSet, 
    PedidoItemViewSet
)

from django.contrib import admin
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


router = DefaultRouter()
router.register(r'categorias_producto', CategoriaViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'resenas_producto', ResenaViewSet)
router.register(r'carritos', CarritoViewSet)
router.register(r'carrito_items', CarritoItemViewSet)
router.register(r'pedidos', PedidoViewSet)
router.register(r'pedido_items', PedidoItemViewSet)


urlpatterns = [
    path('', include(router.urls)),
]