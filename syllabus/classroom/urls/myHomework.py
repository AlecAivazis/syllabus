from django.conf.urls import  url, patterns

from ..views.myHomework import *

# calendar urls
urlpatterns = patterns('', 
    url(r'(?i)^updateEventState/$', updateEventState),    
    url(r'(?i)^$', myHomework),
)
