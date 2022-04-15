from django.contrib import admin
from .models import Meeting, MeetingMinutes, Resources, Event
# Register your models here.
admin.site.register(Meeting)
admin.site.register(MeetingMinutes)
admin.site.register(Resources)
admin.site.register(Event)