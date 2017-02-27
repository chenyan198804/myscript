"""dj08day11 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include


#def active(request):
    #获取url
    #第一段：app名字
    #第二段：view文件名
    #反射的方式找到函数名

urlpatterns = [
    #url对应文件
    url(r'^admin/', admin.site.urls),
    url(r'^web/', include('web.urls')),
 
    #url(r'^', active),
]
