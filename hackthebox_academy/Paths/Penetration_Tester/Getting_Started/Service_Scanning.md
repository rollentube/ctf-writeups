# Service Scanning
## Nmap
Nmap is a tool to scan a target system for open ports.

The default execution scans the first 1023 TCP ports.
```
rollentube@htb[/htb]$ nmap 10.129.42.253

Starting Nmap 7.80 ( https://nmap.org ) at 2021-02-25 16:07 EST
Nmap scan report for 10.129.42.253
Host is up (0.11s latency).
Not shown: 995 closed ports
PORT    STATE SERVICE
21/tcp  open  ftp
22/tcp  open  ssh
80/tcp  open  http
139/tcp open  netbios-ssn
445/tcp open  microsoft-ds

Nmap done: 1 IP address (1 host up) scanned in 2.19 seconds
```

Other Nmap examples:
```
nmap -sV -sC -p- 10.129.42.253
```
* `-sV` performs version scan
* `-sC` uses default scripts for more information
* `-p-` scans all ports

We can also use more Nmap scripts or write our own one and use them. For example, nmap has the following citrix scripts pre-installed:
```
rollentube@htb[/htb]$ locate scripts/citrix

/usr/share/nmap/scripts/citrix-brute-xml.nse
/usr/share/nmap/scripts/citrix-enum-apps-xml.nse
/usr/share/nmap/scripts/citrix-enum-apps.nse
/usr/share/nmap/scripts/citrix-enum-servers-xml.nse
/usr/share/nmap/scripts/citrix-enum-servers.nse
```

To use a specific script:
```
nmap --script <script name> -p<port> <host>
```

## Attacking Network Services
### Banner Grabbing
```
nmap -sV --script=banner <target>
nmap -sV --script=banner -p21 10.10.10.0/24
```
```
nc -nv 10.129.42.253 21
```

### FTP
The Nmap scripts also tries anonymous for ftp servers. Once logged in we can use several ftp commands:
```
$ ftp -p 10.129.42.253

Connected to 10.129.42.253.
220 (vsFTPd 3.0.3)
Name (10.129.42.253:user): anonymous
230 Login successful.
```
```
ls
cd pub
get login.txt
```

### SMB
Server Message Block (SMB) is protocol for file shares on Windows machines (Linux can also use it). SMB is pretty important since it provides many vectors for lateral movement, providing sensitive data or even may be vulnerable.

With Nmap we can scan the service for more information
```
nmap --script smb-os-discovery.nse -p445 10.10.10.40
```
```
nmap -A -p445 10.129.42.253
```
* `-A` enable OS and version detection, script scanning and traceroute

### Shares
The shared files and folders by SMB can be enumerated with tools like `smbclient`:
```
smbclient -N -L \\\\10.129.42.253
```
* `-N` suppresses the password prompt
* `-L` retrieve a list of available shares

If we want to access a specific share as a user we can use the following:
```
smbclient -U bob \\\\10.129.42.253\\users
```

Once connected we can list the directory with `ls`.

### SNMP
Simple Network Management Protocol (SNMP) Community strings provide information and statistics about a router or device, helping us gain access to it. The manufacturer default community strings of public and private are often unchanged. In SNMP versions 1 and 2c, access is controlled using a plaintext community string, and if we know the name, we can gain access to it. Encryption and authentication were only added in SNMP version 3.

SNMP could reveal useful information like credentials, routing information, services bound to additional interfaces or the version of installed software.

We can enumerate the public and private strings:
```
rollentube@htb[/htb]$ snmpwalk -v 2c -c public 10.129.42.253 1.3.6.1.2.1.1.5.0

iso.3.6.1.2.1.1.5.0 = STRING: "gs-svcscan"
```
```
rollentube@htb[/htb]$ snmpwalk -v 2c -c private  10.129.42.253 

Timeout: No Response from 10.129.42.253
```

[onesixtyone](https://github.com/trailofbits/onesixtyone) is a SNMP scanner, that can be uesed to brute force the community string names with a wordlist:
```
rollentube@htb[/htb]$ onesixtyone -c dict.txt 10.129.42.254

Scanning 1 hosts, 51 communities
10.129.42.254 [public] Linux gs-svcscan 5.4.0-66-generic #74-Ubuntu SMP Wed Jan 27 22:54:38 UTC 2021 x86_64
```

## Questions
Answer the question(s) below to complete this Section and earn cubes!

```
Target: 10.129.224.200 
Life Left: 118 minutes 
```

Perform a Nmap scan of the target. What is the version of the service from the Nmap scan running on port 8080?
```
> Apache Tomcat
```
```
$ nmap -sC -sV -p8080 10.129.224.200
Starting Nmap 7.94 ( https://nmap.org ) at 2023-10-11 11:25 EDT
Nmap scan report for 10.129.224.200
Host is up (0.032s latency).

PORT     STATE SERVICE VERSION
8080/tcp open  http    Apache Tomcat
|_http-open-proxy: Proxy might be redirecting requests
|_http-title: Apache Tomcat

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 20.70 seconds
```

Perform an Nmap scan of the target and identify the non-default port that the telnet service is running on.
```
> 2323
```
```
$ nmap -sC -sV 10.129.224.200
Starting Nmap 7.94 ( https://nmap.org ) at 2023-10-11 11:38 EDT
Nmap scan report for 10.129.224.200
Host is up (0.030s latency).
Not shown: 993 closed tcp ports (conn-refused)
PORT     STATE SERVICE     VERSION
21/tcp   open  ftp         vsftpd 3.0.3
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.10.14.119
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
|_drwxr-xr-x    2 ftp      ftp          4096 Feb 25  2021 pub
22/tcp   open  ssh         OpenSSH 8.2p1 Ubuntu 4ubuntu0.1 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 a0:01:d7:79:e9:d2:09:2a:b8:d9:b4:9a:6c:00:0c:1c (RSA)
|   256 2b:99:b2:1f:ec:1a:5a:c6:b7:be:b5:50:d1:0e:a9:df (ECDSA)
|_  256 e4:f8:17:8d:d4:71:d1:4e:d4:0e:bd:f0:29:4f:6d:14 (ED25519)
80/tcp   open  http        Apache httpd 2.4.41 ((Ubuntu))
|_http-title: PHP 7.4.3 - phpinfo()
|_http-server-header: Apache/2.4.41 (Ubuntu)
139/tcp  open  netbios-ssn Samba smbd 4.6.2
445/tcp  open  netbios-ssn Samba smbd 4.6.2
2323/tcp open  telnet      Linux telnetd
8080/tcp open  http        Apache Tomcat
|_http-open-proxy: Proxy might be redirecting requests
|_http-title: Apache Tomcat
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2023-10-11T15:38:57
|_  start_date: N/A
|_nbstat: NetBIOS name: GS-SVCSCAN, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 43.16 seconds
```

List the SMB shares available on the target host. Connect to the available share as the bob user. Once connected, access the folder called 'flag' and submit the contents of the flag.txt file.
```
> dceece590f3284c3866305eb2473d099
```
```
$ smbclient -N -L \\\\10.129.224.200                    

        Sharename       Type      Comment
        ---------       ----      -------
        print$          Disk      Printer Drivers
        users           Disk      
        IPC$            IPC       IPC Service (gs-svcscan server (Samba, Ubuntu))
Reconnecting with SMB1 for workgroup listing.
smbXcli_negprot_smb1_done: No compatible protocol selected by server.
protocol negotiation failed: NT_STATUS_INVALID_NETWORK_RESPONSE
Unable to connect with SMB1 -- no workgroup available
                                                                                                                                                           
┌──(kali㉿kali)-[~]
└─$ smbclient -U bob \\\\10.129.224.200\\users            
Password for [WORKGROUP\bob]:
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Thu Feb 25 18:06:52 2021
  ..                                  D        0  Thu Feb 25 15:05:31 2021
  flag                                D        0  Thu Feb 25 18:09:26 2021
  bob                                 D        0  Thu Feb 25 16:42:23 2021

                4062912 blocks of size 1024. 1124724 blocks available
smb: \> cd flag\
smb: \flag\> ls
  .                                   D        0  Thu Feb 25 18:09:26 2021
  ..                                  D        0  Thu Feb 25 18:06:52 2021
  flag.txt                            N       33  Thu Feb 25 18:09:26 2021

                4062912 blocks of size 1024. 1124720 blocks available
smb: \flag\> get flag.txt 
getting file \flag\flag.txt of size 33 as flag.txt (0.3 KiloBytes/sec) (average 0.3 KiloBytes/sec)
smb: \flag\> 
```
```
$ cat flag.txt            
dceece590f3284c3866305eb2473d099
```