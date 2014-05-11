from django.db import models

# these models encapsulate the day to day interactions between the student and teacher


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
    
    def __unicode__(self):
        return self.title
    
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


# Class Profile


# the required reading for a given class
class Book(models.Model):
    title = models.CharField(max_length=1020)
    author = models.CharField(max_length = 1020)
    isbn = models.CharField(max_length = 1020)
