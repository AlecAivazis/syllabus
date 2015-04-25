# define custom fields used throughout syllabus

# django imports
from django.db import models

class GradeField(models.DecimalField):
    """
    A field that encapulates a grade
    """

    def __init__(self, *args, **kwargs):
        # Restrict the field to 4 digits.
        kwargs['max_digits'] = 4
        # Restrict the field to 2 decimal places.
        kwargs['decimal_places'] = 2
        return super().__init__(*args, **kwargs)

# end of file
