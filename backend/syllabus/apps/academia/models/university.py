# django imports
from django.db import models
# local imports
from syllabus.apps.metadata.decorators import metadata_model
from syllabus.fields import GradeField

@metadata_model
class University(models.Model):
    """
    Responsible for university wide parameters.
    """
    name = models.CharField(max_length=1020)
    min_grade_to_pass = GradeField()


# end of file
