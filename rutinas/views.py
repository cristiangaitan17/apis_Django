from rest_framework import viewsets
from .models import rutinas, grupos_musculares, ejercicios
from .serializers import RutinaSerializer, GrupoMuscularSerializer, EjercicioSerializer

class RutinaViewSet(viewsets.ModelViewSet):
    queryset = rutinas.objects.all()
    serializer_class = RutinaSerializer

class GrupoMuscularViewSet(viewsets.ModelViewSet):
    queryset = grupos_musculares.objects.all()
    serializer_class = GrupoMuscularSerializer

class EjercicioViewSet(viewsets.ModelViewSet):
    queryset = ejercicios.objects.all()
    serializer_class = EjercicioSerializer