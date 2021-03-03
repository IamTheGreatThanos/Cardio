from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField


class Profile(models.Model):
    device_id = models.CharField(max_length=160,null=True,blank=True)

    def __str__(self):
        return self.device_id


class ProfileData(models.Model):
    date = models.CharField(max_length=160,null=True,blank=True)
    data = ArrayField(models.BigIntegerField(), null=True, blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.date}'
