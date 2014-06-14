# django imports
from django.conf.urls import  url, patterns

# import the views
from ..views.gradebook import *

# calendar urls
urlpatterns = patterns('', 
    url(r'(?i)^addGrade/$', addGrade), 
    url(r'(?i)^changeCategory/$', changeCategory), 
    url(r'(?i)^changePossiblePoints/$', changePossiblePoints), 
    url(r'(?i)^gradingScale/setScale/$', setScale), 
    url(r'(?i)^weights/set/$', assignWeights), 
    url(r'(?i)^$', gradebookHome),
)
