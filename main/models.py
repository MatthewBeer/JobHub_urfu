from django.db import models

from django.contrib.auth.models import User
from django.urls import reverse
class Student(models.Model):
    surname = models.CharField(max_length=225)
    name = models.CharField(max_length=225)
    city = models.CharField(max_length=225, null=True, blank=True)
    email = models.EmailField()
    dateOfBirth = models.CharField(max_length=225)
    profession = models.CharField(max_length=225)
    experience = models.CharField(max_length=225)
    about = models.CharField(max_length=225)
    telegram = models.CharField(max_length=225)
    whatsapp = models.CharField(max_length=225)
    vk = models.CharField(max_length=225)
    instagram = models.CharField(max_length=225)
