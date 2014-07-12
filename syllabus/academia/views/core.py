from syllabus import *

from ..models import Interest

import json

# get the classes that are in a given interest
def getInterestClasses(request):
    # define the GET behavior
    if request.method == "GET":
        # see if they gave us an id for the interest
        interestId = request.GET["id"] if "id" in request.GET else 0
        # if they did
        if (interestId):
            # grab the interest instance
            interest = Interest.objects.get(pk = request.GET["id"])
            # build the data object
            classes = {}
            # loop over the classes in the interest
            for profile in interest.courses.all():
                # add it to the collection
                classes[profile.number] = profile.pk

            # and return it
            return HttpResponse(json.dumps(classes), content_type="application/json")
            
