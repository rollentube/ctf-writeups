# Forensic
## Volatility forensics (Task 1)
OS erkennen:
```
s6fnhart@df04:~/tryhackme$ vol.py -f victim.raw imageinfo
Volatility Foundation Volatility Framework 2.6.1
INFO    : volatility.debug    : Determining profile based on KDBG search...
          Suggested Profile(s) : Win7SP1x64, Win7SP0x64, Win2008R2SP0x64, Win2008R2SP1x64_24000, Win2008R2SP1x64_23418, Win2008R2SP1x64, Win7SP1x64_24000, Win7SP1x64_23418
                     AS Layer1 : WindowsAMD64PagedMemory (Kernel AS)
                     AS Layer2 : FileAddressSpace (/home/s6fnhart/tryhackme/victim.raw)
                      PAE type : No PAE
                           DTB : 0x187000L
                          KDBG : 0xf800028420a0L
          Number of Processors : 1
     Image Type (Service Pack) : 1
                KPCR for CPU 0 : 0xfffff80002843d00L
             KUSER_SHARED_DATA : 0xfffff78000000000L
           Image date and time : 2019-05-02 18:11:45 UTC+0000
     Image local date and time : 2019-05-02 11:11:45 -0700
s6fnhart@df04:~/tryhackme$
```

Prozess identifizieren:
```
s6fnhart@df04:~/tryhackme$ vol.py -f victim.raw --profile=Win7SP1x64 pslist | grep -i searchindexer
Volatility Foundation Volatility Framework 2.6.1
0xfffffa8003367060 SearchIndexer.         2180    504     11      629      0      0 2019-05-02 18:03:32 UTC+0000
s6fnhart@df04:~/tryhackme$
```

Das zuletzt verwendetes Verzeichnis kann mit Shellbags erkannt werden. Allerdings handelt es sich hierbei um Verzeichnisse, welche ueber die GUI aufgerufen wurden.

```
s6fnhart@df04:~/tryhackme$ vol.py -f victim.raw --profile=Win7SP1x64 shellbags | grep DIR | grep 2019-04-27
2       1     PROGRA~2       2019-04-27 10:27:26 UTC+0000   2009-07-14 03:20:10 UTC+0000   2019-04-27 10:27:26 UTC+0000   RO, DIR                   C:\Program Files (x86)
0       0     logs           2019-04-27 10:38:22 UTC+0000   2019-04-27 10:38:22 UTC+0000   2019-04-27 10:38:22 UTC+0000   NI, DIR                   Z:\logs
0       0     Capture        2019-04-27 10:36:06 UTC+0000   2019-04-18 00:49:00 UTC+0000   2019-04-27 10:36:06 UTC+0000   DIR                       C:\Program Files (x86)\Capture
0       0     deleted_files  2019-04-27 10:30:26 UTC+0000   2019-04-27 10:38:24 UTC+0000   2019-04-27 10:38:24 UTC+0000   NI, DIR                   Z:\logs\deleted_files
3       1     TCD9405.tmp    2019-04-27 10:33:16 UTC+0000   2019-04-27 10:33:16 UTC+0000   2019-04-27 10:33:16 UTC+0000   NI, DIR                   Local\Temp\TCD9405.tmp
4       0     TCD9312.tmp    2019-04-27 10:33:16 UTC+0000   2019-04-27 10:33:16 UTC+0000   2019-04-27 10:33:16 UTC+0000   NI, DIR                   Local\Temp\TCD9312.tmp
s6fnhart@df04:~/tryhackme$
```

## Task 2
Suspicious open ports
```
s6fnhart@df04:~/tryhackme$ vol.py -f victim.raw --profile=Win7SP1x64 netscan
Volatility Foundation Volatility Framework 2.6.1
Offset(P)          Proto    Local Address                  Foreign Address      State            Pid      Owner          Created
0x5c201ca0         UDPv4    0.0.0.0:5005                   *:*                                   2464     wmpnetwk.exe   2019-05-02 18:05:14 UTC+0000
0x5c201ca0         UDPv6    :::5005                        *:*                                   2464     wmpnetwk.exe   2019-05-02 18:05:14 UTC+0000
0x5c49cbb0         UDPv4    0.0.0.0:59471                  *:*                                   1368     svchost.exe    2019-05-02 18:03:06 UTC+0000
0x5c4a31c0         UDPv4    0.0.0.0:59472                  *:*                                   1368     svchost.exe    2019-05-02 18:03:06 UTC+0000
[...]
```

Mit Malfind koennen solche Prozesse ausfindig gemacht werden. Diese Prozesse duerften diese Berechtigung nicht haben (PAGE\_EXECUTE\_READWRITE - Enables execute, read-only, or read/write access to the committed region of pages.)
```
s6fnhart@df04:~/tryhackme$ vol.py -f victim.raw --profile=Win7SP1x64 malfind
Volatility Foundation Volatility Framework 2.6.1
Process: explorer.exe Pid: 1860 Address: 0x3ee0000
Vad Tag: VadS Protection: PAGE_EXECUTE_READWRITE
Flags: CommitCharge: 1, MemCommit: 1, PrivateMemory: 1, Protection: 6

0x0000000003ee0000  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
0x0000000003ee0010  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
0x0000000003ee0020  00 00 ee 03 00 00 00 00 00 00 00 00 00 00 00 00   ................
0x0000000003ee0030  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................

0x0000000003ee0000 0000             ADD [EAX], AL
0x0000000003ee0002 0000             ADD [EAX], AL
[...]
```

### 1.2 Detecting Injected Code Using VAD (virtual address descriptor)

An important point to note is that when an executable image (such as EXE or DLL) is normally loaded into the memory, that memory region is given a memory protection of PAGE\_EXECUTE\_WRITECOPY(WCX) by the operating system. An application is generally not allowed to allocate a memory with PAGE\_EXECUTE\_WRITECOPY protection using an API call such as VirtualAllocEx. In other words, if an attacker wants to inject a PE file (such as EXE or DLL) or shellcode, then a memory with a PAGE\_EXECUTE\_READWRITE(RWX) protection needs be allocated. Normally, you will see that very few memory ranges have a memory protection of PAGE\_EXECUTE\_READWRITE. A memory range having a protection of PAGE\_EXECUTE\_READWRITE is not always ...

## IOC SAGA (Task 3)
Grepping for Domains
```
s6fnhart@df04:~/tryhackme$ strings -n 10 victim.raw | grep www.go.....ru
www.google.ru
www.go4win.ru
www.gocaps.ru
www.goporn.ru
      <URL>http://www.google.ru/</URL>
s6fnhart@df04:~/tryhackme$ strings -n 10 victim.raw | grep www.i.....com
http://www.iciba.com/search?s=%si
www.ikaka.com
s6fnhart@df04:~/tryhackme$ strings -n 10 victim.raw | grep www.ic.......com
www.icsalabs.com
s6fnhart@df04:~/tryhackme$
```

Grepping for IPs
```
s6fnhart@df04:~/tryhackme$ strings -n 10 victim.raw | grep 202.....233
202.107.233.211
s6fnhart@df04:~/tryhackme$ strings -n 10 victim.raw | grep ....200....164
phttp://209.200.12.164/drm/provider_license_v7.php
s6fnhart@df04:~/tryhackme$ strings -n 10 victim.raw | grep 209.190........
`http://209.190.122.186/drm/license-savenow.asp
s6fnhart@df04:~/tryhackme$
```

What is the unique environmental variable of PID 2464?
```
s6fnhart@df04:~/tryhackme$ vol.py -f victim.raw --profile=Win7SP1x64 envars --pid 2464
Volatility Foundation Volatility Framework 2.6.1
Pid      Process              Block              Variable                       Value
-------- -------------------- ------------------ ------------------------------ -----
[...]
    2464 wmpnetwk.exe         0x00000000002c47a0 OANOCACHE                      1
[...]
s6fnhart@df04:~/tryhackme$
```
