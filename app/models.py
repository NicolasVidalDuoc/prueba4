from django.db import models

# Create your models here.
class Tipo(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    tipo = models.ForeignKey(Tipo, on_delete=models.PROTECT)
    fecha_fabricacion = models.DateField()

    def __str__(self):
        return self.nombre