# These forms are based on the django forms model
from django import forms
from django.forms import ModelForm

# syllabus imports
from syllabus.classroom.models import Event, Class
from syllabus.academia.models import Section

    
# an upload file form
class UploadFile(forms.Form):
    file  = forms.FileField()

# a login form
class LoginForm(forms.Form):
    username = forms.CharField(max_length=1020)
    password = forms.CharField(max_length=1020, widget = forms.PasswordInput)

# new user form
class NewUserForm(forms.Form):
    
    username = forms.CharField(max_length=1020)
    password = forms.CharField(max_length=1020, widget = forms.PasswordInput)
    firstName = forms.CharField(max_length=1020)
    lastName = forms.CharField(max_length=1020)
