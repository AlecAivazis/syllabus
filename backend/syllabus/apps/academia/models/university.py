# django imports
from django.db import models

class University(models.Model):
    """
    Responsible for university wide parameters.
    """
    name = models.CharField(max_length=1020)
    min_grade_to_pass = models.IntegerField(default=50)

# end of file
