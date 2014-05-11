from django.db import models

# this schema handles most of the inter user communication
# either through message boards (two-way, multiple message conversations)
# or through announcements (single message, no reply)

# Messageboard
# --------------------

# a reply to a {topic}
class Post (models.Model):
    author = models.ForeignKey(SyllUser)
    body = models.TextField(max_length=5000, blank=True)
    datePosted = models.DateTimeField(auto_now_add=True)
    files = models.ManyToManyField(File, related_name='posts', blank=True)
    kind = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.body

# the root post in a message board    
class Topic(models.Model):
    title = models.CharField(max_length=1020)
    body = models.TextField(max_length = 5000)
    datePosted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(SyllUser)
    replies = models.ManyToManyField(Post, related_name="replys", blank=True)
    read = models.ManyToManyField(SyllUser, related_name="readThreads", blank=True) 
    def __unicode__(self):
        return self.body
  

# Announcements
# --------------------

# a group of {syllabus.classes} to use as a target group
class Group(models.Model):
    qlass = models.ManyToManyField(Class, related_name='groups', blank=True)
    name = models.CharField(max_length=1020)

# a group of {users} to use as the target
class UserGroup(models.Model):
    managers = models.ManyToManyField(SyllUser, related_name="managed_groups")
    name = models.CharField(max_length=1020)
    users = models.ManyToManyField(SyllUser)
    
# a single message that tracks who reads it - no option of reply
class Announcement(models.Model):
    title = models.CharField(max_length=1020)
    author = models.ForeignKey(SyllUser)
    datePosted = models.DateTimeField(auto_now=True)
    sections = models.ManyToManyField(Section, related_name="announcements", blank=True)
    userGroups = models.ManyToManyField(UserGroup, blank=True)
    message = models.CharField(max_length=1020)
    read = models.ManyToManyField(SyllUser, related_name="read_announcements")
