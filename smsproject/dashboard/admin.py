# Import the Django admin module to customize the admin interface.
from django.contrib import admin

# Import the Message model from the current app's models module.
from .models import Message

# Register your models here.

# Define a custom admin class for the Message model.
class MessageAdmin(admin.ModelAdmin):
    # Specify the fields to display in the list view of the admin panel.
    list_display = ['team_name', 'event_name', 'event_date', 'event_time']  # Fixed field name here

# Register the Message model with the custom admin class to integrate it into the admin site.
admin.site.register(Message, MessageAdmin)
