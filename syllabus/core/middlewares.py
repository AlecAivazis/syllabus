from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings

class UAC(object):
    def process_view(self, request, view_func, view_args, view_kwargs):
        
        perms = settings.PERMS
        
        if request.user.is_superuser:
            return None
        
        if request.user.is_authenticated():
            
            if request.user.groups.all()[0].name != 'super':
                if request.path.split('/')[1].lower() in perms[request.user.groups.all()[0].name]:
                    settings.perms = perms
                    return None

                    
class GetLinks(object):
    def process_view(self, request, view_func, view_args, view_kwargs):
        
        if request.user.is_authenticated():
            if request.user.groups.all():
                if request.user.groups.all()[0].name == 'admin' or request.user.is_superuser:
                    links = [
                        ['home','/'],
                        ['myhomework','/myhomework/?when=today'],
                        ['calendar','/calendar/'],
                        ['gradebook','/gradebook/'],
                        ['myclasses','/myClasses/schedule/'],
                        ['announcements','/announcements/'],
                        ['myprofile','/myProfile/'],
                        ['myclasses','/registrar/classes/'],
                        ['graduationrequirements','/registrar/graduationrequirements/'],
                        ['users','/registrar/users/']
                    ]
                elif request.user.groups.all()[0].name == 'faculty':
                   links = [
                        ['home','/'],
                        ['calendar','/calendar/'],
                        ['gradeBook','/gradebook/'],
                        ['messageboard','/messageboard/']
                    ]
                elif request.user.groups.all()[0].name == 'student':
                   links = [
                        ['home','/'],
                        ['myHomework','/myhomework/'],
                        ['calendar','/calendar/'],
                    ]
                   
                   if request.user.tas.all():
                        links.append(['gradeBook', '/gradebook/'])
                        
                elif request.user.groups.all()[0].name == 'registrar':
                   links = [
                        ['home','/'],
                        ['classes','/registrar/classes/'],
                        ['users', '/registrar/users/'],
                        ['graduationRequirements','/registrar/graduationrequirements/']
                    ]
            else:
                links = []
        else:
            links = []
        request.session['links'] = links
