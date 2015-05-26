# django imports
from django.db import models
from django.conf import settings
# local imports
from .section import Section

class Enrollment(models.Model):
    """ 
    # the connection between students and a particular course

    """

    student = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, related_name="enrollments")
    section = models.ForeignKey(Section) 
    grade = models.CharField(max_length=3, blank=True)


# end of file
