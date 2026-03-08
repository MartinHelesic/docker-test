from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello from Docker on Raspberry Pi")

server = HTTPServer(("0.0.0.0", 8000), Handler)
server.serve_forever()
print("change from github")
print("feature branch change")
print("change from clone")
