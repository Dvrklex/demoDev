from django.shortcuts import render
from contacto.forms import FormularioContacto
# Create your views here.
# Vista Contacto

def contacto(request):
    view_name= 'Contacto'
    #Datos del formulario   
    if request.method == 'POST':
        form = FormularioContacto(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            print(datos)
            
        
        
    return render(request, 'contacto/contacto.html',{'view_name': view_name, 'form': FormularioContacto})
