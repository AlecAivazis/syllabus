from django.db import models

# this schema handles the various message board aspects

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
  
