#!/usr/bin/env python
#_*_coding:utf-8_*_
def login():
    f = open('D:\myjava\WebFramework\View\login.html','r')
    data = f.read()
    return [data.encode('utf-8')]


def logout():
    return ['logout']