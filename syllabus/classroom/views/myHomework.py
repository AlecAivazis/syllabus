# this file contains the views that handle a detailed view of users gradable assignments
# author: alec aivazis

# python imports
import json
# django imports
from django.shortcuts import render_to_response, HttpResponse
# syllabus models
from ..models import Event, State

def myHomework(request):
    """ return a detailed list of the current users homework """
    return render_to_response('myhomework/myhomework.html', locals())

def updateEventState(request):
    """ handle the turnIn of an individual assignment by a particular user """
    # load the json data
    post = json.loads(bytes.decode(request.body))

    # grab the requested id for the target event
    id = post['eventId']
    # and the corresponding event object
    event = Event.objects.get(pk = id)

    # create a state object to log the user turning in this assignment
    state = State()
    state.status = post['status']
    # register the user
    state.user = request.user
    # associate the event with this action
    state.event = event
    # save the record
    state.save()

    # return a success
    return HttpResponse('success')


def myHomework_old(request):
    oz = os
    fileRoot = settings.ROOT
    user = request.user
    when = request.GET['when']
    sections = Section.objects.filter(students = user).order_by('qlass')
    date = 0
    

    if when == 'today':
        dates = [datetime.date.today()]
    elif when == 'tomorrow':
        dates = [datetime.date.today() + datetime.timedelta(days = 1)]

    
    length = len
    
    uploads = {}
    status={}
    completed = []
    

    events = {}
    for date in dates:
        for section in sections:
            targetEvents = section.qlass.events.filter(date=date).exclude(category='lecture').exclude(category='test')
            
            if targetEvents:
                events[section] = targetEvents  
              
            for event in section.qlass.events.all():
                if State.objects.filter(event = event).filter(owner = request.user):
                    status[event.id] = State.objects.filter(event = event).filter(owner = request.user).order_by('-date')[0].status
                    if status[event.id] != 'revoked':
                        completed.append(event.id)
                        
                if Upload.objects.filter(event = event):
                    uploads[event.id] = Upload.objects.filter(event=event).filter(user = request.user)
    
    return render_to_response('myhomework.html', locals())

def turnIn_old(request):
    
    event = Event.objects.get(id = request.GET['event'])
    overwrite = False
    for f in request.FILES.getlist('files'):
        dirname = os.path.join(settings.UPLOAD_DIR, os.path.join(event.classes.all()[0].profile.interest+'-'+str(event.classes.all()[0].profile.number), 'turn-ins'))
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        filename = os.path.join(dirname, f.name)
        
        d = open(filename, 'wb') 
        for chunk in f.chunks():
            d.write(chunk)
        d.close()
        
        if Upload.objects.filter(event = event).filter(user = request.user).filter(file=filename):
            Upload.objects.filter(event=event).filter(user = request.user).get(file=filename).delete()
            overwrite = True
        
        upload = Upload()
        upload.event = event
        upload.user = request.user
        upload.file = filename
        upload.save()

    script = "top.turnedIn('"+ str(event.id)+ "','" + os.path.basename(upload.file) + "');"
    
    if overwrite:
        script = "top.turnedIn('"+ str(event.id)+ "','" + os.path.basename(upload.file) + "', 1);"
    return HttpResponse('<script type="text/javascript">' + script + '</script>')
