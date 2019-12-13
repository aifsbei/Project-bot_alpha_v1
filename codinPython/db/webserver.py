import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler

webdir = 'C:/Users/aifsb/PycharmProjects/codinPython/db'
port = 8080
os.chdir(webdir)
srvaddr = ('localhost', port)
srvobj = HTTPServer(srvaddr, CGIHTTPRequestHandler)
srvobj.serve_forever()