# django imports
from django.db import models

class Event(models.Model):
    """ 
    # the fundamental element of a teachers syllabus

    """

    title = models.CharField(max_length=1020)
    description = models.TextField(max_length=5000)
    date = models.DateField()
    start = models.TimeField(blank=True)
    end = models.TimeField(blank=True)
    # TODO: think this through a bit better
    category = models.CharField(max_length=1020, blank=True, choices=(
        ('assignment','assignment'),
        ('test','test'),
        ('lecture','lecture'),
        ('meeting','meeting'),
    ))


    def save(self, *args, **kwargs):
        # if the end date was given without a start
        if self.end and not self.start:
            raise ValueError('Must specify start time if end is given')
        # otherwise both a start and end were given
        # if the end is before the start
        elif self.end < self.start :
            raise ValueError('Event end time must come after start')
        # otherwise the end is after the start
        else:
            return super().save(*args, **kwargs)

    # event meta data
    #   files 


# end of file
