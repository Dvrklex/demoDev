from .carrito import Carrito
def importe_total_carro(request):
    carrito = Carrito(request)
    total = 0 #Cantidad de productos en el carro
    if request.user.is_authenticated:
        for key, value in request.session["carro"].items():
            # total += float(value["precio"])*value["cantidad"]
            total += int(value["cantidad"])
            
    return {"importe_total_carro":total}