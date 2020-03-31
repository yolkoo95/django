from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import Flight
# .models means ./models

# Create your views here.

def index(request):
    context = {
        'flights': Flight.objects.all()
    }

    return render(request, 'flight/index.html', context)

def flight(request, flight_id):
    try: 
        flight = Flight.objects.get(pk=flight_id)
    except Flight.DoesNotExist:
        raise Http404('Flight does not exist')
    context = {
        'flight': flight
    }

    return render(request, 'flight/flight.html', context)