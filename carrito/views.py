from django.shortcuts import render,redirect
from .carrito import Carrito
from tienda.models import Producto

# Create your views here.
def agregar_producto_carro(request,producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id )
    
    carrito.agregar(producto=producto)    
    return redirect("Tienda")

def eliminar_producto_carro(request,producto_id):
    carrito = Carrito(request)
    carrito.eliminar(producto_id)    
    return redirect("Carrito")

def restar_producto_carro(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    
    carrito.restar_producto(producto)
    
    return redirect("Carrito")


def limpar_carro(request):
    carrito = Carrito(request)
    carrito.vaciar_carro()
    return redirect("Tienda")

