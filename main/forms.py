from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from .models import Student
from main.models import Student

# forms.py
from django import forms
from .models import Student

from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['surname', 'name', 'city', 'email', 'profession', 'experience', 'telegram', 'vk', 'instagram', 'whatsapp', 'about', 'dateOfBirth']

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'surname', 'dateOfBirth', 'email', 'profession', 'experience',
                  'telegram', 'whatsapp', 'vk', 'instagram', 'about']