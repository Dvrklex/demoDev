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
                
                send_email.send()  
                #email de confirmacion  
                email_confirmacion = EmailMessage(
                "Confirmación de recepción de consulta",
                "Hemos recibido tu consulta. En las proximas horas nos pondremos en contacto contigo.\n Detalles de la consulta: \n\n Remitente: {} \n Asunto: {} \n Mensaje: {} \n\n\n Gracias por contactarnos. \n\n Atte. \n Equipo de Soporte de DemoDEV".format(email,asunto,mensaje),
                "",[email])
                
                email_confirmacion.send()
                return redirect("/contacto/?valid")
            except:
                print('Ha ocurrido un error')
                return redirect("/contacto/?invalid")
        else:
            return redirect("/contacto/?incomplete")
    
        
        
    return render(request, 'contacto/contacto.html',{'view_name': view_name, 'form': FormularioContacto})
