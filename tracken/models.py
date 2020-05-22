from django.db import models
from django.contrib.auth.models import User
from vote.models import VoteModel
import datetime

# Create your models here.

class Year (models.Model):
    year = models.PositiveIntegerField()
    student = models.ForeignKey(User, on_delete=models.CASCADE)

class Entry (models.Model):
    hours = models.PositiveIntegerField()
    year = models.ForeignKey(Year, on_delete=models.CASCADE)

class Comment (VoteModel, models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    text = models.TextField(max_length=50000)