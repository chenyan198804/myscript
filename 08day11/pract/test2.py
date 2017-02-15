from wsgiref.simple_server import make_server

def RunServer(environ, start_response):
    start_response('200 OK',[('Content-Type', 'text/html')])
    return [b'<h1>Hello,web</h1>']

if __name__=='__main__':
    httpd = make_server('', 8000, RunServer)
    print('Server HTTP on port 8000')
    httpd.serve_forever()
