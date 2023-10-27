from django.contrib import admin
from .models import Event, Task, RSVP

admin.site.register(Event)
admin.site.register(Task)
admin.site.register(RSVP)