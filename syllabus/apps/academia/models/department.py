# django imports
from django.db import models

class Department(models.Model):
    """
    a `department` of a `college` with some `interests`

    related fields: 
        `interests` from .Interest  
    """
    name = models.CharField(max_length=1020)
    college = models.ForeignKey('College', related_name="departments")
    # majors = models.ManyToManyField('Major', related_name="college", blank=True)

    def __str__(self):
        """ string behavior is to return the name """
        return self.name 

# end of file
