from django.shortcuts import render
from crud.models import Comic

# Create your views here.
def index(request):

    comics = Comic.objects.all()
    return render(request, 'index.html', {'comics': comics})