from rest_framework import viewsets
from rest_framework import status  # 👈 ¡Añade esta línea!
from rest_framework.response import Response
from .models import Administrador, Usuario, Login
from .serializers import AdministradorSerializer, UsuarioSerializer, LoginSerializer

def realizar_borrado_logico(instance):
    instance.activo = False
    instance.save()

# CRUD de tabla administrador (GET, POST, PUT, DELETE)
class AdministradorViewSet(viewsets.ModelViewSet):
    queryset = Administrador.objects.all()
    serializer_class = AdministradorSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        realizar_borrado_logico(instance)
        return Response({'message': 'Administrador desactivado'}, status=status.HTTP_200_OK)

# CRUD de tabla usuarios (GET, POST, PUT, DELETE)
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        realizar_borrado_logico(instance)
        return Response({'message': 'Usuario desactivado'}, status=status.HTTP_200_OK)



# CRUD de tabla login (GET, POST, PUT, DELETE)
class LoginViewSet(viewsets.ModelViewSet):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer

def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        realizar_borrado_logico(instance)
        return Response({'message': 'Login desactivado'}, status=status.HTTP_200_OK)
