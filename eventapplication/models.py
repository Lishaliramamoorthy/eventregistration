from django.db import models

# Create your models here.
from django.contrib import admin
class participant(models.Model):
    username=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    instituition=models.CharField(max_length=50)

class participantAdmin(admin.ModelAdmin):
    list_display = ('username','phone','email','instituition')    
