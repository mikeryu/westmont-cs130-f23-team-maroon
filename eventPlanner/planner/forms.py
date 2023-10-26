from django.forms import ModelForm
from .models import RSVP

class RSVPForm(ModelForm):
    class Meta: 
        model = RSVP
        exclude = ("event", )
