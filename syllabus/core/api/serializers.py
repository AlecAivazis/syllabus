##
# Serializers for core api
#
##
# system imports
from rest_framework import serializers
# syllabus imports
from ..models import MetaData

class MetaDataSerializer(serializers.ModelSerializer):
    class Meta:
        """ meta class for SectionSerializer """
        model = MetaData
        fields = ('key', 'value' )
