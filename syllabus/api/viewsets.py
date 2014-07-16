from .serializers import InterestSerializer, ExemptionSerializer, TermTemplateSerializer

from ..academia.models import  MajorExemption, Term, TermTemplate

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import link

from ..academia.models import Interest


class InterestViewset(viewsets.ModelViewSet):
    """ 
    the viewset for the interest api
    """
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer

class ExemptionViewset(viewsets.ModelViewSet):
    """
    the viewset for the exemption api
    """
    queryset = MajorExemption.objects.all()
    serializer_class = ExemptionSerializer

class TermTemplateViewset(viewsets.ModelViewSet):
    """
    the viewset for the term templates
    """
    queryset = TermTemplate.objects.all()
    serializer_class = TermTemplateSerializer

