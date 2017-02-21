#!/usr/bin/env python
#_*_coding:utf-8_*_

class Dict(dict):
    def __init__(self,**kw):
        super().__init__(**kw)
        
    def __getattr__(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'"%key)
    
    def __setattr__(self,key,value):
        self[key] = value
         
    