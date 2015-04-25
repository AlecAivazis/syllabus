# django imports
from django.db import models

from syllabus.apps.metadata.models import MetadataModel

class University(MetadataModel):
    """
    Responsible for university wide parameters.
    """
    name = models.CharField(max_length=1020)

# end of file
