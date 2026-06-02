from rest_framework import serializers
from .models import Entrenador, EntrenadorDocumento, SolicitudEntrenador


class EntrenadorSerializer(serializers.ModelSerializer):
    activo = serializers.BooleanField(default=True, required=False)
    class Meta:
        model = Entrenador
        fields = '__all__'


class EntrenadorDocumentoSerializer(serializers.ModelSerializer):
    activo = serializers.BooleanField(default=True, required=False)
    class Meta:
        model = EntrenadorDocumento
        fields = '__all__'


class SolicitudEntrenadorSerializer(serializers.ModelSerializer):
    activo = serializers.BooleanField(default=True, required=False)
    class Meta:
        model = SolicitudEntrenador
        fields = '__all__'
