from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import rutinas, grupos_musculares, ejercicios
from .serializers import RutinaSerializer, GrupoMuscularSerializer, EjercicioSerializer


def realizar_borrado_logico(instance):
    instance.activo = False
    instance.save()

class RutinaViewSet(viewsets.ModelViewSet):
    queryset = rutinas.objects.all() 
    serializer_class = RutinaSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        realizar_borrado_logico(instance)
        return Response({'message': 'Rutina desactivada'}, status=status.HTTP_200_OK)

class GrupoMuscularViewSet(viewsets.ModelViewSet):
    queryset = grupos_musculares.objects.all()
    serializer_class = GrupoMuscularSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        realizar_borrado_logico(instance)
        return Response({'message': 'Grupo muscular desactivado'}, status=status.HTTP_200_OK)

class EjercicioViewSet(viewsets.ModelViewSet):
    queryset = ejercicios.objects.all()
    serializer_class = EjercicioSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        realizar_borrado_logico(instance)
        return Response({'message': 'Ejercicio desactivado'}, status=status.HTTP_200_OK)