from django.shortcuts import render
from .models import Pais, Region, Comuna


# Create your views here.
#def registro(request):
#    context = {}
#    return render(request, 'registro.html', context)

def registro(request):
    paises = Pais.objects.all()
    regiones = Region.objects.all()
    comunas = Comuna.objects.all()
    return render(request, 'registro.html', {'paises': paises, 'regiones': regiones, 'comunas': comunas})
