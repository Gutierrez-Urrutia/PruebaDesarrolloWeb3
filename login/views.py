from django.shortcuts import render, redirect
from .forms import FormLogin
from django.contrib.auth import login

def login_view(request):
    if request.method == 'POST':
        form = FormLogin(request.POST)
        if form.is_valid():
            user = form.user
            login(request, user)

            return redirect('home')
    else:
        form = FormLogin()
    return render(request, 'login.html', {'form': form})