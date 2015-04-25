# define custom fields used throughout syllabus

# django imports
from django.db import models

class GradeField(models.DecimalField):
    """
    A field that encapulates a grade
    """

    def __init__(self, *args, **kwargs):
        """
        Restrict the field to 2 digits.
        """
        return super(max_digits=2, *args, **kwargs)

# end of file
