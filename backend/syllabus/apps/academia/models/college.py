# django imports
from django.db import models
# local imports
from syllabus.apps.requirements.models import Prerequisite

class College(models.Model):
    """
    The `college` of a `university` has many `departments` and some `prerequisites`.

    Prerequisites at this level are most likely GEs

    related fields: 
        `departments` from .Department 
    """
    name = models.CharField(max_length=1020)
    prerequisites = models.ManyToManyField(Prerequisite, related_name="colleges", blank=True)
    university = models.ForeignKey('University', related_name="colleges")

# end of file
