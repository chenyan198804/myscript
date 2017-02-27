#!/usr/bin/env:python
#coding:utf-8

from django.shortcuts import render, render_to_response
from django.http.response import HttpResponse

# Create your views here.
from web.models import Asset
from web.models import UserInfo
from web.forms import RegisterForm
def index(request):
    return HttpResponse("index")

def Add(request, name):
    #Asset.objects.create(hostname=name)
    obj = Asset(hostname=name)
    obj.save()
    return HttpResponse('ok')
    
def Delete(request, id):
    Asset.objects.get(id=id).delete()
    return HttpResponse('ok')

def Update(request, id, hostname):
    '''
    #单条更新
    obj = Asset.objects.get(id=id)
    obj.hostname = hostname
    obj.save()
    '''
    #批量修改
    Asset.objects.filter(id__gt=id).update(hostname=hostname)     
    return HttpResponse('ok')

def Get(request,hostname):
    '''
    assetList = Asset.objects.filter(hostname__contains=hostname)
    for item in assetList:
        print(item.id)
    '''
    #alldata = Asset.objects.all()
    #对应的mysql命令：SELECT `web_asset`.`id`, `web_asset`.`hostname`, `web_asset`.`create_data`, `web_asset`.`update_data` FROM `web_asset`
    alldata = Asset.objects.all().values('id')
    #对应的mysql命令：SELECT `web_asset`.`id` FROM `web_asset`
    print(alldata)
    print(alldata.query)
    #alldata = Asset.objects.all().order_by('-id')
    #alldata = Asset.objects.all().order_by('id')
    #temp = Asset.objects.all()[0:2]
    #print(temp)
    return HttpResponse('ok')
    
def AssetList(request):
    asset_list = Asset.objects.all()
    result = render_to_response('assetlisttemp.html',{'data':asset_list,'user':'alex'})
    return result

def Login(request):
    if request.method == 'POST':
        user = request.POST.get('username',None)
        pwd = request.POST.get('password',None)
        print(user,pwd)
        '''
        try:
            UserInfo.objects.get(username=user,password=pwd)
        except Exception as e:
            pass
        '''
        result = UserInfo.objects.filter(username=user,password=pwd)
        if result == 1:
            return HttpResponse('登录成功')
        else:
            return render_to_response('login.html',{'status':'用户名和密码错误'})
    else:
        return render_to_response('login.html')
    
def Register(request):
    registerForm = RegisterForm()
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
        else:
            #print(type(form.errors))
            #django.forms.utils.ErrorDict
            temp = form.errors.as_data()
            print(temp['email'][0]['message'][0])
    return render_to_response('register.html',{'form':registerForm})

