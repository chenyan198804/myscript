#!/usr/bin/env:python
#coding:utf-8

from django.db import models

# Create your models here.
    
class UserType(models.Model):
    
    name = models.CharField(max_length=50)
    
class UserInfo(models.Model):

    username = models.CharField(max_length=50)

    password = models.CharField(max_length=50)
    
    Gender = models.BooleanField(default = False)
    
    Age = models.IntegerField(default = 19)
    
    Memo = models.TextField(default = 'xxxx')
    
    Creatdate = models.DateTimeField(default = '2014-12-12 12:12')
    
    TypeId = models.ForeignKey('UserType')

    
class Group(models.Model):
    
    Name = models.CharField(max_length=50)
    
class User(models.Model):
    
    Name = models.CharField(max_length=50)
    
    Email = models.CharField(max_length=50)
    
    group_relation = models.ManyToManyField('Group')
    
    #models.OneToOneField
    
    
class Args(models.Model):
    
    name = models.CharField(max_length=50, null=True)
    
    not_name = models.CharField(max_length=50, null=False)
    
class Asset(models.Model):
#自动添加和错误提示    
    hostname = models.CharField(max_length=256, null=True)
    
    create_data = models.DateTimeField(auto_now_add = True, error_messages={'invalid':'??????'})
    
    update_data = models.DateTimeField(auto_now = True)
    
    
class UserInfo_Temp(models.Model):
    #就放在内存，不放到数据库里面
    User_CHOICE = (
        (u'1', u'普通用户'),
        (u'2', u'管理员'),
        (u'3', u'超级管理员'),
    )
    UserType = models.CharField(max_length=2,choices = User_CHOICE)
    
    
    
    