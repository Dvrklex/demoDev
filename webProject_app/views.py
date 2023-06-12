from django.shortcuts import render, redirect, HttpResponse
from blog.models import Post
# from carrito.carrito import Carrito
# Vista Home

def home(request):
    view_name= 'Home' #Esto es para que el JavaScript de la vista home.html pueda identificar la vista en la que se encuentra, y así poder cambiar el color del botón de la barra de navegación.
    # carro = Carrito(request)
    context = {
        #Stylesheet
        "css_file":"webProject_app/css/slider.css",
        "home_css":"webProject_app/css/home.css",
        "swiperBundle":"webProject_app/css/swiper-bundle.min.css",
        #Scripts 
        "swiperBundleJs":"webProject_app/js/swiper-bundle.min.js",
        "sliderJs":"webProject_app/js/slider_script.js"
        }
    
    latest_posts = Post.objects.all().order_by('-created')[:6]
    # for post in latest_posts:
    #     print(post.titulo)
    return render(request, 'webProject_app/home.html',{'view_name': view_name,"context":context , "latest_posts":latest_posts})


# Vista Blog

def blog(request):
    view_name= 'Blog'
    return render(request, 'webProject_app/blog.html',{'view_name': view_name})


