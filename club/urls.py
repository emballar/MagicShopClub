from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tourinfo/', views.tourinfo, name='tourinfo'),
    path('meetup/', views.meetup, name='meetup'),
    path('tourdetail/<int:id>', views.tourdetail, name='tourdetail'),
    path('meetupdetail/<int:id>', views.meetupdetail, name='meetupdetail'),
]