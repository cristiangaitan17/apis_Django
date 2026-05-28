from rest_framework import serializers
from .models import Categoria, Producto, Resena, Carrito, CarritoItem, Pedido, PedidoItem

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
        read_only_fields = ['id', 'fecha_creacion', 'fecha_modificacion']

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'
        read_only_fields = ['id', 'fecha_creacion', 'fecha_modificacion']

class ResenaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resena
        fields = '__all__'
        read_only_fields = ['id', 'fecha_creacion', 'fecha_modificacion']

class CarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrito
        fields = '__all__'
        read_only_fields = ['id', 'fecha_creacion', 'fecha_modificacion']

class CarritoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarritoItem
        fields = '__all__'
        read_only_fields = ['id', 'fecha_creacion', 'fecha_modificacion']

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'
        read_only_fields = ['id', 'fecha_creacion', 'fecha_modificacion']

class PedidoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidoItem
        fields = '__all__'
        read_only_fields = ['id', 'fecha_creacion', 'fecha_modificacion']