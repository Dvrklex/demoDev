from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage,send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import Pedido,PedidoDetalle
from carrito.carrito import Carrito
import os
from dotenv import load_dotenv
from .forms import FormularioPedido


# Create your views here.
load_dotenv('./.env')
email_host = os.getenv('EMAIL_HOST')



import os
from dotenv import load_dotenv
load_dotenv('./.env')

destinatario = os.getenv('EMAIL_DESTINATARIO')
# Create your views here.
# Vista Contacto
@login_required(login_url="/auth/login")
def formulario_pedidos(request):
    view_name= 'Pedidos'
    context = {'css_file':"pedidos/css/form.css"}
    #Datos del formulario   
    form = FormularioPedido(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            datos = form.cleaned_data
            nombre = request.POST.get("nombre")
            apellido = request.POST.get("apellido")
            calle = request.POST.get("calle")
            numero = request.POST.get("numero")
            tarjeta = request.POST.get("tarjeta")
            cvv = request.POST.get("cvv")
            
            if len(numero) <= 4 and len(tarjeta) == 16 and len(cvv) == 3:
                try:
                    pedido = Pedido.objects.create(user=request.user)
                    carrito = Carrito(request)
                    lineas_pedido = list()
                    
                    for key, value in carrito.carro.items():
                        lineas_pedido.append(PedidoDetalle(
                            producto_id=key,
                            cantidad=value["cantidad"],
                            user=request.user,
                            pedido=pedido
                        ))
                    
                    PedidoDetalle.objects.bulk_create(lineas_pedido)
                    
                    email_confirmacion(
                        pedido=pedido,
                        lineas_pedido=lineas_pedido,
                        nombre_usuario=request.user.username,
                        email_usuario=request.user.email
                    )
                    
                    carrito.vaciar_carro()
                    return redirect('Carrito')
                
                except:
                    print('Ha ocurrido un error')
                    return redirect("/pedidos/?incomplete") 
            
            else:
                print('Longitud de campo inválida')
                return redirect("/pedidos/?invalid")
        else:
            print('Datos del formulario inválidos')
            return redirect("/pedidos/?invalid")

    
            
            
    return render(request, 'pedidos/info.html',{"view_name":view_name,"context":context,"form":form})
            
            
            
             
    
def email_confirmacion(**kwargs):
    asunto = "Gracias por realizar el pedido en nuestra Tienda" 
    mensaje = render_to_string("pedidos/pedido.html",{
        "pedido": kwargs.get("pedido"),
        "lineas_pedido": kwargs.get("lineas_pedido"),
        "nombre_usuario": kwargs.get("nombre_usuario"),  
        "email_usuario": kwargs.get("email_usuario")   
    })
    mensaje_texto = strip_tags(mensaje)
    remitente = email_host
    destinatario = kwargs.get("email_usuario")
    
    send_mail(asunto, mensaje_texto, remitente, [destinatario], html_message=mensaje)

    
    

    
    
    
    