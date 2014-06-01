from django.contrib import admin

from .models import Weight, WeightCategory, Class

# Register your models here.
admin.site.register(Class)
admin.site.register(Weight)
admin.site.register(WeightCategory)

