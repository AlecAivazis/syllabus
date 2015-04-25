# a generic model with some meta data

# django imports
from django.db import models
# local imports
from .metadata import Metadata


class MetadataModel(models.Model):
    """
    Generic model with metadata.
    """
    # add a meta data field 
    metadata = models.ManyToManyField(Metadata)

    class Meta:
        abstract = True


# end of file
