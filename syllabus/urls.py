# import necessary django url modules
from django.conf.urls import patterns, include, url

# import the syllabus apps
from syllabus import api, academia, classroom, core, messages,  socialservice 

# import django admin module
from django.contrib import admin
admin.autodiscover()

# application wide url patterns
urlpatterns = patterns('',

    # load the admin urls - automatically generates necessary urls using autodiscover()
    url(r'^admin/', include(admin.site.urls)),

    # load the single messages (no replies) to /announcements
    url(r'(?i)^announcements/', include(messages.urls.announcements)),

    # load the calendar urls
    url(r'(?i)^calendar/', include(classroom.urls.calendar)),

    # handle the messageBoards through the course pages
    url(r'(?i)^course/messageBoard/', include(messages.urls.messageboards)),

    # load the course page urls
    url(r'(?i)^course/', include(classroom.urls.spaces)),

    # load the gradebook urls
    url(r'(?i)^gradebook/', include(classroom.urls.gradebook)),

    # load the academia urls
    url(r'(?i)^registrar/', include([
        url(r'(?i)^classes/', include(academia.urls.classManagement)),
        url(r'(?i)^graduationRequirements/', include(academia.urls.gradRequirements)),
        url(r'(?i)^users/', include(academia.urls.userManagement)),
        url(r'(?i)^terms/', include(academia.urls.termManagement)),
        url(r'(?i)^', include(academia.urls.core)),
    ])),

    # load the myClasses urls
    url(r'(?i)^myClasses/', include(classroom.urls.myClasses)),

    # load the tutor urls
    url(r'(?i)^tutors/', include(socialservice.urls.meetings)),

    # load the myHomework urls
    url(r'(?i)^myHomework/', include(core.urls.myHomework)),

    # load the myProfile urls
    url(r'(?i)^myProfile/', include(core.urls.myProfile)),

    # load the api urls
    url(r'(?i)^api/', include(api.urls)),

    # load the miscillaneous urls in core
    url(r'', include(core.urls.core)),

)
