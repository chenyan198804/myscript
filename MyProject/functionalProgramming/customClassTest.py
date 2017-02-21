#!/usr/bin/env python
#_*_coding:utf-8_*_

class Student(object):
    def __init__(self,name):
        self.name = name
        
    def __str__(self):
        return 'Student object (name = %s)' %self.name
    
    __repr__ = __str__
    
    def __getattr__(self, attr):
        if attr == 'age':
            return lambda:25
        raise AttributeError('\'Student\' object has no attribute \' %s \'' % attr)
    
    def __call__(self):
        print('over')
        
s = Student('Candy')
#print(s)
#print(s.job)
s()

'''

class Fib(object):

    def __init__(self):
        self.a,self.b = 0, 1    #初始化两个计数器a,b
        
    def __iter__(self):
        return self     #实例本身就是迭代对象，故返回自己
    
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        
        if self.a > 100:
            raise StopIteration();
        return self.a

    def __getitem__(self,n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b =1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L  
        
    
for n in Fib():
    print(n)
  
print(Fib()[5])  
    
print(Fib()[10])  

#print(list(range(100)[5:10]))

f = Fib()
print(f[0:5])

help(isinstance)
'''
'''
class Chain(object):
    def __init__(self, path=''):
        self._path = path
        
    def __getattr__(self,path):
        return Chain('%s %s' %(self._path, path))
    
    def __str__(self):
        return self._path
    
    __repr__ = __str__
    
    
c = Chain()    
print(c.status.user.timeline.list)
'''
    