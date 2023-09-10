from django.db import models
from django.utils import timezone
import json
from django.contrib.auth.models import AbstractUser

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

class CustomUser(AbstractUser):
    email = models.EmailField('email address', unique=True)
    first_name = models.CharField('First Name', max_length=255, blank=True,null=False)
    last_name = models.CharField('Last Name', max_length=255, blank=True,
                                 null=False)
    access_token = models.CharField(max_length=255)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email} - {self.first_name} {self.last_name}"

    # def save(self, *args, **kwargs):
    #     # print(self.data)
    #     # ## load the current string and
    #     # ## convert string to python dictionary
    #     # data_dict = json.loads(self.data)
    #     #
    #     # ## do something with the dictionary
    #     # for something in somethings:
    #     #     data_dict[something] = some_function(something)
    #     #
    #     # ## if it is empty, save it back to a '{}' string,
    #     # ## if it is not empty, convert the dictionary back to a json string
    #     # if not data_dict:
    #     #     self.data = '{}'
    #     # else:
    #     #     self.data = json.dumps(data_dict)
    #
    #
    #     super(Item, self).save(*args,**kwargs)




# Create your models here.
