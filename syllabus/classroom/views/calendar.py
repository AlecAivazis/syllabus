# syllabus imports
from syllabus import *
from syllabus.classroom.models import Class, Event
from syllabus.academia.models import RegistrationGroup, Term
# python imports
import json


def editEventForm(request):
    
    id = request.GET['id']
    event  = Event.objects.get(pk=int(id))
    
    oz = os
    fileRoot = settings.ROOT
    
    return render_to_response ('calendar/editEventForm.html', locals())

def editEvent(request):
    
    id = request.POST['id']
    event = Event.objects.get(pk=int(id))
    year = request.POST['year']
    month = request.POST['month']
    day = request.POST['day']
    
    if Class.objects.filter(events=event).filter(professor = request.user):
        
        date = datetime.date(int(request.POST['year']), int(request.POST['month']), int(request.POST['day']),)
        
        event.title = request.POST['title']
        event.description = request.POST['description']
        event.date = date
        event.time = request.POST['time']
        event.category = request.POST['category']
        event.save()
        
        if 'possiblePoints' in request.POST and event.category == 'assignment':
            if event.metaData.filter(key='possiblePoints'):
                if request.POST['possiblePoints']== '' :
                    meta = event.metaData.get(key='possiblePoints')
                    event.metaData.remove(meta)
                else:   
                    meta = event.metaData.get(key='possiblePoints')
                    meta.value = request.POST['possiblePoints']
                    meta.save()
                    
            else:
                if request.POST['possiblePoints'] != '' :
                    meta = MetaData()
                    meta.key = 'possiblePoints'
                    meta.value = request.POST['possiblePoints']
                    meta.save()
                
                    event.metaData.add(meta)
                
        if 'associatedReading' in request.POST and event.category == 'lecture':
            if event.metaData.filter(key='associatedReading'):
                if request.POST['associatedReading']== '' :
                    meta = event.metaData.get(key='associatedReading')
                    event.metaData.remove(meta)
                else:   
                    meta = event.metaData.get(key='associatedReading')
                    meta.value = request.POST['associatedReading']
                    meta.save()
                    
            else:
                if request.POST['associatedReading'] != '' :
                    meta = MetaData()
                    meta.key = 'associatedReading'
                    meta.value = request.POST['associatedReading']
                    meta.save()
                
                    event.metaData.add(meta)
                    
        if request.POST['deletedFiles']:
            for uid in request.POST['deletedFiles'].split(','):
                if uid:
                    fyle = File.objects.get(id = uid)
                    event.files.remove(fyle)
                    fyle.delete()
                
        for f in request.FILES.getlist('files'):
            
            dirname = os.path.join(settings.UPLOAD_DIR, os.path.join(event.classes.all()[0].profile.interest+'-' + str(event.classes.all()[0].profile.number), event.category+'s'))
            if not os.path.exists(dirname):
                    os.makedirs(dirname)
            filename = os.path.join(dirname, f.name)
            
            d = open(filename, 'wb') 
            for chunk in f.chunks():
                d.write(chunk)
            d.close()
            
            file = File()
            file.fileName = filename
            file.save()
            
            event.files.add(file)
        
        if 'subCategory' in request.POST:
            if event.metaData.filter(key='subCategory'):
                meta = event.metaData.filter(key='subCategory')[0]
                meta.value = request.POST['subCategory'].lower()
                meta.save()
                
                    
            else:
                meta = MetaData()
                meta.key = 'subCategory'
                meta.value = request.POST['subCategory'].lower()
                
                meta.save()
            
                event.metaData.add(meta)
    
        return HttpResponse('<script type="text/javascript"> top.closeEventForm(' + year + ',' + month + ',' + day +') </script>')

def moveEvent(request):
    
    # load the json data
    post = json.loads(bytes.decode(request.body))
    # load the post
    id = post['id']
    targetDate = post['date']

    print(targetDate)
    
    year= targetDate.split('-')[0]
    month = targetDate.split('-')[1]
    day = targetDate.split('-')[2]
    
    event = Event.objects.get(id=int(id))
    if event:
        if Class.objects.filter(events=event).filter(professor = request.user):
            event.date = date(int(year), int(month), int(day))
            event.save()
            return HttpResponse('success')
        else:
            return HttpResponse('You do not have permission to move this event')
    else:
        return HttpResponse('Event could not be found')

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


def deleteEvent(request):
    
    id = request.POST['id']
    event = Event.objects.get(id=int(id))
    if event:
        if Class.objects.filter(events=event).filter(professor = request.user):    
            event.delete()
    
    
    return HttpResponse('success!')

def getSectionsById(request):
    
    id = request.GET['id']
    sections = Section.objects.filter(qlass__id__exact = int(id))
    
    return render_to_response('calendar/getSectionsById.html', locals())

def loadEvents(request):
    
    targetDate = request.GET['date']
    
    day  = calendar.datetime.date(year=int(targetDate.split('-')[0]), month=int(targetDate.split('-')[1]), day=int(targetDate.split('-')[2]))
    
    eventDict = collections.defaultdict(list)
    
    for qlass in Class.objects.filter(professor = request.user):
        for event in qlass.events.all():
            if str(event.date) == str(day):
                if not event in eventDict[qlass]:
                    eventDict[qlass].append(event)
    order = sorted
    return render_to_response('calendar/sidebarevents.html', locals())

def newEventForm(request):
    
    targetDate = request.GET['date']
    
    year = targetDate.split('-')[0]
    month = targetDate.split('-')[1]
    day = targetDate.split('-')[2]
    
    user = request.user
    
    classes = Class.objects.filter(professor=user).all()
    
    sections = []
        
    for qlass in classes:
        sections.append(qlass.sections.all())
    
    return render_to_response('calendar/newEventForm.html', locals())

def calendarAjax(request):
    
    which = request.GET['which']
    year = request.GET['year']
    number = request.GET['number']
    
    if which =="month":
        c = calendar.Calendar()
        c.setfirstweekday(calendar.SUNDAY)
        today = datetime.date.today()
        klass = []
        
        intMonth = today.month
        
        if year:
            if number:
                monthList =  c.monthdatescalendar(year=int(year), month=int(number))
                intMonth = int(number)
            else:
                monthList = c.monthdatescalendar(month=int(number), year=today.year)      
            
            
        else :
            monthList = c.monthdatescalendar(month=today.month, year=today.year)
            year = today.year
            
        if number:        
            monthName = calendar.month_name[int(number)]
        else: 
            monthName = calendar.month_name[today.month]
            
        eventDict=collections.defaultdict(list)
        
        
        sections = []
        
        for qlass in Class.objects.filter(professor=request.user).all():
            for event in qlass.events.all():
                if event.date.month == intMonth or event.date.month == intMonth-1 or event.date.month == intMonth+1:
                    if not event in  eventDict[str(event.date)]:
                        eventDict[str(event.date)].append(event)
                        
        # lets get the groups that start this month
        groups = defaultdict(list)
        termDates = defaultdict(list)
        

        for group in RegistrationGroup.objects.filter(start__month = intMonth):
            groups[group.start].append((group, 'Start',))

        for group in RegistrationGroup.objects.filter(end__month = intMonth):
            groups[group.end].append((group, 'End',))
            
        for term in Term.objects.filter(start__month=intMonth).filter(start__year = year):
            termDates[term.start].append((term, 'Start'))
        
        for term in Term.objects.filter(end__month=intMonth).filter(end__year = year):
            termDates[term.end].append((term, 'End'))

            
        return render_to_response('calendar/calendarMonthAjax.html', locals())
    
    else:
        
        today = datetime.date.today()
        todayNumber = today.isocalendar()[1] 
        
        if today.weekday() < 6:
            todayNumber = today.isocalendar()[1]
        else:
            todayNumber = today.isocalendar()[1] + 1
        
        if not number:

            iso = today.isocalendar()
            
            if today.weekday() < 6:
                number = iso[1]
            else:
                number = iso[1] + 1
                
            if year:

                year = int(year)
            else: 
                year = iso[0]
        
        else: 
            if not year:
                year = today.year
                
        firstDay = iso_to_gregorian(year, int(number), 0);
                
        
        eventDict = collections.OrderedDict()
        
        day = firstDay

        
        if request.user.groups.filter(name= 'teacher') or request.user.groups.filter(name= 'super') or request.user.groups.filter(name='admin'):
            
            sections = []
            for qlass in Class.objects.filter(professor = request.user):
                for section in qlass.sections.all():
                    sections.append(section)
        elif request.user.groups.filter(name='student'):
            sections = Section.objects.filter(students=request.user)
        
        for i in range(7):
            eventDict[day] = []
            for section in sections:
                for event in section.qlass.events.all():
                    if event.date == day:
                        if event not in eventDict[day]:
                            eventDict[day].append(event)
 

            day = day + datetime.timedelta(days = 1) 
        
        return render_to_response('calendar/calendarWeekAjax.html', locals())

def iso_year_start(iso_year):
    "The gregorian calendar date of the first day of the given ISO year"
    fourth_jan = datetime.date(int(iso_year), 1, 4)
    delta = datetime.timedelta(fourth_jan.isoweekday()-1)
    return fourth_jan - delta 

def iso_to_gregorian(iso_year, iso_week, iso_day):
    "Gregorian calendar date for the given ISO year, week and day"
    year_start = iso_year_start(iso_year)
    return year_start + datetime.timedelta(days=int(iso_day)-1, weeks=int(iso_week)-1)


def calendarHome(request, which='month', year=datetime.date.today().year, number=datetime.date.today().month):
    if which == "month":
        today = datetime.date.today()
        intMonth = today.month
        
        if year:
            if number:
                intMonth = int(number)
            
        else :
            year = today.year
            
        return render_to_response('calendar/home.html', locals())
    elif which == "week":
        
        intMonth = number
        
        today = datetime.date.today()
        
        if not year:
            year = today.year
        
        return render_to_response('calendar/calendar.html', locals())
    else:
        return HttpResponse(which + year + number)
    

def context(request):
    
    return render_to_response('calendar/calendarContext.html', locals())

def createEvent(request):
    year = request.POST['year']
    month = request.POST['month']
    day = request.POST['day']
    
    if request.method == "POST":
        date = datetime.date(int(request.POST['year']), int(request.POST['month']), int(request.POST['day']),)
        qlass = Class.objects.get(id=request.POST['classId'])
        
        event = Event()
        event.title = request.POST['title']
        event.date = date
        event.description = request.POST['description']
        event.category = request.POST['category'].lower()
        
        if request.POST['time'] == 'class':
            timeDay = date.weekday() + 1
            if qlass.times.filter(day=timeDay):
                time = qlass.times.filter(day=timeDay)[0].start
                event.time = time
            else:
                return HttpResponse('<script type="text/javascript"> top.alert("the class does not meet on that day") </script>')
        else:
            event.time = datetime.time(hour=int(request.POST['time'].split(':')[0]), minute=int(request.POST['time'].split(':')[1]))
        
        
        event.save()
        
        if 'associatedReading' in request.POST and event.category == 'lecture':
            meta = MetaData()
            meta.key = 'associatedReading'
            meta.value = request.POST['associatedReading']
            meta.save()
            
            event.metaData.add(meta)
            
        if 'possiblePoints' in request.POST and event.category == 'assignment':
            meta = MetaData()
            meta.key = 'possiblePoints'
            meta.value = request.POST['possiblePoints']
            meta.save()
            
            event.metaData.add(meta)
        
        if request.POST['subCategory']:
            meta = MetaData()
            meta.key = 'subCategory'
            meta.value = request.POST['subCategory'].lower()
            
            meta.save()
            
            event.metaData.add(meta)
            
        
        for f in request.FILES.getlist('files'):
            dirname = os.path.join(settings.UPLOAD_DIR, os.path.join(qlass.profile.interest+'-'+str(qlass.profile.number), event.category+'s'))
            if not os.path.exists(dirname):
                    os.makedirs(dirname)
            filename = os.path.join(dirname, f.name)
            
            d = open(filename, 'wb') 
            for chunk in f.chunks():
                d.write(chunk)
            d.close()
            
            file = File()
            file.fileName = filename
            file.save()
            
            event.files.add(file)
        
        sectionId = int(request.POST['sectionId'])
        if sectionId > 0:
            section = Section.objects.get(id=sectionId)
            section.qlass.events.add(event)
        else:
            qlass.events.add(event)

        return HttpResponse('<script type="text/javascript"> top.closeEventForm(' + year + ',' + month + ',' + day +') </script>')


def newTermStart(request):
    
    date = request.GET['date']
    
    if 'id' in request.GET: pass
    else:
        tutor = ''

    return render_to_response('/calendar/termStartForm.html', locals())

def newTermEnd (request):
    
    date = request.GET['date']
    terms = Term.objects.filter(end=None)
    
    return render_to_response('/calendar/termEndForm.html', locals())

def createTermEnd(request):
    
    term = Term.objects.get(id=request.POST['id'])
    term.end =  datetime.datetime.strptime(request.POST['date'], "%Y-%m-%d").date()
    term.save()

    return HttpResponse('success')
   
def createTerm(request):


    term = Term()
    term.name = request.POST['name']
    term.start = datetime.datetime.strptime(request.POST['date'], "%Y-%m-%d").date()
    term.save()

    return HttpResponse('success')

def startRegistrationForm(request):
    rng = range
    university = University.objects.all()[0]
    date = request.GET['date']
    terms = Term.objects.all()

    return render_to_response('/calendar/registrationStartForm.html', locals())

def endRegistrationForm(request):
    rng = range
    date = request.GET['date']
    terms = Term.objects.all()
    groups = RegistrationGroup.objects.all()

    return render_to_response('/calendar/registrationEndForm.html', locals())


def createRegistrationPass(request):
    
    term = Term.objects.get(id=request.POST['term'])
    
    group  = RegistrationGroup()
    group.name = request.POST['name']
    group.start =  datetime.datetime.strptime(request.POST['date'], "%Y-%m-%d").date()
    group.term = term
    group.save()
       
    return HttpResponse('success!')



def endRegistration(request):
    
    term = Term.objects.get(id=request.POST['term'])
    group = RegistrationGroup.objects.get(id=request.POST['id'])
    
    group.end =  datetime.datetime.strptime(request.POST['date'], "%Y-%m-%d").date()
    group.save()

       
    return HttpResponse('success!')
