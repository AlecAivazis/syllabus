import django

import datetime

from rest_framework import serializers

from ..models import Class, Event, Section

from syllabus.core.models import SyllUser as User

class ClassSerializer(serializers.ModelSerializer):
    
    # add the classes sections as a list of id's
    sections = serializers.PrimaryKeyRelatedField(many = True, read_only = True)
    name = serializers.SerializerMethodField('getName')
    
    class Meta:
        model = Class
        fields = ('id', 'name', 'sections')

    def getName(self, obj):
        return obj.profile.interest.abbrv + " " + str(obj.profile.number)


class GradebookSerializer(serializers.ModelSerializer):

    students = serializers.SerializerMethodField('getStudents')
    events = serializers.SerializerMethodField('getGradableEvents')

    class Meta:
        model = Class
        fields = ('students', 'events')
    
    def getStudents(self, obj):
        users = []
        for user in User.objects.filter(classes__pk = obj.pk):
            users.append(user)

        return users

    def getGradableEvents(self, obj):
        return (Event.objects.filter(classes__id=obj.pk)
                .exclude(category='lecture')
                .exclude(category='meeting')
                .filter(date__lte = django.utils.timezone.now() + datetime.timedelta(days = 1)))


class SectionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Section
        fields = ('id', )

class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ('id',)
