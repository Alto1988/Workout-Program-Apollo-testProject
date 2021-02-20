from __future__ import unicode_literals
from django.db import models
from django.contrib import admin
from .models import Trainees, Message
# Register your models here.

admin.site.register(Trainees)
admin.site.register(Message)