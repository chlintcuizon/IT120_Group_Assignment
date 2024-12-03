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
            account_sid = 'ACc826875119450c4c8a97a337f4ffa2ce'
            auth_token = '30116837c1c5d2c36ffdc7059f622f4b'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                    body=f"Congratulations! {self.name}, your score is {self.score}",
                    from_="+16812460290",
                    to="+639667506130",
                    )
        else:
             account_sid = 'ACc826875119450c4c8a97a337f4ffa2ce'
             auth_token = '30116837c1c5d2c36ffdc7059f622f4b'
             client = Client(account_sid, auth_token)

             message = client.messages.create(
                    body=f"Sorry! {self.name}, your score is {self.score}",
                    from_="+16812460290",
                    to="+639667506130",
                    )
        print(message.sid)
        return super().save(*args, **kwargs)