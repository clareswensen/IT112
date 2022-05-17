from django.test import TestCase
from django.contrib.auth.models import User
from .models import Meeting, MeetingMinutes, Resources, Event
from .forms import MeetingForm, ResourceForm
from django.urls import reverse_lazy, reverse

# Create your tests here.
class MeetingTest(TestCase):
    def setUp(self):
        self.meeting=Meeting(meetingTitle='Orientation', meetingDate='1/1/2022', meetingTime='12:00', location='Seattle Center', agenda='Lets mingle')

    def test_string(self):
        self.assertEqual(str(self.meeting), 'Orientation')

    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class MeetingMinutesTest(TestCase):
    def setUp(self):
        self.meetingID=Meeting(meetingTitle='Orientation')
        self.minutes=MeetingMinutes(meetingID=self.meetingID, minutesText='Howdy Everyone')
    
    def test_string(self):
        self.assertEqual(str(self.meetingID), 'Orientation')

    def test_tablename(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'meetingMinutes')

class ResourceTest(TestCase):
    def setUp(self):
        self.userID=User(username='Joe')
        self.resource=Resources(resourceName='W3Schools',resourceType='online',userID=self.userID,dateEntered='1/1/2022',url='http://www.w3schools.org', description='online resource')

    def test_string(self):
        self.assertEqual(str(self.resource), 'W3Schools')

    def test_tablename(self):
        self.assertEqual(str(Resources._meta.db_table), 'resources')

class EventTest(TestCase):
    def setUp(self):
        self.userID=User(username='Billy')
        self.event=Event(eventTitle='Coding Camp', location='SCC', eventDate='1/1/2022', eventTime='12:00', description='Coding Bananza',userID=self.userID)
    
    def test_tablename(self):
        self.assertEqual(str(Event._meta.db_table), 'event')

class NewMeetingForm(TestCase):
    def test_meetingform(self):
        data = {'meetingTilte':'Happy Hour', 'meetingDate':'1/1/2022','location':'Ferry', 'agenda':'Drink'}
        form=MeetingForm (data)
        self.assertTrue(form.is_valid)

class NewResourceForm(TestCase):
    def test_resourceform(self):
        data = {'resourceName':'Python Club', 'resourceType':'online', 'url':'http://www.pythonclub.org','dateEntered':'2022-01-02', 'userID':'clare', 'description':'non-profit for coders'}
        form=ResourceForm (data)
        self.assertTrue(form.is_valid)

class New_Resource_Authentication_Test(TestCase):
    def setUp(self):
        self.test_userID=User.objects.create_user(username='testuser1', password='password1')
        self.resource=Resources.objects.create(resourceName='W3Schools',resourceType='online',userID=self.test_userID, dateEntered='2022-02-02', url='http://www.w3schools.org', description='online resource')

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newresource'))
        self.assertRedirects(response, '/accounts/login/?next=/club/newResource/')