from django.contrib import admin
from .models import TourInfo, Meetup, Member
# Register your models here.
admin.site.register(TourInfo)
admin.site.register(Meetup)
admin.site.register(Member)