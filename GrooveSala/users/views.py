from django.shortcuts import render, redirect

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

from users.forms import RegisterForm
from users.models import UserProfile
# <--------------------------------------------- USER -------------------------------------------->

def login_view(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        context = {
            'form':form
        }
        return render(request, 'users/login.html', context=context)
    
    elif request.method == 'POST':
        form = AuthenticationForm(request=request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('index')

        else:
            form = AuthenticationForm()
            context = {
                'form':form,
                'errors':'Usuario y/o Contraseña incorrectos!',
            }
            return render(request, 'users/login.html', context=context)

def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        context = {
            'form': form
        }
        return render(request, 'users/signup.html', context=context)
    
    elif request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            return redirect('login')

        context = {
            'errors': form.errors,
            'form':RegisterForm()
        }
        return render(request, 'users/signup.html', context=context)
