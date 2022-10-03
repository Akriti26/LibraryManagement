#from datetime import datetime
#import email
#from unicodedata import name
#from typing_extensions import Self
from django.db import models

# Create your models here.
class Registration(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

    
    def __str__(self):
        return self.name