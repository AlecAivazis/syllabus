from django.db import models

import datetime

Book = 'classroom.Book'
User = 'core.SyllUser'
Section = 'classroom.Section'

# these models handle the school wide operation and general organization
# much of this schema is handled by a "registrar"

# School structure
# -----------------------------

class University(models.Model):
    """ 
    the University object sets school wide standards 
    """
    name = models.CharField(max_length=1020)
    minGradeToPass = models.IntegerField(default=50)


class College(models.Model):
    """
    the {college} of a {university} has many {departments} and some {requirements}
    requirements at this level are most likely GEs
    """
    name = models.CharField(max_length=1020)
    requirements = models.ManyToManyField('MajorRequirement', related_name="colleges", blank=True)
    majors = models.ManyToManyField('Major', related_name="college", blank=True)
    departments = models.ManyToManyField('Department', related_name="college", blank=True)
    university = models.ForeignKey(University, related_name="colleges")


class Department(models.Model):
    """
    a {department} of a {college} with some {interests}
    """
    name = models.CharField(max_length=1020)
    interests = models.ManyToManyField('Interest', related_name="department") 
    
    def __unicode__(self):
        """ string behavior is to return the name """
        return self.name   


class Interest(models.Model):
    """
    an {interest} is a subsection of a {department} used to filter {classProfiles}
    """
    name  = models.CharField(max_length=1020)
    abbrv  = models.CharField(max_length=10)

    def __str__(self):
        """  default string behavior is to return its abbreviation """
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


class ClassProfile(models.Model):
    """
    the profile of a given class - separated from a particular class because it changes every 5 yrs
    """
    name = models.CharField(max_length=1020)
    fullName = models.CharField(max_length=1020)
    units = models.IntegerField()
    description = models.CharField(max_length=1020)
    number = models.IntegerField()
    books = models.ManyToManyField(Book, related_name="books", blank=True)
    prerequisites = models.ManyToManyField('PreRequisiteGroup', related_name="prereqs", 
                                                                symmetrical=False, blank=True)
    interest = models.ForeignKey('Interest', related_name="courses")

    # default string behavior is to return its abbreviation
    def __str__(self):
        return str(self.pk) + ':' + self.name
    def __unicode__(self):
        return self.__str__() 

       
class Enrollment(models.Model):
    """
    the membership of a student in a section is handled a manager to associate a grade
    """
    student = models.ForeignKey(User, null=True, related_name="enrollments")
    section = models.ForeignKey(Section) 
    grade = models.CharField(max_length=3, blank=True)


class RegistrationPass(models.Model):
    """
    a {registrationPass} allows for a user to go add a class regardless of rules in place
    """
    user = models.ForeignKey(User, related_name="addcodes")
    profile = models.ForeignKey(ClassProfile, related_name="addcodes")


# Requirements
# -----------------------------

class Group(models.Model):
    """
    a group of {qlasses} that make up a {GraduationRequirement}
    """
    qlass = models.ManyToManyField(ClassProfile, related_name='groups', blank=True)
    name = models.CharField(max_length=1020)


class Requirement(models.Model):
    """
    the requirement for a specific degree/acheievement
    """
    group = models.ForeignKey(Group)
    number = models.IntegerField()

    
class Achievement(models.Model):
    """
    various degrees and achievments offer by the system
    """
    name = models.CharField(max_length=1020)
    college = models.CharField(max_length=1020)
    requirements = models.ManyToManyField(Requirement, blank=True)
 

class MajorRequirement(models.Model):
    """
    a major requirement specifies a minimum number of classes that must be taken out of a certain
    group of profiles as well as a minimum grade to satisfy that requirement
    """
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


class Major(models.Model):
    """
    a major consists of major and premajor requirements
    """
    name = models.CharField(max_length=1020)
    type = models.CharField(max_length=10)
    preMajor = models.ManyToManyField(MajorRequirement, related_name="pre", blank=True)
    major = models.ManyToManyField(MajorRequirement, related_name="major", blank=True)


class MajorExemption(models.Model):
    """
    an replacement requirement for a major
    """
    user = models.ForeignKey(User, related_name="exemptions")
    profile = models.ForeignKey(ClassProfile, related_name="replaced_set")
    replace = models.ManyToManyField(ClassProfile, related_name="replacing_set")

    def getReplacement(self):
        return self.profile


# Registration
# -----------------------------
    
class TermQuerySet(models.QuerySet):
    """ manage the django Term api """

    def getCurrentTerm(self):
        """ return the current term based on todays date """
        # grab the current date
        today = datetime.date.today()
        return self.filter(start__lte = today).order_by('-start')[0]


class Term(models.Model):
    """
    a group of classes taken simulatenously for a given time period
    """
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


class TermTemplateEntry(models.Model):
    """
    an individual template entry that describes the amount of time before/after an anchor
    as well as the action that needs to take place
    """

    days = models.IntegerField()

    anchor_choices = (
        ('start' , 'start'),
        ('end'   , 'end')
    )
    anchor = models.CharField(max_length=5, choices=anchor_choices)


class TermTemplate(models.Model):
    """
    handle the repititive nature of term management by describing a normal term and then fine
    tune with the calendar
    """
    name = models.CharField(max_length=1020)
    entries = models.ManyToManyField(TermTemplateEntry, related_name="templates")
    

class PreRequisite(models.Model):
    """
    the preRequesite class for a certain class
    """
    course = models.ForeignKey(ClassProfile)
    minGrade = models.IntegerField()


class PreRequisiteGroup(models.Model):
    """
    in order to satisfy a {preReq} for a {classProfile} you must do so for one in the group
    """
    courses = models.ManyToManyField(PreRequisite)


class RegistrationGroup(models.Model):
    """
    defines when it is okay for groups of users to register for classes
    """
    students = models.ManyToManyField(User, related_name="passGroups")
    start = models.DateField(null=True)
    end = models.DateField(null=True)
    name = models.CharField(max_length=1020)
    term = models.ForeignKey(Term, related_name="registrationGroups")
