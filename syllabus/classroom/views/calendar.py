# syllabus imports
from syllabus import *
from syllabus.classroom.models import Class, Event
from syllabus.academia.models import RegistrationGroup, Term
# python imports
import json

def moveLabel(request):
    
    id = request.POST['id']
    targetDate = request.POST['date']

    
    year= targetDate.split('-')[0]
    month = targetDate.split('-')[1]
    day = targetDate.split('-')[2]
    
    if request.POST['type'] == 'group':
        group = RegistrationGroup.objects.get(id=int(id))
        if group:
        
            which = request.POST['which']

            if which == 'start':
                group.start = date(int(year), int(month), int(day))
            else:
                group.end =  date(int(year), int(month), int(day))

            group.save()
            
            return HttpResponse('success')
        else:
            return HttpResponse('Group could not be found')

    elif request.POST['type'] == 'term':
        term = Term.objects.get(id=int(id))
        if term:
        
            which = request.POST['which']

            if which == 'start':
                term.start = date(int(year), int(month), int(day))
            else:
                term.end =  date(int(year), int(month), int(day))

            term.save()
            
            return HttpResponse('success')
        else:
            return HttpResponse('Term could not be found')

