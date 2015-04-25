# django imports
from django.db import models
# local imports
from syllabus.apps.academia.models import CourseProfile


class Exemption(models.Model):
    """
    An exemption from `number_exempted` of `requirement`s `CourseProfile`s 
    fulfilled by passing `number_replacing` of `replacements` `CourseProfile`s.
    """
    requirement = models.ForeignKey('Requirement', related_name='exemptions')
    replacements = models.ManyToManyField(CourseProfile, related_name='exemption_set')
    number_exempted = models.IntegerField()
    number_replacing = models.IntegerField()

# end of file
