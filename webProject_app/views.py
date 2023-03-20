from django.shortcuts import render, redirect, HttpResponse

# Vista Home

def home(request):
    view_name= 'Home' #Esto es para que el JavaScript de la vista home.html pueda identificar la vista en la que se encuentra, y así poder cambiar el color del botón de la barra de navegación.
    return render(request, 'webProject_app/home.html',{'view_name': view_name})

# Vista Servicios

def servicios(request):
    view_name= 'Servicios'
    return render(request, 'webProject_app/servicios.html',{'view_name': view_name})

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

