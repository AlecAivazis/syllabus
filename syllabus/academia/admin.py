from django.contrib import admin

from .models import College, MajorRequirement, Major, Term

# Register your models here.

admin.site.register(College)
admin.site.register(Major)
admin.site.register(MajorRequirement)
admin.site.register(Term)
