class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get("carro", {})
        
        if not carro:
            self.carro = self.session['carro'] = {}
        else:
            self.carro = carro
            
    def guardar_carro(self):
        self.session['carro'] = self.carro
        self.session.modified = True
        print("Carro guardado/actualizado")
        
    def agregar(self, producto):
        if str(producto.id) not in self.carro.keys():
            self.carro[producto.id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": str(producto.precio),
                "cantidad": 1,
                "imagen": producto.imagen.url
            }
        else:
            for key, value in self.carro.items():
                if key == str(producto.id):
                    value["cantidad"] += 1
                    break
        self.guardar_carro()
        
        
    def eliminar(self, producto_id):
        if str(producto_id) in self.carro:
            del self.carro[str(producto_id)]
            self.guardar_carro()
        else:
            print("No se encontró el producto en el carro")
            
    def restar_producto(self, producto):
        for key, value in self.carro.items():
            if key == str(producto.id):
                value["cantidad"] -= 1
                if value["cantidad"] < 1:
                    self.eliminar(producto)
                break
        self.guardar_carro()
        print("Entro a Restar Producto")
        
    def vaciar_carro(self):
        self.session["carro"] = {}
        self.session.modified = True

    def ver_carro(self):
        return self.carro