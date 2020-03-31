from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Flight, Passenger
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
        'flight': flight,
        'passengers': flight.passengers.all(),
        'non_passengers': Passenger.objects.exclude(flights=flight).all()
    }

    return render(request, 'flight/flight.html', context)

def book(request, flight_id):
    try:
        passenger_id = int(request.POST['passenger'])
        passenger = Passenger.objects.get(pk=passenger_id)
        flight = Flight.objects.get(pk=flight_id)
    except KeyError:
        return render(request, 'flight/error.html', {'message': 'No selection'})
    except Passenger.DoesNotExist:
        return render(request, 'flight/error.html', {'message': 'No passenger'})
    except Flight.DoesNotExist:
        return render(request, 'flight/error.html', {'message': 'No flight'})
    
    passenger.flights.add(flight)
    return HttpResponseRedirect(reverse('flight', args=(flight_id,))) # , is very important for touple with only one element
