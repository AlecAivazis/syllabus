import django, datetime, pytz

from django.db import models
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
MetaData = 'core.MetaData'
User = 'core.SyllUser'
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
    
    # string behavior is to return the title
    def __unicode__(self):
        return self.title
    
    # calculate the individual worth of this event based on the weight
    def calculateWorth(self):
        qlass = self.classes.all()[0]

        
        if self.metaData.filter(key = 'weight'):
            return self.metaData.filter(key = 'weight').value
        else:
            if self.metaData.filter(key = 'subCategory'):
                category = self.metaData.get(key = 'subCategory').value
                events = []
                
                for event in qlass.events.filter(category = category):
                    if event not in events:
                        events.append(event)
                
                for event in qlass.events.filter(metaData__key = 'subCategory').filter(metaData__value=category):
                    if event not in events:
                        events.append(event)
 
                count = len(events)
            else:
                category = self.category
                events = []
                
                for event in qlass.events.filter(category = category):
                    if event not in events:
                        events.append(event)
                
                for event in qlass.events.filter(metaData__key = 'subCategory').filter(metaData__value=category):
                    if event not in events:
                        events.append(event)
 
                count = len(events)
                
            # is there a weight for this category?
            if qlass.weights:
                if qlass.weights.categories.filter(category=category):
                    # if so, let's return the percentage divded by the number of events that fit the category
                    totalPercentage = qlass.weights.categories.get(category=category).percentage
                    
                    return totalPercentage/count
                    
                else:
                    return 0
            
            else:   
                return 0

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
               .exclude(category='meeting')
               .filter(date__lte = django.utils.timezone.now() + datetime.timedelta(days = 1)))


    # return the grade of the user with the given is
    def totalGrade(self, id):
        totalPossible = 0
        pointsEarned = 0
        
        for grade in Grade.objects.filter(student = get_user_model().objects.get(id = int(id))).filter(event__in = self.events.all()):
            if grade.event.metaData.filter(key = 'possiblePoints'):
                if grade.event.classes.all()[0].weights:
                    
                    if grade.event.calculateWorth():
                        weight = grade.event.calculateWorth()
                        totalPossible = totalPossible + (weight * int(grade.event.metaData.get(key = 'possiblePoints').value))
                        pointsEarned = pointsEarned + (weight * grade.score)
                else:
                    totalPossible = totalPossible + int(grade.event.metaData.get(key = 'possiblePoints').value)
                    pointsEarned = pointsEarned + grade.score
        
        if totalPossible == 0:        
            return 'n/a',
        else:
            score = pointsEarned/totalPossible * 100
            letter = self.gradingScale.categories.filter(lower__lte = score).order_by('-lower')[0].value
            
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

# a group of weights by category
class Weight(models.Model):
    name = models.CharField(max_length=1020, blank=True)
    categories = models.ManyToManyField(WeightCategory, related_name="weights")
 
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


