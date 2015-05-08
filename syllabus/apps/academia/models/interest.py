# django imports
from django.db import models

class Interest(models.Model):
    """
    An `interest` is a subsection of a `department` used to filter `courseProfiles`.

    related fields: 
        `course_profiles` from .CourseProfile  
    """
    name = models.CharField(max_length=1020)
    abbrv = models.CharField(max_length=10)

    def __str__(self):
        """ default string behavior is to return its abbreviation """
        return self.abbrv

    # should add to a string
    def __add__(self, other):
        if isinstance(other, str):
            return self.abbrv + other
        raise NotImplemented
    def __radd__(self, other):
        if isinstance(other, str):
            return other + self.abbrv
        raise NotImplemented

# end of file