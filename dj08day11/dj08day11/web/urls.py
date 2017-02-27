#!/usr/bin/env python
#_*_coding:utf-8_*_


from django.conf.urls import url
from django.contrib import admin
#from web.views import Add, Delete, Update, Get
from web.views import AssetList,Login,Register

urlpatterns = [
    url(r'^assetlist/$', AssetList),
    url(r'^login/$', Login),
    url(r'^register/', Register),
    #url(r'^add/(?P<name>\d*)/$',Add),          
    #url(r'^delete/(?P<id>\d*)/$',Delete),   
    #url(r'^update/(?P<id>\d*)/(?P<hostname>\w*)/$',Update),   
    #url(r'^get/(?P<hostname>\w*)/$',Get),   
    
    #url(r'^index/$', index),
    #url(r'^login/', login),
    #url(r'^list/(?P<id>\d*)/(?P<name>\d*/$)', list),
    #url(r'^list/(?P<id>\d*)/$', list,{'name':'alex'}),

]
