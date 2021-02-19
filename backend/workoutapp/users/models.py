from django.db import models

# Create your models here.



class Trainees(models.Model):
    userName = models.CharField(max_length=30)
    workout_type = models.CharField(max_length=20)


