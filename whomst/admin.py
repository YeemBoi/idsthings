from django.contrib import admin

# Register your models here.
from .models import Profile, verificationCodes, Post
admin.site.register([Profile, verificationCodes, Post])