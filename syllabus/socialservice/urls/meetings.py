from django.conf.urls import  url

from ..views.meetings import *

urlpatterns = [
    url(r'(?i)^$', home),
    url(r'(?i)^new/$', new),
]
