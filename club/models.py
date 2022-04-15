from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Meeting(models.Model):
    meetingTitle = models.CharField(max_length=255)
    meetingDate = models.DateField()
    meetingTime = models.TimeField()
    location = models.CharField(max_length=255)
    agenda = models.TextField()

    def __str__(self):
        return self.meetingTitle

    class Meta:
        db_table='meeting'
        verbose_name_plural='meetings'

class MeetingMinutes(models.Model):
    meetingID = models.ForeignKey(Meeting, on_delete=CASCADE)
    attendance = models.ManyToManyField(User)
    minutesText = models.TextField()

    def __str__(self):
        return self.meetingID

    class Meta:
        db_table='meetingMinutes'

class Resources(models.Model):
    resourceName = models.CharField(max_length=255)
    resourceType = models.CharField(max_length=255)
    url = models.URLField()
    dateEntered = models.DateField()
    userID = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    description = models.TextField()

    def __str__(self):
        return self.resourceName

    class Meta:
        db_table = 'resources'
        verbose_name_plural = 'resources'

class Event(models.Model):
    eventTitle = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    eventDate = models.DateField()
    eventTime = models.TimeField()
    description = models.TextField()
    userID = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'event'
        erbose_name_plural = 'events'