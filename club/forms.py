from importlib.resources import Resource
from django import forms
from .models import Meeting, MeetingMinutes, Resources, Event

class ResourceForm(forms.ModelForm):
    class Meta:
        model=Resources
        fields='__all__'

class MeetingForm(forms.ModelForm):
    class Meta:
        model=Meeting
        fields='__all__'