from django.shortcuts import render, HttpResponse


# Create your views here.


def home(request):
    return render(request, 'home.html')

def events(request):
    return render(request, 'browseEvents.html')


def event(request):

    return render(request, 'eventDetail.html')