# django imports
from django.db import models
from django.contrib.auth.models import AbstractUser

class SyllabusUser(AbstractUser):
    """ the generic syllabus user can be a teacher, reigstrar, or student """
    avatar = models.FileField()
    
    # student meta data:
    #   majors as meta data
    #   phone and various addresses as meta data
    #   transfer work

# end of file
