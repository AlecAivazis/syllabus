from django.conf.urls import  url

from ..tutorsViews import *

urlpatterns = [
    url(r'(?i)^$', home),
    url(r'(?i)^new/$', new),
]
