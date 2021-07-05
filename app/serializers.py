from django.db.models import fields
from .models import Producto, Tipo
from rest_framework import serializers

class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields = ['url', 'nombre']

class ProductoSerializer(serializers.ModelSerializer):
    nombre_tipo = serializers.CharField(read_only=True, source="tipo.nombre")
    class Meta:
        model = Producto
        fields = ['url', 'nombre', 'nombre_tipo', 'precio', 'descripcion', 'tipo', 'fecha_fabricacion', 'image']
        