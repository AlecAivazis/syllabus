from rest_framework import generics, permissions
from django.http import HttpResponse, HttpResponseBadRequest

from .serializers import (ClassSerializer, SectionSerializer, EventSerializer, 
                          GradebookSerializer, GradingScaleSerializer, WeightSerializer, 
                          CalendarSerializer, HomeworkSerializer, UserClassSchedule, 
                          UserGradeSerializer)


from ..academia.models import Term, Interest
from ..classroom.models import Class, Section, Event, GradingScale, Weight
from ..core.models import SyllUser, MetaData

import django, datetime

# return all of the classes
class ClassList(generics.ListCreateAPIView):
    model = Class
    serializer_class = ClassSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class CurrentClassesForUser(generics.ListAPIView):
    """ return the current terms classes that this user is a part of """
    model = Class
    serializer_class = ClassSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    def get_queryset(self):
        # store the requested pk 
        pk = self.kwargs.get('pk')
        # if they asked for 'me' then replace it with the users pk
        if pk == 'me':
            # if so use grab the current users pk
            pk = self.request.user.pk
        
        # grab the appropriate user
        user =  SyllUser.objects.get(pk = pk)
        # get the current term
        term = Term.objects.getCurrentTerm()
        # return the classes that this user is a part of in the right term
        return Class.objects.filter(sections__students = user).filter(term = term)
        

class ClassScheduleForUser(generics.RetrieveAPIView):
    """ return the sections and classes of requested user in the requested term """
    model = SyllUser
    serializer_class = UserClassSchedule
    permission_classes = [
        permissions.AllowAny
    ]
   
    # return the classes that the user teachers
    def get_object(self):
        # store the requested pk 
        pk = self.kwargs.get('pk')
        # if they asked for 'me' then replace it with the users pk
        if pk == 'me':
            # if so use grab the current users pk
            pk = self.request.user.pk
        
        # grab the appropriate user
        return SyllUser.objects.get(pk = pk)

# return the weights of a class
class WeightsList(generics.RetrieveUpdateDestroyAPIView):
    model = Weight
    serializer_class = WeightSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    # return the classes that the user teachers
    def get_object(self):
        return Class.objects.get(pk = self.kwargs.get('pk')).weights

# return the classes taught by the user
class ClassesTaughtByMe(generics.ListCreateAPIView):
    model = Class
    serializer_class = ClassSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    # return the classes that the user teachers
    def get_queryset(self):
        return Class.objects.filter(professor = self.request.user)

class GradesForUser(generics.RetrieveAPIView):
    """ return a grade summary of the users classes as well as graduation information """
    model = SyllUser
    serializer_class = UserGradeSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    # turn 'me' into a proper pk
    def get_object(self):
        # store the requested pk 
        pk = self.kwargs.get('pk')
        # if they asked for 'me' then replace it with the users pk
        if pk == 'me':
            # if so get the current users pk
            pk = self.request.user.pk

        # grab the appropriate user
        return SyllUser.objects.get(pk = pk)
       
# return the data necessary for a gradebook (read-only)
class Gradebook(generics.RetrieveAPIView):
    model = Class
    serializer_class = GradebookSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    # return the requested class
    def get_object(self):
        return Class.objects.get(pk = self.kwargs.get('pk'))

class GradingScale(generics.RetrieveUpdateDestroyAPIView):
    """ return the grading scale for a given class """
    model = GradingScale
    serializer_class = GradingScaleSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    def get_object(self):
        """ return the grading scale for a given class """
        return Class.objects.get(pk = self.kwargs.get('pk')).gradingScale

# return all of the sections
class SectionList(generics.ListCreateAPIView):
    model = Section
    serializer_class = SectionSerializer
    permission_classes = [
        permissions.AllowAny
    ]

# return all of the events in a class
class ClassEventList(generics.ListCreateAPIView):
    model = Event
    serializer_class = EventSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    # return the events from the requested class
    def get_queryset(self):
        return Class.objects.get(pk = self.kwargs.get('pk')).events.all()

class MyCalendar(generics.RetrieveAPIView):
    """ return the calendar of the current user """
    model = SyllUser
    serializer_class = CalendarSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    # return the classes that the user teachers
    def get_object(self):
        return self.request.user

class InterestDetail(generics.RetrieveAPIView):
    """ return a detailed view of the interest """


class RetrieveEvent(generics.RetrieveUpdateDestroyAPIView):
    """ the CRUD interface for syllabus events """
    model = Event
    serializer_class = EventSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    def get_object(self):
        """ return the event specified by the url """
        return Event.objects.get(pk = self.kwargs.get('pk'))

# return all of the homework events that are before and including tomorrow
class HomeworkByClass(generics.ListCreateAPIView):
    model = Event
    serializer_class = EventSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    def get_queryset(self):
        return (Event.objects.filter(classes__id=self.kwargs.get('id'))
                .exclude(category='lecture')
                .exclude(category='meeting')
                .filter(date__lte = django.utils.timezone.now() + datetime.timedelta(days = 1)))

class HomeworkForUser(generics.ListAPIView):
    """ return the homework of the user designated by the url """
    model = Event
    serializer_class = HomeworkSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    def get_queryset(self):
        """ return the gradable events that are due before or on tomorrow """
        # store the requested pk 
        pk = self.kwargs.get('pk')
        # if they asked for 'me' then replace it with the users pk
        if pk == 'me':
            # if so get the current users pk
            pk = self.request.user.pk

        # grab the appropriate user
        user = SyllUser.objects.get(pk = pk)
        # get the sections that the user is a member of
        sections = Section.objects.filter(students = user).order_by('Qlass')
        # save the gradable events from those sections
        events =  Event.objects.filter(classes__section = sections).gradable()
                                
        
        # save the starting date for the event range
        start = self.request.QUERY_PARAMS.get('start', None)
        # save the ending date for the event range
        end = self.request.QUERY_PARAMS.get('end', None)

        # handle special strings

        # save the current datetime
        now = datetime.date.today()

        # if  they asked for 'today'
        if start == 'today':
            # set the appropriate date
            start = now
        if end == 'today':
            end = now

        # if  they asked for 'tomorrow'
        if start == 'tomorrow':
            # set the appropriate date
            start = now + datetime.timedelta(days=1)
        if end == 'tomorrow':
            end = now + datetime.timedelta(days=1)

        # if they asked for 'yesterday'
        if start == 'yesterday':
            # set the appropriate date
            start = now - datetime.timedelta(days=1)
        if end == 'yesterday':
            end = now - datetime.timedelta(days=1)

        # if only a start is given
        if start is not None and end is None:
            # return the filtered query set
            return events.filter(date__gte = start)

        # if only an end is given
        if end is not None and start is None:
            # return the events that were before the end
            return events.filter(date__lte = end)

        # if both were given
        if end and start:
            # return the events that were after the start
            return events.filter(date__gte = start)

        # otherwise return the events
        return events
        

        
class CreateEvent(generics.CreateAPIView):
    """ create an event """
    model = Event
    serializer_class = EventSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    # handle the creation of an event to add various meta data
    def create(self, *args, **kwargs):

        # grab the posted data
        data = self.request.DATA
        
        # check that the necessary data is here
        if ('title' not in data or 'description' not in data or 'date' not in data or 
            'time' not in data or 'category' not in data or 'classes' not in data):
            return HttpResponseBadRequest 

        # create the event
        event = Event()
        event.title = data['title']
        event.description = data['description']
        event.date = data['date']
        event.time = data['time']
        event.category = data['category']
        event.save()

        # add the possiblePoints metaData
        if 'possiblePoints' in data:
            # create the metaData entry
            meta = MetaData()
            meta.key = 'possiblePoints'
            meta.value = data['possiblePoints']
            meta.save()

            # add the metaData to the entry
            event.metaData.add(meta)

        # add the sub category
        if 'category' in data:
            # create the metaData entry
            meta = MetaData()
            meta.key = 'subCategory'
            meta.value = data['category']
            meta.save()

            # add the metaData to the entry
            event.metaData.add(meta)

        # add the associated reading
        if 'associatedReading' in data:
            # create the metaData entry
            meta = MetaData()
            meta.key = 'associatedReading'
            meta.value = data['associatedReading']
            meta.save()

            # add the metaData to the entry
            event.metaData.add(meta)

        # for each class that this event belongs to
        for pk in data['classes']:
            # add the event to the class
            Class.objects.get(pk=pk).events.add(event)
            
        # return the id of the event
        return HttpResponse(event.id)
