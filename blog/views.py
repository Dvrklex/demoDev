from django.shortcuts import render
from blog.models import Post
# Create your views here.


# Vista Blog

def blog(request):
    view_name= 'Blog'
    posts = Post.objects.all() #importamos todos los objetos dentro de la clase Servicio
    return render(request, 'blog/blog.html',{'view_name': view_name, 'posts': posts})