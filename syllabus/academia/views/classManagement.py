from syllabus import *

dayDict={
    '1':'M',
    '2':'T',
    '3':'W',
    '4':'Th',
    '5':'F',
    '6':'Sat',
    '7':'Sun'
}

def home(request):
    colleges = College.objects.all().order_by('name')
    college = colleges[0]
    
    profiles = ''
    
    departments = college.departments.all().order_by('name')
    
    if departments:
        department = departments[0]
    
        interests = department.interests.all();

    if interests:
        interest = interests[0]
        profiles = interest.courses.all()

    if profiles:
        profile = profiles[0]
    
        classes = profile.classes
        
        times = collections.OrderedDict()
        
        for qlass in classes.all():
                times[qlass]=collections.OrderedDict()
                for time in qlass.times.all():
                    if (time.start, time.end) not in times[qlass]:
                        times[qlass][(time.start,time.end)]=[dayDict[time.day]]
    
    return render_to_response('registrar/classes/home.html', locals())

def newClassProfile(request):
    
    department = Department.objects.get(id=request.GET['id'])
    
    return render_to_response('registrar/classes/classProfileForm.html', locals())


def newClass(request):
    
    teachers = SyllUser.objects.filter(groups__name='teacher')
    supers = SyllUser.objects.filter(groups__name='super')
    
    return render_to_response('registrar/classes/classForm.html',locals())

def newCollege(request):
    return render_to_response('registrar/classes/collegeForm.html')    
    
def newDepartment(request):
    college = College.objects.get(id=request.GET['id'])
    
    return render_to_response('registrar/classes/departmentForm.html', locals())   
   
def createCollege(request):
    
    college = College()
    college.name = request.POST['name']
    college.university = University.objects.get(id=1)
    college.save()
    
    return HttpResponse('success!')

def departmentList(request):
    
    colleges = College.objects.all()
    college = College.objects.get(id=request.GET['id'])    
    departments = Department.objects.filter(college__id = college.id).order_by('name')
    
    return render_to_response('registrar/classes/departmentList.html', locals())

def createDepartment(request):
    
    college = College.objects.filter(id=request.POST['id'])
    if college:
            college = college.all()[0]
            
            department = Department()
            department.name = request.POST['name']
            department.save()
            
            college.departments.add(department)
    
    
    
    return HttpResponse('success!')
  
def collegeList(request):
    
    colleges = College.objects.all().order_by('name')
    
    return render_to_response('registrar/classes/collegeList.html', locals())

def profileList(request):
    department = Department.objects.get(id=request.GET['id'])
    
    interests = department.interests.all()
    if interests:
        interest = interests[0]
        profiles = interest.courses.all().order_by('number')


    return render_to_response('registrar/classes/profileList.html', locals())

def interestList(request):
    department = Department.objects.get(id=request.GET['id'])
    interests = department.interests.all().order_by('name')
    
    return render_to_response('registrar/classes/interestList.html', locals())
    
def profile(request):
    
    profile = ClassProfile.objects.get(id = request.GET['id'])
    department = profile.department.all()[0]
    classes = profile.classes
    times = collections.OrderedDict()
    
    for qlass in classes.all():
            times[qlass]=collections.OrderedDict()
            for time in qlass.times.all():
                if (time.start, time.end) not in times[qlass]:
                    times[qlass][(time.start,time.end)]=[dayDict[time.day]]
    
    
    return render_to_response('registrar/classes/classesList.html' ,locals())

def newProfile(request):
    
    department = Department.objects.get(id=request.GET['id'])
    
    return render_to_response('registrar/classes/profileForm.html', locals())
