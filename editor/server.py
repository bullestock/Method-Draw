import SimpleHTTPServer
import SocketServer
import logging
import cgi
import time
import xml.etree.ElementTree

PORT = 8000

class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_GET(self):
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        data_string = self.rfile.read(int(self.headers['Content-Length']))

        root = xml.etree.ElementTree.fromstring(data_string)
        # Remove first child (background)
        firstborn = root.getchildren()[0]
        root.remove(firstborn)

        # Save as SVG file
        fname = "%d.svg" % int(time.time())
        svg_file = open(fname, "w")
        svg_file.write(xml.etree.ElementTree.tostring(root));
        svg_file.close()
        self.send_response(200)
        self.end_headers()

Handler = ServerHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()
