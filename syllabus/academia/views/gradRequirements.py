from syllabus import *

from syllabus.academia.models import Major, College, MajorRequirement, ClassProfile

def home(request):
    
    #majors = Major.objects.all().distinct('name')
    majors = Major.objects.all().order_by('name')
    colleges = College.objects.all()
    
    return render_to_response('/registrar/graduationRequirements/home.html', locals())

def viewCollegeDegree(request):
    
    college = College.objects.get(id = request.GET['id'])
    
    return render_to_response('/registrar/graduationRequirements/viewCollege.html', locals())

def viewDegree(request):
    
    major = Major.objects.get(id = request.GET['id'])
    
    if major.type != 'BS':
        bs = Major.objects.filter(name=major.name).filter(type='BS')
        if bs:
            major = bs[0]
    
    degrees = [major.type]
    
    for degree in Major.objects.filter(name=major.name).exclude(type=major.type):
        if major.type not in degrees:
            degrees.append(major.type)
            
    if type in request.GET:
        target = Major.objects.filter(name=major.name).filter(type=request.GET['type'])
        if target:
            major = target[0]
        
    
    preMajor = major.preMajor
    requirements = major.major
        
    return render_to_response('/registrar/graduationRequirements/viewDegree.html',locals())

def newCollegeRequirement(request):
    college = College.objects.get(id=request.GET['id'])
    interests = []
    for profile in ClassProfile.objects.all():
        if profile.interest not in interests:
            interests.append(profile.interest)
    
    
    return render_to_response('/registrar/graduationRequirements/requirementForm.html',locals())
    

def newRequirement(request):
    major = Major.objects.get(id=request.GET['major'])
    interests = []
    
    for profile in ClassProfile.objects.all():
        if profile.interest not in interests:
            interests.append(profile.interest)
    
    
    return render_to_response('/registrar/graduationRequirements/requirementForm.html',locals())


def editRequirement(request):
    requirement = MajorRequirement.objects.get(id=request.GET['id'])
    
    interests = []
    profiles = {}
    
    
    for profile in requirement.courses.all():
        if profile.interest not in profiles:
            profiles[profile.interest]=[]
            
        profiles[profile.interest] = ClassProfile.objects.filter(interest=profile.interest)
    
    for profile in ClassProfile.objects.all():
        if profile.interest not in interests:
            interests.append(profile.interest)
    
    
    return render_to_response('/registrar/graduationRequirements/requirementForm.html',locals())

def submitCollegeRequirement(request):
    
    requirement = MajorRequirement()
    requirement.name = request.POST['name']
    requirement.minGrade = request.POST['minGrade']
    requirement.number = request.POST['number']
    requirement.save()
    
    for id in request.POST['classes'].split(','):
        if id: 
            profile = ClassProfile.objects.get(id=id)
            if profile:
                requirement.courses.add(profile)
    
    College.objects.get(id=request.POST['id']).requirements.add(requirement)
    
    return HttpResponse('success!')

def majorList(request):
    
    majors = Major.objects.all().order_by('name')
    
    return render_to_response('/registrar/graduationRequirements/majorList.html', locals())

def newMajor(request):
    
    colleges = College.objects.all()
    
    return render_to_response('/registrar/graduationRequirements/majorForm.html', locals())

def createMajor(request):
    
    if College.objects.filter(id=request.POST['college']):
        major = Major()
        major.name = request.POST['name']
        major.type = request.POST['type']
        major.save()
        
        College.objects.get(id=request.POST['college']).majors.add(major)
        
        return HttpResponse('success!')

def submitRequirement(request):
    
    requirement = MajorRequirement()
    requirement.minGrade = request.POST['minGrade']
    requirement.number = request.POST['number']
    requirement.save()
    
    for id in request.POST['classes'].split(','):
        if id: 
            profile = ClassProfile.objects.get(id=id)
            if profile:
                requirement.courses.add(profile)
    
    major = Major.objects.get(id=request.POST['id'])
                
    if request.POST['level'] == 'preMajor':
        major.preMajor.add(requirement)
    else:
        major.major.add(requirement)
    
    return HttpResponse('success!')


def modifyRequirement(request):
    
    requirement = MajorRequirement.objects.get(id=request.POST['id'])
    requirement.minGrade = request.POST['minGrade']
    requirement.number = request.POST['number']
    requirement.save()
    
    requirement.courses.clear()
    
    for id in request.POST['classes'].split(','):
        if id: 
            profile = ClassProfile.objects.get(id=id)
            if profile:
                requirement.courses.add(profile)
                
    return HttpResponse('success!')

def profilesByInterest(request):
    
    interest = request.GET['interest']
    profiles = ClassProfile.objects.filter(interest__abbrv = interest)
    
    return render_to_response('/registrar/graduationRequirements/profileList.html',locals())
    
def deleteRequirement(request):
    
    requirement = MajorRequirement.objects.filter(id=request.GET['id'])
    
    requirement.delete()
    
    return HttpResponse('success!')
        
    
    
    
