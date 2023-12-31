from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('events/', views.events, name = 'events'),
    path('event/<int:id>', views.event, name = 'event'),  
    path('createEvent', views.createEvent, name = 'createEvent'),
    path('EventCenter', views.myEvents, name = 'myEvents'),
    path('login', views.userLogin, name = 'loginPage'),
    path('signup', views.signup, name = 'signUp'),
    path('manageAccount', views.manageAccount, name='manageAccount'),
    path('deleteEvent', views.deleteEvent, name='deleteEvent'),
    path('unrsvp', views.unrsvp, name='unrsvp'),
]
