#!/usr/bin/env python
#_*_coding:utf-8_*_

from numpy import *
import itchat
import urllib
import requests
import os
import PIL.Image as Image
from os import listdir
import math

proxies = { "http": "http://10.144.1.10:8080", "https": "https://10.144.1.10:8080", }   
requests.get("https://login.weixin.qq.com", proxies=proxies)  

itchat.auto_login(enableCmdQR=True)
friends = itchat.get_friends(update=True)[0:]
user = friends[0]["username"]
print(user)
os.mkdir(user)
num = 0

for i in friends:
    img = itchat.get_head_img(userName=i["UserName"])
    fileImage = open(user + "/" + str(num) + ".jpg",'wb')
    fileImage.close()
    num += 1
    
pics = listdir(user)
numPic = len(pics)
print(numPic)
eachsize = int(math.sqrt(float(640*640))/numPic)
print(eachsize)

numline = int(640/ eachsize)
toImage = Image.new('RGBA',(640,640))
print(numline)

x = 0
y = 0
for i in pics:
    try:
        img = Image.open(user,"/", i)
    except IOError:
        print("Error:没有找到文件或者读取文件失败")
        
    else:
        img = img.resize((eachsize,eachsize),Image.ANTIALIAS)
        toImage.paste(img, (x*eachsize,y*eachsize))
        x += 1
        if x ==numline:
            x = 0
            y += 1
            
toImage.save(user + 'jpg')

itchat.send_image(user + ".jpg" + 'filehelper')
