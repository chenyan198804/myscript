#!/usr/bin/env python
#_*_coding:utf-8_*_
def index():
    return ['<h1>index</h1>']

def login():
    return [b'<h1>login</h1>']

def routers():
    
    urlpatterns = (
                   ('/index/',index),
                   ('/login/',login),
                   )

    print(type(urlpatterns),urlpatterns)

    
routers()
