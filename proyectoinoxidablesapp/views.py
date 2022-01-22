from django.shortcuts import render

from .models import carousel



# Create your views here.

def home(request):

    obj =carousel.objects.all()
    context = {
        'obj':obj

    }
    return render(request, "proyectoinoxidablesapp/home.html" , context)




