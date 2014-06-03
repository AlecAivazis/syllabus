from syllabus import *
import json

# syllabus model imports
from syllabus.core.models import Upload, SyllUser, MetaData
from syllabus.classroom.models import (Class, Section, Grade, Event, Weight, WeightCategory,
                                       GradingScale, GradingCategory )

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

    # load the json data
    post = json.loads(bytes.decode(request.body))
    # load the post data
    student = SyllUser.objects.get(id = int(post['student']))
    score = post['score']
    event = Event.objects.get(id = int(post['event']))
    
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
        else:
            return HttpResponse('fail')

def loadEvent(request):
    
    id = request.GET['id']
    event = Event.objects.get(id = int(id))
    
    return render_to_response('gradebook/loadEvent.html', locals())

def changePossiblePoints(request):
    
    post = json.loads(bytes.decode(request.body))

    id = post['id']
    
    event = Event.objects.get(id = int(id))
    
    if Class.objects.filter(events=event).filter(professor = request.user):
        
        if event.metaData.filter(key = 'possiblePoints'):
            data = event.metaData.get(key = 'possiblePoints')
            data.value = post['value']
            data.save()
        else:
            data = MetaData()
            data.key = 'possiblePoints'
            data.value = post['value']
            data.save()
            
            event.metaData.add(data)
            
        
        return HttpResponse('sucess');

def changeCategory(request):
    
    # load the post data
    post = json.loads(bytes.decode(request.body))
    # grab the corresponding event
    event = Event.objects.get(id = int(post['id']))
    # check if the user is the professor
    if Class.objects.filter(events=event).filter(professor = request.user):
        # check if there is a sub category assigned yet
        meta = event.metaData.filter(key='subCategory')
        # if it exists
        if meta:
            # set its value
            meta[0].value = post['value'].lower()
            meta[0].save()
        else:
            meta = MetaData()
            meta.key = 'subCategory'
            meta.value = post['value'].lower()
            meta.save()
            
            event.metaData.add(meta)
            
        return HttpResponse('success')

def assignWeights(request):
    
    # load the json data
    post = json.loads(bytes.decode(request.body))

    # create an empty weight group
    weight = Weight()
    # with the supplied name if there is one
    weight.name = "hello" #post['weights']['name'] if 'name' in post['weights'] else ''
    # save the group to the database
    weight.save()

    # add the given categories
    for category in post['weights']['categories']:
        # make an empty one
        weightCategory = WeightCategory()
        # set its parameter
        weightCategory.category = category['category']
        weightCategory.percentage = category['percentage']
        # add it to the database
        weightCategory.save()
        # add it to the group
        weight.categories.add(weightCategory)

    # update the classes weight
    klass = Class.objects.get(pk = post['classId'])
    klass.weights = weight
    klass.save()

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
    
    # load the json data
    post = json.loads(bytes.decode(request.body))

    # check if they named this scale
    if 'name' not in post:
        
        categories = []
        scale = ''
        
        #let's start with every scale that has the same number of categories as what 
        # was given to be filtered
        scales = (GradingScale.objects.all().annotate(count=Count('categories'))
                                            .filter(count=len(post['gradingScale']['categories'])))
        # for ever category you asked to create
        for category in post['gradingScale']['categories']:
            # check if this category already exists
            gradeList = (GradingCategory.objects.filter(lower = float(category['lower']))
                                                .filter(value = category['value']));
            # if it does
            if gradeList:
                # grab it
                cat = gradeList[0]
                # and add it to the list
                categories.append(cat)
            # otherwise
            else:
                # create a new category
                cat = GradingCategory()
                cat.lower = category['lower']
                cat.value = category['value']
                # save the new category
                cat.save()
                # and add it to the list
                categories.append(cat)
            # filter scales to have this category
            scales = scales.filter(categories = cat)
        # if there is still a scale    
        if scales:
            # grab the first one
            scale = scales[0]
        # otherwise make a new one
        else:
            scale = GradingScale()
            scale.save()
            # with the right categories
            for category in categories:
                scale.categories.add(category)
    else:
        scale = GradingScale.objects.get(name=post['name'])
                
    qlass =  Class.objects.get(id=post['classId'])
    
    qlass.gradingScale = scale
    qlass.save()
    
                
    return HttpResponse("success")
    
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
