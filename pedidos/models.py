from django.db import models
from django.contrib.auth import get_user_model
from tienda.models import Producto
from django.db.models import F,Sum, FloatField
# Create your models here.

User = get_user_model()


class Pedido(models.Model):
    user = models.ForeignKey(User,verbose_name='Usuario' ,on_delete=models.CASCADE)
    creado= models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.id
    
    
    @property
    def total(self):
        return self.PedidoDetalle_set.aggregate(
            total = Sum(F("Precio")*F("Cantidad"), output_field = FloatField)            
        )["total"]
    
    class Meta: 
        db_table = 'Pedido'
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

        ordering=["id"]
        
        
class PedidoDetalle(models.Model):
    user = models.ForeignKey(User,verbose_name='Usuario' ,on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto,verbose_name='Producto' ,on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido,verbose_name='N° Pedido' ,on_delete=models.CASCADE)
    cantidad = models.IntegerField(verbose_name="Cantidad",default=1)
    creado = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f'{self.cantidad} unidades de {self.producto.nombre}'
    
    class Meta: 
        db_table = 'PedidoDetalle'
        verbose_name = 'Detalle Pedido'
        verbose_name_plural = 'Detalles Pedidos'

        ordering=["id"]