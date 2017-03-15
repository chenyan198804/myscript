#!/usr/bin/env python
#_*_coding:utf-8_*_

from ChengduLab.dbhelper import dbapi
from ChengduLab.conf import settings
import os
import requests
import urllib
 
class Admin():
    __database = "{0}.db".format(os.path.join(settings.DATABASE['dbpath'], settings.DATABASE["tables"]["user"]))

    def __init__(self):
        self.password = ""
        self.username = ""
        self.userinfo = {}
        self.db_load()

    def db_load(self):
        self.dict_user = dbapi.load_data_from_db(self.__database)
    
    def login(self):    
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
                    'username':self.username,
                    'password':self.password,
                    'btnSubmit':'Sign In',
                    }
        
        postData = urllib.parse.urlencode(postDict).encode()
        result = s.post(url,data=postData,verify=False)
        print('login status %s' % result.status_code)
