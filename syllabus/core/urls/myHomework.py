from django.conf.urls import url, patterns

from ..views.myHomework import *

urlpatterns = patterns( '', 
    url(r'(?i)^turnIn/$', turnIn),
    url(r'(?i)^$', myHomework),
)
