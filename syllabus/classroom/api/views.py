from rest_framework import generics, permissions

from .serializers import ClassSerializer, SectionSerializer
from ..models import Class, Section

class ClassList(generics.ListCreateAPIView):
    model = Class
    serializer_class = ClassSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class SectionList(generics.ListCreateAPIView):
    model = Section
    serializer_class = SectionSerializer
    permission_classes = [
        permissions.AllowAny
    ]
