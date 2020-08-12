from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    card_id = models.CharField(
        max_length=160,
        null=True,
        blank=True
    )
    device_id = models.CharField(
        max_length=160,
        null=True,
        blank=True
    )
    date = models.DateField(
        null=True,
        blank=True
    )
    data = models.CharField(
        max_length=256,
        null=True,
        blank=True
    )
    def __str__(self):
        return self.user.username