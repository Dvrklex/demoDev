from django.shortcuts import render
from tienda.models import CategoriaProducto, Producto
# Create your views here.
# Vista Tienda

def tienda(request):
    view_name= 'Tienda'
    context =  {
        "tienda":"tienda/css/tienda.css",
        "producto":"tienda/css/producto.css",
        "carrito":"tienda/css/tienda.css",
        "subNav":"tienda/css/sub_nav.css"
        
        }
    
    productos = Producto.objects.all()
    return render(request, 'tienda/tienda.html',{'view_name': view_name,'context':context,'productos':productos})
