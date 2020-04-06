from django.shortcuts import render

# Create your views here.

def index(request):
    context = {

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