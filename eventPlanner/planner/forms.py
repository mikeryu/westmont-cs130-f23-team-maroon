from django import forms
from django.forms import ModelForm
from .models import Event, RSVP

#A form model for the create event page. Currently unused, as the implementation of the
#form right now pulls straight from the POST data of the page, not a form object.
class CreateEventForm2(forms.Form): 
    #Each field of this form corresponds to an instance variable of the event model
    event_name = forms.CharField(label="Event name", max_length=100)
    event_host = forms.CharField(label="Enter your name", max_length=100)
    event_location = forms.CharField(label="Location", max_length=100)
    event_date = forms.CharField(label="Date", max_length=100)
    event_time = forms.CharField(label="time", max_length=100)
    event_description = forms.CharField(label="Describe your event.", max_length=250)
    
    class Meta:
        model = Event
        exclude = ("user", )

class RSVPForm(ModelForm):
    class Meta: 
        model = RSVP
        exclude = ("event", )
