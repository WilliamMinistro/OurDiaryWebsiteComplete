from django.db import models
from django.contrib.auth.models import Permission, User
from django import forms

# Create your models here.
from FinalProj import settings


class Info(models.Model):
    task = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    finished = models.BooleanField(default=False)
    username = models.CharField(max_length=50, default='User')
    emotion = models.CharField(max_length=50, default='Neutral')
    anon = models.BooleanField(default=False)

