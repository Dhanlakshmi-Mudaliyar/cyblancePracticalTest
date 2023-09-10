from django.db import models
from django.utils import timezone
import json

class Person(models.Model):
    GENDER = (('male','Male'),
              ('female','Female'),
              ('other','Other'),
              )
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    gender = models.CharField(max_length=10, choices=GENDER)
    hobbies = models.TextField(blank=True, null=True, default='{}')


class PractTestUsers(models.Model):
    email = models.EmailField('email address', unique=True)
    first_name = models.CharField('First Name', max_length=255, blank=True,null=False)
    last_name = models.CharField('Last Name', max_length=255, blank=True,
                                     null=False)
    access_token = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

# Create your models here.
