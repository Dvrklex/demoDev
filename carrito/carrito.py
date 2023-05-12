class Carrito:
    def __init__ (self, request):
        self.request = request
        self.session = request.session
        self.carro = self.session.get("carro")
        
        if not self.carro:
            self.carro = self.session['carro']={}
        else:
            self.carro = self.session['carro']
            
    def agregar(self,producto):
        if str(producto.id) not in self.carro.keys():
            self.carro[producto.id] = {
                "producto_id":producto.id,
                "nombre":producto.nombre,
                "precio":str(producto.precio),
                "cantidad":1,
                "imagen":producto.imagen.url
            }
        else:
            for key,value in self.carro.items():
                if key==str(producto.id):
                    value["cantidad"] = value["cantidad"]+1
                    break
        self.guardar_carro()
        print("Producto agregado")
        
    def guardar_carro(self):
        self.session['carro'] = self.carro
        self.session.modified=True
        print("Carro guardado/actualizado")
        
    def eliminar(self,producto):
        if str(producto.id) in self.carro:
            del self.carro[producto.id]
            self.guardar_carro()
        print("Producto Eliminado")
            
    def restar_producto(self,producto):
        for key,value in self.carro.items():
            if key==str(producto.id):
                value["cantidad"] = value["cantidad"]-1
                if value["cantidad"] < 1:
                    self.eliminar(producto)
                break
        self.guardar_carro()
        print("Entro a Restar Producto")
        
    def vaciar_carro(self):
        self.session["carro"]={}
        self.session.modified=True
        
        
        