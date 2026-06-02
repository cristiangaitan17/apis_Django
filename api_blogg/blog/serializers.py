from rest_framework import serializers
from .models import Categoria, Noticia, ArticuloSeccion, Nutricion, DietaComida, ComentarioComunidad, RespuestaComentario

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class NoticiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noticia
        fields = '__all__'

class ArticuloSeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticuloSeccion
        fields = '__all__'

class NutricionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nutricion
        fields = '__all__'

class DietaComidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DietaComida
        fields = '__all__'

class ComentarioComunidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComentarioComunidad
        fields = '__all__'

class RespuestaComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = RespuestaComentario
        fields = '__all__'