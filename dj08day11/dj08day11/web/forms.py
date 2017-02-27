#!/usr/bin/env python
#_*_coding:utf-8_*_

from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField(required=True,error_messages={'invalid':'邮箱格式错误'})
