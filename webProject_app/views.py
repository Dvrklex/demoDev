from django.shortcuts import render, redirect, HttpResponse
from blog.models import Post

# Vista Home

def home(request):
    view_name= 'Home' #Esto es para que el JavaScript de la vista home.html pueda identificar la vista en la que se encuentra, y así poder cambiar el color del botón de la barra de navegación.
    latest_posts = Post.objects.all().order_by('-created')[:6]
    for post in latest_posts:
        print(post.titulo)
    return render(request, 'webProject_app/home.html',{'view_name': view_name,"latest_posts":latest_posts})

# Vista Tienda

def tienda(request):
    view_name= 'Tienda'
    return render(request, 'webProject_app/tienda.html',{'view_name': view_name})

# Vista Blog

def blog(request):
    view_name= 'Blog'
    return render(request, 'webProject_app/blog.html',{'view_name': view_name})

# Vista Contacto

def contacto(request):
    view_name= 'Contacto'
    return render(request, 'webProject_app/contacto.html',{'view_name': view_name})

