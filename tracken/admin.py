from django.contrib import admin
from .models import Year, Entry, Comment

# Register your models here.
admin.site.register([Year, Entry, Comment])