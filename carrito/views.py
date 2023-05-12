from django.shortcuts import render,redirect
from .carrito import Carrito
from tienda.models import Producto

# Create your views here.
def agregar_producto_carro(request,producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id )
    
    carrito.agregar(producto=producto)    
    
    return redirect("tienda")

def eliminar_producto_carro(request,producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id )
    
    carrito.eliminar(producto=producto)    
    
    return redirect("tienda")

def restar_producto_carro(request,producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id )
    
    carrito.restar_producto(producto=producto)    
    
    return redirect("tienda")

def limpar_carro(request):
    carrito = Carrito(request)
    carrito.vaciar_carro()
    
    return redirect("tienda")