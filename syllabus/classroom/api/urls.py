from django.conf.urls import patterns, url, include

from .views import ClassList, ClassesTaughtByMe, Gradebook, GradingScale, ClassScheduleForUser
from .views import SectionList 
from .views import ClassEventList, HomeworkByClass
from .views import WeightsList
from .views import MyCalendar
from .views import RetrieveEvent, CreateEvent, HomeworkForUser
from .views import GradesForUser


# the class api urls
class_urls = patterns('', 
    url(r'(?i)^(?P<pk>[0-9a-zA-Z_-]+)/', include([
        url(r'(?i)^events/', ClassEventList.as_view(), name="api-classes-gradebook"),
        url(r'(?i)^gradebook/', Gradebook.as_view(), name="api-classes-gradebook"),
        url(r'(?i)^gradingScale/', GradingScale.as_view(), name="api-classes-gradingScale"),
        url(r'(?i)^weights/', WeightsList.as_view(), name="api-classes-gradebook"),
    ])),
    url(r'(?i)^taughtByMe/', ClassesTaughtByMe.as_view(), name="api-classes-taughtByMe"),
    url(r'^$', ClassList.as_view(), name="api-classes-list")
)

# the event api urls
event_urls = patterns('',
    url(r'(?i)^homeworkByClass/(?P<id>[0-9a-zA-Z_-]+)/$', HomeworkByClass.as_view(), 
                                                          name="api-events-byClass"),
    url(r'(?i)^create/$', CreateEvent.as_view(), name="api-event-create"),
    url(r'^(?P<pk>[0-9a-zA-Z_-]+)/$', RetrieveEvent.as_view(), name="api-event-retrieve")
)

# urls added to the user api
user_urls = patterns('', 
    # return the calendar based on the request user
    url(r'(?i)^me/calendar/',   MyCalendar.as_view(), name="api-user-mycalendar"),
    # grab users by their pk or me
    url(r'(?i)^(?P<pk>[0-9a-zA-Z_-]+)/',  include([
        url(r'(?i)^schedule/',  ClassScheduleForUser.as_view(), name="api-user-schedule"),
        url(r'(?i)^homework/',  HomeworkForUser.as_view(), name="api-user-homework"),
        url(r'(?i)^grades/',    GradesForUser.as_view(), name="api-user-grades"),
    ])),
)

# the class api urls
section_urls = patterns('', 
    url(r'^$', SectionList.as_view(), name="api-sections-list")
)
# combine the various urls
urlpatterns = patterns('', 
    url(r'(?i)^classes/',  include(class_urls)),
    url(r'(?i)^events/',   include(event_urls)),
    url(r'(?i)^sections/', include(section_urls)),
    url(r'(?i)^users/',    include(user_urls)),
)
