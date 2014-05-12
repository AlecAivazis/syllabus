from django.conf.urls import  url

from ..classManagementViews import *

# calendar urls
urlpatterns = [
    url(r'(?i)^$', home),
    url(r'(?i)^createCollege/$', createCollege),
    url(r'(?i)^newCollege/$', newCollege),
    url(r'(?i)^collegeList/$', collegeList),
    url(r'(?i)^departmentList/$', departmentList),
    url(r'(?i)^profileList/$', profileList),
    url(r'(?i)^interestList/$', interestList),
    url(r'(?i)^newDepartment/$', newDepartment),
    url(r'(?i)^createDepartment/$', createDepartment),
    url(r'(?i)^newClass/$', newClass),
    url(r'(?i)^newProfile/$', newProfile),
    url(r'(?i)^profile/$', profile),
]
