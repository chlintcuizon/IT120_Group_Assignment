# Import the Django ORM models module to define database models.
from django.db import models

# Import the Twilio Client for sending SMS messages.
from twilio.rest import Client

# Create your models here.

class Message(models.Model):
    # Define a 'name' field to store a string with a maximum length of 100 characters.
    name = models.CharField(max_length=100)

    # Define a 'score' field to store an integer, defaulting to 0.
    score = models.IntegerField(default=0)

    # String representation of the model; returns the name of the object.
    def __str__(self):
        return self.name

    # Overriding the save method to include custom behavior when saving an object.
    def save(self, *args, **kwargs):
        # Check if the score is greater than or equal to 70.
        if self.score >= 70:
            # Twilio Account SID and Auth Token (should ideally be stored securely, e.g., in environment variables).
            account_sid = 'AC1b19cb75cd7b50ca291b1d8bf468927b'
            auth_token = '0f89eb4c0538f801955f243ddd16875c'
            client = Client(account_sid, auth_token)

            # Create and send a congratulatory SMS message using Twilio.
            message = client.messages.create(
                body=f"Congratulations! {self.name}, your score is {self.score}",
                from_="+17753739447",  # Twilio phone number
                to="+639171887729",    # Recipient phone number
            )
        else:
            # Use the same credentials for Twilio.
            account_sid = 'AC1b19cb75cd7b50ca291b1d8bf468927b'
            auth_token = '0f89eb4c0538f801955f243ddd16875c'
            client = Client(account_sid, auth_token)

            # Create and send an apology SMS message using Twilio.
            message = client.messages.create(
                body=f"Sorry! {self.name}, your score is {self.score}",
                from_="+17753739447",  # Twilio phone number
                to="+639171887729",    # Recipient phone number
            )
        
        # Print the unique SID of the message for debugging or logging purposes.
        print(message.sid)

        # Call the parent class's save method to ensure normal behavior.
        return super().save(*args, **kwargs)
