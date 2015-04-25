# django imports
from django.db import models

class College(models.Model):
    """
    The `college` of a `university` has many `departments` and some `requirements`.

    Requirements at this level are most likely GEs.
    """
    
    name = models.CharField(max_length=1020)
    # requirements = models.ManyToManyField('Requirement', related_name="colleges", blank=True)
    university = models.ForeignKey('University', related_name="colleges")

# end of file
