from socket import fromshare
from django import forms
from .models import Meetup, Member

class MeetupForm(forms.ModelForm):
    class Meta:
        model = Meetup
        fields='__all__'

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields='__all__'