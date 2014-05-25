from rest_framework import serializers

from ..models import Class, Section

class ClassSerializer(serializers.ModelSerializer):
    
    # add the classes sections as a list of id's
    sections = serializers.PrimaryKeyRelatedField(many = True, read_only = True)
    
    class Meta:
        model = Class
        fields = ('id', 'sections')

class SectionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Section
        fields = ('id')
