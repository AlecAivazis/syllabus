from django.db import models

# syllabus core models
# most of these are misc models used throughout the application

# encapsulates generic metaDeta about an object
class MetaData(models.Model):
    key = models.CharField(max_length=1020)
    value = models.CharField(max_length=1020)    
    
# points to a file in the system
class File(models.Model):
    fileName = models.CharField(max_length=4096)    
