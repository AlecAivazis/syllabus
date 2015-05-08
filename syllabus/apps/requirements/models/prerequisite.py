# django imports
from django.db import models
# local imports
CourseProfile = 'academia.CourseProfile'

class Prerequisite(models.Model):
    """
    A group of `course_profiles` of which a certain `number` must be taken.

    related fields:
        `exemptions` from .Exemption
    """
    name = models.CharField(max_length=10, blank=True)
    full_name = models.CharField(max_length=1020, blank=True)
    course_profiles = models.ManyToManyField(CourseProfile, related_name="required_by")
    number = models.IntegerField()

# end of file
