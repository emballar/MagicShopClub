from django.test import TestCase
from .models import TourInfo, Meetup, Member
from django.contrib.auth.models import User
from .forms import MeetupForm, MemberForm
from django.urls import reverse_lazy, reverse
import datetime

class TourTest(TestCase):
    def setUp(self):
        self.type= TourInfo(title='BTS WORLD TOUR 2022 : PROOF in SEATTLE')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'BTS WORLD TOUR 2022 : PROOF in SEATTLE')

    def test_tablename(self):
        self.assertEqual(str(TourInfo._meta.db_table), 'tourinfo')

class MeetupFormTest(TestCase):
    def test_meetupform(self):
        data={
            'title':'Networking Event',
            'date' : datetime.date(2022,9,31),
            'location':'Amazon Spheres',
            'time' : '10 AM',
            'description' : 'ARMY networking event',
            'user' : 'namjoon'
            }
        form=MeetupForm(data)
        self.assertTrue(form.is_valid)

class MemberFormTest(TestCase):
    def test_memberform(self):
        data={
            'name':'Erin',
            'age' : '25',
            'bias':'Namjoon',
            'blurb' : 'any armycarats here?',
            'user' : 'Erin',
            }
        form=MemberForm(data)
        self.assertTrue(form.is_valid)

class New_Member_Authentication_Test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='namjoon', password='W1nning!')
        self.name=Member.objects.create(name='Namjoon')
        self.age=Member.objects.create(age=27)
        self.member=Member.objects.create(name=self.name, age=self.age, bias = 'taehyung', blurb= 'im literally RM of BTS', user=self.test_user)

#NULL Value error??
    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newmember'))
        self.assertRedirects(response, '/accounts/login/?next=/club/newmember/')
