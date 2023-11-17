from django.test import TestCase
from django.urls import reverse 
from .models import Event
# Create your tests here.

class EventTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.event=Event.objects.create(
            name='My event',
            host='joe',
            description='Event details',
            location='Home'
        )
    
    def test_event_model(self):
        self.assertEqual(self.event.name, 'My event')
        self.assertEqual(self.event.host,'joe')
        self.assertEqual(self.event.description, 'Event details')
        self.assertEqual(self.event.location, 'Home')

    def test_delete_event(self):
        response=self.client.post(reverse("delete-event", args="1"))
        self.assertEqual(response.status_code, 302)
        # self.assertTemplateUsed(response, "event_delete_confirm.html")

    
    


    
