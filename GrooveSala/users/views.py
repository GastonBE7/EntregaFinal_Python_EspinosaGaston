from django.shortcuts import render, redirect

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

from django.contrib.auth.decorators import login_required
from users.forms import RegisterForm, UserProfileForm
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

# <--------------------------------------------- PROFILE -------------------------------------------->
def update_user_profile(request):
    if request.method == 'GET':
        form = UserProfileForm(
            initial= {
                'user':request.user.profile.user,
                'members':request.user.profile.members, 
                'musical_genre':request.user.profile.musical_genre,
                'contact':request.user.profile.contact,
                'profile_picture':request.user.profile.profile_picture,
            }
        )
        context = {
            'form': form
        }
        return render(request, 'users/update-profile.html', context=context)
    
    elif request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        user = request.user
        if form.is_valid():
            user.profile.members=form.cleaned_data.get('members')
            user.profile.musical_genre=form.cleaned_data.get('musical_genre')
            user.profile.contact=form.cleaned_data.get('contact')
            user.profile.profile_picture=form.cleaned_data.get('profile_picture')
            user.profile.save()
            return redirect('index')

        context = {
            'errors': form.errors,
            'form':UserProfileForm()
        }
        return render(request, 'users/signup.html', context=context)