from django.http import JsonResponse
from django.shortcuts import render #redirect
from .models import Pais, Region, Comuna
from django.views.decorators.csrf import csrf_exempt
#from .forms import ClienteForm



# Create your views here.
#def registro(request):
#    context = {}
#    return render(request, 'registro.html', context)

def registro(request):
    if(request.method == 'GET'):
        paises = Pais.objects.all()
        regiones = Region.objects.all()
        comunas = Comuna.objects.all()
        return render(request, 'registro.html', {'paises': paises, 'regiones': regiones, 'comunas': comunas})
    else:
        request.POST[""]
def todos_los_paises(request):
    paises = Pais.objects.all()
    paises_list = list(paises.values('id_pais', 'nombre_pais'))  # Asumiendo que el modelo tiene estos campos
    return JsonResponse(paises_list, safe=False)

def regiones_por_pais(request, id_pais):
    regiones = Region.objects.filter(id_pais=id_pais)
    regiones_list = list(regiones.values('id_region', 'nombre_region'))  # Asumiendo que el modelo tiene estos campos
    return JsonResponse(regiones_list, safe=False)

def comunas_por_region(request, id_region):
    # Filtrar las comunas que pertenecen a la región especificada
    comunas = Comuna.objects.filter(id_region=id_region)
    # Crear una lista de diccionarios con la información de las comunas
    comunas_list = list(comunas.values('id_comuna', 'nombre_comuna'))
    # Devolver la respuesta en formato JSON
    return JsonResponse(comunas_list, safe=False)

# @csrf_exempt
# def registrar_cliente(request):
#     if request.method == 'POST':
#         form = ClienteForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = ClienteForm()
#     return render(request, 'registro.html', {'form': form})