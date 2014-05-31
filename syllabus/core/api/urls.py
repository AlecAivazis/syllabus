from django.conf.urls import patterns, url, include

from .views import ClassList, ClassesTaughtByMe, Gradebook, GradingScale
from .views import SectionList 
from .views import EventList, EventsByClass, HomeworkByClass

# define the class api urls
class_urls = patterns('', 
    url(r'(?i)^(?P<pk>[0-9a-zA-Z_-]+)/gradebook/$', Gradebook.as_view(),
                                                    name="api-classes-gradebook"),
    url(r'(?i)^(?P<pk>[0-9a-zA-Z_-]+)/gradingScale/$', GradingScale.as_view(),
                                                    name="api-classes-gradingScale"),
    url(r'(?i)^taughtByMe/$', ClassesTaughtByMe.as_view(), name="api-classes-taughtByMe"),
    url(r'^$', ClassList.as_view(), name="api-classes-list")
)

# define the event api urls
event_urls = patterns('',
    url(r'(?i)^byClass/(?P<id>[0-9a-zA-Z_-]+)/$', EventsByClass.as_view(), 
                                                  name="api-events-byClass"),
    url(r'(?i)^homeworkByClass/(?P<id>[0-9a-zA-Z_-]+)/$', HomeworkByClass.as_view(), 
                                                          name="api-events-byClass"),
    url(r'^$', EventList.as_view(), name="api-events-list")                    
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
)
