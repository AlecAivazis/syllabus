from django.conf.urls import  url, patterns

from ..views.core import *

urlpatterns = patterns('', 
    (r'(?i)^getInterestClasses/$', getInterestClasses ),
)
