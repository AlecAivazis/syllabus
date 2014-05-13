from syllabus import *

from syllabus.classroom.models import Class, Section
from syllabus.academia.models import Enrollment

from ..models import UserGroup, Announcement

def newAnnouncement(request):
    classes = Class.objects.filter(professor = request.user)
    sections = Section.objects.filter(tas= request.user)
    groups = UserGroup.objects.filter(managers = request.user)
    
    return render_to_response('/announcements/newAnnouncement.html', locals())
   
def create(request):
    
    if 'message' in request.POST and 'title' in request.POST and 'to' in request.POST:
        
        announcement = Announcement()
        announcement.title=request.POST['title']
        announcement.author = request.user
        announcement.datePosted = datetime.datetime.now()
        announcement.message = request.POST['message']
        announcement.save()
        
        for target in request.POST['to'].split(','):
            if target:
                announcement.sections.add(Section.objects.get(id=target))
        
    
    return HttpResponse('success!')
    
def home(request):
    announcements = []
    
    if Class.objects.filter(professor=request.user) or UserGroups.objects.filter(managers = request.user):
        canPost = True
    
    sections = []
    for enrollment in Enrollment.objects.filter(student=request.user).filter(grade=''):
        sections.append(enrollment.section)
        for announcement in enrollment.section.announcements.all():
            announcements.append(announcement)
    
    userGroups = UserGroup.objects.filter(users = request.user).order_by('name')
    for group in userGroups.all():    
        for announcement in group.announcements.all():
            announcements.append(announcement)
    
    
            
    return render_to_response('/announcements/home.html', locals())

def view(request):
    if 'type' in request.GET and 'id' in request.GET:
        if request.GET['type']=='section':
            section = Section.objects.get(id=request.GET['id'])
            announcements =  Announcement.objects.filter(sections = section).order_by('datePosted')
            
        elif request.GET['type'] == 'all':
            announcements = Announcement.objects.all()
            
        return render_to_response('announcements/announcements.html', locals())
            
