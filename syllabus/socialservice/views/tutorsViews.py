from common import *

def render_to_response(filename, context={},mimetype=default_mimetype):
    template = env.get_template(filename)
    rendered = template.render(**context)
    return HttpResponse(rendered,mimetype=mimetype)


def home(request):
    userTutor = Tutor.objects.get(user=request.user)
    tutors = Tutor.objects.all()
    
    dd = dayDict

    interests = []
    
    for profile in ClassProfile.objects.filter(classes__sections__students = request.user):
        if profile.interest  not in interests:
            interests.append(profile.interest)
   
    print interests
 
    return render_to_response('/tutors/home.html', locals())

def new(request):
    
    interests = []

    for profile in ClassProfile.objects.filter(classes__sections__students = request.user):
        if profile.interest  not in interests:
            interests.append(profile.interest)
   
    return render_to_response('/tutors/tutorForm.html', locals())
