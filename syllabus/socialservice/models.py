from django.db import models

User = 'core.SyllUser'
Timeslot = 'core.TimeSlot'
ClassProfile = 'academia.ClassProfile'

# this application handles interactions between users where one has a service and is rated
# using aggregate thumbs up and downs (normalized a la reddit) 

# represents the user as a service
class Tutor(models.Model):
    user = models.ForeignKey(User)
    available = models.ManyToManyField(Timeslot, related_name="tutors")
    up = models.IntegerField(default=0)
    down = models.IntegerField(default=0)
    appointments = models.ManyToManyField("TutorAppointment", blank=True)
    courses = models.ManyToManyField(ClassProfile, related_name="tutors")
    rate = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)

# appointment associated with this service
class TutorAppointment(models.Model):
    student = models.ForeignKey(User)
    time = models.ForeignKey(Timeslot)
