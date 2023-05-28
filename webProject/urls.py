"""webProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webProject_app.urls')), #si dejo el path vacío, se importan los urls de la aplicación webProject_app sin necesidad de poner el path de la aplicación
    path('servicios/', include('servicios.urls')), #importo los urls de la aplicación servicios
    path('blog/', include('blog.urls')),
    path('contacto/', include('contacto.urls')),
    path('tienda/',include('tienda.urls')),
    path('carrito/',include('carrito.urls')),
    path('auth/',include('autenticacion.urls')),
]
