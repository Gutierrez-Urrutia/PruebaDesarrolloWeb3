from django.shortcuts import render, redirect
from .models import Comic
from .forms import FormComic

# Create your views here.
def crud(request):
    context = {}
    return render(request, 'crud.html', context)

def listar(request):
    comics = Comic.objects.all()
    return render(request, 'listar.html', {'comics': comics})

def crear(request):
    if request.method == "POST":
        form = FormComic(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar')
    else:
        form = FormComic()
    return render(request, 'crear.html', {'form': form})

def eliminar(request, id):
    comic = Comic.objects.get(id=id)
    if comic:
        comic.delete()
        return redirect('listar')
    else:
        message = "No se encontró el comic"
        return redirect('listar')

def editar(request, id):
    comic = Comic.objects.get(id=id)
    if comic:
        if request.method == "POST":
            form = FormComic(request.POST, instance=comic)
            if form.is_valid():
                form.save()
                return redirect('listar')
        else:
            form = FormComic(instance=comic)
        return render(request, 'editar.html', {'form': form})