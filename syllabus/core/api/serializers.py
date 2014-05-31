##
# Serializers for core api
#
##
# system imports
from rest_framework import serializers
# syllabus imports
from ..models import MetaData

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        """ meta class for SectionSerializer """
        model = Section
        fields = ('id', )
