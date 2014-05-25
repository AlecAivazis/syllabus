from django.conf.urls import patterns, url, include

from .views import ClassList, SectionList

# define the class api urls
class_urls = patterns('', 
    url(r'^$', ClassList.as_view(), name="class-list")
)


# define the class api urls
section_urls = patterns('', 
    url(r'^$', SectionList.as_view(), name="api-sections-list")
)
# combine the various urls
urlpatterns = patterns('', 
    url(r'^classes', include(class_urls)),
    url(r'^sections', include(section_urls)),
)
