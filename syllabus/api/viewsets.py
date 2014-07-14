from .serializers import InterestSerializer

from ..academia.models import Term

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
