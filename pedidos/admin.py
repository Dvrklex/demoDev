from django.contrib import admin
from .models import Pedido, PedidoDetalle
# Register your models here.

#class PedidoAdmin()


admin.site.register([Pedido,PedidoDetalle])