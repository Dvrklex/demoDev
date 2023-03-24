from django.shortcuts import render
from blog.models import Post, Categoria
# Create your views here.


# Vista Blog

def blog(request):
    view_name = 'Blog'
    posts = Post.objects.all() #importamos todos los objetos dentro de la clase Servicio
    return render(request, 'blog/blog.html',{'view_name': view_name, 'posts': posts})

def categoria(request, categoria_id):
    view_name = 'Categoria'
    categoria = Categoria.objects.get(id=categoria_id)
    posts = Post.objects.filter(categoria=categoria)
    # print('Este es el post de la categoria: ', post)
    return render(request, 'blog/categoria.html',{'view_name': view_name, 'categoria': categoria, 'posts': posts})