#!/usr/bin/env python
#_*_coding:utf-8_*_
print(abs(-10))
print(abs)
f= abs
print(f(-5))


#高阶函数
def add(x,y,f):
    return f(x)+f(y)

result = add(3,-4,abs)
print(result)

