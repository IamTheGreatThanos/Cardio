from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
  
    def __str__(self):
        return self.name

class Device(models.Model):
    number = models.CharField(max_length=120)
    description = models.TextField()
    owner = models.ForeignKey('User', related_name='devices', on_delete=models.CASCADE)

    def __str__(self):
        return self.description