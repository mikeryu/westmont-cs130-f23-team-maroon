from django.db import models





#event class
#descbribes an specifc event with a name, data, time and location
class Event(models.Model):
    name = models.CharField(max_length=250)
    host = models.CharField(max_length= 100, default="Joe")
    date = models.CharField(max_length=100) #Need to be updated to DateField in future release
    time = models.CharField(max_length=100)  #Need to be updated to TimeField in future release
    location = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, default="Lorem ipsum blah blah blah")

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
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
# rsvp class
# stores a singular RSVP for a given event
class RSVP(models.Model):
    name = models.CharField(max_length=50)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

