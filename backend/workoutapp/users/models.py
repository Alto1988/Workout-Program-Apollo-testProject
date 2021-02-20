from __future__ import unicode_literals
from django.db import models
# Create your models here.



class Trainees(models.Model):
    userName = models.CharField(max_length=30)
    workout_type = models.CharField(max_length=20)



class Message(models.Model):
    user = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    message = models.TextField()
    creation_at = models.DateTimeField(auto_now_add=True)