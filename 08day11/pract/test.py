#!/usr/bin/env python
#coding:utf-8
import socket
'''应用程序'''
def handle_request(client):
    client.recv(1024)
    client.send("HTTP/1.1 200 OK\r\n\r\n".encode('utf-8'))
    client.send("Hello,Seven".encode('utf-8'))

'''服务器程序'''
def main():
    sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sk.bind(('localhost',8000))
    sk.listen(5)

    while True:
        conn,add = sk.accept()
        handle_request(conn)
        conn.close()

if __name__=='__main__':
    main()