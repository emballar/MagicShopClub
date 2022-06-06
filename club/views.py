from django.shortcuts import render
from .models import TourInfo, Meetup

# Create your views here.
def index(request):
    return render(request, 'club/index.html')

def tourinfo(request):
    tour_list=TourInfo.objects.all()
    return render(request, 'club/tourinfo.html', {'tour_list' : tour_list})

def meetup(request):
    meetup_list=Meetup.objects.all()
    return render(request, 'club/meetup.html', {'meetup_list' : meetup_list})