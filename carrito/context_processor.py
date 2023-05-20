#from .carrito import Carrito
#from .carrito import Carrito
def importe_total_carro(request):
    total = 0
    if "carro" in request.session:
        carro = request.session["carro"]
        for key, value in carro.items():
            total += int(value["cantidad"])
    return {"importe_total_carro": total}
