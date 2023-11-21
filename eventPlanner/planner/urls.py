from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('events/', views.events, name = 'events'),

    #this need to be changed later to event/<int:event_id>, but for now it is just eventDetail because we don't have the database setup yet
    path('event/<int:id>', views.event, name = 'event'),  
    path('createEvent', views.createEvent, name = 'createEvent'),
    path('login', views.userLogin, name = 'loginPage'),
    path('signup', views.signup, name = 'signUp'),
    path('manageAccount', views.manageAccount, name='manageAccount'),
]
