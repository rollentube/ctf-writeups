# chrono
How to automate tasks to run at intervals on linux servers? (100 Points)
Additional details will be available after launching your challenge instance.

## Solution
Looking for cronjobs since it is the most common way to automate task under linux. Here you can find the flag.
```
[root@picoctf ~]$ ssh -p 60163 picoplayer@saturn.picoctf.net

picoplayer@saturn.picoctf.net's password:
[...]
picoplayer@challenge:~$ ls -al
total 12
drwxr-xr-x 1 picoplayer picoplayer   20 Mar 15 11:01 .
drwxr-xr-x 1 root       root         24 Mar 15 02:28 ..
-rw-r--r-- 1 picoplayer picoplayer  220 Feb 25  2020 .bash_logout
-rw-r--r-- 1 picoplayer picoplayer 3771 Feb 25  2020 .bashrc
drwx------ 2 picoplayer picoplayer   34 Mar 15 11:01 .cache
-rw-r--r-- 1 picoplayer picoplayer  807 Feb 25  2020 .profile
picoplayer@challenge:~$ crontab -l
no crontab for picoplayer
picoplayer@challenge:~$ ls -al /etc/cron
cron.d/       cron.daily/   cron.hourly/  cron.monthly/ cron.weekly/  crontab
picoplayer@challenge:~$ ls -al /etc/crontab
-rw-r--r-- 1 root root 43 Mar 15 02:28 /etc/crontab
picoplayer@challenge:~$ cat /etc/crontab
# picoCTF{Sch3DUL7NG_T45K3_L1NUX_72d4f32d}
picoplayer@challenge:~$ Connection to saturn.picoctf.net closed by remote host.
Connection to saturn.picoctf.net closed.
[root@picoctf ~]$
```
