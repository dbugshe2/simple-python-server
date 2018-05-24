from http.server import HTTPServer, BaseHTTPRequestHandler


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

    # Handle a GET request
    def do_GET(self):  # This method is called when the HTTP method is GET
        '''Overide of the do_GET() method in BaseRequestHandler
        '''
        page = self.create_page()
        self.send_page(page)

    def create_page(self):
        '''This is where we fill in the formatting placeholders
        '''
        

    def send_page(self, page):
        self.send_response(200)
        self.send_response("Content-Type", "text/html")
        self.send_response("Content-Length", str(len(page)))
        self.end_headers()
        self.wfile.write(bytes(page, "utf-8"))


if __name__ == '__main__':
    serverAddress = ('', 8080)
    server = HTTPServer(serverAddress, RequestHandler)
    print("Server Running on 8080")
    server.serve_forever()
