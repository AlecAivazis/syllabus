# django imports
from django.db import models
# local imports
from syllabus.apps.metadata.decorators import metadata_model

@metadata_model
class University(models.Model):
    """
    Responsible for university wide parameters.
    """
    name = models.CharField(max_length=1020)


# end of file
