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


def view_product(request, product_id):
    view_name = 'view_product'
    context =  {
        "tienda":"tienda/css/tienda.css",
        "producto":"tienda/css/producto.css",
        "carrito":"tienda/css/tienda.css",
        "subNav":"tienda/css/sub_nav.css"
        
        }
    
    producto  = Producto.objects.get(id=product_id)
    
    return render(request, 'tienda/producto.html',{'view_name':view_name,'context':context,'producto':producto,'product_id':product_id})