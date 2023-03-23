from django.db import models
from django.contrib.auth.models import User
# Create your models here.
 
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True) #cuando se crea el registro
    updated = models.DateTimeField(auto_now_add=True) #cuando se actualiza el registro

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nombre 
    
class Post(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='post', null=True, blank=True) #opcional cargar una imagen en cada post
    autor = models.ForeignKey(User, on_delete=models.CASCADE) #eliminar en cascada todos los post de un usuario
    categoria = models.ManyToManyField(Categoria) #relación mucho a mucho
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now_add=True) 

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.titulo