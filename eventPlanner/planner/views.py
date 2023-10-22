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
    return render(request, 'createEvent.html')

def getCreatedEvent(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = CreateEventForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/Your event has been created! View it on the Browse Events Page/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CreateEventForm()
        
    return render(request, "createEvent.html", {"form": form})
