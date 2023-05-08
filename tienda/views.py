from django.shortcuts import render

# Create your views here.
# Vista Tienda

def tienda(request):
    view_name= 'Tienda'
    return render(request, 'tienda/tienda.html',{'view_name': view_name})
