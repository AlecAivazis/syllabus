from django.conf.urls import patterns, url

from ..views.announcementViews import *

# announcement urls
urlpatterns = [
    url(r'(?i)^create$', create),
    url(r'(?i)^newAnnouncement/$', newAnnouncement),
    url(r'(?i)^view/$', view),
    url(r'(?i)^$', home),
]
