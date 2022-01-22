from django.shortcuts import render
from .models import Proyecto

from django.urls import path

# Create your views here.
def proyectos(request):
    proyectos=Proyecto.objects.all()

    return render(request,"proyectos/proyectos.html", {"proyectos":proyectos})