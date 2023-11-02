from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Event, RSVP, Task
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

        tasks = Task.objects.filter(event = event).values()

        context = {'event': event, 'form': form, 'attendees': attendees, 'tasks': tasks}
    
    except Event.DoesNotExist:
        return redirect('events')
    
    return render(request, 'eventDetail.html', context)

#Create event page
def createEvent(request):
    
    #Check to see the request method. POST means the form was just submitted.
    if request.method == "POST":
        
        #Using the POST data from the form to create an event
        name = request.POST["name"]
        host = request.POST["host"]
        location = request.POST["location"]
        date = request.POST["date"]
        time = request.POST["time"]
        description = request.POST["description"]

        #Get the list of tasks from the form
        tasks = request.POST.getlist("task-item")

        #create the event
        event = Event(name=name, host=host, location=location, date=date, time=time, description=description)
        #Save the event to the database
        event.save()

        #link all tasks to the event and save them
        for task in tasks:
            newtask = Task(name=task, event=event)
            newtask.save()
 
        
        #Send the user to the browse events page
        return redirect('events')

    #In the case of a GET request, just render the create event form
    return render(request, 'createEvent.html')


def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signUp.html')
