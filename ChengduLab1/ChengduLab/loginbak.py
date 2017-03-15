#!/usr/bin/env python
#_*_coding:utf-8_*_
import urllib
import requests


def login(username,password):    
    header = {
    
              'Connection': 'Keep-Alive',
              'Accept-Language': 'zh-CN',
              'Accept': 'text/html, application/xhtml+xml, */*',
              'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0; chromeframe/29.0.1547.57) like Gecko',
              'Accept-Encoding': 'gzip, deflate',
              'Host': '10.68.148.38',
              }
    s = requests.Session()
    s.headers = header
    
    url = 'https://10.68.148.38/dana-na/auth/url_default/login.cgi'
    
    postDict = {
                'tz_offset':'480',
                'realm':'NSN-AD',
                'username':username,
                'password':password,
                'btnSubmit':'Sign In',
                }
    
    postData = urllib.parse.urlencode(postDict).encode()
    result = s.post(url,data=postData,verify=False)
    print('login status %s' % result.status_code)
    
if __name__=="__main__":
    _user_list = {"username":'y35chen@nsn-intra',"password":'2017s1@nokia'}
    username = _user_list["username"]
    password = _user_list["password"]
    login(username,password)



