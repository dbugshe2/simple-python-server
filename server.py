from http.server import HTTPServer, BaseHTTPRequestHandler
import os


class ServerException(Exception):
    '''For internal error reporting'''
    pass


class case_no_file(object):
    '''File or Directory does not exixts'''

    def test(self, handler):
        return not os.path.exists(handler.full_path)

    def act(self, handler):
        raise ServerException("'{0}' not found".format(handler.path))


class case_existing_file(object):
    '''File exists'''

    def test(self, handler):
        return os.path.isfile(handler.full_path)

    def act(self, handler):
        handler.handle_file(handler.full_path)


class case_always_fail(object):
    '''Base case if nothing else worked.'''

    def test(self, handler):
        return True

    def act(self, handler):
        raise ServerException("Unknown Object '{0}'".format(handler.path))


class RequestHandler(BaseHTTPRequestHandler):
    '''If the requested path maps to a file, the file is served
    if anythiing goes wrong an error page is constructed.
    '''
    Cases = [case_no_file(),
             case_existing_file(),
             case_always_fail()]

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
            self.full_path = os.getcwd() + self.path

            # figure out how to handle it
            for case in self.Cases:
                if case.test(self):
                    case.act(self)
                    break
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
