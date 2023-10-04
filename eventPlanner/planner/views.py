from django.shortcuts import render, HttpResponse


# Create your views here.

#home page view for the event planner
def home(request):
    return render(request, 'home.html')

#browse events view
def events(request):
    return render(request, 'browseEvents.html')

#event detail view: viewing a specific event
def event(request):
    return render(request, 'eventDetail.html')