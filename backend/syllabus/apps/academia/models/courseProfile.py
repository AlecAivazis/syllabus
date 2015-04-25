# django imports
from django.db import models


class CourseProfile(models.Model):
    """
    the profile of a given class - separated from a particular class because it changes every 5 yrs

    related fields:
        `required_by` from requirements.Requirement
    """
    name = models.CharField(max_length=1020)
    full_name = models.CharField(max_length=1020)
    units = models.IntegerField()
    description = models.CharField(max_length=1020)
    number = models.IntegerField()
    #prerequisites = models.ManyToManyField('PreRequisiteGroup', related_name="prereqs", 
    #                                                            symmetrical=False, blank=True)
    interest = models.ForeignKey('Interest', related_name="course_profiles")

    def __str__(self):
        """ default string behavior is to return its abbreviation """
        return str(self.pk) + ':' + self.name

# end of file
