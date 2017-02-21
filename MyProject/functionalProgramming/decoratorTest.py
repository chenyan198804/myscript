#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
def now():
    print('2017-2-20')
    
f = now 
f()

print(now.__name__)
'''

'''
def log(func):
    def wrapper(*args,**kw):
        print('call %s():' %(func.__name__))
        return func(*args,**kw)
    return wrapper

@log
def now():
    print('2017-2-20')
    
now()
'''
import functools
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('%s call %s():' %(text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2017-2-20')
    #print(now.__name__)
now()