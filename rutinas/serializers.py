from rest_framework import serializers

from .models import rutinas
class RutinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = rutinas
        fields = '__all__'