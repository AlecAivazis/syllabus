# django imports
from django.db import models
# local imports
CourseProfile = 'academia.CourseProfile'
from syllabus.apps.authentication.models import SyllabusUser
from .prerequisite import Prerequisite


class AddCode(models.Model):
    """
    allows for a user to go add a class regardless of rules in place
    """
    user = models.ForeignKey(SyllabusUser, related_name="addcodes")
    profile = models.ForeignKey(CourseProfile, related_name="addcodes")


# end of file
