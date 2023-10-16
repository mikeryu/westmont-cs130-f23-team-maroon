from django.shortcuts import render, HttpResponse
from .models import Event


# Create your views here.

#home page view for the event planner
def home(request):
    return render(request, 'home.html')

#browse events view
def events(request):
    events = Event.objects.all()
    context = {'events': events}

    return render(request, 'browseEvents.html', context)

#event detail view: viewing a specific event
def event(request):
    return render(request, 'eventDetail.html')

def createEvent(request):
    return render(request, 'createEvent.html')

