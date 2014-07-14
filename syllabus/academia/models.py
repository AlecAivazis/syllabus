from django.db import models

import datetime

Book = 'classroom.Book'
User = 'core.SyllUser'
Section = 'classroom.Section'

# these models handle the school wide operation and general organization
# much of this schema is handled by a "registrar"

# School structure
# -----------------------------

# the University object to set school wide standards
class University(models.Model):
    name = models.CharField(max_length=1020)
    minGradeToPass = models.IntegerField(default=50)

# the {college} of a {university} has many {departments} and some {requirements}
# requirements at this level are most likely GEs
class College(models.Model):
    name = models.CharField(max_length=1020)
    requirements = models.ManyToManyField('MajorRequirement', related_name="colleges", blank=True)
    majors = models.ManyToManyField('Major', related_name="college", blank=True)
    departments = models.ManyToManyField('Department', related_name="college", blank=True)
    university = models.ForeignKey(University, related_name="colleges")

# a {department} of a {college} with some {interests}
class Department(models.Model):
    name = models.CharField(max_length=1020)
    interests = models.ManyToManyField('Interest', related_name="department") 
    
    # string behavior is to return the name
    def __unicode__(self):
        return self.name   

# an {interest} is a subsection of a {department} used to filter {classProfiles}
class Interest(models.Model):
    name  = models.CharField(max_length=1020)
    abbrv  = models.CharField(max_length=10)

    # default string behavior is to return its abbreviation
    def __str__(self):
        return self.abbrv
    def __unicode__(self):
        return self.__str__() 
    
    # should add to a string
    def __add__(self, other):
        if isinstance(other, str):
            return self.abbrv + other
        raise NotImplemented
    def __radd__(self, other):
        if isinstance(other, str):
            return other + self.abbrv
        raise NotImplemented


# the profile of a given class - separated from a particular class because it changes every 5 yrs
class ClassProfile(models.Model):
    name = models.CharField(max_length=1020)
    fullName = models.CharField(max_length=1020)
    units = models.IntegerField()
    description = models.CharField(max_length=1020)
    number = models.IntegerField()
    books = models.ManyToManyField(Book, related_name="books", blank=True)
    prerequisites = models.ManyToManyField('PreRequisiteGroup', related_name="prereqs", symmetrical=False, blank=True)
    interest = models.ForeignKey('Interest', related_name="courses")

    # default string behavior is to return its abbreviation
    def __str__(self):
        return str(self.pk) + ':' + self.name
    def __unicode__(self):
        return self.__str__() 
    

       
# the membership of a student in a section is handled a manager to associate a grade
class Enrollment(models.Model):
    student = models.ForeignKey(User, null=True, related_name="enrollments")
    section = models.ForeignKey(Section) 
    grade = models.CharField(max_length=3, blank=True)


# an {registrationPass} allows for a user to go add a class regardless of rules in place
class RegistrationPass(models.Model):
    user = models.ForeignKey(User, related_name="addcodes")
    profile = models.ForeignKey(ClassProfile, related_name="addcodes")

# Requirements
# -----------------------------

# a group of {qlasses} that make up a {GraduationRequirement}
class Group(models.Model):
    qlass = models.ManyToManyField(ClassProfile, related_name='groups', blank=True)
    name = models.CharField(max_length=1020)

# degree requirements
class Requirement(models.Model):
    group = models.ForeignKey(Group)
    number = models.IntegerField()
    
#various degrees and achievments offer by the system
class Achievement(models.Model):
    name = models.CharField(max_length=1020)
    college = models.CharField(max_length=1020)
    requirements = models.ManyToManyField(Requirement, blank=True)

# major requirements
class MajorRequirement(models.Model):
    name = models.CharField(max_length=1020, blank=True)
    abbrv = models.CharField(max_length=10, blank=True)
    courses = models.ManyToManyField(ClassProfile, related_name="required", blank=True)
    number = models.IntegerField()
    minGrade = models.IntegerField()

    # return a list of the interests that compose this requirement group
    def getInterests(self):
        interests = []
        for course in courses:
            if course.Interest not in interests:
                interests.append(course.interest)
        
        return interests

# a major consists of major and premajor requirements
class Major(models.Model):
    name = models.CharField(max_length=1020)
    type = models.CharField(max_length=10)
    preMajor = models.ManyToManyField(MajorRequirement, related_name="pre", blank=True)
    major = models.ManyToManyField(MajorRequirement, related_name="major", blank=True)

# an replacement requirement for a major
class MajorExemption(models.Model):
    user = models.ForeignKey(User, related_name="exemptions")
    profile = models.ForeignKey(ClassProfile, related_name="replaced_set")
    replace = models.ManyToManyField(ClassProfile, related_name="replacing_set")

# Registration
# -----------------------------
    
  
class TermQuerySet(models.QuerySet):
    """ manage the django Term api """

    def getCurrentTerm(self):
        """ return the current term based on todays date """
        # grab the current date
        today = datetime.date.today()
        return self.filter(start__lte = today).order_by('-start')[0]

# a term groups classes taken simulatenously for a given time period
class Term(models.Model):
    name = models.CharField(max_length=50)
    start = models.DateField()
    end = models.DateField(blank=True, null=True)
    
    # default string behavior is {name} - {start.year}
    def __unicode__(self):
        return getTitle()
    
    def getTitle(self):
        """ return the title of the term """
        return  self.name + ' - ' + str(self.start.year)

    # set the object manager
    objects = TermQuerySet.as_manager()

# the preRequesite class for a certain class
class PreRequisite(models.Model):
    course = models.ForeignKey(ClassProfile)
    minGrade = models.IntegerField()

# in order to satisfy a {preReq} for a {classProfile} you must do so for one in the group
class PreRequisiteGroup(models.Model):
    courses = models.ManyToManyField(PreRequisite)

# defines when it is okay for groups of users to register for classes
class RegistrationGroup(models.Model):
    students = models.ManyToManyField(User, related_name="passGroups")
    start = models.DateField(null=True)
    end = models.DateField(null=True)
    name = models.CharField(max_length=1020)
    term = models.ForeignKey(Term, related_name="registrationGroups")
