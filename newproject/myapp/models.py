from django.db import models

# Create your models here.

class Users(models.Model):
      name = models.CharField(max_length=200)
      email = models.EmailField(max_length=200)
      number = models.IntegerField(max_length=20)    
