# Common Gateway Interface (CGI) Protocol
in order to add new functionality to a server, servers have always supported a mechanism called the Common Gateway Interface (CGI), which provides a standard way for a web server to run an external program in order to satisfy a request.

For example, suppose we want the server to be able to display the local time in an HTML page. We can do this in a standalone program with just a few lines of code:

    from datetime import datetime
    print ('''\
    <html>
    <body>
    <p>Generated {0}</p>
    </body>
    </html>''').format(datetime.now())

In order to get the web server to run this program for us, we add a handler represented as the method `case_cgi_file` which tests if the path ends with `.py` then it acts by telling `RequestHandler`  to run it. This is generally acheived through the following core steps.

### Core Ideas

1. Run the program in a subprocess.
2. Capture whatever that subprocess sends to standard output.
3. Send that back to the client that made the request.

The full CGI protocol is much richer than this

But just doing that is very insecure because,  if someone knows the path to a Python file on our server, we're just letting them run it without worrying about what data it has access to, whether it might contain an infinite loop, or anything else.

## Cleaning up
Our `RequestHandler` class is becoming quite tangled  initially had one method, handle_file, for dealing with content. We have now added two special cases in the form of list_dir and run_cgi, These three methods don't really belong where they are, since they're primarily used by other classes.

a straightforward way to fix this is to:
- create a parent class `base_case` for all our case handlers, and
- move other methods to that class if (and only if) they are shared by two or more handlers. 

## What has changed
- first we after figure out the full of the thing being requested(like in the previous version)
- then we loop over a set of cases stored in a list (created at the top of `RequestHandler`). Each case is an object with two methods
    + `test()` which tells us whether it able to handle the request
    + and `act()` which actually takes some action
- as soon as the right case is found, it handles the request and we break out of the loop
- There are three case classes that reproduce the behavior of our previous server version
    + `case_no_file` - The File or directory does noto exist
    + `case_existing_file` - The File exists
    + `case_always_fail` - Base case for if nothing else works
- Next we try to teach our server to serve up the `index.html` page for a directory if there is one
    + the helper method `index_path` in the `case_directory_index_file` method constructs the path to the `index.html` file
    + here the test method checks whether the directory containing an `index.html` page and asks the request handler to handle that page
    + then lastly we a `case_directory_index_file` object is added to the Cases list in `RequestHandler`
- and a listing of the directory if there isn't.
    + This case is similar to the step above except that our test checks whether there isn't an `index.html` file, this is done in the `case_directory_no_index_file` class.
    + we add a `list_dir` method to `RequestHandler` to generate a directory listing and then we call `list_dir` from the case handlers `act` method.
 