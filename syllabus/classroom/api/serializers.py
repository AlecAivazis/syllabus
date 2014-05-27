import django

import datetime

from rest_framework import serializers

from ..models import Class, Event, Section

from syllabus.core.models import SyllUser as User

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        """ meta class for ClassSerializer """
        model = Class
        fields = ('id', 'name', 'sections')

    # the class sections as a list of id's
    sections = serializers.PrimaryKeyRelatedField(many = True, read_only = True)
    # the name of the class
    name = serializers.SerializerMethodField('getName')
    
    def getName(self, obj):
        """return the name of the class"""
        return obj.profile.interest.abbrv + " " + str(obj.profile.number)


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        """ meta class for EventSerializer """
        model = Event
        fields = ('id',)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        """ meta class for UserSerializer """
        model = User
        fields = ('name', 'id')

    # the name of the user
    name = serializers.SerializerMethodField('getName')

    def getName(self, obj):
        """ return the name of the user """
        return obj.first_name + ' ' + obj.last_name

class GradebookSerializer(serializers.ModelSerializer):
    class Meta:
        """ meta class for GradebookSerializer """
        model = Class
        fields = ('students', 'events')
    
    # the students in the class
    students = serializers.SerializerMethodField('getStudents')
    # the gradable events
    events = serializers.SerializerMethodField('getGradableEvents')

    def getStudents(self, obj):
        """ return the students in the serialized class """
        # get the users who are in the class
        users = User.objects.filter(classes__pk = obj.pk)
        # serialize the users
        serializer = UserSerializer(users)
        # return the serialized data
        return serializer.data

    def getGradableEvents(self, obj):
        """ return the events that are gradable """
        # gradable events are not lectures or meetings that are due before tomorrow
        events = (Event.objects.filter(classes__id=obj.pk)
                .exclude(category='lecture')
                .exclude(category='meeting')
                .filter(date__lte = django.utils.timezone.now() + datetime.timedelta(days = 1)))
        # serialize the events
        serializer = EventSerializer(events)
        # return the serialized data
        return serializer.data

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        """ meta class for SectionSerializer """
        model = Section
        fields = ('id', )
