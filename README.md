# Hello, Web
The first version of simple web server. The basic idea is simple:

1. Wait for someone to connect to our server and send an HTTP request;
2. parse that request;
3. figure out what it's asking for;
4. fetch that data (or generate it dynamically);
5. format the data as HTML; and
6. send it back.

Steps 1, 2, and 6 are the same from one application to another, so the Python standard library has a module called BaseHTTPServer that does those for us. We just have to take care of steps 3-5

__Note: In the python 2 implemetation of this version uses `BaseHTTPServer` module, which has been merged into `http.server` in Python 3 and, it longer contains `HTTPServer` - which is also a member of `http.server`, which . The 2to3 tool will automatically adapt imports when converting your sources to Python 3.__