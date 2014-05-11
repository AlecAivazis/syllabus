from django.db import models

# syllabus core models
# most of these are misc models used throughout the application

# encapsulates generic metaDeta about an object as a key value pair
class MetaData(models.Model):
    key = models.CharField(max_length=1020)
    value = models.CharField(max_length=1020)    
    
# points to a file in the system
class File(models.Model):
    fileName = models.CharField(max_length=4096)    

# the generic syllabus user can be a teacher, reigstrar, or student
class SyllUser(AbstractUser): 
    avatar = models.ForeignKey(File, null=True)
    major = models.ManyToManyField(Major, blank=True, related_name="students")
    residential =  models.ForeignKey(Address, null=True, related_name="residential")
    permanent = models.ForeignKey(Address, null=True, related_name="permanent")
    emergency = models.ForeignKey(Contact, null=True)
    phone = models.CharField(max_length=20)
    unitsTransfered = models.IntegerField(null=True)
    wishList = models.ManyToManyField(ClassProfile, through="WishList")
 
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
    
# encapsulates an uploaded document
# this should eventually be implemented as a django file instead of a filepath
class Upload(models.Model):
    event = models.ForeignKey(Event)
    user = models.ForeignKey(SyllUser)
    file = models.CharField(max_length=4096)
    date = models.DateField(auto_now_add=True)    
