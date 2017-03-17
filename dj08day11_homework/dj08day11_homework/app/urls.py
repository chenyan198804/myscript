#!/usr/bin/env python
#_*_coding:utf-8_*_


from django.conf.urls import url
from django.contrib import admin
#from web.views import Add, Delete, Update, Get
from app.views import Host

urlpatterns = [
    url(r'^host/$', Host),

]
