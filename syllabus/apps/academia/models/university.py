# django imports
from django.db import models
# local imports
from syllabus.fields import GradeField


class University(models.Model):
    """
    Responsible for university wide parameters.

    related fields: 
        `colleges` from .College  
    """
    name = models.CharField(max_length=1020)
    min_grade_to_pass = GradeField()


# end of file
