from django.shortcuts import render, redirect, HttpResponse

# Vista Home

def home(request):
    return render(request, 'webProject_app/home.html')

# Vista Servicios

def servicios(request):
    return render(request, 'webProject_app/servicios.html')

# Vista Tienda

def tienda(request):
    return render(request, 'webProject_app/tienda.html')

# Vista Blog

def blog(request):
    return render(request, 'webProject_app/blog.html')

# Vista Contacto

def contacto(request):
    return render(request, 'webProject_app/contacto.html')

