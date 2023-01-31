from django.shortcuts import render, redirect

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate

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
                context = {
                    'message':f'Bienvenido {username}!'
                }
                return render(request, 'index.html',context=context)

        else:
            form = AuthenticationForm()
            context = {
                'form':form,
                'errors':'Usuario y/o Contraseña incorrectos!',
            }
            return render(request, 'users/login.html', context=context)

def register(request):
    if request.method == 'GET':
        form = UserCreationForm()
        context = {
            'form': form
        }
        return render(request, 'users/signup.html', context=context)
    
    elif request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

        context = {
            'errors': form.errors,
            'form':UserCreationForm()
        }
        return render(request, 'users/signup.html', context=context)
