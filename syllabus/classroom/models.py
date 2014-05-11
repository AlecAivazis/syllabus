from django.db import models

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

# the main connection between the teacher and the student
class Class(models.Model):
    professor = models.ManyToManyField(SyllUser, related_name="classesTeaching")
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
            letter = self.gradingScale.gradingCategories.filter(lower__lte = score).order_by('-lower')[0].value
            
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
    students = models.ManyToManyField(SyllUser, related_name='students', through='Enrollment')
    tas = models.ManyToManyField(SyllUser, related_name='tas', blank=True)
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
    gradingCategories = models.ManyToManyField(GradingCategory, related_name='gradingCategories')
    
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


# Class profile
# -----------------------------

# the required reading for a given class
class Book(models.Model):
    title = models.CharField(max_length=1020)
    author = models.CharField(max_length = 1020)
    isbn = models.CharField(max_length = 1020)

