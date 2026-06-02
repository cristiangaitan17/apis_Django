from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import SedeGimnasio, GimnasioClase, ResenaGimnasio
from .serializers import (
    SedeGimnasioSerializer,
    GimnasioClaseSerializer,
    ResenaGimnasioSerializer
)


class BaseViewSet(viewsets.ModelViewSet):
    """ViewSet base con respuestas personalizadas y soft delete"""
    
    def get_queryset(self):
        # Solo muestra registros activos en las listas
        return self.queryset.filter(activo=True)
    
    def list(self, request):
        """Listar solo registros activos"""
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'success': True,
            'status': 200,
            'message': 'Petición exitosa',
            'data': serializer.data
        })
    
    def create(self, request):
        """Crear un nuevo registro"""
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True,
                'status': 201,
                'message': 'Registro creado exitosamente',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            'success': False,
            'status': 400,
            'message': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        """Obtener un registro por ID (incluye inactivos)"""
        try:
            # Buscar en TODOS los registros (sin filtrar por activo)
            instance = self.queryset.model.objects.get(pk=pk)
            serializer = self.get_serializer(instance)
            return Response({
                'success': True,
                'status': 200,
                'message': 'Petición exitosa',
                'data': serializer.data
            })
        except self.queryset.model.DoesNotExist:
            return Response({
                'success': False,
                'status': 404,
                'message': 'Registro no encontrado'
            }, status=status.HTTP_404_NOT_FOUND)
    
    def update(self, request, pk=None):
        """Actualizar un registro (parcial o total)"""
        try:
            instance = self.queryset.model.objects.get(pk=pk)
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'success': True,
                    'status': 200,
                    'message': 'Registro actualizado exitosamente',
                    'data': serializer.data
                })
            return Response({
                'success': False,
                'status': 400,
                'message': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        except self.queryset.model.DoesNotExist:
            return Response({
                'success': False,
                'status': 404,
                'message': 'Registro no encontrado'
            }, status=status.HTTP_404_NOT_FOUND)
    
    def destroy(self, request, pk=None):
        """Soft delete: solo cambia activo a False"""
        try:
            instance = self.queryset.model.objects.get(pk=pk)
            instance.activo = False
            instance.save()
            return Response({
                'success': True,
                'status': 200,
                'message': 'Registro desactivado exitosamente'
            })
        except self.queryset.model.DoesNotExist:
            return Response({
                'success': False,
                'status': 404,
                'message': 'Registro no encontrado'
            }, status=status.HTTP_404_NOT_FOUND)


class SedeGimnasioViewSet(BaseViewSet):
    queryset = SedeGimnasio.objects.all()
    serializer_class = SedeGimnasioSerializer


class GimnasioClaseViewSet(BaseViewSet):
    queryset = GimnasioClase.objects.all()
    serializer_class = GimnasioClaseSerializer


class ResenaGimnasioViewSet(BaseViewSet):
    queryset = ResenaGimnasio.objects.all()
    serializer_class = ResenaGimnasioSerializer