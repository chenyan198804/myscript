#usr/bin/env python
#coding:utf-8
from wsgiref.simple_server import make_server
from WebFramework.Controller.Admin import *
from WebFramework.Controller.Account import *

urlpatterns = (
    ('/index/',index),
    ('/login/',login),
)


def RunServer(environ, start_response):

    start_response('200 OK',[('Content-Type', 'text/html')])

    url = environ['PATH_INFO']

    func = None
    for item in urlpatterns:
        if item[0] == url:
            func = item[1]
            break
    if func:
        result = func()
    else:
        result = [b'<h1>404 not found</h1>']

    return result

if __name__=='__main__':
    httpd = make_server('', 8000, RunServer)
    print('Server HTTP on port 8000')
    httpd.serve_forever()