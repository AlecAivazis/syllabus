from django.conf.urls import  url, patterns

from ..views.calendar import *


# calendar urls
urlpatterns = patterns('', 
    url(r'(?i)^moveLabel/$', moveLabel),    
    url(r'(?i)^$', home),
)

