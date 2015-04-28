# django imports
from django.db import models
# local imports
CourseProfile = 'academia.CourseProfile'
from .prerequisite import Prerequisite


class Exemption(models.Model):
    """
    An exemption from `number_exempted` of `prerequisites`s `CourseProfile`s 
    fulfilled by passing `number_replacing` of `replacements` `CourseProfile`s.
    """
    prerequisite = models.ForeignKey(Prerequisite, related_name='exemptions')
    replacements = models.ManyToManyField(CourseProfile, related_name='exemption_set')
    number_exempted = models.IntegerField()
    number_replacing = models.IntegerField()

# end of file
