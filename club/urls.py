from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('resources/', views.resources, name='resources'),
   path('resourceDetail/<int:id>', views.resourceDetail, name='resourcedetail'),
   path('meetings/', views.meetings, name='meetings'),
   path('meetingDetail/<int:id>', views.meetingDetail, name='detail'),
   path('newResource/', views.newResource, name='newresource'),
   path('newMeeting/', views.newMeeting, name='newmeeting'),
]