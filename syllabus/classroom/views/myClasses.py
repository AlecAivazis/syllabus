from syllabus import *

# syllabus imports
from syllabus.classroom.models import Section, Class
from syllabus.academia.models import Term, Department, Interest, ClassProfile
from syllabus.core.models import Timeslot


dayDict={
    '1':'M',
    '2':'T',
    '3':'W',
    '4':'Th',
    '5':'F',
    '6':'Sat',
    '7':'Sun'
}

def classPage(request):
    
    if 'id' in request.GET:
        klass = Class.objects.get(id=request.GET['id'])
        
        
    else:
        
        classes = Class.objects.filter(sections__students = request.user).order_by('profile__term__end')
        pages = defaultdict(list)
        
        for qlass in classes:
            pages[qlass.term].append(qlass)
    
    return render_to_response('/spaces/space.html', locals())
    
    
    
def schedule(request):
    
    terms = defaultdict(list)
    termz = []
    
    classes = []
    
    for section in Section.objects.filter(students = request.user):
        term = section.qlass.term
        if not term.name in terms[str(term.start.year)]:
            terms[str(term.start.year)].append(term.name)
        
        if section.qlass.term not in termz:    
            termz.append(term)
            
        if section.qlass not in classes:
            classes.append(section.qlass)
    
    currentTerm = ''
    
    for term in termz:
        if term.start <= datetime.date.today() < term.end:
            currentTerm = term
    
    string = str
    
        
    times = collections.OrderedDict()
    
    
    for qlass in classes:
        times[qlass]=collections.OrderedDict()
        for time in qlass.times.all():
            if (time.start, time.end) not in times[qlass]:
                times[qlass][(time.start,time.end)]=[dayDict[time.day]]
            else:
                times[qlass][(time.start,time.end)].append(dayDict[time.day])
                
        for section in qlass.sections.all():
            times[section]=collections.OrderedDict()
            for time in section.times.all():
                if (time.start, time.end) not in times[section]:
                    times[section][(time.start,time.end)]=[dayDict[time.day]]
                else:
                    times[section][(time.start,time.end)].append(dayDict[time.day])    
        
    return render_to_response('myClasses/schedule.html', locals())

def confDrop(request):
    
    qlass = Class.objects.get(pk=request.GET['id'])
    
    return render_to_response('myClasses/confDrop.html', locals())
    
def getSchedule(request):
    year = int(request.GET['year'])
    name = request.GET['term']
    user = request.user
    term = Term.objects.filter(name=name,start__year=year)
    
    sectionDict = defaultdict(list)
    
    sectionz = Section.objects.filter(students = request.user).filter(qlass__term=term)
    classes = Class.objects.filter(sections__students = request.user).filter(term=term)
    sections = []

    for section in sectionz:
        if section not in sections:
            sections.append(section)
            
    return render_to_response('myClasses/getSchedule.html', locals())
    
def grades(request):
    grades = {}
    colleges = []    
    
    for major in request.user.major.all():
        if major.college not in colleges:
            colleges.append(major.college.all()[0])
    
    for qlass in Class.objects.filter(sections__students = request.user):
        if qlass.term.start.year not in grades:
            grades[qlass.term.start.year] = []
        
        grades[qlass.term.start.year].append(qlass)
    return render_to_response('myClasses/grades.html', locals())

def courseInfoTable(request):
    classes = []
    
    for section in Section.objects.filter(students = request.user):
        if section.qlass not in classes:
            classes.append(section.qlass)
            
    times = collections.OrderedDict()
    
    
    for qlass in classes:
        times[qlass]=collections.OrderedDict()
        for time in qlass.times.all():
            if (time.start, time.end) not in times[qlass]:
                times[qlass][(time.start,time.end)]=[dayDict[time.day]]
            else:
                times[qlass][(time.start,time.end)].append(dayDict[time.day])
                
        for section in qlass.sections.all():
            times[section]=collections.OrderedDict()
            for time in section.times.all():
                if (time.start, time.end) not in times[section]:
                    times[section][(time.start,time.end)]=[dayDict[time.day]]
                else:
                    times[section][(time.start,time.end)].append(dayDict[time.day])
            
    return render_to_response('myClasses/classInfoTable.html', locals())
    
def runTask(request):
    cmd = request.GET['cmd']
    
    if cmd == "drop":
        qlass = Class.objects.get(id = request.GET['id'])
        section = Section.objects.filter(qlass = qlass).filter(students = request.user)
        enrollment = Enrollment.objects.filter(student=request.user).get(section=section)
        
        enrollment.student = None
        enrollment.save()
        
        return HttpResponse('You have successfully dropped ' + str(qlass) + "!")

    
def catalog(request):
    
    terms = Term.objects.all()
    
    currentTerm = Term.objects.getCurrentTerm()
    
    departments = Department.objects.all()
    
    courses = []
    
    for klass in  Class.objects.filter(term = currentTerm):
        if klass.profile not in courses:
            courses.append(klass.profile)
            
    interests = Interest.objects.all()
 
    occupancy = {}
    
    times = collections.OrderedDict()
    
    courseDict = collections.defaultdict(list)

    for course in courses:
        classes = course.classes.all()
        prepareCatalog(course, classes, times, occupancy, courseDict)
    
    return render_to_response('myClasses/catalog/base.html', locals())
    
def filterCatalog(request):
    
    # catch the current term
    term = Term.objects.get(id = request.GET['term'])
    
    # collect all of this term's classes
    classes = Class.objects.filter(term = term)
    
    #filter...
    if 'interest' in request.GET:
        classes = classes.filter(profile__interest=request.GET['interest'])
        
    if 'unitsLower' in request.GET:
        classes = classes.filter(profile__units__gte = int(request.GET['unitsLower']))
        
    if 'unitsUpper' in request.GET:
        classes = classes.filter(profile__units__lte = int(request.GET['unitsUpper']))
    
    if 'courseNumber' in request.GET:
        classes = classes.filter(profile__number = request.GET['number'])
    
    # lets filter times by creating all of the possible time slots and matching against that list
    
    timez = Timeslot.objects.all()
        
    if 'timeStart' in request.GET:
        timeInfo = request.GET['timeStart'].split(':')
        time = datetime.time(int(timeInfo[0]), int(timeInfo[1]))
        timez = timez.filter(start__gte = time)
        
    if 'timeEnd' in request.GET:
        timeInfo = request.GET['timeEnd'].split(':')
        time = datetime.time(int(timeInfo[0]), int(timeInfo[1]))
        timez = timez.filter(end__lte = time)
    
    # split days on '-'
    
    if 'days' in request.GET:
        days = request.GET['days'].split('-')

        timez = timez.filter(day__in = days)
    
    classes = classes.filter(times__in = timez).distinct()
                
            
    
    # build list of profiles
    courses = []
    
    for qklass in classes:
        if qklass.profile not in courses:
            courses.append(qklass.profile)
    
    #layout dictionaries    
    occupancy = {}
    times = collections.OrderedDict()
    courseDict = collections.defaultdict(list)
    
    for course in courses:
        prepareCatalog(course, classes.filter(profile=course), times, occupancy, courseDict)    
    
    
    return render_to_response('myClasses/catalog/list.html', locals())


def prepareCatalog(course, classes, times, occupancy, courseDict):
    
    for qlass in classes:
        times[qlass]={}
        enrolled = 0
        
        courseDict[course].append(qlass)
        
        for time in qlass.times.all().order_by('day'):
            if (time.start, time.end) not in times[qlass]:
                times[qlass][(time.start,time.end)]=[dayDict[time.day]]
            else:
                times[qlass][(time.start,time.end)].append(dayDict[time.day])
                
        for section in qlass.sections.all():
            times[section]=collections.OrderedDict()
            for time in section.times.all():
                if (time.start, time.end) not in times[section]:
                    times[section][(time.start,time.end)]=[dayDict[time.day]]
                else:
                    times[section][(time.start,time.end)].append(dayDict[time.day])
            
            occupancy[section]=[section.maxOccupancy,section.students.all().count()]
    
            enrolled += section.students.count()
        
        occupancy[qlass]=[qlass.maxOccupancy,enrolled]

def addSection(request):
    section = Section.objects.get(id=request.POST['id'])
    qlass = section.qlass
    
    
    enrolledClasses = []
    
    for enrollment in request.user.enrollments.all():
        if enrollment.section.qlass not in enrolledClasses:
            enrolledClasses.append(enrollment.section.qlass.profile)

    if qlass.profile in enrolledClasses:
        enrollment = Enrollment.objects.filter(section__qlass__profile = qlass.profile).get(student=request.user)
        
        enrollment.delete()

    enrollment = Enrollment()
    enrollment.section = section
    enrollment.student = request.user
    enrollment.save()
    
    return HttpResponse('success')
        

def confirmAddSection(request):
    section = Section.objects.get(id = request.GET['id'])
    qlass = section.qlass
    eligible = qlass.isEligible(request.user, True)
    which = request.GET['which']
    switch = request.GET['zwitch']

    return render_to_response('/myClasses/catalog/confirmAddSection.html', locals())
