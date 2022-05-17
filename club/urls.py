from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('resources/', views.resources, name='resources'),
   path('meetings/', views.meetings, name='meetings'),
   path('meetingDetail/<int:id>', views.meetingDetail, name='detail'),
   path('resourceDetail/<int:id>', views.resourceDetail, name='resourcedetail'),
   path('newMeeting/', views.newMeeting, name='newmeeting'),
   path('newResource/', views.newResource, name='newresource'),
   path('loginmessage/', views.loginmessage, name='loginmessage'),
   path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]