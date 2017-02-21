#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)
    
    
class MyList(list,MetaClass=ListMetaclass):
    pass

L=MyList()
L.add(1)
'''