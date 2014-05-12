from common import *

def sentry(request):
    if request.user.is_authenticated():
        return render_to_response('base.html', locals())
    else:
        form = LoginForm()
        return render_to_response('sentry.html', locals())



def myHomework(request):
    oz = os
    fileRoot = settings.ROOT
    user = request.user
    when = request.GET['when']
    sections = Section.objects.filter(students = user).order_by('qlass')
    date = 0
    

    if when == 'today':
        dates = [datetime.date.today()]
    elif when == 'tomorrow':
        dates = [datetime.date.today() + datetime.timedelta(days = 1)]

    
    length = len
    
    uploads = {}
    status={}
    completed = []
    

    events = {}
    for date in dates:
        print date
        for section in sections:
            targetEvents = section.qlass.events.filter(date=date).exclude(category='lecture').exclude(category='test')
            
            if targetEvents:
                events[section] = targetEvents  
              
            for event in section.qlass.events.all():
                if State.objects.filter(event = event).filter(owner = request.user):
                    status[event.id] = State.objects.filter(event = event).filter(owner = request.user).order_by('-date')[0].status
                    if status[event.id] != 'revoked':
                        completed.append(event.id)
                        
                if Upload.objects.filter(event = event):
                    uploads[event.id] = Upload.objects.filter(event=event).filter(user = request.user)
    
    return render_to_response('myhomework.html', locals())

def turnIn(request):
    
    event = Event.objects.get(id = request.GET['event'])
    overwrite = False
    for f in request.FILES.getlist('files'):
        dirname = os.path.join(settings.UPLOAD_DIR, os.path.join(event.classes.all()[0].profile.interest+'-'+str(event.classes.all()[0].profile.number), 'turn-ins'))
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        filename = os.path.join(dirname, f.name)
        
        d = open(filename, 'wb') 
        for chunk in f.chunks():
            d.write(chunk)
        d.close()
        
        if Upload.objects.filter(event = event).filter(user = request.user).filter(file=filename):
            Upload.objects.filter(event=event).filter(user = request.user).get(file=filename).delete()
            overwrite = True
        
        upload = Upload()
        upload.event = event
        upload.user = request.user
        upload.file = filename
        upload.save()

    script = "top.turnedIn('"+ str(event.id)+ "','" + os.path.basename(upload.file) + "');"
    
    if overwrite:
        script = "top.turnedIn('"+ str(event.id)+ "','" + os.path.basename(upload.file) + "', 1);"
    return HttpResponse('<script type="text/javascript">' + script + '</script>')

def protectedDownload(request, path):
    
    with open(settings.UPLOAD_DIR + '/' + path) as file:
        name = os.path.basename(file.name)
        mime =  mimetypes.guess_type(file.name)
        
        head = os.path.split(path)[0].split('/')
        
        interest = head[0].split('-')[0]
        number = head[0].split('-')[1]
        if Class.objects.filter(profile__interest = interest).filter(profile__number = number):
            qlass = Class.objects.filter(profile__interest = interest).filter(profile__number = number)[0]
            if qlass.sections.filter(students = request.user) or request.user in qlass.professor or qlass.sections.filter(tas = request.user):
                if head[1] == 'turn-ins':
                    if request.user in qlass.professor.all():
                        allowed = True
                    else:
                        allowed = False
                else:
                    allowed = True
        else:
            allowed = True
            
            
        if allowed:
            response = HttpResponse(file.read(), mimetype=mime[0])
            response['Content-Disposition'] = 'attachment; filename=' + name.replace(' ', '')
            response['Content-Length'] = os.path.getsize(settings.UPLOAD_DIR + '/' + path)
     
            return response

def updateState(request):
    state = State()
    state.user = User.objects.get(username = request.POST['user'])
    state.owner = User.objects.get(username = request.POST['owner'])
    state.event = Event.objects.get(id=request.POST['event'])
    state.status = request.POST['status']
    state.save()
    
    return HttpResponse('success')
    
def syllogout(request):
    logout(request)
    request.session.clear()
    return HttpResponseRedirect('/')

def upload(request):
    
    return render_to_response('upload.html',locals())

def syllogin(request):
    logout(request)
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse('success')
                
def viewClass(request):
    
    profile = ClassProfile.objects.get(id = request.GET['class'])
    
    return render_to_response('viewClass.html', locals())

def downloadSubmission(request):
    student = SyllUser.objects.get(id = request.GET['student'])
    event = Event.objects.get(id = request.GET['event'])
    uploads = Upload.objects.filter(user = student).filter(event = event)
    
    if uploads.all():
        if len(uploads.all()) == 1:
            with open(uploads.all()[0].file) as file:
                name = os.path.basename(file.name)
                mime =  mimetypes.guess_type(file.name)
                    
                response = HttpResponse(file.read(), mimetype=mime[0])
                response['Content-Disposition'] = 'attachment; filename=' + name.replace(' ', '')
                response['Content-Length'] = os.path.getsize(uploads.all()[0].file)
         
                return response
        else:
            
            temp = tempfile.TemporaryFile()
            archive = zipfile.ZipFile(temp, 'w')
            
            cwd = os.path.abspath(os.getcwd())
            
            os.chdir(os.path.join(settings.UPLOAD_DIR, event.classes.all()[0].profile.interest + '-' + str(event.classes.all()[0].profile.number)))
            
            for upload in uploads.all():
                archive.write(os.path.join(student.username, os.path.basename(upload.file)))
            archive.close()
            
            
            wrapper = FileWrapper(temp)
            response = HttpResponse(wrapper, content_type='application/zip')

            
            response['Content-Disposition'] = 'attachment; filename=' + student.first_name + student.last_name + '-' + event.title.replace(' ', '') + '.zip'
            response['Content-Length'] = temp.tell()
            temp.seek(0)
            
            
            os.chdir(cwd)
            return response
            
    
def viewEvent(request):
    event = Event.objects.get(id=request.GET['id'])

    return render_to_response('viewEvent.html', locals())
    
def test(request):
    
    return HttpResponse('hello world')
