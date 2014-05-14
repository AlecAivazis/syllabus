from django.conf.urls import  url, include, patterns

from ..views.spaces import *

# calendar urls
urlpatterns = patterns('', 
    url(r'(?i)^announcements/view/$', viewAnnouncements),
    url(r'(?i)^setSyllabus/$', setSyllabus),
    url(r'(?i)^syllabus/view/$', viewSyllabus),

    # timeline urls
    url (r'(?i)^timeline/', include([
        url(r'(?i)^view/$', viewTimeline),
        url(r'(?i)^changeEventTitle/$', changeEventTitle),
        url(r'(?i)^changeEventDescription/$', changeEventDescription),
        url(r'(?i)^changeEventAssocReading/$', changeEventAssocReading),
    ])),
)
