from django.db import models
from django.contrib.auth.models import User
from vote.models import VoteModel
from django.urls import reverse
import datetime

# Create your models here.

class Year (models.Model):
    year = models.PositiveIntegerField()
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    hours_goal = models.PositiveSmallIntegerField(verbose_name='Goal for hours to accomplish', default=120)
    def __str__(self):
        return self.student.username + ' ' + str(self.year)
    
    def get_absolute_url(self):
        return reverse('tracken:progress')

class Entry (models.Model):
    work_date = models.DateTimeField('Time work happened', auto_now_add=True)
    #updated_date = models.DateTimeField(auto_now=True)
    time_spent = models.DurationField('Time spent on IDS', default=datetime.timedelta(hours=1))
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    goal = models.TextField(verbose_name='Goals for work period', null=True, blank=True)
    accomplishments = models.TextField(verbose_name='Work accomplished', default='Something, anyways')

    def get_absolute_url(self):
        return reverse('tracken:entry', kwargs={"pk": self.id})

    def __str__(self):
        return self.accomplishments

class Comment (VoteModel, models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Thoughts on entry', max_length=50000)