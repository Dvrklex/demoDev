from django.shortcuts import render
from blog.models import Post, Categoria
# Create your views here.


# Vista Blog

def blog(request):
    view_name = 'Blog'
    posts = Post.objects.all() #importamos todos los objetos dentro de la clase Servicio
    return render(request, 'blog/blog.html',{'view_name': view_name, 'posts': posts})

# Vista Categoria filtrada
def categoria(request, categoria_id):
    view_name = 'Categoria'
    categoria = Categoria.objects.get(id=categoria_id)
    posts = Post.objects.filter(categoria=categoria)
    categorias = Categoria.objects.all()
    return render(request, 'blog/categoria.html', {
        'view_name': view_name,
        'categoria': categoria,
        'posts': posts,
        'categorias': categorias,
        'categoria_id': categoria_id # Pasar el categoria_id a la plantilla
    })
    
# Vista Buscador
def buscar(request):
    query = request.GET.get('search')
    results = Post.objects.filter(titulo__icontains=query) | Post.objects.filter(contenido__icontains=query)
    categorias = Categoria.objects.all()
    return render(request, 'blog/busqueda.html', {'results': results, 'categorias': categorias})

def view_post(request, post_id):
    post = Post.objects.get(id=post_id)
    categorias = Categoria.objects.all()
    return render(request, 'blog/post.html', {'post': post,'post_id':post_id,'categorias': categorias})