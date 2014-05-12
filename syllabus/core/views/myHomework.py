from syllabus import *

def myHomework(request):
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

def turnIn(request):
    
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
