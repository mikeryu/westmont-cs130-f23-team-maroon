from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Event, RSVP
from django.http import Http404, HttpResponseRedirect
from .forms import CreateEventForm2, RSVPForm
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
        attendees = RSVP.objects.filter(event=event).values()
        form = RSVPForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                rsvp = form.save(commit=False)
                rsvp.event = event
                rsvp.save()
        context = {'event': event, 'form': form, 'attendees': attendees}
    
    except Event.DoesNotExist:
        return redirect('events')
    
    return render(request, 'eventDetail.html', context)

def createEvent(request):
    
    
    if request.method == "POST":
        
        name = request.POST["name"]
        host = request.POST["host"]
        location = request.POST["location"]
        date = request.POST["date"]
        time = request.POST["time"]
        description = request.POST["description"]
        event = Event(name=name, host=host, location=location, date=date, time=time, description=description)
        event.save()
        
        return redirect('events')

    return render(request, 'createEvent.html')
