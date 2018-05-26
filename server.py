from http.server import HTTPServer, BaseHTTPRequestHandler
import os


class ServerException(Exception):
    '''For internal error reporting'''
    pass


class RequestHandler(BaseHTTPRequestHandler):
    '''handle HTTP request by returning a fixed 'page'. '''

    Error_Page = """\
    <html>
    <body>
    <h1>Error Accessing {path} </h1>
    <p>{msg}</p>
    </body>
    </html>
    """

    # Handle a GET request
    def do_GET(self):  # This method is called when the HTTP method is GET
        '''Overide of the do_GET() method in BaseRequestHandler'''
        try:
            # figure out exactly what is requested
            full_path = os.getcwd() + self.path

            # it does does not exist....
            if not os.path.exists(full_path):
                raise ServerException("file at{0} not found".format(self.path))

            # ...it's a file...
            elif os.path.isfile(full_path):
                self.handle_file(full_path)

            # ...it's something we don't handle
            else:
                raise ServerException("Unknown Object {0}".format(self.path))
        # handle errors
        except Exception as msg:
            self.handle_error(msg)

    def handle_file(self, full_path):
        try:
            with open(full_path, 'rb') as reader:
                content = reader.read()
            self.send_content(content)
        except IOError as msg:
            msg = "'{0}' cannot be read: {1}".format(self.path, msg)
            self.handle_error(msg)

    # handle unknown objects
    def handle_error(self, msg):
        content = self.Error_Page.format(path=self.path, msg=msg)
        self.send_content(bytes(content, "utf-8"), 404)

    def send_content(self, content, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)


if __name__ == '__main__':
    try:
        serverAddress = ('', 8080)
        server = HTTPServer(serverAddress, RequestHandler)
        print("Server Running on 8080")
        server.serve_forever()
    except (KeyboardInterrupt, Exception):
        print("Closing server")
        server.socket.close()
