from django.contrib import admin
from .models import Tipo, Producto, Contacto

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "tipo", "fecha_fabricacion"]

admin.site.register(Tipo)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Contacto)