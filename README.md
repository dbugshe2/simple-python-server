# Serving Static pages

In this version, the web server serves pages from the disk instead of generating them on the fly.

- first we rewrite the do_GET() method from the previous version.
    + firt we assume that it's allowed to serve any file inside or below the directory that our server (`server.py`) is running from,
    + then to the path to the file the user wants, we find the full path (`full_path`) of the requested file by combining the path where the server is running from which is provided by`os.getcwd` with the path provided by the URL which the library automatically puts in `self.path`(and which always starts with a leading `/`)
    + if the file dosen't exist, or if it isn't a file, the method reports an error by raising and catching an exception
    + if matches a file, it calls a helper method named `handle_file()` to read and return the contents the file (this method jsut reads the file and sends it using the existing `send_content()` method to send it back to the client).
__Note: in this line `with open(full_path, 'rb') as reader:` we ar opening the file in binary mode (the 'b' in `rb`) which means that python won't alterbyte sequences that look like a windows line ending__

__also in this example we read the whole file into memory this a bad idea in real life, because the file could be very seceral gigabytes large, but that is beyond the scope of this example__