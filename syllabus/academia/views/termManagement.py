from syllabus import *

def home(request):
    
    return render_to_response('registrar/terms/home.jade', locals())
