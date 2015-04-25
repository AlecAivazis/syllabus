# django imports
from django.db import models


class DataTypes:
    """
    Supported data types of `Metadata.type`.
    """
    
    types = {
        'INTEGER': 'int',
        'FLOAT': 'flt',
        'PERCENTAGE': 'pct',
        'STRING': 'str'   
    }

    def __init__(self):
        # add each type as
        for key, value in self.types.items():
            # add the attribute to the instance
            setattr(self, key, value)

    @classmethod
    def get_type_tuple(cls):
        # start off with an empty list
        types = []
        # for each type
        for key, value in cls.types.items():
            # add it to the list
            types.append((value, key))
        # turn the list into a tuple
        return tuple(types)


class Metadata(models.Model):
    """
    Encapsulates generic metadata about an object as a key value pair with a type.
    """

    # acts as an container for supported value types
    types = DataTypes()

    key = models.CharField(max_length=1020)
    value = models.CharField(max_length=1020)
    type = models.CharField(max_length=3, choices=DataTypes.get_type_tuple())



# end of file
