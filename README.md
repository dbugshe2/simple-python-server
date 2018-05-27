# Listing Directories

In this version, the web server will display the listing of a directory's content when the path in the URL points to a directory rather than a file.

It can also be modified to look in that directory for an index.html file to display, and only show a listing of the directory's contents if that file is not present.

But building these rules into do_GET would be a mistake, since the resulting method would be a long tangle of if statements controlling special behaviors. The right solution is to step back and solve the general problem, which is figuring out what to do with a URL. Here's a rewrite of the do_GET method:

## What has changed
- first we after figure out the full of the thing being requested(like in the previous version)
- then we loop over a set of cases stored in a list (created at the top of `RequestHandler`). Each case is an object with two methods
    + `test()` which tells us whether it able to handle the request
    + and `act()` which actually takes some action
- as soon as the right case is found, it handles the request and we break out of the loop
- There are three case classes that reproduce the behavior of our perevious server version
    + `case_no_file` - The File or directory does noto exist
    + `case_existing_file` - The File exists
    + `case_always_fail` - Base case for if nothing else works