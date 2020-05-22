from django.db import models
from django.contrib.auth.models import User
from vote.models import VoteModel
import datetime

# Create your models here.

class Year (models.Model):
    year = models.PositiveIntegerField()
    student = models.ForeignKey(User)

class Entry (models.Model):
    hours = models.PositiveIntegerField()
    year = models.ForeignKey(Year, on_delete=CASCADE)

class Comment (VoteModel, models.Model):
    entry = models.ForeignKey(Entry, on_delete=cascade)
    text = models.TextField(max_length=50000)