from django.conf.urls import patterns, url

# announcement urls
urlpatterns = [
    url(r'(?i)^announcements/create$', announcements.create),
    url(r'(?i)^announcements/$', announcements.home),
    url(r'(?i)^announcements/newAnnouncement/$', announcements.newAnnouncement),
    url(r'(?i)^announcements/view/$', announcements.view),
]
