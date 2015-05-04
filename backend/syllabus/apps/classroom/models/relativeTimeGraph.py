# django imports
from django.db import models


# TODO:
# break this into two files
# figure out the right way to flatten this


class RelativeTimeGraph(models.Model):
    """

    related fields: 
        `root_nodes` from .RelativeTimeNode  
    """
    duration = models.DurationField(default=0)

    def flatten_in_date_range(self, region):
        """
        Return list of {start, duration} dictionaries.

        `region` is a {start, end} dictionary.



        """
        results = []
        for root in root_nodes.all():

        return results

    def matches(self, target, region):
        """
        True if `target` is within the times specified by the graph relative to `region`.

        `region` is a {start, end} dictionary.
        """
        # allow `target` to be just the `start` datetime
        if not isinstance(target, dict):
            target = {'start': target}
        # allow `duration` to be optional key in `target`
        if 'duration' not in target:
            target['duration'] = 0
        # True if any of the timeslots contain `target`
        return any((d['start'] <= target['start']) and 
                   ((target['start'] + target['duration']) <= d['end'] 
                   for d in self.flatten_in_date_range(region)))


class RelativeTimeNode(models.Model):
    """
    Designates a time relative to `parent`.

    related fields: 
        `children` from self  
    """
    # relative index
    # TODO: literally wtf on that max_length...
    value = models.CommaSeparatedIntegerField(max_length=1000)
    # qualifies the time scale
    qualifier = models.CharField(max_length=1, choices=(
        ('m', 'month'),
        ('w', 'week'),
        ('d', 'day'),
        ('h', 'hour'),
    ))
    duration = models.DurationField(blank=True)
    graph = models.ForeignKey('RelativeTimeGraph', blank=True, related_name='root_nodes')
    parent = models.ForeignKey('self', related_name='children')

    def save(self, *args, **kwargs):
        if self.parent and self.graph:
            raise ValidationError('RelativeTimeNode cannot have both parent and graph.')
        else:
            return super().save(*args, **kwargs)

    def get_duration(self):
        if self.has_duration():
            return self.duration
        return self.parent.get_duration()

    def has_duration(self):
        return bool(self.duration == 0 or self.duration)

