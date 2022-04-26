from django.shortcuts import render
from .models import Meeting, MeetingMinutes, Resources, Event

# Create your views here.
def index(request): 
    return render(request, 'club/index.html')

def meetings(request):
    meeting_list=Meeting.objects.all()
    return render(request, 'club/meetings.html', {'meeting_list': meeting_list})

