from django.db import models

# these models handle the school wide operations
# most of these models are handled by "registrar"

# Requirements
# -----------------------------

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
    preMajor = models.ManyToManyField(MajorRequirement, related_name="pre", blank=True)             a
    major = models.ManyToManyField(MajorRequirement, related_name="major", blank=True)

# School Structure
# -----------------------------

# the University object to set school wide standards
class University(models.Model):
    name = models.CharField(max_length=1020)
    minGradeToPass = models.IntegerField(default=50)
    
    
# a term groups classes taken simulatenously for a given time period
class Term(models.Model):
    name = models.CharField(max_length=50)
    start = models.DateField()
    end = models.DateField(blank=True, null=True)
    
    # default string behavior is {name} - {start.year}
    def __unicode__(self):
        return  self.name + ' - ' + str(self.start.year)

# the {college} of a {university} has many {departments} and some {requirements}
# requirements at this level are most likely GEs
class College(models.Model):
    name = models.CharField(max_length=1020)
    requirements = models.ManyToManyField(MajorRequirement, related_name="colleges", blank=True)
    majors = models.ManyToManyField(Major, related_name="college", blank=True)
    departments = models.ManyToManyField(Department, related_name="college", blank=True)
    university = models.ForeignKey(University, related_name="colleges")

# an {interest} is a subsection of a {department} used to filter {classProfiles}
class Interest(models.Model):
    name  = models.CharField(max_length=1020)
    abbrv  = models.CharField(max_length=10)

    # default string behavior is to return its abbreviation
    def __unicode__(self):
        return self.abbrv
    
    # should add like a string
    def __add__(self, other):
        if isinstance(other, str):
            return self.abbrv + other
        raise NotImplemented
    def __radd__(self, other):
        if isinstance(other, str):
            return other + self.abbrv
        raise NotImplemented

# a {department} of a {college} with some {interests}
class Department(models.Model):
    name = models.CharField(max_length=1020)
    interests = models.ManyToManyField(Interest, related_name="department") 
    
    # string behavior is to return the name
    def __unicode__(self):
        return self.name   

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
    
# the membership of a student in a section is handled a manager to associate a grade
class Enrollment(models.Model):
    student = models.ForeignKey(SyllUser, null=True, related_name="enrollments")
    section = models.ForeignKey(Section) 
    grade = models.CharField(max_length=3, blank=True)

# Registration
# -----------------------------

# the preRequesite class for a certain class
class PreRequisite(models.Model):
    course = models.ForeignKey(ClassProfile)
    minGrade = models.IntegerField()

# in order to satisfy a {preReq} for a {classProfile} you must do so for one in the group
class PreRequisiteGroup(models.Model):
    courses = models.ManyToManyField(PreRequisite)

# defines when it is okay for groups of users to register for classes
class RegistrationGroup(models.Model):
    students = models.ManyToManyField(SyllUser, related_name="passGroups")
    start = models.DateField(null=True)
    end = models.DateField(null=True)
    name = models.CharField(max_length=1020)
    term = models.ForeignKey(Term, related_name="registrationGroups")
