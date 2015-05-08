# define decorators that are useful for interaction with meta data

# django imports
from django.db import models
# local imports
from .models import Metadata


def metadata_model(cls):
    """
    Add a metadata field to the class record.
    """
    # create a many-to-many field pointing to meta data
    field = models.ManyToManyField(Metadata) 
    # add the field to the class
    field.contribute_to_class(cls, "metadata")


# end of file
