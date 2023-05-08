from django.db import models

# Create your models here.

class CategoriaProducto (models.Model):
    nombre = models.CharField(verbose_name="Categoria",max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    udpated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="Categoria Producto"
        verbose_name_plural = "Categorias Productos"

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(verbose_name="Producto", max_length=100)
    descripcion = models.CharField(verbose_name="Descripcion", max_length=300)
    categoria = models.ForeignKey(CategoriaProducto, verbose_name="Categoria",on_delete=models.CASCADE)
    imagen = models.ImageField(verbose_name="Imagen", upload_to="tienda", null=True, blank=True)
    precio = models.FloatField(verbose_name="Precio")
    disponibilidad = models.BooleanField(verbose_name="Disponibilidad",default=True)
    created = models.DateTimeField(auto_now_add=True)
    udpated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        
    def __str__(self):
        return self.nombre