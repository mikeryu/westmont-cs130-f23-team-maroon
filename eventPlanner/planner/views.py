from django.shortcuts import render, HttpResponse, redirect
from .models import Event
from django.http import Http404, HttpResponseRedirect
from .forms import CreateEventForm
# from django.shortcuts import render


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
def event(request, id):
    try: 
        event = Event.objects.get(id=id)
    except Event.DoesNotExist:
        return redirect('events')
    
    context = {'event': event}
    
    return render(request, 'eventDetail.html', context)

def createEvent(request):

    if request.method == "POST":
        

        return redirect('events')

    return render(request, 'createEvent.html')
