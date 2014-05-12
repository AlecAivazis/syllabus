from django.conf.urls import  url

from ..views.calendarViews import *

# calendar urls
urlpatterns = [

    url(r'(?i)^createEvent/$', createEvent),
    url(r'(?i)^deleteEvent/$', deleteEvent),
    url(r'(?i)^editEvent/$', editEvent),
    url(r'(?i)^editEventForm/$', editEventForm),
    url(r'(?i)^getSectionsById/$', getSectionsById),
    url(r'(?i)^loadEvents/$', loadEvents),
    url(r'(?i)^moveEvent/$', moveEvent),    
    url(r'(?i)^moveLabel/$', moveLabel),    
    url(r'(?i)^newEventForm/$', newEventForm),
    url(r'(?i)^ajax/$', calendarAjax),
    url(r'(?i)^newTermStart/$', newTermStart),
    url(r'(?i)^createTerm/$', createTerm),
    url(r'(?i)^newTermEnd/$', newTermEnd),
    url(r'(?i)^createTermEnd/$', createTermEnd),
    url(r'(?i)^createRegistration/$', createRegistrationPass),
    url(r'(?i)^endRegistrationForm/$', endRegistrationForm),
    url(r'(?i)^endRegistration/$', endRegistration),
    url(r'(?i)^startRegistration/$', startRegistrationForm),
    url(r'(?i)^$', calendarHome),
]
