from common import *

def home(request):
    
    interests = []
    
    for course in ClassProfile.objects.all():
        if course.interest not in interests:
            interests.append(course.interest)
    
    return render_to_response('/myProfile/home.html',locals())

def updateAddress(request):
       
    which = request.POST['which']
    new = False
    user = request.user
    
    if which == 'residential':
        address = user.residential
    if which == 'permanent':
        address = user.permanent
    if which == 'emergency':
        emergency = user.emergency
        if emergency:
            address = emergency.address
        else:
            address = Address()
            new = True
        
    if not address:
        address = Address()
        new = True
        
    address.line1 = request.POST['line1']
    address.line2 = request.POST['line2']
    address.city = request.POST['city']
    address.state = request.POST['state']
    address.zipCode = request.POST['zip']
    address.country = request.POST['country']
    
    address.save()
    
    if which == 'emergency':
        if user.emergency:
            emergency = user.emergency
        else:
            emergency = Contact()
            
        emergency.name = request.POST['name']
        emergency.phone = request.POST['phone']
        emergency.address = address
        emergency.save()
        
        user.emergency = emergency
        user.save()
        
    elif new:
        
        
        if which == 'residential':
            user.residential = address
            user.save()
            
        if which == 'permanent':
            user.permanent = address
            user.save()
        
    
    return HttpResponse('success')
    
def updatePhone(request):
    
    user = request.user
    
    user.phone = request.POST['phone']
    user.save()
    
    return HttpResponse('success')

def updateEmail(request):
    
    user = request.user
    
    user.email = request.POST['email']
    user.save()
    
    return HttpResponse('success')
