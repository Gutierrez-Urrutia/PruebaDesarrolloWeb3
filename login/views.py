from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import FormLogin

def login_view(request):
    if request.method == 'POST':
        form = FormLogin(request.POST)
        if form.is_valid():
            user = form.user
            login(request, user)
            return redirect('home.html')
        # No crear una nueva instancia de FormLogin, usar la existente
        return render(request, 'login.html', {'form': form})
    else:
        form = FormLogin()
    return render(request, 'login.html', {'form': form})