from django.shortcuts import render, HttpResponse, redirect
from .models import Event, RSVP
from django.http import Http404
from .forms import RSVPForm

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
    return render(request, 'createEvent.html')

