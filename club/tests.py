from django.test import TestCase
from django.contrib.auth.models import User
from .models import Meeting, MeetingMinutes, Resources, Event

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
