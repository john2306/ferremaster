from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path('', views.carruselproductos, name="Productos"),
    path('residencial/', views.residencial, name="residencial"),
    path('industrial/', views.industrial, name="industrial"),
    path('hospitalaria/', views.hospitalaria, name="hospitalaria"),
    path('veterinaria/', views.veterinaria, name="veterinaria"),
    path('imnovadora/', views.imnovadora, name="imnovadora"),
    path('producto_final/', views.producto_final, name="producto_final")

   
   
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)
