from http.server import HTTPServer, BaseHTTPRequestHandler
import os


class ServerException(Exception):
    '''For internal error reporting'''
    pass


class base_case(object):
    '''parent for case handlers'''

    def handle_file(self, handler, full_path):
        try:
            with open(full_path, 'rb') as reader:
                content = reader.read()
            handler.send_content(content)
        except IOError as msg:
            msg = "'{0}' cannot be read: {1}".format(full_path, msg)
            handler.handle_error(msg)

    def index_path(self, handler):
        return os.path.join(handler.full_path, 'index.html')

    def test(self, handler):
        assert False, 'Not Implemeted'

    def act(self, handler):
        assert False, 'Not Implemeted.'


class case_no_file(base_case):
    '''File or Directory does not exixts'''

    def test(self, handler):
        return not os.path.exists(handler.full_path)

    def act(self, handler):
        raise ServerException("'{0}' not found".format(handler.path))


class case_existing_file(base_case):
    '''File exists'''

    def test(self, handler):
        return os.path.isfile(handler.full_path)

    def act(self, handler):
        self.handle_file(handler, handler.full_path)


class case_always_fail(base_case):
    '''Base case if nothing else worked.'''

    def test(self, handler):
        return True

    def act(self, handler):
        raise ServerException("Unknown Object '{0}'".format(handler.path))


class case_directory_index_file(base_case):
    '''Serve index.html page for a directory'''

    def test(self, handler):
        return os.path.isdir(handler.full_path) and \
                os.path.isfile(self.index_path(handler))

    def act(self, handler):
        self.handle_file(handler, self.index_path(handler))


class case_directory_no_index_file(base_case):
    '''Serve listing for a directory without an index.html page'''

    Listing_Page = '''\
        <html>
        <body>
        <ul>
        {0}
        </ul>
        </body>
        </html>
        '''

    def list_dir(self, handler, full_path):
        try:
            entries = os.listdir(full_path)
            bullets = ['<li> {0} </li>'.format(e)
                       for e in entries if not e.startswith('.')]
            page = self.Listing_Page.format('\n'.join(bullets))
            handler.send_content(bytes(page, 'utf-8'))
        except OSError as msg:
            msg = "'{0}' cannot be listed {1}".format(self.path, msg)
            handler.handle_error(msg)

    def test(self, handler):
        return os.path.isdir(handler.full_path) and \
               not os.path.isfile(self.index_path(handler))

    def act(self, handler):
        self.list_dir(handler, handler.full_path)


class case_cgi_file(base_case):
    '''Something runnable'''

    def run_cgi(self, handler):
        cmd = "python " + handler.full_path
        process = os.popen(cmd)
        data = process.read()
        process.close()
        handler.send_content(bytes(data, 'utf-8'))

    def test(self, handler):
        return os.path.isfile(handler.full_path) and \
                handler.full_path.endswith('.py')

    def act(self, handler):
        self.run_cgi(handler)


class RequestHandler(BaseHTTPRequestHandler):
    '''If the requested path maps to a file, the file is served
    if anythiing goes wrong an error page is constructed.
    '''
    Cases = [case_no_file(),
             case_cgi_file(),
             case_existing_file(),
             case_directory_index_file(),
             case_directory_no_index_file(),
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
