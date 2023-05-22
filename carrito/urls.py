from django.urls import path
from . import views

app_name='carrito'
urlpatterns = [
    path("agregar/<int:producto_id>/", views.agregar_producto_carro, name='agregar'),
    path("eliminar/<int:producto_id>/", views.eliminar_producto_carro, name='eliminar'),
    path("restar/<int:producto_id>/", views.restar_producto_carro, name='restar'),
    path("sumar/<int:producto_id>/", views.sumar_producto_carro, name='sumar'),
    path("limpiar/", views.limpar_carro, name='limpiar'),
]