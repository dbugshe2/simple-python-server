# Displaying Request Values

In the second version of the web server displays some of the values included in the HTTP request. To keep our code clean, the code for creating the page (`create_page()`) is seperated from the code sending it (`send_page()`)

The main body of the program is unchanged: as before, 
- it creates an instance of the `HTTPServer` class with an address and this request handler as parameters, 
- then serves requests forever. 
- If we run it and send a request from a browser for `http://localhost:8080/something.html`, we get:
    ```Date and time  Mon, 24 Feb 2014 17:17:12 GMT
    Client host    127.0.0.1
    Client port    54548
    Command        GET
    Path           /something.html
    ```

__Notice that we do not get a 404 error, even though the page something.html doesn't exist as a file on disk. That's because a web server is just a program, and can do whatever it wants when it gets a request:__