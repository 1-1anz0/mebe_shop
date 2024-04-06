from django.shortcuts import render
from carts.models import Carts
from users.forms import *
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

def login(request):
    form = UserLoginForm()
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)

        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            session_key = request.session.session_key

            if user:
                auth.login(request, user)
                messages.success(request, f'{username} - Siz Akkaundynyza girdiniz')

                if session_key:
                    Carts.objects.filter(session_key=session_key).update(user=user)

                if request.POST.get('next', None):
                    return HttpResponseRedirect(request.POST.get('next'))
                return HttpResponseRedirect(reverse('main:index'))
            
        else:
            form = UserLoginForm()

    context = {
        'form': form,
 
    }

    return render(request, 'users/login.html', context)

def registration(request):

    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)

        if form.is_valid():
            form.save()
            session_key = request.session.session_key
            user = form.instance
            auth.login(request, user)
            messages.success(request, f'{user.username} - Siz Registrasiya edildiniz')
            if session_key:
                    Carts.objects.filter(session_key=session_key).update(user=user)
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserCreationForm()
    
    context = {
        'form': form
    }

    return render(request, 'users/registration.html', context)

@login_required
def profile(request):

    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, f'{request.user.username} Sizin Akkaundynyza Uytgetmeler girirzildi')
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = ProfileForm(instance=request.user)
    
    context = {
        'form': form,
    }
    
    return render(request, 'users/profile.html', context)

def user_cart(request):
    
    return render(request, 'users/user_cart.html')

@login_required
def logout(request):
    messages.success(request, f'{request.user.username} - Siz Akkaundynyzdan Cykdynyz')
    auth.logout(request)
    return redirect(reverse('main:index'))