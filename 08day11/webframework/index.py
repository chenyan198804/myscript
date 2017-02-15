#usr/bin/env python
#coding:utf-8
from wsgiref.simple_server import make_server

def index():
    return [b'<h1>index</h1>']

def login():
    html = b'<p>username:<input /></p><p>password:<input /></p>'
    return [html]

def routers():
    
    urlpatterns = (
           ('/index/',index),
           ('/login/',login),
           )
    
    return urlpatterns
    
def RunServer(environ, start_response):
    start_response('200 OK',[('Content-Type', 'text/html')])
    
    url = environ['PATH_INFO']
    urlpatterns = routers()
    
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