import os
import sys
from http.server import HTTPServer, CGIHTTPRequestHandler

webdir = 'C:/Users/aifsb/PycharmProjects/codinPython/trash'
port = 8888
os.chdir(webdir)
srvaddr = ('localhost', port)
srvobj = HTTPServer(srvaddr, CGIHTTPRequestHandler)
srvobj.serve_forever()