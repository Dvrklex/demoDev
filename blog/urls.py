from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.blog, name='Blog'),
    path('categoria/<int:categoria_id>/', views.categoria, name='categoria')
]

#Leer las imagenes de la carpeta media en el navegador
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)