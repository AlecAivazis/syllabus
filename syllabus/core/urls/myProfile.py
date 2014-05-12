from django.conf.urls import url 

from ..views.myProfile import *

# myProfile (students, eventually teachers)
urlpatters =[
    url(r'(?i)^$', home),
    url(r'(?i)^updateAddress/$', updateAddress),
    url(r'(?i)^updatePhone/$', updatePhone),
    url(r'(?i)^updateEmail/$', updateEmail),
]    
