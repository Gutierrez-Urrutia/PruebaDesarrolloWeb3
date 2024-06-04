from django.shortcuts import render

from django.shortcuts import render

# Create your views here.
def registro(request):
    context = {}
    return render(request, 'registro.html', context)