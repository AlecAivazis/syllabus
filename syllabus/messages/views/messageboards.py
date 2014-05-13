from syllabus import *

from syllabus.classroom.models import Class

def home(request):
    qlass = Class.objects.get(id=request.GET['id'])
    messageBoard = qlass.messageBoard
    
    return render_to_response('/spaces/messageBoards/messageBoard.html', locals())

def newTopic(request):
    
    return render_to_response('/spaces/messageBoards/newTopic.html', locals())

def createTopic(request):
    
    qlass = Class.objects.get(id=request.POST['id'])
    
    if qlass.sections.filter(students = request.user) or request.user in qlass.professors.all() or qlass.sections.filter(tas = request.user):
        topic = Topic()
        topic.author = request.user
        topic.body = request.POST['body']
        topic.title = request.POST['title']
        topic.save()
        
        qlass.messageBoard.add(topic)
        
        return HttpResponse('success!')
    
def viewTopic(request):
    
    topic = Topic.objects.get(id=request.GET['id'])
    
    if request.user not in topic.read.all():
        topic.read.add(request.user)
    
    oz = os
    fileRoot = settings.ROOT
    now = datetime.datetime.now()
    nt = int
    
    return render_to_response('/spaces/messageBoards/topic.html', locals())

    
def createReply(request):
    qlass = Topic.objects.get(id=request.POST['topic']).qlass.all()[0]
    if qlass.sections.filter(students = request.user) or request.user in qlass.professors.all() or qlass.sections.filter(tas = request.user):

        topic = Topic.objects.get(id=request.POST['topic'])
        
        reply = Post()
        
        reply.author = request.user
        reply.body = request.POST['body']
        reply.kind = request.POST['kind']
        
        reply.save()
        
        for f in request.FILES.getlist('file'):
            dirname = os.path.join(settings.UPLOAD_DIR, os.path.join(topic.qlass.all()[0].profile.interest+'-'+str(topic.qlass.all()[0].profile.number), 'messageboard'))
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
            
            reply.files.add(file)
        
        topic.replies.add(reply)
        
        topic.read.clear()
       
        
        return HttpResponse('<script type="text/javascript"> top.viewTopic('+ str(topic.id) + ') </script>')    
