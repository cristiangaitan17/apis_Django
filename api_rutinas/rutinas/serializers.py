from rest_framework import serializers
# Importación única y completa de todos tus modelos
from .models import rutinas, grupos_musculares, ejercicios

class RutinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = rutinas
        fields = '__all__'
        
class GrupoMuscularSerializer(serializers.ModelSerializer):
    class Meta:
        model = grupos_musculares
        fields = '__all__'
        
class EjercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ejercicios
        fields = '__all__'