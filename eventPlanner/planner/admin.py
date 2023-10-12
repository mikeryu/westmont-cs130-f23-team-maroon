from django.contrib import admin

# Register your models here.
from .models import Event, Task

admin.site.register(Event)
admin.site.register(Task)
