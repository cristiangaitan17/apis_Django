from rest_framework import serializers
from .models import SedeGimnasio, GimnasioClase, ResenaGimnasio


class SedeGimnasioSerializer(serializers.ModelSerializer):
    class Meta:
        model = SedeGimnasio
        fields = '__all__'


class GimnasioClaseSerializer(serializers.ModelSerializer):
    gimnasio_nombre = serializers.ReadOnlyField(source='gimnasio.nombre')
    
    class Meta:
        model = GimnasioClase
        fields = '__all__'


class ResenaGimnasioSerializer(serializers.ModelSerializer):
    gimnasio_nombre = serializers.ReadOnlyField(source='gimnasio.nombre')
    
    class Meta:
        model = ResenaGimnasio
        fields = '__all__'