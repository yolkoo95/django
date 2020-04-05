from django.shortcuts import render
from django.http import HttpResponse
from .checker import regular_expression_checker
import json

# Create your views here.

def homepage(request):

    context = {

    }

    return render(request, 'RETest/homepage.html', context)

def index(request):
    context = {

    }
    return render(request, 'RETest/index.html', context)

def checker(request):
    u_input = request.POST['re_input']
    u_samples = request.POST['re_samples']
    
    if (u_input is None) or (u_samples is None):
        return HttpResponse("ValueError: fail to receive data")

    # begin to check
    pattern = u_input
    test_samples = u_samples.splitlines()
    
    results = regular_expression_checker(pattern, test_samples)

    context = {
        'pattern': pattern,
        'results': results,
    }

    return render(request, 'RETest/index.html', context)

    # return HttpResponse(json.dumps(results))

    