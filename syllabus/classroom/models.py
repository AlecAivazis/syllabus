import django, datetime, pytz

from django.db import models
from django.db.models import Sum
from django.contrib.auth import get_user_model


# implements a switch statement with generators
class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration
    
    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args: # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False


# local imports defined as string references
File = 'core.File'
from ..core.models import MetaData
from ..core.models import SyllUser as User
Timeslot = 'core.Timeslot'
GradingScale = 'GradingScale'
Weight = 'Weight'
Topic = 'messages.Topic'
Term = 'academia.Term'
User = 'core.SyllUser'
Enrollment = 'academia.Enrollment'
ClassProfile = 'academia.ClassProfile'

# these models encapsulate the day to day interactions between the student and teacher

# Classroom
# -----------------------------

class EventQuerySet(models.QuerySet):
    """ manage the event django api """

    def assignments(self):
        """ return the assignments """
        return self.filter(category = 'assignment')

    def tests(self):
        """ return the tests """
        return self.filter(category = 'test')

    def lectures(self):
        """ return the lectures """
        return self.filter(category = 'lecture')

    def meetings(self):
        """ return the meetings """
        return self.filter(category = 'meeting')

# the fundamental element of a teachers syllabus
# can be one of assignment, lecture, test, meeting
class Event(models.Model):
    title = models.CharField(max_length=1020)
    description = models.TextField(max_length=5000)
    date = models.DateField()
    time = models.TimeField(blank=True)
    files = models.ManyToManyField(File, related_name='files', blank=True)
    metaData = models.ManyToManyField(MetaData, related_name='events', blank=True)
    category = models.CharField(max_length=1020, blank = True, choices=(
        ('assignment','assignment'),
        ('test','test'),
        ('lecture','lecture'),
        ('meeting','meeting'),
    ))

    # set the object manager
    objects = EventQuerySet.as_manager()
    
    # string behavior is to return the title
    def __str__(self):
        return self.title

    # get the weighted grade for the given student
    def getWeightedGrade(self, id):
        # see if there is a grade entry
        grades = Grade.objects.filter(student__pk = id).filter(event = self)
        if grades:
            grade = grades[0].score
            # check if there is a entry for possible points
            metaData = self.metaData.filter(key = 'possiblePoints')
            # if so
            if metaData:
                # grab the possible points
                possiblePoints = int(metaData[0].value)
                if not self.calculateWorth():
                    worth = 0
                else:
                    worth = self.calculateWorth()
                    
                return (grade/possiblePoints) * worth
            # since there is no metaData for possible points
            else:
                return 0
        else:
            return 0

    def getPossiblePoints(self):
        """ return the possible points in this event, otherwise return 0 """
        if not self.metaData:
            return 0
        # search for a meata data for possible points
        data = self.metaData.filter(key='possiblePoints')
        # if it exists
        if data:
            # return its value
            return float(data[0].value)
        else:
            return 0
        
    
    # calculate the individual worth of this event based on the weight
    def calculateWorth(self):
        # grab the events class
        qlass = self.classes.all()[0]
        # figure out the category of the event
        # if it has a subcategory
        if self.metaData.filter(key = 'subCategory'):
            # use it
            category = self.metaData.get(key = 'subCategory').value
        # otherwise
        else:
            # use the event category
            category = self.category

        # gather the events of this category including matching subCategory
        events = (qlass.events.filter(category = category) | 
                  qlass.events.filter(metaData__key = 'subCategory')
                              .filter(metaData__value = category)).distinct()
        
        # the total  number of possible points for this category
        possiblePoints = 0

        # for each such event
        for event in events.all():
            # add up the possible points
            possiblePoints += event.getPossiblePoints()
        
        # get a corresponding weight entry
        weightEntry = (WeightCategory.objects.filter(weights__sections = qlass)
                                             .filter(category = category))
        if weightEntry:
            percentage = weightEntry[0].percentage
            # grab the events possible points
            eventPossible = self.getPossiblePoints()
            # calculate the weight
            weight = (eventPossible/possiblePoints) * percentage
            # return the weight
            return round(weight)

    def isStudentOnTime(self, student):

        # get the due datetime of the event
        eventDateTime = datetime.datetime(year = self.date.year, 
                                          month = self.date.month, 
                                          day = self.date.day, 
                                          hour = self.time.hour, 
                                          minute = self.time.minute, tzinfo=pytz.UTC)
        # get now
        now = django.utils.timezone.now()

        # check if this event is past due
        if now < eventDateTime:
            return True
        # since its pastdue, check if there is any states
        states = self.state.filter(owner=student)
        # if there arent
        if not states:
            # then its not on time
            return False

        # get the most recent activity by the student
        recentState = self.state.filter(owner=student).order_by('-date')[0]
        
        for case in switch(recentStatus.status):
            # if it was turned in most recently
            if case('turned-in'):
                # and that was after the due date
                if state.date <= eventDateTime:
                    return True
                else:
                    return False
            # if it was most recently revoked, then its not turned in (aka not on time)
            if case('revoked'):
                return False
            # if it was ignored, its not ever going to be on time
            if case('ignored'):
                return False
            

# the main connection between the teacher and the student
class Class(models.Model):
    professor = models.ManyToManyField(User, related_name="classesTeaching")
    profile = models.ForeignKey(ClassProfile, related_name="classes")
    times = models.ManyToManyField(Timeslot)
    location = models.CharField(max_length=1020)
    syllabus = models.CharField(max_length=100000, blank=True)
    lectures = models.ManyToManyField(Event, blank=True, related_name="lecture_classes")
    events = models.ManyToManyField(Event, blank=True, related_name="classes")
    gradingScale = models.ForeignKey(GradingScale, related_name='gradingSchema')
    weights = models.ForeignKey(Weight, related_name='sections', null=True, blank=True)
    messageBoard = models.ManyToManyField(Topic, related_name="qlass", blank=True)
    maxOccupancy = models.IntegerField()
    term = models.ForeignKey(Term)
    
    # string behavior is to return {interest}-{number} ie PHYS-21
    def __unicode__(self):
        return self.profile.interest + '-' + str(self.profile.number)  

    def getGradableEvents(self):
        """ return the events that get a grade """
        return (self.events.all()
               .exclude(category='lecture')
               .exclude(category='meeting'))


    # return the grade of the user with the given id
    def totalGrade(self, id):
        totalPossible = 0
        
        for event in self.getGradableEvents():
            totalPossible += event.getWeightedGrade(id)

        if totalPossible == 0:        
            return -1
        else:
            score = round(totalPossible, 2)
            letter = (self.gradingScale.categories.filter(lower__lte = score)
                                                  .order_by('-lower')[0].value)
            
            return letter,"%.1f" % (score)

    # check if the user can register for the class
    def isEligible(self, user, includeCurrent):
        enrolled = 0
        for section in self.sections.all():
            enrolled =+ section.students.all().count()
        
        eligible = False

        for group in self.profile.prerequisites.all():
            
            # if any of these are eligible, we're good to go
            for preReq in group.courses.all():
                # preReq is an invdividual course and minimum grade
                sections = []
                for qlass in preReq.course.classes.all():
                    for section in qlass.sections.all():
                        sections.append(section)
                
                enrollment = Enrollment.objects.filter(student = user).filter(section__in = sections)
                
                if enrollment:
                    if (includeCurrent and not enrollment.grade):
                        eligible = True
                        break;
                    else:
                        if (enrollment.grade > preReq.minimumGrade):
                            eligible = True
                            break;

        else:
            eligible = True
                        
            
        return eligible

# the {sections} of a particular {class} to add more user based organization
class Section(models.Model):
    name = models.CharField(max_length=508)
    students = models.ManyToManyField(User, related_name='classes', through=Enrollment)
    tas = models.ManyToManyField(User, related_name='tas', blank=True)
    qlass = models.ForeignKey(Class, related_name='sections')
    times = models.ManyToManyField(Timeslot, related_name="sections", blank=True)
    location= models.CharField(max_length=1020, blank=True)
    maxOccupancy = models.IntegerField()
    
    def __unicode__(self):
        return self.name
     

# Gradebook 
# -----------------------------

# the range over which to call a certain {value}
class GradingCategory(models.Model):
    lower = models.FloatField()
    value = models.CharField(max_length=1020)
    
    # string behavior is to return {lower} = {value} ie 40 = B+
    def __unicode__(self):
        return str(self.lower) + ' = ' + self.value

# a group of {GradingCategories} to reuse across various {Classes}
class GradingScale(models.Model):
    name = models.CharField(max_length=1020, blank=True)
    categories = models.ManyToManyField(GradingCategory, related_name='categories')
    
    # string behavior is to return {name}
    def __unicode__(self):
        return self.name

# gives a weight to {events} with a {event.category} equal to {category}
class WeightCategory(models.Model):
    category = models.CharField(max_length=1020)
    percentage = models.IntegerField()

# a group of weights by category/
class Weight(models.Model):
    name = models.CharField(max_length=1020, blank=True)
    categories = models.ManyToManyField(WeightCategory, related_name="weights")
 
    # string behavior is to return {name}
    def __str__(self):
        if self.name:
            return self.name
        else:
            return 'no name'

# a {students} grade for a particular {event} - teacher can associate a {comment}
class Grade(models.Model):
    student = models.ForeignKey(User, related_name='student')
    event = models.ForeignKey(Event, related_name='event')
    score = models.FloatField()
    comment = models.CharField(max_length=1020, default='')
    
    def __unicode__(self):
        return self.score 
 
# {states} track a users progress of an {event}
class State(models.Model):
    user = models.ForeignKey(User)
    owner = models.ForeignKey(User, related_name="owner")
    event = models.ForeignKey(Event, related_name="state")
    status = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

# Class profile
# -----------------------------

# the required reading for a given class
class Book(models.Model):
    title = models.CharField(max_length=1020)
    author = models.CharField(max_length = 1020)
    asbn = models.CharField(max_length = 1020)


