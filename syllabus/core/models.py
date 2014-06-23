from django.db import models
from django.contrib.auth.models import AbstractUser

Event = 'classroom.Event'
Major = 'academia.Major'
from ..academia.models import University, Enrollment
Address = 'core.address'
Contact = 'core.contact'
ClassProfile = 'academia.ClassProfile'
File = 'core.File'
WishList = 'wishlist.WishList'

# most of these are random models used throughout the application

# Core
# --------------------

# encapsulates generic metaDeta about an object as a key value pair
class MetaData(models.Model):
    key = models.CharField(max_length=1020)
    value = models.CharField(max_length=1020)    
    
# points to a file in the system
class File(models.Model):
    fileName = models.CharField(max_length=4096)    

# encapsulates an uploaded document
# this should eventually be implemented as a django file instead of a filepath
class Upload(models.Model):
    event = models.ForeignKey(Event)
    user = models.ForeignKey('SyllUser')
    file = models.CharField(max_length=4096)
    date = models.DateField(auto_now_add=True)    


# a {timeslot} is a {start} and {end} time on a particular {day}
class Timeslot (models.Model):
    day = models.CharField(max_length=10)
    start = models.TimeField()
    end = models.TimeField()
    
    def __unicode__(self):
        return str(self.day + ": " + self.start.strftime('%I:%M')) + ' - ' + str(self.end.strftime('%I:%M %p'))
    
    # return the abbreviation for the requested part of the timeslot
    def abrreviation(self, char):
        if char == 1 :
            if self.day.lower() == 'monday':
                return 'M'
            if self.day.lower() == 'tuesday':
                return 'T'
            if self.day.lower() == 'wednesday':
                return 'W'
            if self.day.lower() == 'thursday':
                return 'R'
            if self.day.lower() == 'friday':
                return 'F'
            if self.day.lower() == 'saturday':
                return 'Sat'
            if self.day.lower() == 'sunday':
                return 'Sun'


# User
# --------------------

# the generic syllabus user can be a teacher, reigstrar, or student
class SyllUser(AbstractUser): 
    avatar = models.ForeignKey(File, null=True)
    major = models.ManyToManyField(Major, blank=True, related_name="students")
    residential =  models.ForeignKey('Address', null=True, related_name="residential")
    permanent = models.ForeignKey('Address', null=True, related_name="permanent")
    emergency = models.ForeignKey('Contact', null=True)
    phone = models.CharField(max_length=20)
    unitsTransfered = models.IntegerField(null=True)
    wishList = models.ManyToManyField(ClassProfile, through=WishList)

    # calculate how many units this user has completed
    def unitsCompleted(self):
        units = 0
        minGrade = University.objects.all()[0].minGradeToPass
        for enrollment in Enrollment.objects.filter(student=self):
            if enrollment.grade:
                if enrollment.grade > minGrade:
                    units = units + enrollment.section.qlass.profile.units
                
        return units

    # check if the user satisfies a given requirement
    def satisfiesRequirement(self, requirement):
        
        count = 0
        
        for profile in requirement.courses.all():
            enrollment = Enrollment.objects.filter(student=self).filter(section__qlass__profile = profile)
            if enrollment:
                enrollment = enrollment[0]
                if enrollment.grade:
                    if enrollment.grade >= requirement.minGrade:
                        count = count + 1

        
        if count >= requirement.number:
            return True
        else:
            return False
        
    # check if the user satisfies all of this graudation requirements
    def canGraduate(self):
        
        can = True
        
        colleges = []
        for major in self.major.all():
            if major.college not in colleges:
                colleges.append(major.college.all()[0])
            
            for requirement in major.preMajor.all():
                if not self.satisfiesRequirement(requirement):
                    can = False
            
            for requirement in major.major.all():
                if not self.satisfiesRequirement(requirement):
                    can = False
            
        for college in colleges:
            for requirement in college.requirements.all():
                if not self.satisfiesRequirement(requirement):
                    can = False
        
        return can

    # check if the user can register today
    def canRegister(self):
        today = datetime.date.today()
        registrationGroup = RegistrationGroup.objects.filter(start__lt = today).filter(end__gt =today)

        if registrationGroup:
            return registrationGroup

# a generic address schema
class Address(models.Model):
    line1 = models.CharField(max_length=1020)
    line2 = models.CharField(max_length=1020)
    city = models.CharField(max_length=1020)
    state = models.CharField(max_length=1020)
    zipCode = models.CharField(max_length=1020)
    country = models.CharField(max_length=1020)

# a contact for the user
class Contact(models.Model):
    name = models.CharField(max_length=1020, blank=True)
    phone = models.CharField(max_length=10, blank=True)
    address = models.ForeignKey(Address, null=True)
