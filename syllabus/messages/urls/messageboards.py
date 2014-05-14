from django.conf.urls import patterns, url

from ..views.messageboards import *

# announcement urls
urlpatterns = patterns('', 
    url(r'(?i)^createReply/$', createReply),
    url(r'(?i)^viewTopic/$', viewTopic),
    url(r'(?i)^newTopic/$', newTopic),
    url(r'(?i)^createTopic/$', createTopic),
    url(r'(?i)^view/$', home),
)
