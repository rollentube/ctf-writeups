# Memory Forensics
Verwendete Befehle:
```
vol.py -f Snapshot6.vmem --profile=Win7SP1x64 hashdump
vol.py -f Snapshot19.vmem --profile=Win7SP1x64 shutdowntime
vol.py -f Snapshot19.vmem --profile=Win7SP1x64 consoles
vol.py -f Snapshot14.vmem --profile=Win7SP1x64 truecryptpassphrase
```

## Detect Profile
Moegliche Versionen erkennen und sanity check. Vermutlich fuer alle Dumps gleich.
```
vol.py -f Snapshot6.vmem imageinfo
vol.py -f Snapshot6.vmem --profile=Win7SP1x64 kdbgscan
```

Profil scheint zu stimmen.

## Finding Userpassword (Task 1)
NTLM Hashes extrahieren
```
s6fnhart@df04:~/tryhackme$ vol.py -f Snapshot6.vmem --profile=Win7SP1x64 hashdump
Volatility Foundation Volatility Framework 2.6.1
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
John:1001:aad3b435b51404eeaad3b435b51404ee:47fbd6536d7868c873d5ea455f2fc0c9:::
HomeGroupUser$:1002:aad3b435b51404eeaad3b435b51404ee:91c34c06b7988e216c3bfeb9530cabfb:::
s6fnhart@df04:~/tryhackme$ 
```

Hash kann bspw. mit https://crackstation.net/ gecrackt werden. Das Passwort ist 'charmander999'

## Analysis (Task 2)
### Last Shutdown
Letzter Shutdown kann ausgelesen werden.
```
s6fnhart@df04:~/tryhackme$ vol.py -f Snapshot19.vmem --profile=Win7SP1x64 shutdowntime
Volatility Foundation Volatility Framework 2.6.1
Registry: SYSTEM
Key Path: ControlSet001\Control\Windows
Key Last updated: 2020-12-27 22:50:12 UTC+0000
Value Name: ShutdownTime
Value: 2020-12-27 22:50:12 UTC+0000

s6fnhart@df04:~/tryhackme$
```


### Console
Letzte Consolen Eingaben auslesen, hier kann die Flag gefunden werden.
```
s6fnhart@df04:~/tryhackme$ vol.py -f Snapshot19.vmem --profile=Win7SP1x64 consoles
Volatility Foundation Volatility Framework 2.6.1
**************************************************
ConsoleProcess: conhost.exe Pid: 2488
Console: 0xffa66200 CommandHistorySize: 50
HistoryBufferCount: 1 HistoryBufferMax: 4
OriginalTitle: %SystemRoot%\System32\cmd.exe
Title: Administrator: C:\Windows\System32\cmd.exe
AttachedProcess: cmd.exe Pid: 1920 Handle: 0x60
----
CommandHistory: 0x21e9c0 Application: cmd.exe Flags: Allocated, Reset
CommandCount: 7 LastAdded: 6 LastDisplayed: 6
FirstCommand: 0 CommandCountMax: 50
ProcessHandle: 0x60
Cmd #0 at 0x1fe3a0: cd /
Cmd #1 at 0x1f78b0: echo THM{You_found_me} > test.txt
Cmd #2 at 0x21dcf0: cls
Cmd #3 at 0x1fe3c0: cd /Users
Cmd #4 at 0x1fe3e0: cd /John
Cmd #5 at 0x21db30: dir
Cmd #6 at 0x1fe400: cd John
----
Screen 0x200f70 X:80 Y:300
Dump:

C:\>cd /Users

C:\Users>cd /John
The system cannot find the path specified.

C:\Users>dir
 Volume in drive C has no label.
 Volume Serial Number is 1602-421F

 Directory of C:\Users

12/27/2020  02:20 AM    <DIR>          .
12/27/2020  02:20 AM    <DIR>          ..
12/27/2020  02:21 AM    <DIR>          John
04/12/2011  08:45 AM    <DIR>          Public
               0 File(s)              0 bytes
               4 Dir(s)  54,565,433,344 bytes free

C:\Users>cd John

C:\Users\John>
s6fnhart@df04:~/tryhackme$
```

## Truecrypt (Task 3)
Kennwort kann ausgelesen werden.
```
s6fnhart@df04:~/tryhackme$ vol.py -f Snapshot14.vmem --profile=Win7SP1x64 truecryptpassphrase
Volatility Foundation Volatility Framework 2.6.1
Found at 0xfffff8800512bee4 length 11: forgetmenot
s6fnhart@df04:~/tryhackme$
```

