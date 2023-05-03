from django.shortcuts import render
from servicios.models import Servicio
# Create your views here.
# Vista Servicios

def servicios(request):
    view_name= 'Servicios'
    context = {"css_file":'servicios/css/servicios.css'}
    servicios = Servicio.objects.all() #importamos todos los objetos dentro de la clase Servicio
    return render(request, 'servicios/servicios.html',{'view_name': view_name,"context":context ,'servicios':servicios} )





