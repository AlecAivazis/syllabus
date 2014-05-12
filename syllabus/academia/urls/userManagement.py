from django.conf.urls import  url

from ..userManagementViews import *

urlpatterns = [
    (r'(?i)^$', home),
    (r'(?i)^new/$', new),
    (r'(?i)^delete/$', delete),
    (r'(?i)^create/$', create),
    (r'(?i)^addExemption/$', addExemption),
    (r'(?i)^userProfile/$', userProfile),
    (r'(?i)^list/$', listRequirement),
    (r'(?i)^edit/$', editRequirement),
    (r'(?i)^addExemption/$', addExemption),
    (r'(?i)^getInterestCourseNumbers/$', getInterestCourseNumber),
]
