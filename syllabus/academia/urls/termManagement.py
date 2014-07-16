from django.conf.urls import  url, patterns

from ..views.termManagement import *

urlpatterns = patterns('', 
    (r'(?i)^$', home),
)
