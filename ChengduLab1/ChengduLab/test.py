#!/usr/bin/env python
#_*_coding:utf-8_*_
import base64

s1 = base64.encodestring(bytes('zifuchuang',encoding='utf-8'))
s11 = s1.decode('utf-8')
print(s1,s11,type(s1),type(s11))

s2 = s11.encode('utf-8')
s22 = base64.decodestring(s2)
print(s2,type(s2))
print(s22.decode('utf-8'),type(s22))




    