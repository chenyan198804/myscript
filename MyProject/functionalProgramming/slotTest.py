#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
class Student(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def set_score(self,value):
        if not isinstance(value, int):
            raise ValueError('Score must be an integer')
        if value < 0 or value > 100:
            raise ValueError('Score must be in 0~100')
        else:
            self._score = value
        
s = Student()
s.set_score = 69
s.set_score=9999

'''

class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,value):
        self._width = value
        
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,value):
        self._height = value
        
    @property
    def resolution(self):
        return self._height*self._width
    
    
s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
#assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution