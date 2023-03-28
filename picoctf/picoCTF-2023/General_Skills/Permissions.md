# Permissions
Can you read files in the root file? (100 Points)
Additional details will be available after launching your challenge instance.

## Solution
If you inspect the filesystem root you can find a folder called 'challenge'. In here is a file called 'metadata.json'. You can read this out with every tool you want and find the flag inside
```
[root@picoctf ~]$ ssh -p 61297 picoplayer@saturn.picoctf.net
[...]
picoplayer@challenge:~$ ls -al
total 16
drwxr-xr-x 1 picoplayer picoplayer   36 Mar 15 10:50 .
drwxr-xr-x 1 root       root         24 Mar 15 02:46 ..
-rw-r--r-- 1 picoplayer picoplayer  220 Feb 25  2020 .bash_logout
-rw-r--r-- 1 picoplayer picoplayer 3771 Feb 25  2020 .bashrc
drwx------ 2 picoplayer picoplayer   34 Mar 15 10:48 .cache
-rw-r--r-- 1 picoplayer picoplayer  807 Feb 25  2020 .profile
-rw------- 1 picoplayer picoplayer  744 Mar 15 10:50 .viminfo
picoplayer@challenge:~$ ls -al /
total 0
drwxr-xr-x    1 root   root     51 Mar 15 10:48 .
drwxr-xr-x    1 root   root     51 Mar 15 10:48 ..
-rwxr-xr-x    1 root   root      0 Mar 15 10:48 .dockerenv
lrwxrwxrwx    1 root   root      7 Mar  1 02:03 bin -> usr/bin
drwxr-xr-x    2 root   root      6 Apr 15  2020 boot
drwxr-xr-x    1 root   root     21 Mar 15 02:46 challenge
drwxr-xr-x    5 root   root    340 Mar 15 10:48 dev
drwxr-xr-x    1 root   root     66 Mar 15 10:48 etc
drwxr-xr-x    1 root   root     24 Mar 15 02:46 home
lrwxrwxrwx    1 root   root      7 Mar  1 02:03 lib -> usr/lib
lrwxrwxrwx    1 root   root      9 Mar  1 02:03 lib32 -> usr/lib32
lrwxrwxrwx    1 root   root      9 Mar  1 02:03 lib64 -> usr/lib64
lrwxrwxrwx    1 root   root     10 Mar  1 02:03 libx32 -> usr/libx32
drwxr-xr-x    2 root   root      6 Mar  1 02:03 media
drwxr-xr-x    2 root   root      6 Mar  1 02:03 mnt
drwxr-xr-x    2 root   root      6 Mar  1 02:03 opt
dr-xr-xr-x 4641 nobody nogroup   0 Mar 15 10:48 proc
drwx------    1 root   root     23 Mar 15 02:46 root
drwxr-xr-x    1 root   root     66 Mar 15 10:56 run
lrwxrwxrwx    1 root   root      8 Mar  1 02:03 sbin -> usr/sbin
drwxr-xr-x    2 root   root      6 Mar  1 02:03 srv
dr-xr-xr-x   13 nobody nogroup   0 Mar 15 10:48 sys
drwxrwxrwt    1 root   root      6 Mar 15 02:46 tmp
drwxr-xr-x    1 root   root     18 Mar  1 02:03 usr
drwxr-xr-x    1 root   root     28 Mar  1 02:06 var
picoplayer@challenge:~$ ls -al /challenge/
total 4
drwxr-xr-x 1 root root 21 Mar 15 02:46 .
drwxr-xr-x 1 root root 51 Mar 15 10:48 ..
-rw-r--r-- 1 root root 98 Mar 15 02:46 metadata.json
picoplayer@challenge:~$ cat /challenge/metadata.json
{"flag": "picoCTF{uS1ng_v1m_3dit0r_580c4b47}", "username": "picoplayer", "password": "cPC09LVcyM"}picoplayer@challenge:~$ Connection to saturn.picoctf.net closed by remote host.
Connection to saturn.picoctf.net closed.
[root@picoctf ~]$
```
