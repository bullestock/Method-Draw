import SimpleHTTPServer
import SocketServer
import logging
import cgi
import time

PORT = 8000

class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_GET(self):
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        data_string = self.rfile.read(int(self.headers['Content-Length']))
        self.send_response(200)
        self.end_headers()        
        fname = "%d.svg" % int(time.time())
        print("File: %s\n" % fname)
        print("SVG: %s" % data_string)
        svg_file = open(fname, "w")
        svg_file.write(data_string);
        svg_file.close()
        #SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

Handler = ServerHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()
