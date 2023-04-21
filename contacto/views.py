from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from contacto.forms import FormularioContacto

import os
from dotenv import load_dotenv
load_dotenv('./.env')

destinatario = os.getenv('EMAIL_DESTINATARIO')
# Create your views here.
# Vista Contacto

def contacto(request):
    view_name= 'Contacto'
    #Datos del formulario   
    if request.method == 'POST':
        form = FormularioContacto(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            nombre = request.POST.get("nombre")
            apellido = request.POST.get("apellido")
            email = request.POST.get("email")
            asunto = request.POST.get("asunto")
            mensaje = request.POST.get("mensaje")

            send_email = EmailMessage(
                asunto,
                "{} {}, desde {} ha realizado la siguiente consulta: \n\n {}".format(nombre,apellido,email,mensaje),
                "",[destinatario], reply_to=[email])
            try:
                send_email.send()  # Llama al método send() en el objeto send_email
                print('Mensaje enviado')
                print(nombre,apellido,email,asunto,mensaje)
                return redirect("/contacto/?valid")
            except:
                print('Ha ocurrido un error')
                return redirect("/contacto/?invalid")
        else:
            return redirect("/contacto/?incomplete")
    
        
        
    return render(request, 'contacto/contacto.html',{'view_name': view_name, 'form': FormularioContacto})
