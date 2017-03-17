from django.db import models

# Create your models here.
class Group(models.Model):
    
    grounpname = models.CharField(max_length=50)
    
class User(models.Model):
    
    hostname = models.CharField(max_length=50)
    
    ip = models.CharField(max_length=50)
    
    groupinfo = models.ManyToManyField('Group')
    