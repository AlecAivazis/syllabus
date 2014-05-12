from django.conf.urls import url

from ..views.core import *

urlpatterns = [
    # myProfile (students, eventually teachers)
    url(r'(?i)^myProfile/$', myProfile.home),
    url(r'(?i)^myProfile/updateAddress/$', myProfile.updateAddress),
    url(r'(?i)^myProfile/updatePhone/$', myProfile.updatePhone),
    url(r'(?i)^myProfile/updateEmail/$', myProfile.updateEmail),
    
    # misc urls
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'(?i)^$', sentry),
    url(r'(?i)^downloadSubmission/$', downloadSubmission),
    url(r'(?i)^updateState/$', updateState),
    url(r'(?i)^login/$', syllogin),
    url(r'(?i)^logout/$', syllogout),
    url(r'(?i)^test/$', test),
    url(r'(?i)^viewEvent/$', viewEvent),
    url(r'(?i)^viewClass/$', viewClass),
    
    url(r'^resources/uploads/(?P<path>.*)$', protectedDownload),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': djangoSettings.STATIC_ADMIN_MEDIA_ROOT}),
    url(r'^resources/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': djangoSettings.STATIC_DOC_ROOT}), 
]
