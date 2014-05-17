from syllabus import *

from ...core.models import SyllUser
from ..models import MajorExemption as Exemption

def home(request):
    
    users = SyllUser.objects.all()
    
    return render_to_response('registrar/users/home.html', locals())

def delete(request):
    
    user = SyllUser.objects.get(id = request.GET['id'])
    
    if user:
        user.delete()
    
    return HttpResponse('success!')

def getInterestCourseNumber(request):
    
    courses = []

    interest = Interst.objects.get(id = request.GET['id'])
    
    for course in interest.courses.all():
        if course not in interest:
            courses.append(coures)

    return render_to_response('registrar/users/interestCourseNumbers.html', locals())


def userProfile(request):

    user = SyllUser.objects.get(id=request.GET['id'])
    exemptions = Exemption.objects.filter(user=request.user)

    # all of the required courses for the user
    courses = []
    for major in user.major.all():
        requirements = []
        for requirement in  major.preMajor.all():
            if requirement not in requirements:
                requirements.append(requirement)

        for requirement in major.major.all():
            if requirement not in requirements:
                requirements.append(requirement)
        
        for requirement in major.college.all()[0].requirements.all():
            if requirements not in requirements:
                requirements.append(requirement)
                
        for requirement in requirements:
            for course in requirement.courses.all():
                if (course, requirement.id) not in courses:
                    courses.append((course, requirement.id))

    interests = []
    interests = Interest.objects.all()

    return render_to_response('registrar/users/userProfile.html', locals())


def addExemption(request):

    student = SyllUser.objects.get(id=request.GET['id'])
    
    

    return render_to_response('/registrar/users/exemptionForm.html', locals())


def new(request):
    
    return render_to_response('/registrar/users/form.html',locals())

def create(request):
    
    user = SyllUser()
    user.username = request.POST['username']
    user.email = request.POST['email']
    user.first_name = request.POST['firstName']
    user.last_name = request.POST['lastName']
    user.major = Major.objects.get(name="Undeclared")
    user.set_password(request.POST['password'])
    user.save()
    
    role = request.POST['role']
    user.groups.add(AuthGroup.objects.get(name = role))
    
    return HttpResponse('success!')

def listRequirements(request):
    
    users = SyllUser.objects.all()
    
    return render_to_response('/registrar/users/userList.html',locals())

def editRequirement(request):
    user = SyllUser.objects.get(id=request.GET['id'])
    return render_to_response('/registrar/users/form.html', locals())

def modify(request):
    
    user = SyllUser.objects.get(id=request.POST['id'])
    user.username = request.POST['username']
    user.email = request.POST['email']
    user.first_name = request.POST['firstName']
    user.last_name = request.POST['lastName']
    user.major = Major.objects.get(name="Undeclared")
    user.set_password(request.POST['password'])
    user.save()
    
    return HttpResponse('success!')
