from django.conf.urls import  url

from ..views.gradRequirements import *

urlpatterns = [
    url(r'(?i)^$', home),
    url(r'(?i)^viewDegree/$', viewDegree),
    url(r'(?i)^viewCollegeDegree/$', viewCollegeDegree),
    url(r'(?i)^newCollegeRequirement/$', newCollegeRequirement),
    url(r'(?i)^newRequirement/$', newRequirement),
    url(r'(?i)^submitCollegeRequirement/$', submitCollegeRequirement),
    url(r'(?i)^submitRequirement/$', submitRequirement),
    url(r'(?i)^profilesByInterest/$', profilesByInterest),
    url(r'(?i)^deleteRequirement/$', deleteRequirement),
    url(r'(?i)^editRequirement/$', editRequirement),
    url(r'(?i)^modifyRequirement/$', modifyRequirement),
    url(r'(?i)^majorList/$', majorList),
    url(r'(?i)^newMajor/$', newMajor),
    url(r'(?i)^createMajor/$', createMajor),
]
