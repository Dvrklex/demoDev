#from .carrito import Carrito
#from .carrito import Carrito
def importe_total_carro(request):
    # total = 0
    cantidad = 0
    if request.user.is_authenticated:
        if "carro" in request.session:
            carro = request.session["carro"]
            for key, value in carro.items():
                # total += float(value['precio'])
                cantidad += int(value["cantidad"])
    # else: 
    #     cantidad="Debes hacer login"
    return {'cantidad_productos':cantidad}
