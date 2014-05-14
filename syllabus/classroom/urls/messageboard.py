from django.conf.urls import url, patterns

from ..views.messboards import *

urlpatterns = patterns('', 
    url(r'(?i)^createReply/$', createReply),
    url(r'(?i)^viewTopic/$', viewTopic),
    url(r'(?i)^newTopic/$', newTopic),
    url(r'(?i)^createTopic/$', createTopic),
    url(r'(?i)^$', home),
) 
