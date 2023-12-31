from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from .models import Event, RSVP, Task
from .forms import RSVPForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.forms.models import model_to_dict
from datetime import date



"""
Once the user has been logged in, there may be pages we do not want them to access.
If they do try to access those pages, we want to redirect them to a different page.
That page is defined here.
"""
default_logged_in_redirect = 'myEvents'


"""
home page view for the event planner
"""
def home(request):
    #if the user is already logged in, redirect them to the events page
    if request.user.is_authenticated:
        return redirect(default_logged_in_redirect)
    
    return render(request, 'home.html')



"""
browse events view
here user should be able to see a list of events
"""
@login_required
def events(request):
    events = Event.objects.filter(date__gte=date.today()).order_by("date")
    context = {}

    # if request.method == "POST":
    #     print("submit")
    #     search = request.POST["filter"]
    #     filtered_events = []
    #     for event in events: 
    #         if search in event.name or search in event.description:
    #             filtered_events.append(event)
    #     context = {'events': [model_to_dict(e) for e in list(events)], 'user': request.user}
    # else:
    context = {'events':  [model_to_dict(e) for e in list(events)], 'user': request.user}
    
    return render(request, 'browseEvents.html', context)


"""
event detail view
here the user should be able to see the details of an event

if the user has submitted the RSVP form, save the RSVP to the database
"""
@login_required
def event(request, id):
    notification = request.GET.get('notification', None)
    if request.method == "POST":
        guests = request.POST["guests"]
        #grab the task id from the form
        taskId = request.POST.get('selectedTask')

        try:
            task = Task.objects.get(id=taskId)
        except Task.DoesNotExist:
            #if the tasks doesn't exist, we just assume the user is doing nothing for the event
            task = Task(name = "only attend", event  = Event.objects.get(id=id), completed = True)
        task.completed = True
        task.save()
        if(task.name != "only attend"):
            task.event.completedTasks += 1

        #create the RSVP and save it to the database
        rsvp = RSVP(name=request.user.username, event=task.event, task=task, guests=guests ,rsvp = True)
        rsvp.save()

        task.event.attendees += int(guests) + 1
        task.event.save()
        return redirect('event', id=id)

    else: #if the request method is GET, just render the event detail page normally
        try: 
            event = Event.objects.get(id=id)
        except Event.DoesNotExist:
            return redirect('events')
        
        attendees = RSVP.objects.filter(event=event)
        rsvp = RSVP.objects.filter(event = event, name = request.user, rsvp = True)


        #otherwise, just render the event detail page with the event, form, tasks, and attendees
        tasks = Task.objects.filter(event = event, completed = False).values()

        headCount = 0
        for attendee in attendees:
            headCount += attendee.guests + 1

        context = {'event': event, 'attendees': attendees, 'tasks': tasks, 'user': request.user, 'headCount':headCount, 'rsvp':rsvp, 'notification': notification }
        
        return render(request, 'eventDetail.html', context)





"""
Create event page
here the user should be able to create an event on this page

tasks that are created on this page will also be parsed and created, then linked to the event after the event is created
"""
@login_required
def createEvent(request):
    #Check to see the request method. POST means the form was just submitted.
    if request.method == "POST":
        
        #Using the POST data from the form to create an event
        name = request.POST["name"]
        location = request.POST["location"]
        date = request.POST["date"]
        time = request.POST["time"]
        description = request.POST["description"]

        #Get the list of tasks from the form
        tasks = request.POST.getlist("task-item")
        #Get the user of the event 
        user = request.user

        #create the event
        event = Event(name=name, location=location, date=date, time=time, description=description,user=user, completedTasks=0, totalTasks=len(tasks))
        #Save the event to the database
        event.save()

        #link all tasks to the event and save them
        for task in tasks:
            if len(task) > 0:
                newtask = Task(name=task, event=event)
                newtask.save()
 
        
        #Send the user to the browse events page
        return redirect('event', id=event.id)

    else:
        #In the case of a GET request, just render the create event form
        return render(request, 'createEvent.html', {'user': request.user})

@login_required
def manageAccount(request):
    if request.method == "POST":
        newUsername = request.POST['username']
        if User.objects.filter(username=newUsername).exists():
            return render(request, 'manageAccount.html', {'error_message': 'Username is already taken'})
        
        currUser = request.user
        currUser.username = newUsername
        currUser.save()
        return redirect('myEvents')
    
    return render(request, 'manageAccount.html', {'user': request.user})

@login_required
def deleteEvent(request):
    if request.method == "POST":
        event = Event.objects.get(id=request.POST['eventId'])
        event.delete()
        notification_message = "The event: " + event.name + " was deleted. There is no going back."
        url = reverse('myEvents') + f'?notification={notification_message}'
        return redirect(url)

@login_required
def unrsvp(request):
    if request.method == "POST":
        event = Event.objects.get(id=request.POST['eventId'])
        rsvp = RSVP.objects.get(event=event)
        
        rsvp.task.completed = False
        if(rsvp.task.name != "only attend"):
            rsvp.task.save()
            rsvp.event.completedTasks -= 1
        rsvp.event.attendees -= 1 + rsvp.guests
        rsvp.delete()

        notification_message = "You successfully Un-RSVP'd from the event: " + event.name
        url = reverse('event', args=[event.id]) + f'?notification={notification_message}'
        return redirect(url)



@login_required
def myEvents(request):
    notification = request.GET.get('notification', None)
    myHostedEvents = Event.objects.filter(user=request.user).order_by("date")
    myRSVP = RSVP.objects.filter(name=request.user)

    myRSVPEvents = []
    for rsvp in myRSVP:
        myRSVPEvents.append(rsvp.event)

    tasks = []
    for rsvp in myRSVP:
        if rsvp.task != None and str(rsvp.task) != "only attend":
            tasks.append(rsvp.task)


    context = {'myHostedEvents': myHostedEvents, 'myRSVPEvents': myRSVPEvents, 'user': request.user, 'tasks': tasks, 'notification': notification}
    return render(request, 'myEvents.html', context)


"""
login page, here the user should be able to login
logs in the user and redirects them to the events page
if the user does not provide the correct login credientials, 
they will be redirected back to the login page with an error message saying that the login credientials were invalid
"""
def userLogin(request):
    #if the user is already logged in, redirect them to the events page
    if request.user.is_authenticated:
        return redirect(default_logged_in_redirect)

    #if the user has submitted the login form, authenticate them and log them in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        # if the user is authenticated, log them in and redirect them to the events page
        if user is not None:
             login(request, user)
             return redirect(default_logged_in_redirect)
        else: # otherwise, render the login page with an error message
            return render(request, 'login.html', context = {'error_message': 'Invalid login credientials'})

    return render(request, 'login.html')


"""
signup page, 
here the user should be able to signup and create a new account
for now, we are just using the email as the username, but this can be easily changed later
if the user already exists, they will be redirected back to the signup page with an error message
saying that that email already exists
"""
def signup(request):
    #if the user is already logged in, redirect them to the events page
    if request.user.is_authenticated:
        return redirect(default_logged_in_redirect)
    
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        first = request.POST['first']
        last = request.POST['last']

        # check to make sure the passwords match
        if password != request.POST['password_again']:
            return render(request, 'signUp.html', {'error_message': 'Passwords do not match'})

        # check to see if the user already exists
        if User.objects.filter(username=username).exists():
            return render(request, 'signUp.html', {'error_message': 'Username already exists'})
        else:
            # if the user doesn't already exist, we go ahead and crreate the user, then log them in
            user = User.objects.create_user(username=username, email=email, password=password, first_name=first, last_name=last)
            user.save()
    
            login(request, user)

            return redirect(default_logged_in_redirect)
        
    return render(request, 'signUp.html')
        