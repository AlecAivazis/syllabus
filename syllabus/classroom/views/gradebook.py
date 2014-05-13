from syllabus import *

# syllabus model imports
from syllabus.core.models import Upload, SyllUser
from syllabus.classroom.models import Class, Section, Grade, Event

# django imports
from django.db.models import Count

def gradebookHome(request):
    
    classes = []
    sections = []
    for qlass in Class.objects.filter(professor = request.user):
        for section in qlass.sections.all():
            sections.append(section)
            
    for section in sections:
        if section.qlass not in classes:
            classes.append(section.qlass)
    
    if not classes:
        for section in Section.objects.filter(tas = request.user):
            if section.qlass not in classes:
                classes.append(section.qlass)
                
    if 'selectedClass' in request.GET:
        selectedClass = request.GET['selectedClass']
    
    return render_to_response('gradebook/home.html', locals())

def viewGradeBook(request):
    
    classId = request.GET['classId']
    sectionId = "";
    
    if 'sectionId' in request.GET:
        sectionId = request.GET['sectionId']
    
    qlass = Class.objects.get(id= int(classId))
    sections = Section.objects.filter(qlass = qlass)
    
    
    
    students = []
    breadcrumb = []
    
    gradeBook = collections.OrderedDict()
    #gradeBook = {}
    possiblePoints = {}
    
    tas = []
    
    
    
    if sectionId :
        
        section = Section.objects.get(id = int(sectionId))
        
        # create the breadcrumb
        students = section.students
        child = [section.name]
        
        breadcrumb.append(qlass.profile.interest + ' ' + str(qlass.profile.number))
        breadcrumb.append(' > ')
        breadcrumb.append(child)
        
        events = []
        events = section.qlass.events.exclude(category='lecture').exclude(category = 'meeting').filter(date__lte = datetime.date.today() + datetime.timedelta(days = 1))
        
        studentsSorted  = students.order_by('last_name', 'first_name').all()
        eventsSorted = events.order_by('date')
        
        if section.tas.all():
            tas = section.tas.all()
            
    else: 
        
        for section in sections.all():
            for student in section.students.all().order_by('last_name').order_by('first_name'):
                if student not in students:
                    students.append(student)
            
        
        # create the breadcrumb
                    
        breadcrumb.append(qlass.profile.interest + ' ' + str(qlass.profile.number))
        
        qlass = Class.objects.get(id = int(classId))
        sections = Section.objects.filter(qlass = Class.objects.get(id = int(classId)))
        events = []
        
        
        for event in qlass.events.exclude(category='lecture').exclude(category='meeting').all():
            if event.date <= datetime.date.today() + datetime.timedelta(days = 1):
                events.append(event)
            
        studentsSorted = sorted(students, key=lambda x: x.last_name)
        eventsSorted = sorted(events, key = lambda x: x.date)
        
    #create gradeBook and onTime tracker and files
    onTime = {}
    files = {}
    for student in studentsSorted:
        gradeBook[student] = {}
        onTime[student] = {}
        files[student] = {}
        for event in events:
            grade = Grade.objects.filter(student = student).filter(event = event)
            uploads = Upload.objects.filter(event = event).filter(user = student)
            
            if grade:
                gradeBook[student][event] = grade[0]
                
            if uploads:
                files[student][event] = True
            else:
                files[student][event] = False
                
            if event.state.all():
                # if the most recent status='turned-in' is less than the due date then it is on time
                eventDateTime = datetime.datetime(year = event.date.year, month = event.date.month, day = event.date.day, hour = event.time.hour, minute = event.time.minute)
                #if it was never turned in, it's late
                if event.state.filter(status = 'turned-in').all():
                    if event.state.filter(status='turned-in').filter(owner=student):
                        if event.state.filter(status = 'turned-in').filter(owner=student).order_by('-date')[0].date < eventDateTime:
                            # unless it's been revoked since then or ignored
                            if event.state.filter(status='revoked').filter(date__gt = event.state.filter(status = 'turned-in').order_by('-date')[0].date) or event.state.filter(status='ignored').filter(date__gt = event.state.filter(status = 'turned-in').order_by('-date')[0].date):
                                onTime[student][event] = False
                            else:
                                onTime[student][event] = True
                        else:
                            onTime[student][event] = False
                    else:
                            onTime[student][event] = False
                else:
                    onTime[student][event] = False
            else:
                onTime[student][event] = False
    
    # create possiblePoints
                
    for event in events:
        data = event.metaData.filter(key = 'possiblePoints')
        if data:
            possiblePoints[event.id] = data[0].value
        else:
            possiblePoints[event.id] = '--'
            
    # create totalGrade
    
    totalGrade = {}
    for section in sections:
        for student in studentsSorted:
            totalGrade[student.id] = qlass.totalGrade(student.id)
            
    # calculate total average
    
    number = 0.0
    total = 0.0
    
    for student in studentsSorted:
        if len(totalGrade[student.id])>1:
            number = number + 1
            total = total + float(totalGrade[student.id][1])

        
    if number != 0:
        totalAverage = "%.1f" % (total/number) + '%'
        
    else:
        totalAverage = 'n/a'
    
    length = len
    
    
    if sections.filter(qlass__professor=request.user) or sections.filter(tas = request.user):
        return render_to_response('gradebook/gradebook.html', locals())

def sectionsForClass(request):
    
    id = request.GET['id']
    
    sections = Section.objects.filter(qlass__id__exact = int(id))
    
    if not sections :
        sections = Section.objects.filter(qlass__id__exact = int(id)).filter(tas = request.user)
    
    return render_to_response('gradebook/sectionsForClass.html', locals())

def eventsForClass(request, classId, sectionId = False):
    
    qlass = Class.objects.get(id = int(classId))
    
    if not sectionId:
        events = []
        for section in Section.objects.filter(id = int(qlass.id)):
            eventz = section.events.all()
            for event in eventz:
                if not Grade.objects.filter(section = section).filter(event = event):
                    if event not in events:
                        events.append(event)
    
    if events:    
        return render_to_response('gradebook/eventsForClass.html', locals())
    else:
        return HttpResponse('fail')

def addGrade(request):
    student = SyllUser.objects.get(id = int(request.POST['student']))
    score = request.POST['score'].strip()
    event = Event.objects.get(id = int(request.POST['event']))
    
    if student and event:
        if Class.objects.filter(events=event).filter(professor = request.user):
            grade = Grade.objects.filter(student = student).filter(event = event)
            if grade:
                grade[0].score = score
                grade[0].save()
            else:
                grade = Grade()
                grade.event = event
                grade.student = student
                grade.score = score
                grade.save()
        
        
            return HttpResponse('sucess')

        print("nope.")
            
    else:
        return HttpResponse('fail')

def loadEvent(request):
    
    id = request.GET['id']
    event = Event.objects.get(id = int(id))
    
    return render_to_response('gradebook/loadEvent.html', locals())

def changePossiblePoints(request):
    
    id = request.POST['id']
    
    event = Event.objects.get(id = int(id))
    
    if Class.objects.filter(events=event).filter(professor = request.user):
    
        if event.metaData.filter(key = 'possiblePoints'):
            data = event.metaData.get(key = 'possiblePoints')
            data.value = request.POST['value']
            data.save()
        else:
            data = MetaData()
            data.key = 'possiblePoints'
            data.value = request.POST['value']
            data.save()
            
            event.metaData.add(data)
            
        
        return HttpResponse('sucess');

def changeCategory(request):
    
    event = Event.objects.get(id = int(request.POST['id']))
    if Class.objects.filter(events=event).filter(professor = request.user):
        meta = event.metaData.filter(key='subCategory')
        if meta:
            meta[0].value = request.POST['value'].lower()
            meta[0].save()
        else:
            meta = MetaData()
            meta.key = 'subCategory'
            meta.value = request.POST['value'].lower()
            meta.save()
            
            event.metaData.add(meta)
        
        return HttpResponse('success')

def assignWeights(request):
    
    qlass = Class.objects.get(id = request.POST['class'])
      
    weight = Weight()
    
    weight.save()
    
    for category in request.POST['weights'].split('||'):
        if category != '' :
            info=category.split('//')
            if info[0] != '' and info[1] != '':
                weightCategory = WeightCategory()
                weightCategory.category = info[0].lower()
                weightCategory.percentage = info[1]
                
                weightCategory.save()
                
                weight.categories.add(weightCategory)
                
            
            
    qlass.weights = weight
    qlass.save()
    
    return HttpResponse('success')

def removeWeight(request):
    
    if 'section' in request.POST:
        section = section.objects.filter(id=request.POST['section']).filter(qlass__professor = request.user).all()[0]
        weight = section.weight
        section.weight = None
        weight.remove()
    elif 'class' in request.POST:
        for section in Class.objects.filter(id=request.POST['class']).filter(professor = request.user).all()[0].sections.all():
            weight = section.weights
            section.weight = None
            weight.delete()
            section.save()
            
    return HttpResponse('success')

def eventWeight(request):
    
    event = Event.objects.get(id=request.GET['id'])
    
    return HttpResponse(event.calculateWorth())
    
def totalGrade(request):
    qlass = Class.objects.filter(id=int(request.GET['classId'])).filter(sections__students__id__exact = request.GET['studentId'])
    if qlass:
        tup = qlass[0].totalGrade(request.GET['studentId'])
        if tup[0] != 'n/a':
            return HttpResponse('<span style="float: left;">' + tup[0] + '</span><span style="float: right;" class="score">' + str(tup[1]) + '%</span>')
        else:
            return HttpResponse(tup[0])
            
def count(request):
    
    sort = sorted
    data = request.GET['data'].split(',')
    histogram = collections.Counter()
    
    if 'scale' in request.GET:
        scale = GradingScale.objects.get(id=request.GET['scale'])
    else:
        scale = GradingScale.objects.get(name='tens')
        
    for datum in data:
        category = scale.gradingCategories.filter(lower__lte = datum).order_by('-lower')[0]
        histogram[category.lower] += 1
        
    return render_to_response('gradebook/count.html', locals())

def gradingScale(request):
    
    if 'section' in request.GET:
        scale = Section.objects.get(id = request.GET['section']).qlass.gradingScale
    elif 'class' in request.GET: 
        scale = qlass = (Class.objects.get(id = request.GET['class'])).gradingScale
    else:
        scale = GradingScale.objects.get(name = 'default')
    
    return render_to_response('gradebook/gradingScale.html', locals())

def viewWeights(request):
    
    if 'class' in request.GET: 
        weights = Class.objects.get(id = request.GET['class']).weights
    else:
        weights = []
    
    return render_to_response('gradebook/weights.html', locals())
    
def setScale(request):
    
    if 'name' not in request.POST:
        
        categories = []
        scale = ''
        
        #let's start with every scale that has the same number of categories as what was given to be filter
        scales = GradingScale.objects.all().annotate(count=Count('gradingCategories')).filter(count=len(request.POST['categories'].split(',')))
        
        
        for pair in request.POST['categories'].split(','):
            gradeList = GradingCategory.objects.filter(lower = pair.split('-')[0]).filter(value = pair.split('-')[1]);
            if gradeList:
                category = gradeList[0]
                categories.append(category)
            else:
                category = GradingCategory()
                category.lower = pair.split('-')[0]
                category.value = pair.split('-')[1]
                
                category.save()
                
                
                
                categories.append(category)
                
            scales = scales.filter(gradingCategories = category)
            
        if scales:
            scale = scales[0]
            
        else:
            scale = GradingScale()
            scale.save()
            
            for category in categories:
                scale.gradingCategories.add(category)
    else:
        scale = GradingScale.objects.get(name=request.GET['name'])
    
    qlass =  Class.objects.get(id=request.POST['class'])
        
    qlass.gradingScale = scale
    qlass.save()
    
                
    return HttpResponse(scale.gradingCategories)
    
def allStudents(request):
    
    users = User.objects.all()
    
    return render_to_response('gradebook/assistants.html', locals())
    
def selectedAssistants(request):
    
    if 'sectionId' in request.GET:
        tas = Section.objects.get(id = request.GET['sectionId']).tas.all()
    else:
        tas=[]
        for section in Class.objects.get(id=request.GET['classId']).sections.all():
            for user in section.tas.all():
                tas.append(user)
                
    return render_to_response('/gradebook/preSelectedAssistants.html', locals())
    
def setSectionAssistants(request):
    id = request.GET['id']
    ids = request.GET['ids']
    
    listOfIds = ids.split(',')
    section = Section.objects.get(id = int(id))
    section.tas.clear()
    
    for varId in listOfIds:
        if varId != '':
            student = User.objects.get(id = int(varId))
            section.tas.add(student)
            
    
    return HttpResponse('success!')
