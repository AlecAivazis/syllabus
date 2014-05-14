from syllabus import *

from syllabus.classroom.models import Class

def setSyllabus(request):
    
    if 'syllabus' in request.POST:
        
        qlass = Class.objects.get(id=request.POST['id'])
        if request.user in qlass.professor.all():
            qlass.syllabus = request.POST['syllabus']
            qlass.save()
        
            return HttpResponse('success!')

def viewTimeline(request):
    
    qlass = Class.objects.get(id = request.GET['id'])
    timeline = OrderedDict()
    
    events = qlass.events.order_by('date')
    
    for event in events:
        if event.date not in timeline:
            timeline[event.date]=[event]
        else:
            timeline[event.date].append(event)
    
    oz = os
    fileRoot = settings.ROOT
    
    return render_to_response('/spaces/timeline.html', locals())
    

def changeEventTitle(request):
    
    event = Event.objects.get(id = request.POST['id'])
    if request.user in event.classes.all()[0].professor.all():
        event.title = request.POST['title']
        event.save()
        
    
    return HttpResponse('success')

def viewAnnouncements(request):

    klass = Class.objects.get(id=request.GET['id'])
    announcements = []

    for section in klass.sections.all():
        for announcement in section.announcements.all():
            if announcement not in announcements:
                announcements.append(announcement)

    return render_to_response('/spaces/announcements.html', locals())

def changeEventAssocReading(request):
    event = Event.objects.get(id = request.POST['id'])
    if request.user in event.classes.all()[0].professor.all():
        metas = event.metaData.filter(key = 'associatedReading')
        if metas:
            meta = metas.all()[0]
            meta.value = request.POST['associatedReading']
            meta.save()
        else:
            meta = Meta()
            meta.key = 'associatedReading'
            meta.value = request.POST['associatedReading']
            meta.save()
            
            event.metaData.add(meta)
        
    
    return HttpResponse('success')


def changeEventDescription(request):
    
    event = Event.objects.get(id = request.POST['id'])
    if request.user in event.classes.all()[0].professor.all():
        event.description = request.POST['description']
        event.save()
        
    
    return HttpResponse('success')


def viewSyllabus(request):
    
    if 'id' in request.GET:
        klass = Class.objects.get(id=request.GET['id'])
        
        return render_to_response('spaces/syllabus.html', locals())

def viewSpace(request):
    if 'id' in request.GET:
        qlass = Class.objects.get(id=request.GET['id'])
        
        return render_to_response('/spaces/space.html', locals())
    else:
        
        classes = Class.objects.filter(sections__students = request.user).order_by('profile__term__end')
        pages = defaultdict(list)
        
        for qlass in classes:
            pages[qlass.profile.term].append(qlass)
            
        return render_to_response('/spaces/home.html', locals())
