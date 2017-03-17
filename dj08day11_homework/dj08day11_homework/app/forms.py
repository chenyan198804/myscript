#!/usr/bin/env python
#_*_coding:utf-8_*_
from django import forms

class HostForm(forms.Form):
    hostname = forms.CharField()
    ip = forms.CharField()
    groupinfo = forms.CharField()

    