# django imports
from django.db import models
# local imports
from syllabus.apps.requirements.models import Prerequisite

class Major(models.Model):
    """
    An academic achievment offered by a particular `department` given for satisfying
    a set of `reuirements`.

    `type` distinguishes BA from BS, BFA, etc.
    """
    name = models.CharField(max_length=1020)
    type = models.CharField(max_length=10)
    college = models.ForeignKey('College')
    preMajor = models.ManyToManyField(Prerequisite, related_name="required_for_premajor")
    major = models.ManyToManyField(Prerequisite, related_name="required_for_major")


# end of file
