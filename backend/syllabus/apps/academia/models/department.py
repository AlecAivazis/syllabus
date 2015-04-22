# django imports
from django.db import models

class Department(models.Model):
    """
    a `department` of a `college` with some `interests`
    """
    name = models.CharField(max_length=1020)
    interests = models.ManyToManyField('Interest', related_name="department")

    def __unicode__(self):
        """ string behavior is to return the name """
        return self.name 

# end of file