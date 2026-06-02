from rest_framework import viewsets
from rest_framework.response import Response  # 👈 ¡Añade esta línea!
from rest_framework import viewsets, status
from .models import Entrenador, EntrenadorDocumento, SolicitudEntrenador
from .serializers import (
    EntrenadorSerializer,
    EntrenadorDocumentoSerializer,
    SolicitudEntrenadorSerializer,
)
def realizar_borrado_logico(instance):
    instance.activo = False
    instance.save()
    


# CRUD de tabla entrenadores (GET, POST, PUT, DELETE)
class EntrenadorViewSet(viewsets.ModelViewSet):
    queryset = Entrenador.objects.all()
    serializer_class = EntrenadorSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        realizar_borrado_logico(instance)
        return Response({'message': 'Entrenador desactivado'}, status=status.HTTP_200_OK)



# CRUD de tabla entrenador_documentos (GET, POST, PUT, DELETE)
class EntrenadorDocumentoViewSet(viewsets.ModelViewSet):
    queryset = EntrenadorDocumento.objects.all()
    serializer_class = EntrenadorDocumentoSerializer
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        realizar_borrado_logico(instance)
        return Response({'message': 'Entrenador desactivado'}, status=status.HTTP_200_OK)



# CRUD de tabla solicitudes_entrenador (GET, POST, PUT, DELETE)
class SolicitudEntrenadorViewSet(viewsets.ModelViewSet):
    queryset = SolicitudEntrenador.objects.all()
    serializer_class = SolicitudEntrenadorSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        realizar_borrado_logico(instance)
        return Response({'message': 'solicitud desactivada'}, status=status.HTTP_200_OK)
