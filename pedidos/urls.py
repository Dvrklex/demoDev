from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.formulario_pedidos, name='formulario_pedidos'),
    #path('/completo', views.procesar_pedido, name='procesar_pedido'),


    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 