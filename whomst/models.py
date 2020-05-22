from django.db import models
from django.contrib.auth.models import User
from vote.models import VoteModel
from random import randint

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name="bio image", null=True, blank=True)
    bio = models.TextField(verbose_name="bio text", blank=True)


class verificationCodes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    def randomCode(self):
        return randint(11111, 99999)
    code = models.PositiveIntegerField(verbose_name="verification code", default=randomCode)



class Post(VoteModel, models.Model):
    CATEGORY_CHOICES = [
        ('TO', 'thought'),
        ('ME', 'meme'),
        ('IG', 'image'),
        ('QN', 'question'),
        ('AN', 'answer'),
    ]
    title = models.CharField(verbose_name="post title", max_length=250, blank=True, null=True)
    content = models.TextField(verbose_name="post content", help_text="What do you want to write about?")
    author = models.ForeignKey(User, on_delete=models.SET_NULL)
    uppers = models.ManyToManyField('self', symmetrical=False)
    category = models.CharField(verbose_name='post category', max_length=2, choices=CATEGORY_CHOICES)
    isOC = models.BooleanField(verbose_name="is the content original")

