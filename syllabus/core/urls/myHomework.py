from django.conf.urls import url

from ..views.myHomework import *

urlpatterns = [
    url(r'(?i)^turnIn/$', turnIn),
    url(r'(?i)^$', myHomework),
]
