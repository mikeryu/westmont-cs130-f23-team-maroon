from django.db import models
from django.contrib.auth.models import User





#event class
#descbribes an specifc event with a name, host, data, time, location, and description.
class Event(models.Model):
    name = models.CharField(max_length=250)
    date = models.DateField(max_length=100) #Need to be updated to DateField in future release
    time = models.TimeField(max_length=100)  #Need to be updated to TimeField in future release
    location = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, default="Lorem ipsum blah blah blah") #Has a default value because it was implemented later
    user = models.ForeignKey(User, on_delete=models.CASCADE,default = None)
    attendees = models.IntegerField(default=0)
    totalTasks = models.IntegerField(default=0)
    completedTasks = models.IntegerField(default=0)

    """
    Features to be added in future releases
    capacity = models.IntegerField() 
    image = models.ImageField(upload_to='images/') 
    """

    def __str__(self):
        return self.name
    
#task class
#describes a task for a specific event
class Task(models.Model):
    name = models.CharField(max_length=250)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, default=None)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

# rsvp class
# stores a singular RSVP for a given event
class RSVP(models.Model):
    name = models.CharField(max_length=50)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, default=None)
    task = models.ForeignKey(Task, on_delete=models.DO_NOTHING, default=None, null=True)
    guests = models.IntegerField(default=0)
    rsvp = models.BooleanField(default=False)

    def __str__(self):
        return self.name


