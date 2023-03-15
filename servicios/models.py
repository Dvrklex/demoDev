from django.db import models

# Create your models here.
class Servicio(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.TextField()
    imagen = models.ImageField() #para subir imagenes necesitamos instalar pillow pip install pillow
    created = models.DateTimeField(auto_now_add=True) #cuando se crea el registro
    updated = models.DateTimeField(auto_now_add=True) #cuando se actualiza el registro

    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'

    def __str__(self):
        return self.titulo