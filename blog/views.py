from django.shortcuts import render,redirect
from blog.models import Post, Categoria
from django.conf import settings

# Create your views here.


# Vista Blog

def blog(request):
    view_name = 'Blog'
    context =  {
        "css_file":"blog/css/blog.css",
        "subMenu":"blog/css/sub_nav.css",
        "busqueda":"blog/css/busqueda.css",
        "catFilter":"blog/css/post.css"
        
        }
    posts = Post.objects.all().order_by('-created')
    categorias = Categoria.objects.all()
    return render(request, 'blog/blog.html',{'view_name': view_name,"context":context , 'posts': posts, 'categorias': categorias})

# Vista Categoria filtrada
def categoria(request, categoria_id):
    view_name = 'Categoria'
    context = {
        "css_file":"blog/css/blog.css",
        "subMenu":"blog/css/sub_nav.css",
        "busqueda":"blog/css/busqueda.css",
        "catFilter":"blog/css/post.css"
        
        }
    categoria = Categoria.objects.get(id=categoria_id)
    posts = Post.objects.filter(categoria=categoria)
    categorias = Categoria.objects.all()
    return render(request, 'blog/categoria.html', {
        'view_name': view_name,
        'context': context,
        'categoria': categoria,
        'posts': posts,
        'categorias': categorias,
        'categoria_id': categoria_id # Pasar el categoria_id a la plantilla
    })
    
# Vista Buscador
def buscar(request):
    view_name = 'Buscar'
    context = {
         "css_file":"blog/css/blog.css",
        "subMenu":"blog/css/sub_nav.css",
        "busqueda":"blog/css/busqueda.css"
        
        }
    query = request.GET.get('search')
    results = Post.objects.filter(titulo__icontains=query) | Post.objects.filter(contenido__icontains=query)
    categorias = Categoria.objects.all()
    return render(request, 'blog/busqueda.html', {
        'view_name':view_name,
        'context':context, 
        'results': results, 
        'categorias': categorias
        })


#View one post 
def view_post(request, post_id): 
    view_name = 'View_post'
    context = {
        "css_file":"blog/css/post.css",
        "subMenu":"blog/css/sub_nav.css"
        }
    post = Post.objects.get(id=post_id)
    categorias = Categoria.objects.all()
    return render(request, 'blog/post.html', {'view_name':view_name,"context":context ,'post': post,'post_id':post_id,'categorias': categorias})


#Create post 
def create_post(request):
    view_name = 'Create_Post'
    context = {
        "css_file": "blog/css/create_post.css",
    }
    categorias = Categoria.objects.all()
    
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        categoria_id = request.POST.get('categoria')
        contenido = request.POST.get('contenido')
        categoria_id = request.POST.get('categoria')
        categoria = Categoria.objects.get(id=categoria_id)
        imagen = request.FILES.get('imagen')
        autor = request.user

        if imagen and imagen.size > settings.MAX_UPLOAD_SIZE:
            error_message = 'La imagen es demasiado grande. El tamaño máximo permitido es de 5 MB.'
            return render(request, 'blog/create_post.html', {
                'view_name': view_name,
                'context': context,
                'categorias': categorias,
                'error_message': error_message,
                'titulo': titulo,
                'categoria_id': int(categoria_id),
                'contenido': contenido
            })
        else:
            post = Post(titulo=titulo, contenido=contenido, imagen=imagen, autor=autor)
            post.save()
            post.categoria.set([categoria])
            return redirect('Blog')

    return render(request, 'blog/create_post.html', {
        'view_name': view_name,
        'context': context,
        'categorias': categorias
    })
