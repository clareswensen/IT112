
from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinutes, Resources, Event
from .forms import ResourceForm, MeetingForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request): 
    return render(request, 'club/index.html')

def meetings(request):
    meeting_list=Meeting.objects.all()
    return render(request, 'club/meetings.html', {'meeting_list': meeting_list})

def resources(request):
    resource_list=Resources.objects.all()
    return render(request, 'club/resources.html', {'resource_list': resource_list})

def meetingDetail(request, id):
    meeting=get_object_or_404(Meeting, pk=id)
    return render(request, 'club/meetingdetail.html', {'meeting': meeting})

def resourceDetail(request, id):
    resource=get_object_or_404(Resources, pk=id)
    return render(request, 'club/resourcedetail.html', {'resources': resource})

@login_required
def newMeeting(request):
    form=MeetingForm

    if request.method=='POST':
        form=MeetingForm(request.POST)
        if form.is_valid():
                post=form.save(commit=True)
                post.save()
                form=MeetingForm()
    else:
        form=MeetingForm()
    return render(request, 'club/newMeeting.html', {'form': form})

@login_required
def newResource(request):
    form=ResourceForm

    if request.method=='POST':
        form=ResourceForm(request.POST)
        if form.is_valid():
                post=form.save(commit=True)
                post.save()
                form=ResourceForm()
    else:
        form=ResourceForm()
    return render(request, 'club/newResource.html', {'form': form})

def loginmessage(request):
    return render(request, 'club/loginmessage.html')

def logoutmessage(request):
    return render(request, 'club/logoutmessage.html')