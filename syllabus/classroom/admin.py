from django.contrib import admin

from .models import Weight, WeightCategory, Class, Event, State

# Register your models here.
admin.site.register(Class)
admin.site.register(Event)
admin.site.register(State)
admin.site.register(Weight)
admin.site.register(WeightCategory)

