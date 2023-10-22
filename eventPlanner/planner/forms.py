from django import forms
from .models import Event

class CreateEventForm()
    event_name = forms.CharField(label="Event name", max_length=100)
    event_host = forms.CharField(label="Enter your name", max_length=100)
    event_location = forms.CharField(label="Location", max_length=100)
    event_date = forms.CharField(label="Date", max_length=100)
    event_time = forms.CharField(label="time", max_length=100)
    event_description = forms.CharField(label="Describe your event.", max_length=250)