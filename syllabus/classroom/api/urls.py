from django.conf.urls import patterns, url, include

from .views import ClassList, SectionList, ClassTaughtByMe

# define the class api urls
class_urls = patterns('', 
                      
    url(r'(?i)^taughtByMe/$', ClassTaughtByMe.as_view(), name="classes-taughtByMe"),
    url(r'^$', ClassList.as_view(), name="class-list")
)


# define the class api urls
section_urls = patterns('', 
    url(r'^$', SectionList.as_view(), name="api-sections-list")
)
# combine the various urls
urlpatterns = patterns('', 
    url(r'(?i)^classes/', include(class_urls)),
    url(r'(?i)^sections/', include(section_urls)),
)
