from django.shortcuts import render

# Create your views here.
# Vista Contacto

def contacto(request):
    view_name= 'Contacto'
    return render(request, 'contacto/contacto.html',{'view_name': view_name})
