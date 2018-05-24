from http.server import HTTPServer, BaseHTTPRequestHandler


class RequestHandler(BaseHTTPRequestHandler):
    '''handle HTTP request by returning a fixed 'page'. '''

    # Page to send back.
    Page = '''\
<html>
<body>
<p>Hello World</p>
</body>
</html>
'''

    # Handle a GET request
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(self.Page)))
        self.end_headers()
        self.wfile.write(bytes(self.Page, "utf-8"))


if __name__ == '__main__':
    serverAddress = ('', 8080)
    server = HTTPServer(serverAddress, RequestHandler)
    print("Server Running on 8080")
    server.serve_forever()
