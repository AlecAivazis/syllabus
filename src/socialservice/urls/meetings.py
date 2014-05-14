from django.conf.urls import  url, patterns

from ..views.meetings import *

urlpatterns = patterns('', 
    url(r'(?i)^$', home),
    url(r'(?i)^new/$', new),
)
