from django.shortcuts import render
import random

# Create your views here.

def index(request):

    num = random.randint(0, 22)
    
    context = {
        'num': num,
    }

    return render(request, 'logindemo/login.html', context)

def register(request):
    context = {

    }

    return render(request, 'logindemo/register.html', context)

def terms(request):
    context = {

    }

    return render(request, 'logindemo/terms.html', context)