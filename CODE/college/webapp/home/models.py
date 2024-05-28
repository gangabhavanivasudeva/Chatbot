from django.db import models
from django.db.models.base import Model
from django.db.models.fields import IntegerField, UUIDField
from django.db.models.lookups import In
import uuid
from django.contrib.auth.models import User

# Create your models here.
class Branch(models.Model):
    branch = models.CharField(max_length=200)
    desc = models.TextField(max_length=1000)
    special = models.CharField(max_length=200)
    professors = models.CharField(max_length=200)
    fees = models.CharField(max_length=200)
    duration = models.CharField(max_length=200)
    seats = models.CharField(max_length=200)


class placements(models.Model):
    company = models.CharField(max_length=200)
    package = models.IntegerField()
    full_time = models.BooleanField()


class AboutCollege(models.Model):
    infra = models.CharField(max_length=200)
    events = models.CharField(max_length=200)
    env = models.CharField(max_length=200)
    achievements = models.CharField(max_length=200)
    hostel = models.IntegerField()
    naac = models.IntegerField()
    NIRF = models.IntegerField()

class Reminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    alarm = models.CharField(max_length=200)
    Event = models.CharField(max_length=200)