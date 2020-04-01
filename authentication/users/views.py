from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index(request):
    if not request.user.is_authenticated: # 'request.user' is built in authenticate modules
        return render(request, 'users/login.html', {'msg': None})
    context = {
        'user': request.user,
    }
    return render(request, 'users/user.html', context)

def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None: # means user exists and password is right
        login(request, user) # authenticate user
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'users/login.html', {'msg': 'Invalid credential.'})

def logout_view(request):
    logout(request)
    return render(request, 'users/login.html', {'msg': 'Logged out.'})