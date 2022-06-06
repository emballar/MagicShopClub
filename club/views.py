from django.shortcuts import render, get_object_or_404
from .models import TourInfo, Meetup, Member
from .forms import MeetupForm, MemberForm

# Create your views here.
def index(request):
    return render(request, 'club/index.html')

def tourinfo(request):
    tour_list=TourInfo.objects.all()
    return render(request, 'club/tourinfo.html', {'tour_list' : tour_list})

def meetup(request):
    meetup_list=Meetup.objects.all()
    return render(request, 'club/meetup.html', {'meetup_list' : meetup_list})

def member(request):
    member_list=Member.objects.all()
    return render(request, 'club/member.html', {'member_list' : member_list})

def tourdetail(request, id):
    tour = get_object_or_404(TourInfo, pk = id)
    return render(request, 'club/tourdetail.html', {'tour' : tour})

def meetupdetail(request, id):
    meetup = get_object_or_404(Meetup, pk = id)
    return render(request, 'club/meetupdetail.html', {'meetup' : meetup})

def memberdetail(request, id):
    member = get_object_or_404(Member, pk = id)
    return render(request, 'club/memberdetail.html', {'member' : member})

def newMeetup(request):
    form= MeetupForm

    if request.method == 'POST':
        form=MeetupForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=MeetupForm()
    
    else:
        form=MeetupForm()
    
    return render(request, 'club/newmeetup.html', {'form' : form})

def newMember(request):
    form= MemberForm

    if request.method == 'POST':
        form=MemberForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=MemberForm()
    
    else:
        form=MemberForm()
    
    return render(request, 'club/newmember.html', {'form' : form})