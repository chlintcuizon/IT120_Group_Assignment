from django.db import models
import os
from twilio.rest import Client
# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.score >=70:
            account_sid = 'AC1b19cb75cd7b50ca291b1d8bf468927b'
            auth_token = '0f89eb4c0538f801955f243ddd16875c'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                    body=f"Congratulations! {self.name}, your score is {self.score}",
                    from_="+17753739447",
                    to="+639171887729",
                    )
        else:
             account_sid = 'AC1b19cb75cd7b50ca291b1d8bf468927b'
             auth_token = '0f89eb4c0538f801955f243ddd16875c'
             client = Client(account_sid, auth_token)

             message = client.messages.create(
                    body=f"Sorry! {self.name}, your score is {self.score}",
                    from_="+17753739447",
                    to="+639171887729",
                    )
        print(message.sid)
        return super().save(*args, **kwargs)