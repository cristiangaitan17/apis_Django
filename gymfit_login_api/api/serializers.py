from rest_framework import serializers
from .models import Administrador, Usuario, Login


class AdministradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrador
        fields = '__all__'


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = '__all__'
