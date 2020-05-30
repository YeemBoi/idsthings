from django.db import models
from django.contrib.auth.models import User
from vote.models import VoteModel
from django.urls import reverse
import datetime

# Create your models here.

class Year (models.Model):
    year = models.PositiveIntegerField()
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.student.username + ' ' + str(self.year)
    
    def get_absolute_url(self):
        return reverse('tracken:progress')

class Entry (models.Model):
    work_date = models.DateTimeField('time work happened', auto_now_add=True)
    #updated_date = models.DateTimeField(auto_now=True)
    hours = models.PositiveIntegerField(default=1)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    goal = models.TextField(null=True, blank=True)
    accomplishments = models.TextField(default="Something, anyways")

    def get_absolute_url(self):
        return reverse('tracken:entry', kwargs={"pk": self.id})

    def __str__(self):
        return self.accomplishments

class Comment (VoteModel, models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    text = models.TextField(max_length=50000)