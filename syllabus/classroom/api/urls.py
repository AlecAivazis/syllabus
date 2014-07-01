from django.conf.urls import patterns, url, include

from .views import ClassList, ClassesTaughtByMe, Gradebook, GradingScale, ClassScheduleForUser
from .views import SectionList 
from .views import ClassEventList, HomeworkByClass
from .views import WeightsList
from .views import MyCalendar
from .views import RetrieveEvent, CreateEvent, HomeworkForUser


# define the class api urls
class_urls = patterns('', 
    url(r'(?i)^(?P<pk>[0-9a-zA-Z_-]+)/events/$', ClassEventList.as_view(),
                                                    name="api-classes-gradebook"),
    url(r'(?i)^(?P<pk>[0-9a-zA-Z_-]+)/gradebook/$', Gradebook.as_view(),
                                                    name="api-classes-gradebook"),
    url(r'(?i)^(?P<pk>[0-9a-zA-Z_-]+)/gradingScale/$', GradingScale.as_view(),
                                                    name="api-classes-gradingScale"),
    url(r'(?i)^(?P<pk>[0-9a-zA-Z_-]+)/weights/$', WeightsList.as_view(),
                                                    name="api-classes-gradebook"),
    url(r'(?i)^taughtByMe/$', ClassesTaughtByMe.as_view(), name="api-classes-taughtByMe"),
    url(r'^$', ClassList.as_view(), name="api-classes-list")
)

# define the event api urls
event_urls = patterns('',
    url(r'(?i)^homeworkByClass/(?P<id>[0-9a-zA-Z_-]+)/$', HomeworkByClass.as_view(), 
                                                          name="api-events-byClass"),
    url(r'(?i)^create/$', CreateEvent.as_view(), name="api-event-create"),
    url(r'^(?P<pk>[0-9a-zA-Z_-]+)/$', RetrieveEvent.as_view(), name="api-event-retrieve")
)

# define the class api urls
section_urls = patterns('', 
    url(r'^$', SectionList.as_view(), name="api-sections-list")
)
# combine the various urls
urlpatterns = patterns('', 
    url(r'(?i)^classes/', include(class_urls)),
    url(r'(?i)^events/', include(event_urls)),
    url(r'(?i)^sections/', include(section_urls)),
    # return the calendar based on the request user
    url(r'(?i)^users/me/calendar/',  MyCalendar.as_view(),
                                    name="api-user-mycalendar"),
    url(r'(?i)^users/(?P<pk>[0-9a-zA-Z_-]+)/schedule/',  ClassScheduleForUser.as_view(),
                                    name="api-user-schedule"),
    url(r'(?i)^users/(?P<pk>[0-9a-zA-Z_-]+)/homework/',  HomeworkForUser.as_view(),
                                    name="api-user-homework")
)
