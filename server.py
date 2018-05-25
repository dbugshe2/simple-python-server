from http.server import HTTPServer, BaseHTTPRequestHandler
import os


class RequestHandler(BaseHTTPRequestHandler):
    '''handle HTTP request by returning a fixed 'page'. '''

    # the page is a string containig some html with formatting placeholders
    Page = '''\
<html>
<body>
<table>
<tr>  <td>Header</td>         <td>Value</td>          </tr>
<tr>  <td>Date and time</td>  <td>{date_time}</td>    </tr>
<tr>  <td>Client host</td>    <td>{client_host}</td>  </tr>
<tr>  <td>Client port</td>    <td>{client_port}s</td> </tr>
<tr>  <td>Command</td>        <td>{command}</td>      </tr>
<tr>  <td>Path</td>           <td>{path}</td>         </tr>
</table>
</body>
</html>
'''

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
        '''Overide of the do_GET() method in BaseRequestHandler
        '''
        try:
            # figure out exactly what is requested
            full_path = os.getcwd() + self.path

            # it does does not exist....
            if not os.path.exists(full_path):
                ServerException("{} not found".format(self.path))

            # ...it's a file...
            elif os.path.isfile(full_path):
                self.handle_file(full_path)

            # ...it's something we don't handle
            else:
                raise ServerException("Unknown Object {}".format(self.path))
        # handle errors
        except Exception as msg:
            self.handle_errors(msg)

    def handle_file(self):
        try:
            with open(full_path, 'rb') as reader:
                content = reader.read()
            self.send_content(content)
        except IOError as msg:
            msg = "'{0}' cannot bee read: {1}".format(self.path, msg)

    def handle_error(self, msg):
        content = self.Error_Page.format(path=self.path, msg=msg)
        self.send_content(content)

    def create_page(self):
        '''This is where we fill in the formatting placeholders
        '''
        values = {
            'date_time': self.date_time_string(),
            'client_host': self.client_address[0],
            'client_port': self.client_address[1],
            'command': self.command,
            'path': self.path
        }
        page = self.Page.format(**values)
        return page

    def send_page(self, page):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(page)))
        self.end_headers()
        self.wfile.write(bytes(page, "utf-8"))


if __name__ == '__main__':
    serverAddress = ('', 8080)
    server = HTTPServer(serverAddress, RequestHandler)
    print("Server Running on 8080")
    server.serve_forever()
