from rest_framework import generics, permissions
from django.http import HttpResponse

from .serializers import ClassSerializer, SectionSerializer, EventSerializer, GradebookSerializer
from ..models import Class, Section, Event

import django, datetime

# return all of the classes
class ClassList(generics.ListCreateAPIView):
    model = Class
    serializer_class = ClassSerializer
    permission_classes = [
        permissions.AllowAny
    ]

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

# return all of the sections
class SectionList(generics.ListCreateAPIView):
    model = Section
    serializer_class = SectionSerializer
    permission_classes = [
        permissions.AllowAny
    ]

# return all of the sections
class EventList(generics.ListCreateAPIView):
    model = Event
    serializer_class = EventSerializer
    permission_classes = [
        permissions.AllowAny
    ]

# return all of the sections
class EventsByClass(generics.ListCreateAPIView):
    model = Event
    serializer_class = EventSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    # return the events from the requested class
    def get_queryset(self):
        return Event.objects.filter(classes__id=self.kwargs.get('id'))

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

