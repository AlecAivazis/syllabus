# Various fields to be used in serializers throughout the application
# author: alec aivazis

from rest_framework import serializers

from .models import MetaData

class MetaDataField(serializers.WritableField):
    """ a field that encapsulates a particular piece of meta data 
        built around the many-to-many relationship named 'metaData' """

    def to_native(self, obj):
        """ called to convert the native rep into a primitive datatype """
        # grab the appropriate metaData
        data = obj.filter(key = self.name)
        # if it exists
        if data:
            # return it
            return data[0].value
        else:
            # return a blank string
            return ' '

    def from_native(self, data):
        """ called to restore a primitive datatype into its native rep """
        # store the event were serializing
        event = self.parent.object
        # check if there is already a metaData item with this name
        replacement = event.metaData.filter(key = self.name)

        # if there is
        if replacement:
            # grab the old data
            meta = replacement[0]
            # change its value
            meta.value = data
            # save the changes
            meta.save()

        #otherwise
        else:
            # create an empty meta data object
            meta = MetaData()
            # with the appropriate attributes
            meta.key = self.name
            meta.value = data 
            # save it to the database
            meta.save()
            # add it to the events metaData
            event.metaData.add(meta)

        # return the events metaData list
        return event.metaData.all()

    def __init__(self, name):
        """ save the name that will be used as the key to return the value """
        self.name = name
        super().__init__(source = 'metaData')
