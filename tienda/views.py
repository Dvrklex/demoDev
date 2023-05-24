from django.shortcuts import render
from tienda.models import CategoriaProducto, Producto

from carrito.carrito import Carrito
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
    categorias = CategoriaProducto.objects.all()
    print('Categorias',categorias)

    return render(request, 'tienda/tienda.html',{
        'view_name': view_name,
        'context':context,
        'productos':productos,
        'categorias': categorias,
        })


def view_product(request, product_id):
    view_name = 'view_product'
    context =  {
        "tienda":"tienda/css/tienda.css",
        "producto":"tienda/css/producto.css",
        "carrito":"tienda/css/tienda.css",
        "subNav":"tienda/css/sub_nav.css"
        
        }
    
    producto  = Producto.objects.get(id=product_id)
    categorias = CategoriaProducto.objects.all()

    return render(request, 'tienda/producto.html',{
        'view_name':view_name,
        'context':context,
        'producto':producto,
        'product_id':product_id,
        'categorias': categorias,
        })

def view_carrito(request):
    carrito = Carrito(request)  # Crear instancia de la clase Carrito
    elementos_carro = carrito.carro  # Obtener los elementos del carro
    context = {
        'carrito':'tienda/css/carrito.css',
        'subNav':'tienda/css/sub_nav.css'       
               }
    total_carro = 0
    for key, value in elementos_carro.items():
        value['total'] = float(value['precio']) * int(value['cantidad'])
        total_carro += float(value['total'])

    return render(request, 'tienda/carrito.html',{'elementos_carro':elementos_carro,'context':context,'total_carro':total_carro})


def categoria_producto(request, categoria_id):
    view_name = 'Categoria'
    context = {
        "tienda":"tienda/css/tienda.css",
        "producto":"tienda/css/producto.css",
        "carrito":"tienda/css/tienda.css",
        "subNav":"tienda/css/sub_nav.css",
        'no_categoria':'tienda/css/no_categoria.css'}
    categoria = CategoriaProducto.objects.get(id=categoria_id)
    productos = Producto.objects.filter(categoria=categoria)
    categorias = CategoriaProducto.objects.all()
    return render(request, 'tienda/categoria_producto.html', {
        'view_name':view_name,
        'context':context,
        'categoria': categoria,
        'productos': productos,
        'categorias': categorias,
        'categoria_id':categoria_id,
        })
    
def search_bar (request):
    view_name = 'Search'
    context = {
        "tienda":"tienda/css/tienda.css",
        "producto":"tienda/css/producto.css",
        "carrito":"tienda/css/tienda.css",
        "subNav":"tienda/css/sub_nav.css",
        'no_categoria':'tienda/css/no_categoria.css'
        
        }
    query = request.GET.get('search')
    results = Producto.objects.filter(nombre__icontains=query) 
    categorias = CategoriaProducto.objects.all()
    return render(request, 'tienda/search_result.html', {
        'view_name':view_name,
        'query':query,
        'context':context, 
        'results': results, 
        'categorias': categorias
        })
