from rest_framework import viewsets
from .models import Administrador, Usuario, Login
from .serializers import AdministradorSerializer, UsuarioSerializer, LoginSerializer


# CRUD de tabla administrador (GET, POST, PUT, DELETE)
class AdministradorViewSet(viewsets.ModelViewSet):
    queryset = Administrador.objects.all()
    serializer_class = AdministradorSerializer


# CRUD de tabla usuarios (GET, POST, PUT, DELETE)
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


# CRUD de tabla login (GET, POST, PUT, DELETE)
class LoginViewSet(viewsets.ModelViewSet):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer
