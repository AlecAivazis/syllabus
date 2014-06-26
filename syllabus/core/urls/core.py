from django.conf import settings
from django.conf.urls import url, patterns, include

from ..views.core import *

urlpatterns = patterns('', 
    # misc urls
    url(r'(?i)^$', sentry),
    url(r'(?i)^downloadSubmission/$', downloadSubmission),
    url(r'(?i)^updateState/$', updateState),
    url(r'(?i)^login/$', syllogin),
    url(r'(?i)^logout/$', syllogout),
    url(r'(?i)^test/$', test),
    url(r'(?i)^viewEvent/$', viewEvent),
    url(r'(?i)^viewClass/$', viewClass),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    url(r'^resources/uploads/(?P<path>.*)$', protectedDownload),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.STATIC_ADMIN_MEDIA_ROOT}),
    url(r'^resources/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_DOC_ROOT}), 
    url(r'^templates/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.TEMPLATES}), 
)
