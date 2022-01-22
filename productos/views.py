from django.shortcuts import render

from .models import carouselproductos 


def carruselproductos (request):

    obj =carouselproductos.objects.all()
    context = {
        'obj':obj

    }
    return render(request, "productos/productos.html" , context)

def residencial(request):

   
    return render(request, "productos/residencial.html")

def industrial(request):

   
    return render(request, "productos/industrial.html")

def hospitalaria(request):

   
    return render(request, "productos/hospitalaria.html")

def veterinaria(request):

   
    return render(request, "productos/veterinaria.html")

def imnovadora(request):

   
    return render(request, "productos/imnovadora.html")

def producto_final(request):

    return render(request,"productos/producto_final.html")




