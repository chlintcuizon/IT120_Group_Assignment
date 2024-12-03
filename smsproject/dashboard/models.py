
from django.db import models
import os
from twilio.rest import Client
# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
   