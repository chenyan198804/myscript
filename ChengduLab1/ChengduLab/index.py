#!/usr/bin/env python
#_*_coding:utf-8_*_
import urllib
import http.cookiejar
import ssl



def getOpener(head):
    cookie = http.cookiejar.CookieJar()
    proxy = urllib.request.ProxyHandler({'http':'http://10.144.1.10:8080'})
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler,proxy)
    header = []
    for key,value in head.items():
        elem = (key,value)
        header.append(elem)
    opener.addheaders = header
    return opener

'''
def ungzip(data):
    try:#尝试解压
        print('正在解压!')
        data = gzip.decompress(data)
        print('解压完毕!')
    except:
        print('未经压缩，无需解压')
    return data
'''
        
header = {
          #POST https://10.68.148.38/dana-na/auth/url_default/login.cgi HTTP/1.1,
          'Connection': 'Keep-Alive',
          'Accept-Language': 'zh-CN',
          'Accept': 'text/html, application/xhtml+xml, */*',
          'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0; chromeframe/29.0.1547.57) like Gecko',
          'Accept-Encoding': 'gzip, deflate',
          'Host': '10.68.148.38',
          #'Set-Cookie': 'DSASSERTREF=x; path=/; expires=Thu, 01 Jan 1970 22:00:00 GMT; secure',
          #'Set-Cookie': 'DSID=d2036e07f75ab511672e23a30343d7c5; path=/; secure',
          #'Set-Cookie':' DSFirstAccess=1489383090; path=/; secure',
          #'Referer': 'https://10.68.148.38/dana-na/auth/url_default/welcome.cgi',
          #'Content-Type': 'application/x-www-form-urlencoded',
          #'Content-Length': 93,
          #'Cache-Control': 'no-cache',

          #'Cookie': 'lastRealm=NSN-AD; DSSIGNIN=url_default; DSLastAccess=1489387260; DSLaunchURL=2F64616E612F686F6D652F696E6672616E65742E636769,tz_offset=480&username=y35chen@nsn-intra&password=2017s1@nokia&realm=NSN-AD&btnSubmit=Sign+In'
          }
#s = requests.Session()
#s.headers = header

url = 'https://10.68.148.38/dana-na/auth/url_default/login.cgi'
opener = getOpener(header)

username='y35chen@nsn-intra'
password='2017s1@nokia'
postDict = {
            'tz_offset':480,
            'realm':'NSN-AD',
            'username':username,
            'password':password,
            'btnSubmit':'Sign In',
             'rememberme': "forever",
            }

postData = urllib.parse.urlencode(postDict).encode()
filename = 'cookie.txt'

pCookie = http.cookiejar.MozillaCookieJar(filename)

ssl._create_default_https_context = ssl._create_unverified_context

result = opener.open(url,postData)

data = result.read()
print(data)
#ungzipdata = ungzip(data)
#print(ungzipdata,type(ungzipdata))

