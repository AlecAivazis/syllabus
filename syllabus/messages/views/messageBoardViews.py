from common import *
  
_paragraph_re = re.compile(r'(?:\r\n|\r|\n){2,}')

def nl2br(value):
    result = u'\n\n'.join(u'<p>%s</p>' % p.replace('\n', '<br>\n') for p in _paragraph_re.split(escape(value)))
    return result

env.filters['linebreaks'] = nl2br
    
def home (request):
    
    boards = MessageBoard.objects.filter(members = request.user)
    
    if 'board' in request.GET:
        selectedBoard = request.GET['board']
        
        if 'action' in request.GET:
            action = request.GET['action']

    
    return render_to_response('messageBoard/home.html', locals())
 
def replies(request):
    replies = Topic.objects.get(id = request.GET['topic']).replies
    
    oz = os
    fileRoot = settings.ROOT
    
    return render_to_response('messageBoard/replies.html', locals())
   
def viewBoard(request):
    board = MessageBoard.objects.get(id=request.GET['id'])
    
    return render_to_response('messageBoard/messageBoard.html', locals())
    
def viewThread (request):
    
    topic = Topic.objects.get(id = request.GET['topic'])
    if request.user not in topic.read.all():
        topic.read.add(request.user)
    oz = os
    fileRoot = settings.ROOT
    
    return render_to_response('messageBoard/thread.html', locals())
    
def newTopic(request):
    
    return render_to_response('messageBoard/newTopic.html', locals())

def topics(request):
    
    board = MessageBoard.objects.get(id=request.GET['board'])
    topics = board.topics.all()
    
    return render_to_response('messageBoard/topics.html', locals())
    
def createTopic(request):
    board = MessageBoard.objects.get(id=request.POST['board'])
    
    topic = Topic()
    
    topic.title = request.POST['title']
    topic.body = request.POST['body']
    topic.author = request.user
    
    topic.save()
    
    board.topics.add(topic)
    
    return render_to_response('messageBoard/createTopic.html', locals())
    
def createReply(request):
    
    topic = Topic.objects.get(id=request.POST['topic'])
    
    reply = Post()
    
    reply.author = request.user
    reply.body = request.POST['body']
    
    reply.save()
    
    for f in request.FILES.getlist('file'):
        dirname = os.path.join(os.path.join(settings.UPLOAD_DIR, "messageboard"), '%s' %(topic.board.all()[0].name))
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
   
    
    return HttpResponse(topic.id)
    
def allUsers(request):
    
    users = User.objects.all()
    
    return render_to_response('/messageBoard/allUsers.html', locals())
    
def subscribers(request):
    
    users = MessageBoard.objects.get(id=request.GET['board']).members.all()
    
    return render_to_response('/messageBoard/preselected.html', locals())
    
def admins(request):
    
    users = MessageBoard.objects.get(id=request.GET['board']).admins.all()
    
    return render_to_response('/messageBoard/preselected.html', locals())
    
def setSubscribers(request):
    id = request.GET['id']
    ids = request.GET['ids']
    
    listOfIds = ids.split(',')
    board = MessageBoard.objects.get(id = int(id))
    board.members.clear()
    
    for varId in listOfIds:
        if varId != '':
            student = User.objects.get(id = int(varId))
            
            membership = MessageBoardMembership()
            membership.board = board
            membership.member = student
            membership.save()
            
    
    return HttpResponse('success!')
    
def setAdmins(request):
    id = request.GET['id']
    ids = request.GET['ids']
    
    listOfIds = ids.split(',')
    board = MessageBoard.objects.get(id = int(id))
    board.admins.clear()
    
    for varId in listOfIds:
        if varId != '':
            user = User.objects.get(id = int(varId))
            board.admins.add(user)
            
    
    return HttpResponse('success!')
