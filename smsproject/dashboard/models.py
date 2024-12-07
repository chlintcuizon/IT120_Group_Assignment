from django.db import models
import os
from twilio.rest import Client
from django.utils import timezone

# Define a callable function for the default time value
def get_current_time():
    return timezone.now().time()

class Message(models.Model):
    # Define a 'team_name' field to store the name of the team, with a default value.
    team_name = models.CharField(max_length=100, default='Default Team')  # Provide a default value for team_name

    # Define an 'event_name' field to store the name of the event.
    event_name = models.CharField(max_length=100, default='Default Team')

    # Define an 'event_date' field to store the date of the event. Default to today's date.
    event_date = models.DateField(default=timezone.now)  # Default to the current date

    # Define an 'event_time' field to store the time of the event. Use the callable function for the default value.
    event_time = models.TimeField(default=get_current_time)  # Default to the current time using a callable function

    # String representation of the model; returns the team name and event name.
    def __str__(self):
        return f"{self.team_name} - {self.event_name}"

    # Overriding the save method to include custom behavior when saving an object.
    def save(self, *args, **kwargs):
        # Twilio Account SID and Auth Token (should ideally be stored securely, e.g., in environment variables).
        account_sid = 'AC1b19cb75cd7b50ca291b1d8bf468927b'
        auth_token = '7b6b0b0464cd0600d820647259e2a6f8'
        client = Client(account_sid, auth_token)

        # Create the event reminder SMS message body with team and event details.
        body = f"Hi {self.team_name}, this is a reminder about our upcoming event: {self.event_name} on {self.event_date} at {self.event_time}. Let's gather prepared and ready to discuss our next steps. Keep up the great work, and see you all there!"

        # Create and send the reminder SMS message using Twilio.
        message = client.messages.create(
            body= body,
            from_="+17753739447",  # Twilio phone number
            to="+639171887729",    # Recipient phone number
        )
        
        # Print the unique SID of the message for debugging or logging purposes.
        print(message.sid)

        # Call the parent class's save method to ensure normal behavior.
        return super().save(*args, **kwargs)
