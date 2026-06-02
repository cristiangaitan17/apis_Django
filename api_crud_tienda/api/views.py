from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Categoria, Producto, Resena, Carrito, CarritoItem, Pedido, PedidoItem
from .serializers import (
    CategoriaSerializer, ProductoSerializer, ResenaSerializer,
    CarritoSerializer, CarritoItemSerializer, PedidoSerializer, PedidoItemSerializer
)

class BaseViewSet(viewsets.ModelViewSet):
    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response({'success': True, 'status': 200, 'message': 'Petición exitosa', 'data': serializer.data})

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'status': 201, 'message': 'Registro creado exitosamente', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'success': False, 'status': 400, 'message': 'Error al crear el registro', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(self.get_object())
            return Response({'success': True, 'status': 200, 'message': 'Petición exitosa', 'data': serializer.data})
        except:
            return Response({'success': False, 'status': 404, 'message': 'Registro no encontrado', 'data': {}}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(self.get_object(), data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'success': True, 'status': 200, 'message': 'Registro actualizado exitosamente', 'data': serializer.data})
            return Response({'success': False, 'status': 400, 'message': 'Error al actualizar', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'success': False, 'status': 404, 'message': 'Registro no encontrado', 'data': {}}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.activo = False
            instance.save()
            return Response({'success': True, 'status': 200, 'message': 'Registro desactivado exitosamente', 'data': {}})
        except:
            return Response({'success': False, 'status': 404, 'message': 'Registro no encontrado', 'data': {}}, status=status.HTTP_404_NOT_FOUND)


class CategoriaViewSet(BaseViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProductoViewSet(BaseViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ResenaViewSet(BaseViewSet):
    queryset = Resena.objects.all()
    serializer_class = ResenaSerializer

class CarritoViewSet(BaseViewSet):
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer

class CarritoItemViewSet(BaseViewSet):
    queryset = CarritoItem.objects.all()
    serializer_class = CarritoItemSerializer

class PedidoViewSet(BaseViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class PedidoItemViewSet(BaseViewSet):
    queryset = PedidoItem.objects.all()
    serializer_class = PedidoItemSerializer