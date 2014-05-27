##
# Serializers for classroom api
#
##

# system imports
import django, datetime
from rest_framework import serializers
# syllabus imports
from ..models import Class, Event, Section, Grade, GradingScale, GradingCategory
from syllabus.core.models import Upload
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
        fields = ('id', 'possiblePoints')

    possiblePoints = serializers.SerializerMethodField('getPossiblePoints')

    def getPossiblePoints(self, obj):
        """ return the total number of possible points associated with this event"""
        data = obj.metaData.filter(key = 'possiblePoints')
        if data:
            return data[0].value
        else:
            return '--'

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
        fields = ('breadcrumb', 'events', 'gradebook', 'students')
    
    # the meta data of students in the class
    students = serializers.SerializerMethodField('getStudents')
    # the meta data of gradable events in the class
    events = serializers.SerializerMethodField('getGradableEvents')
    # the gradebook dictionary of {student} -> {event} -> {grade}
    gradebook = serializers.SerializerMethodField('getGradebook')
    # get the breadcrumb
    breadcrumb = serializers.SerializerMethodField('getBreadcrumb')

    def getStudents(self, obj):
        """ return the students in the serialized class """
        # save the data as a list of dictionarys
        data = []
        # get the users who are in the class
        users = User.objects.filter(classes__pk = obj.pk)
        # for each user
        for user in users:
            # save the name
            data.append({
                "name" : user.first_name + ' ' + user.last_name,
                "id": user.pk,
                "totalGrade": obj.totalGrade(user.id),
            })
        
        # return the serialized data
        return data

    def getGradableEvents(self, obj):
        """ return the events that are gradable """
        # gradable events are not lectures or meetings that are due before tomorrow
        events = obj.getGradableEvents()
        # serialize the events
        serializer = EventSerializer(events)
        # return the serialized data
        return serializer.data

    def getGradebook(self, obj):
        """ return a dictionary of students pointing another dict
            of events to gradebook data """
        # gradebook is a dictionary of dictionaries
        gradebook = {}
        # the first level of keys correspond to the id of the student
        for student in User.objects.filter(classes__pk = obj.pk):
            gradebook[student.pk] = {}
            # the second level is the event
            for event in obj.getGradableEvents():
                gradebook[student.pk][event.pk] = {}
                
                # get the grades associated with this student/event
                grade = Grade.objects.filter(student = student).filter(event = event)
                # if there is a grade save it, otherwise use an empty string
                gradebook[student.pk][event.pk]['grade'] = grade[0].score if grade else ''

                # get the uploads
                uploads = Upload.objects.filter(event = event).filter(user = student).count()
                # if there are uploads, set it to true otherwise false
                gradebook[student.pk][event.pk]['hasUploads'] = True if uploads else False
                
                # set the onTime
                gradebook[student.pk][event.pk]['onTime'] = event.isStudentOnTime(student)
                

        return gradebook

    def getBreadcrumb(self, obj):
       return [obj.profile.interest + ' ' + str(obj.profile.number)] 

class GradingCategorySerializer(serializers.ModelSerializer):
    class Meta:
        """ meta class for GradingCategorySerializer """
        model = GradingCategory
        fields = ("lower", "value")

class GradingScaleSerializer(serializers.ModelSerializer):
    class Meta:
        """ meta class for GradingScaleSerializer """
        model = GradingScale
        fields = ('name', 'gradingCategories')

    gradingCategories = serializers.SerializerMethodField('getCategories')

    def getCategories(self, obj):
       """ return a serialization of the categories for this scale""" 
       categories = obj.gradingCategories.all()
       serializer = GradingCategorySerializer(categories)
       return serializer.data
       
       

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        """ meta class for SectionSerializer """
        model = Section
        fields = ('id', )
