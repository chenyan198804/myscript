#!/usr/bin/env python
#_*_coding:utf-8_*_
from django import template
from django.utils.safestring import mark_safe
from django.template.base import Node, TemplateSyntaxError

register = template.Library()

@register.simple_tag
def mymethod(v1):
    result = 1000*v1
    return result