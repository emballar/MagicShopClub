
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TourInfo(models.Model):
    title=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    date=models.DateField()
    time=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title

    class Meta:
        db_table='tourinfo'

class Meetup(models.Model):
    title=models.CharField(max_length=255)
    date=models.DateField()
    location=models.CharField(max_length=255)
    time=models.CharField(max_length=255)
    description=models.TextField(null=True, blank=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table='meetup'