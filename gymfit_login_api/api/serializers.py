from rest_framework import serializers
from .models import Administrador, Usuario, Login


class AdministradorSerializer(serializers.ModelSerializer):
    activo = serializers.BooleanField(default=True, required=False)
    class Meta:
        model = Administrador  # 👈 ¡Añade esta línea que faltaba!
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    activo = serializers.BooleanField(default=True, required=False)
    class Meta:
        model = Usuario
        fields = '__all__'


class LoginSerializer(serializers.ModelSerializer):
    activo = serializers.BooleanField(default=True, required=False)
    class Meta:
        model = Login
        fields = '__all__'
