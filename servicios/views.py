from django.shortcuts import render
from servicios.models import Servicio
# Create your views here.
# Vista Servicios

def servicios(request):
    view_name= 'Servicios'
    servicios = Servicio.objects.all() #importamos todos los objetos dentro de la clase Servicio
    return render(request, 'servicios/servicios.html',{'view_name': view_name,'servicios':servicios} )





