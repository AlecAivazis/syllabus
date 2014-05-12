from django.conf.urls import  url

from ..views.userManagement import *

urlpatterns = [
    (r'(?i)^$', home),
    (r'(?i)^new/$', new),
    (r'(?i)^delete/$', delete),
    (r'(?i)^create/$', create),
    (r'(?i)^addExemption/$', addExemption),
    (r'(?i)^userProfile/$', userProfile),
    (r'(?i)^list/$', listRequirements),
    (r'(?i)^edit/$', editRequirement),
    (r'(?i)^addExemption/$', addExemption),
    (r'(?i)^getInterestCourseNumbers/$', getInterestCourseNumber),
]
