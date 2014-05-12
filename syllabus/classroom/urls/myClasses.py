from django.conf.urls import  url

from ..views.myClasses import *

urlpatterns = [
    url(r'(?i)^classPage/$', classPage),
    url(r'(?i)^classPages/$', classPage),
    url(r'(?i)^confDrop/$', confDrop),
    url(r'(?i)^courseInfoTable/$', courseInfoTable),
    url(r'(?i)^getSchedule/$', getSchedule),
    url(r'(?i)^schedule/$', schedule),
    url(r'(?i)^catalog/addSection/$', addSection),
    url(r'(?i)^catalog/confirmAddSection/$', confirmAddSection),
    url(r'(?i)^catalog/$', catalog),
    url(r'(?i)^filterCatalog/$', filterCatalog),
    url(r'(?i)^runTask/$', runTask),
    url(r'(?i)^grades/$', grades),
]
