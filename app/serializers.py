from django.db.models import fields
from .models import Producto, Tipo
from rest_framework import serializers

class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    nombre_tipo = serializers.CharField(read_only=True, source="tipo.nombre")
    class Meta:
        model = Producto
        fields = '__all__'