from rest_framework import generics, permissions
from django.http import HttpResponse

from .serializers import ClassSerializer, SectionSerializer
from ..models import Class, Section

# return all of the classes
class ClassList(generics.ListCreateAPIView):
    model = Class
    serializer_class = ClassSerializer
    permission_classes = [
        permissions.AllowAny
    ]

# return the classes taught by the user
class ClassTaughtByMe(generics.ListCreateAPIView):
    model = Class
    serializer_class = ClassSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    # return the classes that the user teachers
    def get_queryset(self):
        return Class.objects.filter(professor = self.request.user)

# return all of the sections
class SectionList(generics.ListCreateAPIView):
    model = Section
    serializer_class = SectionSerializer
    permission_classes = [
        permissions.AllowAny
    ]
