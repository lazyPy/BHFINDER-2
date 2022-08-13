from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import *


# Create your views here.

def homePage(request):
    return render(request, 'home.html')


def loginPage(request):
    #if request.user.is_authenticated:
    #    return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'login.html')


def registerPage(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {
        'form': form,
    }
    return render(request, 'register.html', context)
