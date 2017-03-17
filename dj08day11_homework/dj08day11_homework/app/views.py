from django.shortcuts import render, render_to_response
from django.http.response import HttpResponse
# Create your views here.
from app.models import Host
from app.forms import HostForm

def GetHostinfo():
    alldata = Host.objects.all().values('id')
    return render_to_response('hostinfo.html',{'form':HostForm})