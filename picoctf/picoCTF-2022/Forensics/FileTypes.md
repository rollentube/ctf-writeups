# File types
This file was found among some files marked confidential but my pdf reader cannot read it, maybe yours can.

## Loesung
Bei der Datei handelt es sich um ein Shell Archive. Diese kann entpackt werden indem man es mit 'sh' aufruft. Danach entspinnt sich ein Decompressing mit verschiedensten Archiv Dateien. Einige mussten nachinstalliert werden. **MANCHE TOOLS ERWARTEN EINE BESTIMMTE DATEIENDUNG DES ARCHIVS**. Ansonsten wirft die Dekomprimierung einen Fehler. Am Ende erhaelt man zwei Zeichenketten, welche mit cyberchef 'Magic' geloest werden koennen. Diese ergeben dann die Flag.

Die Algorithmen waren:
- sh
- ar
- cpio
- bzip2
- gzip
- lzip
- LZ4
- LZMA
- lzop
- lzip
- lzop
- lzip
- XZ
- Hex/Base (Cyberchef)

Die Flag lautet: picoCTF{f1len@m3\_m@n1pul@t10n\_f0r\_0b2cur17y\_3c79c5ba}


Konsolenausgabe waehrend der Analyse:
```
 root  …  picoctf  writeups  picoCTF-2022  file Flag.pdf
Flag.pdf: shell archive text
 root  …  picoctf  writeups  picoCTF-2022  exiftool Flag.pdf
ExifTool Version Number         : 12.50
File Name                       : Flag.pdf
Directory                       : .
File Size                       : 5.2 kB
File Modification Date/Time     : 2023:02:09 00:15:15+01:00
File Access Date/Time           : 2023:02:09 00:15:46+01:00
File Inode Change Date/Time     : 2023:02:09 00:15:44+01:00
File Permissions                : -rw-r--r--
File Type                       : sh script
File Type Extension             : sh
MIME Type                       : text/x-sh
 root  …  picoctf  writeups  picoCTF-2022  vim Flag.pdf
 root  …  picoctf  writeups  picoCTF-2022  sh Flag.pdf
egrep: warning: egrep is obsolescent; using grep -E
x - created lock directory _sh00046.
x - extracting flag (text)
Flag.pdf: line 119: uudecode: command not found
restore of flag failed
flag: MD5 check failed
x - removed lock directory _sh00046.
 root  …  picoctf  writeups  picoCTF-2022  vim Flag.pdf
 root  …  picoctf  writeups  picoCTF-2022  cp Flag.pdf Flag.sh
 root  …  picoctf  writeups  picoCTF-2022  ./Fl
-bash: ./Fl: No such file or directory
 root  …  picoctf  writeups  picoCTF-2022  chmod +x Flag.sh
 root  …  picoctf  writeups  picoCTF-2022  ./Flag.sh
egrep: warning: egrep is obsolescent; using grep -E
x - created lock directory _sh00046.
x - extracting flag (text)
./Flag.sh: line 119: uudecode: command not found
restore of flag failed
flag: MD5 check failed
x - removed lock directory _sh00046.
 root  …  picoctf  writeups  picoCTF-2022  
 root  …  picoctf  writeups  picoCTF-2022  ./Flag.sh
egrep: warning: egrep is obsolescent; using grep -E
x - created lock directory _sh00046.
x - extracting flag (text)
./Flag.sh: line 119: uudecode: command not found
restore of flag failed
flag: MD5 check failed
x - removed lock directory _sh00046.
 root  …  picoctf  writeups  picoCTF-2022  ls -al
total 36
drwxr-xr-x 5 root users 4096 Feb  9 00:17 .
drwxr-xr-x 3 root users 4096 Feb  8 23:30 ..
drwxr-xr-x 2 root users 4096 Feb  9 00:00 basic-file-exploit
drwxr-xr-x 2 root users 4096 Feb  9 00:05 file-run
-rw-r--r-- 1 root users 5161 Feb  9 00:15 Flag.pdf
-rwxr-xr-x 1 root users 5161 Feb  9 00:17 Flag.sh
drwxr-xr-x 2 root users 4096 Feb  9 00:14 GDBTestDrive
 root  …  picoctf  writeups  picoCTF-2022  vim Flag.sh
 root  …  picoctf  writeups  picoCTF-2022  strings Flag.sh | less
 root  …  picoctf  writeups  picoCTF-2022  
 root  …  picoctf  writeups  picoCTF-2022  
 root  …  picoctf  writeups  picoCTF-2022  
 root  …  picoctf  writeups  picoCTF-2022  pacman -Ss uudecode
 root  …  picoctf  writeups  picoCTF-2022  uu                                                                                                    1 
uuclient   uuidd      uuidgen    uuidparse  uuserver
 root  …  picoctf  writeups  picoCTF-2022  uu                                                                                                    1 
uuclient   uuidd      uuidgen    uuidparse  uuserver
 root  …  picoctf  writeups  picoCTF-2022  pacman -Ss sharutils
extra/sharutils 4.15.2-4
    Makes so-called shell archives out of many files
 root  …  picoctf  writeups  picoCTF-2022  sudo pacman -S sharutils
[sudo] password for root:
resolving dependencies...
looking for conflicting packages...

Packages (1) sharutils-4.15.2-4

Total Download Size:   0.27 MiB
Total Installed Size:  1.28 MiB

:: Proceed with installation? [Y/n] y
:: Retrieving packages...
 sharutils-4.15.2-4-x86_64                                         275.2 KiB  2.32 MiB/s 00:00 [########################################################] 100%
(1/1) checking keys in keyring                                                                 [########################################################] 100%
(1/1) checking package integrity                                                               [########################################################] 100%
(1/1) loading package files                                                                    [########################################################] 100%
(1/1) checking for file conflicts                                                              [########################################################] 100%
(1/1) checking available disk space                                                            [########################################################] 100%
:: Processing package changes...
(1/1) installing sharutils                                                                     [########################################################] 100%
:: Running post-transaction hooks...
(1/2) Arming ConditionNeedsUpdate...
(2/2) Updating the info directory file...
 root  …  picoctf  writeups  picoCTF-2022  ./Flag.sh
egrep: warning: egrep is obsolescent; using grep -E
x - created lock directory _sh00046.
x - extracting flag (text)
x - removed lock directory _sh00046.
 root  …  picoctf  writeups  picoCTF-2022  ls -al
total 40
drwxr-xr-x 5 root users 4096 Feb  9 00:19 .
drwxr-xr-x 3 root users 4096 Feb  8 23:30 ..
drwxr-xr-x 2 root users 4096 Feb  9 00:00 basic-file-exploit
drwxr-xr-x 2 root users 4096 Feb  9 00:05 file-run
-rw-r--r-- 1 root users 1092 Mar 15  2022 flag
-rw-r--r-- 1 root users 5161 Feb  9 00:15 Flag.pdf
-rwxr-xr-x 1 root users 5161 Feb  9 00:17 Flag.sh
drwxr-xr-x 2 root users 4096 Feb  9 00:14 GDBTestDrive
 root  …  picoctf  writeups  picoCTF-2022  cat flag
!<arch>
flag/           0           0     0     644     1024      `
ih ѣ##'SGzѨrш@4@hb0C@1F=_@{O}ѦM4M
"<M)hVτHIW8"'f0D!xr_fT  h4ª~ѣMb@4h#G@@S&

1'ÅO{ojK51]<T[s-!ΥA2'͛$:eP/9>}pKb&q['
Z3##Ŏ.p!,q      EX?AX%-Ó.x<G.%i"+vCBx`IX!vۮn")4$>#By
          TRAILER!!! root  …  picoctf  writeups  picoCTF-2022  file flag
flag: current ar archive
 root  …  picoctf  writeups  picoCTF-2022  
 root  …  picoctf  writeups  picoCTF-2022  
 root  …  picoctf  writeups  picoCTF-2022  file flag
flag: current ar archive
 root  …  picoctf  writeups  picoCTF-2022  binwalk flag

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
100           0x64            bzip2 compressed data, block size = 900k

 root  …  picoctf  writeups  picoCTF-2022  nautilus .
** Message: 00:19:58.077: Connecting to org.freedesktop.Tracker3.Miner.Files



^C
 root  …  picoctf  writeups  picoCTF-2022                                                                                                   SIGINT 
 root  …  picoctf  writeups  picoCTF-2022  ls -al                                                                                           SIGINT 
total 40
drwxr-xr-x 5 root users 4096 Feb  9 00:19 .
drwxr-xr-x 3 root users 4096 Feb  8 23:30 ..
drwxr-xr-x 2 root users 4096 Feb  9 00:00 basic-file-exploit
drwxr-xr-x 2 root users 4096 Feb  9 00:05 file-run
-rw-r--r-- 1 root users 1092 Mar 15  2022 flag
-rw-r--r-- 1 root users 5161 Feb  9 00:15 Flag.pdf
-rwxr-xr-x 1 root users 5161 Feb  9 00:17 Flag.sh
drwxr-xr-x 2 root users 4096 Feb  9 00:14 GDBTestDrive
 root  …  picoctf  writeups  picoCTF-2022  rm -rf flag
 root  …  picoctf  writeups  picoCTF-2022  sh Flag.
sh: Flag.: No such file or directory
 root  …  picoctf  writeups  picoCTF-2022  sh Flag.pdf
egrep: warning: egrep is obsolescent; using grep -E
x - created lock directory _sh00046.
x - extracting flag (text)
x - removed lock directory _sh00046.
 root  …  picoctf  writeups  picoCTF-2022  ls -al
total 40
drwxr-xr-x 5 root users 4096 Feb  9 00:20 .
drwxr-xr-x 3 root users 4096 Feb  8 23:30 ..
drwxr-xr-x 2 root users 4096 Feb  9 00:00 basic-file-exploit
drwxr-xr-x 2 root users 4096 Feb  9 00:05 file-run
-rw-r--r-- 1 root users 1092 Mar 15  2022 flag
-rw-r--r-- 1 root users 5161 Feb  9 00:15 Flag.pdf
-rwxr-xr-x 1 root users 5161 Feb  9 00:17 Flag.sh
drwxr-xr-x 2 root users 4096 Feb  9 00:14 GDBTestDrive
 root  …  picoctf  writeups  picoCTF-2022  cat flag
!<arch>
flag/           0           0     0     644     1024      `
ih ѣ##'SGzѨrш@4@hb0C@1F=_@{O}ѦM4M
"<M)hVτHIW8"'f0D!xr_fT  h4ª~ѣMb@4h#G@@S&

1'ÅO{ojK51]<T[s-!ΥA2'͛$:eP/9>}pKb&q['
Z3##Ŏ.p!,q      EX?AX%-Ó.x<G.%i"+vCBx`IX!vۮn")4$>#By
          TRAILER!!! root  …  picoctf  writeups  picoCTF-2022  strings flag
 root  …  picoctf  writeups  picoCTF-2022  strings flag
!<arch>
flag/           0           0     0     644     1024      `
0b<7
flag
BZh91AY&SY
"'f0
jK#K
Kb&I
EX?AX%
vCBx
TRAILER!!!
 root  …  picoctf  writeups  picoCTF-2022  hexdump -C flag | less
 root  …  picoctf  writeups  picoCTF-2022  vim Flag.sh
 root  …  picoctf  writeups  picoCTF-2022  
 root  …  picoctf  writeups  picoCTF-2022  sh Flag.sh
egrep: warning: egrep is obsolescent; using grep -E
x - created lock directory _sh00046.
x - SKIPPING flag (file already exists)
x - removed lock directory _sh00046.
 root  …  picoctf  writeups  picoCTF-2022  file flag
flag: current ar archive
 root  …  picoctf  writeups  picoCTF-2022  ar
ar                          arm-none-eabi-ar            arm-none-eabi-gcc-nm        arm-none-eabi-objcopy       arptables
arandr                      arm-none-eabi-as            arm-none-eabi-gcc-ranlib    arm-none-eabi-objdump       arptables-nft
arara                       arm-none-eabi-c++           arm-none-eabi-gcov          arm-none-eabi-ranlib        arptables-nft-restore
archlinux-java              arm-none-eabi-c++filt       arm-none-eabi-gcov-dump     arm-none-eabi-readelf       arptables-nft-save
archlinux-keyring-wkd-sync  arm-none-eabi-cpp           arm-none-eabi-gcov-tool     arm-none-eabi-size          arptables-restore
arch-meson                  arm-none-eabi-dwp           arm-none-eabi-gprof         arm-none-eabi-strings       arptables-save
arecord                     arm-none-eabi-elfedit       arm-none-eabi-ld            arm-none-eabi-strip         aruba2john
arecordmidi                 arm-none-eabi-g++           arm-none-eabi-ld.bfd        arp
argon2                      arm-none-eabi-gcc           arm-none-eabi-ld.gold       arpaname
arlatex                     arm-none-eabi-gcc-12.2.0    arm-none-eabi-lto-dump      arpd
arm-none-eabi-addr2line     arm-none-eabi-gcc-ar        arm-none-eabi-nm            arping
 root  …  picoctf  writeups  picoCTF-2022  ar --help
 root  …  picoctf  writeups  picoCTF-2022  ar --help
Usage: ar [emulation options] [-]{dmpqrstx}[abcDfilMNoOPsSTuvV] [--plugin <name>] [member-name] [count] archive-file file...
       ar -M [<mri-script]
 commands:
  d            - delete file(s) from the archive
  m[ab]        - move file(s) in the archive
  p            - print file(s) found in the archive
  q[f]         - quick append file(s) to the archive
  r[ab][f][u]  - replace existing or insert new file(s) into the archive
  s            - act as ranlib
  t[O][v]      - display contents of the archive
  x[o]         - extract file(s) from the archive
 command specific modifiers:
  [a]          - put file(s) after [member-name]
  [b]          - put file(s) before [member-name] (same as [i])
  [D]          - use zero for timestamps and uids/gids (default)
  [U]          - use actual timestamps and uids/gids
  [N]          - use instance [count] of name
  [f]          - truncate inserted file names
  [P]          - use full path names when matching
  [o]          - preserve original dates
  [O]          - display offsets of files in the archive
  [u]          - only replace files that are newer than current archive contents
 generic modifiers:
  [c]          - do not warn if the library had to be created
  [s]          - create an archive index (cf. ranlib)
  [l <text> ]  - specify the dependencies of this library
  [S]          - do not build a symbol table
  [T]          - deprecated, use --thin instead
  [v]          - be verbose
  [V]          - display the version number
  @<file>      - read options from <file>
  --target=BFDNAME - specify the target object format as BFDNAME
  --output=DIRNAME - specify the output directory for extraction operations
  --record-libdeps=<text> - specify the dependencies of this library
  --thin       - make a thin archive
 optional:
  --plugin <p> - load the specified plugin
 emulation options:
  No emulation specific options
ar: supported targets: elf64-x86-64 elf32-i386 elf32-iamcu elf32-x86-64 pei-i386 pe-x86-64 pei-x86-64 elf64-little elf64-big elf32-little elf32-big pe-bigobj-x86-64 pe-i386 pdb elf64-bpfle elf64-bpfbe srec symbolsrec verilog tekhex binary ihex plugin
Report bugs to <https://bugs.archlinux.org/>
 root  …  picoctf  writeups  picoCTF-2022  ar p flag
 root  …  picoctf  writeups  picoCTF-2022  ar p flag
ih ѣ##'SGzѨrш@4@hb0C@1F=_@{O}ѦM4M
"<M)hVτHIW8"'f0D!xr_fT  h4ª~ѣMb@4h#G@@S&

1'ÅO{ojK51]<T[s-!ΥA2'͛$:eP/9>}pKb&q['
Z3##Ŏ.p!,q      EX?AX%-Ó.x<G.%i"+vCBx`IX!vۮn")4$>#By
          TRAILER!!! root  …  picoctf  writeups  picoCTF-2022  
 root  …  picoctf  writeups  picoCTF-2022  
 root  …  picoctf  writeups  picoCTF-2022  ar --help
Usage: ar [emulation options] [-]{dmpqrstx}[abcDfilMNoOPsSTuvV] [--plugin <name>] [member-name] [count] archive-file file...
       ar -M [<mri-script]
 commands:
  d            - delete file(s) from the archive
  m[ab]        - move file(s) in the archive
  p            - print file(s) found in the archive
  q[f]         - quick append file(s) to the archive
  r[ab][f][u]  - replace existing or insert new file(s) into the archive
  s            - act as ranlib
  t[O][v]      - display contents of the archive
  x[o]         - extract file(s) from the archive
 command specific modifiers:
  [a]          - put file(s) after [member-name]
  [b]          - put file(s) before [member-name] (same as [i])
  [D]          - use zero for timestamps and uids/gids (default)
  [U]          - use actual timestamps and uids/gids
  [N]          - use instance [count] of name
  [f]          - truncate inserted file names
  [P]          - use full path names when matching
  [o]          - preserve original dates
  [O]          - display offsets of files in the archive
  [u]          - only replace files that are newer than current archive contents
 generic modifiers:
  [c]          - do not warn if the library had to be created
  [s]          - create an archive index (cf. ranlib)
  [l <text> ]  - specify the dependencies of this library
  [S]          - do not build a symbol table
  [T]          - deprecated, use --thin instead
  [v]          - be verbose
  [V]          - display the version number
  @<file>      - read options from <file>
  --target=BFDNAME - specify the target object format as BFDNAME
  --output=DIRNAME - specify the output directory for extraction operations
  --record-libdeps=<text> - specify the dependencies of this library
  --thin       - make a thin archive
 optional:
  --plugin <p> - load the specified plugin
 emulation options:
  No emulation specific options
ar: supported targets: elf64-x86-64 elf32-i386 elf32-iamcu elf32-x86-64 pei-i386 pe-x86-64 pei-x86-64 elf64-little elf64-big elf32-little elf32-big pe-bigobj-x86-64 pe-i386 pdb elf64-bpfle elf64-bpfbe srec symbolsrec verilog tekhex binary ihex plugin
Report bugs to <https://bugs.archlinux.org/>
 root  …  picoctf  writeups  picoCTF-2022  ar x flag
 root  …  picoctf  writeups  picoCTF-2022  ls -al
 root  …  picoctf  writeups  picoCTF-2022  ls -al
total 40
drwxr-xr-x 5 root users 4096 Feb  9 00:23 .
drwxr-xr-x 3 root users 4096 Feb  8 23:30 ..
drwxr-xr-x 2 root users 4096 Feb  9 00:00 basic-file-exploit
drwxr-xr-x 2 root users 4096 Feb  9 00:05 file-run
-rw-r--r-- 1 root users 1024 Feb  9 00:25 flag
-rw-r--r-- 1 root users 5161 Feb  9 00:15 Flag.pdf
-rwxr-xr-x 1 root users 5161 Feb  9 00:17 Flag.sh
drwxr-xr-x 2 root users 4096 Feb  9 00:14 GDBTestDrive
 root  …  picoctf  writeups  picoCTF-2022  cat flag
ih ѣ##'SGzѨrш@4@hb0C@1F=_@{O}ѦM4M
"<M)hVτHIW8"'f0D!xr_fT  h4ª~ѣMb@4h#G@@S&

1'ÅO{ojK51]<T[s-!ΥA2'͛$:eP/9>}pKb&q['
Z3##Ŏ.p!,q      EX?AX%-Ó.x<G.%i"+vCBx`IX!vۮn")4$>#By
          TRAILER!!! root  …  picoctf  writeups  picoCTF-2022  
 root  …  picoctf  writeups  picoCTF-2022  
 root  …  picoctf  writeups  picoCTF-2022  
 root  …  picoctf  writeups  picoCTF-2022  
 root  …  picoctf  writeups  picoCTF-2022  
 root  …  picoctf  writeups  picoCTF-2022  
 root  …  picoctf  writeups  picoCTF-2022  
 root  …  picoctf  writeups  picoCTF-2022  
 root  …  picoctf  writeups  picoCTF-2022  
 root  …  picoctf  writeups  picoCTF-2022  
 root  …  picoctf  writeups  picoCTF-2022  
 root  …  picoctf  writeups  picoCTF-2022  ar -x flag
ar: flag: file format not recognized
 root  …  picoctf  writeups  picoCTF-2022  ls -al                                                                                                1 
total 40
drwxr-xr-x 5 root users 4096 Feb  9 00:23 .
drwxr-xr-x 3 root users 4096 Feb  8 23:30 ..
drwxr-xr-x 2 root users 4096 Feb  9 00:00 basic-file-exploit
drwxr-xr-x 2 root users 4096 Feb  9 00:05 file-run
-rw-r--r-- 1 root users 1024 Feb  9 00:25 flag
-rw-r--r-- 1 root users 5161 Feb  9 00:15 Flag.pdf
-rwxr-xr-x 1 root users 5161 Feb  9 00:17 Flag.sh
drwxr-xr-x 2 root users 4096 Feb  9 00:14 GDBTestDrive
 root  …  picoctf  writeups  picoCTF-2022  cat flag
ih ѣ##'SGzѨrш@4@hb0C@1F=_@{O}ѦM4M
"<M)hVτHIW8"'f0D!xr_fT  h4ª~ѣMb@4h#G@@S&

1'ÅO{ojK51]<T[s-!ΥA2'͛$:eP/9>}pKb&q['
Z3##Ŏ.p!,q      EX?AX%-Ó.x<G.%i"+vCBx`IX!vۮn")4$>#By
          TRAILER!!! root  …  picoctf  writeups  picoCTF-2022  file flag
flag: cpio archive
 root  …  picoctf  writeups  picoCTF-2022  cpio -i < flag
cpio: flag not created: newer or same age version exists
2 blocks
 root  …  picoctf  writeups  picoCTF-2022  ls -al
total 40
drwxr-xr-x 5 root users 4096 Feb  9 00:23 .
drwxr-xr-x 3 root users 4096 Feb  8 23:30 ..
drwxr-xr-x 2 root users 4096 Feb  9 00:00 basic-file-exploit
drwxr-xr-x 2 root users 4096 Feb  9 00:05 file-run
-rw-r--r-- 1 root users 1024 Feb  9 00:25 flag
-rw-r--r-- 1 root users 5161 Feb  9 00:15 Flag.pdf
-rwxr-xr-x 1 root users 5161 Feb  9 00:17 Flag.sh
drwxr-xr-x 2 root users 4096 Feb  9 00:14 GDBTestDrive
 root  …  picoctf  writeups  picoCTF-2022  file flag
flag: cpio archive
 root  …  picoctf  writeups  picoCTF-2022  cpio -it < flag
flag
2 blocks
 root  …  picoctf  writeups  picoCTF-2022  cp flag cpio.arch
 root  …  picoctf  writeups  picoCTF-2022  cpio -it < cpio.arch
flag
2 blocks
 root  …  picoctf  writeups  picoCTF-2022  cpio -i < cpio.arch
cpio: flag not created: newer or same age version exists
2 blocks
 root  …  picoctf  writeups  picoCTF-2022  
 root  …  picoctf  writeups  picoCTF-2022  ls -al
total 44
drwxr-xr-x 5 root users 4096 Feb  9 00:26 .
drwxr-xr-x 3 root users 4096 Feb  8 23:30 ..
drwxr-xr-x 2 root users 4096 Feb  9 00:00 basic-file-exploit
-rw-r--r-- 1 root users 1024 Feb  9 00:26 cpio.arch
drwxr-xr-x 2 root users 4096 Feb  9 00:05 file-run
-rw-r--r-- 1 root users 1024 Feb  9 00:25 flag
-rw-r--r-- 1 root users 5161 Feb  9 00:15 Flag.pdf
-rwxr-xr-x 1 root users 5161 Feb  9 00:17 Flag.sh
drwxr-xr-x 2 root users 4096 Feb  9 00:14 GDBTestDrive
 root  …  picoctf  writeups  picoCTF-2022  rm -rf flag
 root  …  picoctf  writeups  picoCTF-2022  cpio -i < cpio.arch
2 blocks
 root  …  picoctf  writeups  picoCTF-2022  ls -al
total 44
drwxr-xr-x 5 root users 4096 Feb  9 00:27 .
drwxr-xr-x 3 root users 4096 Feb  8 23:30 ..
drwxr-xr-x 2 root users 4096 Feb  9 00:00 basic-file-exploit
-rw-r--r-- 1 root users 1024 Feb  9 00:26 cpio.arch
drwxr-xr-x 2 root users 4096 Feb  9 00:05 file-run
-rw-r--r-- 1 root users  511 Feb  9 00:27 flag
-rw-r--r-- 1 root users 5161 Feb  9 00:15 Flag.pdf
-rwxr-xr-x 1 root users 5161 Feb  9 00:17 Flag.sh
drwxr-xr-x 2 root users 4096 Feb  9 00:14 GDBTestDrive
 root  …  picoctf  writeups  picoCTF-2022  cat flag
ih ѣ##'SGzѨrш@4@hb0C@1FM
"<M)hVτHIW8"'f0D!xr_fT  h4ª~ѣMb@4h#G@@S&

1'ÅO{ojK51]<T[s-!ΥA2'͛$:eP/9>}pKb&q['
Z3##Ŏ.p!, root  …  picoctf  writeups  picoCTF-2022  file flag
flag: bzip2 compressed data, block size = 900k
 root  …  picoctf  writeups  picoCTF-2022  bz
bzcat             bzgrep            bzip2recover      bzr               bzr-upload-pack
bzdiff            bzip2             bzmore            bzr-receive-pack  bzz
 root  …  picoctf  writeups  picoCTF-2022  bzip2
bzip2         bzip2recover
 root  …  picoctf  writeups  picoCTF-2022  bzip2 -d flag
bzip2: Can't guess original name for flag -- using flag.out
 root  …  picoctf  writeups  picoCTF-2022  ls -al
total 44
drwxr-xr-x 5 root users 4096 Feb  9 00:27 .
drwxr-xr-x 3 root users 4096 Feb  8 23:30 ..
drwxr-xr-x 2 root users 4096 Feb  9 00:00 basic-file-exploit
-rw-r--r-- 1 root users 1024 Feb  9 00:26 cpio.arch
drwxr-xr-x 2 root users 4096 Feb  9 00:05 file-run
-rw-r--r-- 1 root users  357 Feb  9 00:27 flag.out
-rw-r--r-- 1 root users 5161 Feb  9 00:15 Flag.pdf
-rwxr-xr-x 1 root users 5161 Feb  9 00:17 Flag.sh
drwxr-xr-x 2 root users 4096 Feb  9 00:14 GDBTestDrive
 root  …  picoctf  writeups  picoCTF-2022  file flag.out
flag.out: gzip compressed data, was "flag", last modified: Tue Mar 15 06:50:36 2022, from Unix, original size modulo 2^32 329
 root  …  picoctf  writeups  picoCTF-2022  cat flag.out
<70bflagILZIP
                O'6@onXC1kEy;"i?(;&F9%
NjNy5i({j©DlQ/(U_w8M>4Ԥit3h.m%*(]vFi|BMWQiSnqy[]gp?c'}z{$Tc^3jI root  …  picoctf  writeups  picoCTF-2022  bzip2 -d flag.out
 root  …  picoctf  writeups  picoCTF-2022  bzip2 -d flag.out
bzip2: Can't guess original name for flag.out -- using flag.out.out
bzip2: flag.out is not a bzip2 file.
 root  …  picoctf  writeups  picoCTF-2022  ls -al                                                                                                2 
total 44
drwxr-xr-x 5 root users 4096 Feb  9 00:28 .
drwxr-xr-x 3 root users 4096 Feb  8 23:30 ..
drwxr-xr-x 2 root users 4096 Feb  9 00:00 basic-file-exploit
-rw-r--r-- 1 root users 1024 Feb  9 00:26 cpio.arch
drwxr-xr-x 2 root users 4096 Feb  9 00:05 file-run
-rw-r--r-- 1 root users  357 Feb  9 00:27 flag.out
-rw-r--r-- 1 root users 5161 Feb  9 00:15 Flag.pdf
-rwxr-xr-x 1 root users 5161 Feb  9 00:17 Flag.sh
drwxr-xr-x 2 root users 4096 Feb  9 00:14 GDBTestDrive
 root  …  picoctf  writeups  picoCTF-2022  file flag.out
flag.out: gzip compressed data, was "flag", last modified: Tue Mar 15 06:50:36 2022, from Unix, original size modulo 2^32 329
 root  …  picoctf  writeups  picoCTF-2022  gzip --help
Usage: gzip [OPTION]... [FILE]...
Compress or uncompress FILEs (by default, compress FILES in-place).

Mandatory arguments to long options are mandatory for short options too.

  -c, --stdout      write on standard output, keep original files unchanged
  -d, --decompress  decompress
  -f, --force       force overwrite of output file and compress links
  -h, --help        give this help
  -k, --keep        keep (don't delete) input files
  -l, --list        list compressed file contents
  -L, --license     display software license
  -n, --no-name     do not save or restore the original name and timestamp
  -N, --name        save or restore the original name and timestamp
  -q, --quiet       suppress all warnings
  -r, --recursive   operate recursively on directories
      --rsyncable   make rsync-friendly archive
  -S, --suffix=SUF  use suffix SUF on compressed files
      --synchronous synchronous output (safer if system crashes, but slower)
  -t, --test        test compressed file integrity
  -v, --verbose     verbose mode
  -V, --version     display version number
  -1, --fast        compress faster
  -9, --best        compress better

With no FILE, or when FILE is -, read standard input.

Report bugs to <bug-gzip@gnu.org>.
 root  …  picoctf  writeups  picoCTF-2022  gzip -d flag.out
gzip: flag.out: unknown suffix -- ignored
 root  …  picoctf  writeups  picoCTF-2022  ls -al                                                                                                2 
total 44
drwxr-xr-x 5 root users 4096 Feb  9 00:28 .
drwxr-xr-x 3 root users 4096 Feb  8 23:30 ..
drwxr-xr-x 2 root users 4096 Feb  9 00:00 basic-file-exploit
-rw-r--r-- 1 root users 1024 Feb  9 00:26 cpio.arch
drwxr-xr-x 2 root users 4096 Feb  9 00:05 file-run
-rw-r--r-- 1 root users  357 Feb  9 00:27 flag.out
-rw-r--r-- 1 root users 5161 Feb  9 00:15 Flag.pdf
-rwxr-xr-x 1 root users 5161 Feb  9 00:17 Flag.sh
drwxr-xr-x 2 root users 4096 Feb  9 00:14 GDBTestDrive
 root  …  picoctf  writeups  picoCTF-2022  file flag.out
flag.out: gzip compressed data, was "flag", last modified: Tue Mar 15 06:50:36 2022, from Unix, original size modulo 2^32 329
 root  …  picoctf  writeups  picoCTF-2022  
 root  …  picoctf  writeups  picoCTF-2022  
 root  …  picoctf  writeups  picoCTF-2022  
 root  …  picoctf  writeups  picoCTF-2022  
 root  …  picoctf  writeups  picoCTF-2022  
 root  …  picoctf  writeups  picoCTF-2022  
 root  …  picoctf  writeups  picoCTF-2022  
 root  …  picoctf  writeups  picoCTF-2022  
 root  …  picoctf  writeups  picoCTF-2022  
 root  …  picoctf  writeups  picoCTF-2022  
 root  …  picoctf  writeups  picoCTF-2022  
 root  …  picoctf  writeups  picoCTF-2022  
 root  …  picoctf  writeups  picoCTF-2022  nautilus .
** Message: 00:29:06.718: Connecting to org.freedesktop.Tracker3.Miner.Files
^C
 root  …  picoctf  writeups  picoCTF-2022                                                                                                   SIGINT 
 root  …  picoctf  writeups  picoCTF-2022  gzip --help
Usage: gzip [OPTION]... [FILE]...
Compress or uncompress FILEs (by default, compress FILES in-place).

Mandatory arguments to long options are mandatory for short options too.

  -c, --stdout      write on standard output, keep original files unchanged
  -d, --decompress  decompress
  -f, --force       force overwrite of output file and compress links
  -h, --help        give this help
  -k, --keep        keep (don't delete) input files
  -l, --list        list compressed file contents
  -L, --license     display software license
  -n, --no-name     do not save or restore the original name and timestamp
  -N, --name        save or restore the original name and timestamp
  -q, --quiet       suppress all warnings
  -r, --recursive   operate recursively on directories
      --rsyncable   make rsync-friendly archive
  -S, --suffix=SUF  use suffix SUF on compressed files
      --synchronous synchronous output (safer if system crashes, but slower)
  -t, --test        test compressed file integrity
  -v, --verbose     verbose mode
  -V, --version     display version number
  -1, --fast        compress faster
  -9, --best        compress better

With no FILE, or when FILE is -, read standard input.

Report bugs to <bug-gzip@gnu.org>.
 root  …  picoctf  writeups  picoCTF-2022  file flag.out
flag.out: gzip compressed data, was "flag", last modified: Tue Mar 15 06:50:36 2022, from Unix, original size modulo 2^32 329
 root  …  picoctf  writeups  picoCTF-2022  gzip -d flag.out
gzip: flag.out: unknown suffix -- ignored
 root  …  picoctf  writeups  picoCTF-2022  gzip -d -f flag.out                                                                                     
gzip: flag.out: unknown suffix -- ignored
 root  …  picoctf  writeups  picoCTF-2022  gzip d flag.out                                                                                   2 
gzip: d: No such file or directory
 root  …  picoctf  writeups  picoCTF-2022  gun                                                                                                   1 
gunicorn_pecan  gunzip
 root  …  picoctf  writeups  picoCTF-2022  gunzip --help
Usage: /usr/bin/gunzip [OPTION]... [FILE]...
Uncompress FILEs (by default, in-place).

Mandatory arguments to long options are mandatory for short options too.

  -c, --stdout      write on standard output, keep original files unchanged
  -f, --force       force overwrite of output file and compress links
  -k, --keep        keep (don't delete) input files
  -l, --list        list compressed file contents
  -n, --no-name     do not save or restore the original name and timestamp
  -N, --name        save or restore the original name and timestamp
  -q, --quiet       suppress all warnings
  -r, --recursive   operate recursively on directories
  -S, --suffix=SUF  use suffix SUF on compressed files
      --synchronous synchronous output (safer if system crashes, but slower)
  -t, --test        test compressed file integrity
  -v, --verbose     verbose mode
      --help        display this help and exit
      --version     display version information and exit

With no FILE, or when FILE is -, read standard input.

Report bugs to <bug-gzip@gnu.org>.
 root  …  picoctf  writeups  picoCTF-2022  
 root  …  picoctf  writeups  picoCTF-2022  
 root  …  picoctf  writeups  picoCTF-2022  
 root  …  picoctf  writeups  picoCTF-2022  ls -al
total 44
drwxr-xr-x 5 root users 4096 Feb  9 00:30 .
drwxr-xr-x 3 root users 4096 Feb  8 23:30 ..
drwxr-xr-x 2 root users 4096 Feb  9 00:00 basic-file-exploit
-rw-r--r-- 1 root users 1024 Feb  9 00:26 cpio.arch
drwxr-xr-x 2 root users 4096 Feb  9 00:05 file-run
-rw-r--r-- 1 root users  389 Feb  9 00:27 flag.out.gz
-rw-r--r-- 1 root users 5161 Feb  9 00:15 Flag.pdf
-rwxr-xr-x 1 root users 5161 Feb  9 00:17 Flag.sh
drwxr-xr-x 2 root users 4096 Feb  9 00:14 GDBTestDrive
 root  …  picoctf  writeups  picoCTF-2022  file flag.out.gz
flag.out.gz: gzip compressed data, was "flag.out", last modified: Wed Feb  8 23:27:04 2023, from Unix, original size modulo 2^32 357
 root  …  picoctf  writeups  picoCTF-2022  gunzip flag.out.gz
 root  …  picoctf  writeups  picoCTF-2022  ls -al
total 44
drwxr-xr-x 5 root users 4096 Feb  9 00:31 .
drwxr-xr-x 3 root users 4096 Feb  8 23:30 ..
drwxr-xr-x 2 root users 4096 Feb  9 00:00 basic-file-exploit
-rw-r--r-- 1 root users 1024 Feb  9 00:26 cpio.arch
drwxr-xr-x 2 root users 4096 Feb  9 00:05 file-run
-rw-r--r-- 1 root users  357 Feb  9 00:27 flag.out
-rw-r--r-- 1 root users 5161 Feb  9 00:15 Flag.pdf
-rwxr-xr-x 1 root users 5161 Feb  9 00:17 Flag.sh
drwxr-xr-x 2 root users 4096 Feb  9 00:14 GDBTestDrive
 root  …  picoctf  writeups  picoCTF-2022  file flag.out
flag.out: gzip compressed data, was "flag", last modified: Tue Mar 15 06:50:36 2022, from Unix, original size modulo 2^32 329
 root  …  picoctf  writeups  picoCTF-2022  gunzip flag.out.gz
gzip: flag.out.gz: No such file or directory
 root  …  picoctf  writeups  picoCTF-2022  gunzip flag.out
gzip: flag.out: unknown suffix -- ignored
 root  …  picoctf  writeups  picoCTF-2022  file flag.out                                                                                         2 
flag.out: gzip compressed data, was "flag", last modified: Tue Mar 15 06:50:36 2022, from Unix, original size modulo 2^32 329
 root  …  picoctf  writeups  picoCTF-2022  cat flag.out
<70bflagILZIP
                O'6@onXC1kEy;"i?(;&F9%
NjNy5i({j©DlQ/(U_w8M>4Ԥit3h.m%*(]vFi|BMWQiSnqy[]gp?c'}z{$Tc^3jI root  …  picoctf  writeups  picoCTF-2022  binwalk flag.out

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             gzip compressed data, has original file name: "flag", from Unix, last modified: 2022-03-15 06:50:36
20            0x14            lzip compressed data, version: 1

 root  …  picoctf  writeups  picoCTF-2022  mv flag.out flag.out.gz
 root  …  picoctf  writeups  picoCTF-2022  gun
gunicorn_pecan  gunzip
 root  …  picoctf  writeups  picoCTF-2022  gunzip flag.out.gz
 root  …  picoctf  writeups  picoCTF-2022  ls -al
total 44
drwxr-xr-x 5 root users 4096 Feb  9 00:32 .
drwxr-xr-x 3 root users 4096 Feb  8 23:30 ..
drwxr-xr-x 2 root users 4096 Feb  9 00:00 basic-file-exploit
-rw-r--r-- 1 root users 1024 Feb  9 00:26 cpio.arch
drwxr-xr-x 2 root users 4096 Feb  9 00:05 file-run
-rw-r--r-- 1 root users  329 Feb  9 00:27 flag.out
-rw-r--r-- 1 root users 5161 Feb  9 00:15 Flag.pdf
-rwxr-xr-x 1 root users 5161 Feb  9 00:17 Flag.sh
drwxr-xr-x 2 root users 4096 Feb  9 00:14 GDBTestDrive
 root  …  picoctf  writeups  picoCTF-2022  file flag.out
flag.out: lzip compressed data, version: 1
 root  …  picoctf  writeups  picoCTF-2022  
 root  …  picoctf  writeups  picoCTF-2022  
 root  …  picoctf  writeups  picoCTF-2022  
 root  …  picoctf  writeups  picoCTF-2022  
 root  …  picoctf  writeups  picoCTF-2022  
 root  …  picoctf  writeups  picoCTF-2022  pl
pl2pm         platex        pldd          plipconfig    plistutil     plookup       pltotf        plugctl       pluginviewer  plugreport
 root  …  picoctf  writeups  picoCTF-2022  lz
lz        lz4c      lzcat     lzdiff    lzf       lzgrep    lzma      lzmainfo
lz4       lz4cat    lzcmp     lzegrep   lzfgrep   lzless    lzmadec   lzmore
 root  …  picoctf  writeups  picoCTF-2022  lz
lz        lz4c      lzcat     lzdiff    lzf       lzgrep    lzma      lzmainfo
lz4       lz4cat    lzcmp     lzegrep   lzfgrep   lzless    lzmadec   lzmore
 root  …  picoctf  writeups  picoCTF-2022  lz
lz        lz4c      lzcat     lzdiff    lzf       lzgrep    lzma      lzmainfo
lz4       lz4cat    lzcmp     lzegrep   lzfgrep   lzless    lzmadec   lzmore
 root  …  picoctf  writeups  picoCTF-2022  lz
lz        lz4c      lzcat     lzdiff    lzf       lzgrep    lzma      lzmainfo
lz4       lz4cat    lzcmp     lzegrep   lzfgrep   lzless    lzmadec   lzmore
 root  …  picoctf  writeups  picoCTF-2022  lz --help
 root  …  picoctf  writeups  picoCTF-2022  lz --help

/usr/bin/lz: could not read "--help".
 root  …  picoctf  writeups  picoCTF-2022  lz -h

/usr/bin/lz: could not read "-h".
 root  …  picoctf  writeups  picoCTF-2022  lz
Reading directory of  standard input.
gzip: compressed data not read from a terminal. Use -f to force decompression.
For help, type: gzip -h
tar: This does not look like a tar archive
tar: Exiting with failure status due to previous errors
 root  …  picoctf  writeups  picoCTF-2022  lz flag.out                                                                                           2 

Reading directory of  "flag.out".

gzip: flag.out: not in gzip format
tar: This does not look like a tar archive
tar: Exiting with failure status due to previous errors
 root  …  picoctf  writeups  picoCTF-2022  ls -al                                                                                                2 
total 44
drwxr-xr-x 5 root users 4096 Feb  9 00:32 .
drwxr-xr-x 3 root users 4096 Feb  8 23:30 ..
drwxr-xr-x 2 root users 4096 Feb  9 00:00 basic-file-exploit
-rw-r--r-- 1 root users 1024 Feb  9 00:26 cpio.arch
drwxr-xr-x 2 root users 4096 Feb  9 00:05 file-run
-rw-r--r-- 1 root users  329 Feb  9 00:27 flag.out
-rw-r--r-- 1 root users 5161 Feb  9 00:15 Flag.pdf
-rwxr-xr-x 1 root users 5161 Feb  9 00:17 Flag.sh
drwxr-xr-x 2 root users 4096 Feb  9 00:14 GDBTestDrive
 root  …  picoctf  writeups  picoCTF-2022  file flag.out
flag.out: lzip compressed data, version: 1
 root  …  picoctf  writeups  picoCTF-2022  binwalk flag.out

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             lzip compressed data, version: 1

 root  …  picoctf  writeups  picoCTF-2022  lz
lz        lz4c      lzcat     lzdiff    lzf       lzgrep    lzma      lzmainfo
lz4       lz4cat    lzcmp     lzegrep   lzfgrep   lzless    lzmadec   lzmore
 root  …  picoctf  writeups  picoCTF-2022  pacman -Ss lzip
community/lzip 1.23-2
    A lossless file compressor based on the LZMA algorithm
 root  …  picoctf  writeups  picoCTF-2022  sudo pacman -S lzip
[sudo] password for root:
resolving dependencies...
looking for conflicting packages...

Packages (1) lzip-1.23-2

Total Download Size:   0.07 MiB
Total Installed Size:  0.13 MiB

:: Proceed with installation? [Y/n] y
:: Retrieving packages...
 lzip-1.23-2-x86_64                                                 73.0 KiB   664 KiB/s 00:00 [########################################################] 100%
(1/1) checking keys in keyring                                                                 [########################################################] 100%
(1/1) checking package integrity                                                               [########################################################] 100%
(1/1) loading package files                                                                    [########################################################] 100%
(1/1) checking for file conflicts                                                              [########################################################] 100%
(1/1) checking available disk space                                                            [########################################################] 100%
:: Processing package changes...
(1/1) installing lzip                                                                          [########################################################] 100%
:: Running post-transaction hooks...
(1/2) Arming ConditionNeedsUpdate...
(2/2) Updating the info directory file...
 root  …  picoctf  writeups  picoCTF-2022  lzip --help
 root  …  picoctf  writeups  picoCTF-2022  lzip --help
Lzip is a lossless data compressor with a user interface similar to the one
of gzip or bzip2. Lzip uses a simplified form of the 'Lempel-Ziv-Markov
chain-Algorithm' (LZMA) stream format and provides a 3 factor integrity
checking to maximize interoperability and optimize safety. Lzip can compress
about as fast as gzip (lzip -0) or compress most files more than bzip2
(lzip -9). Decompression speed is intermediate between gzip and bzip2.
Lzip is better than gzip and bzip2 from a data recovery perspective. Lzip
has been designed, written, and tested with great care to replace gzip and
bzip2 as the standard general-purpose compressed format for unix-like
systems.

Usage: lzip [options] [files]

Options:
  -h, --help                     display this help and exit
  -V, --version                  output version information and exit
  -a, --trailing-error           exit with error status if trailing data
  -b, --member-size=<bytes>      set member size limit in bytes
  -c, --stdout                   write to standard output, keep input files
  -d, --decompress               decompress
  -f, --force                    overwrite existing output files
  -F, --recompress               force re-compression of compressed files
  -k, --keep                     keep (don't delete) input files
  -l, --list                     print (un)compressed file sizes
  -m, --match-length=<bytes>     set match length limit in bytes [36]
  -o, --output=<file>            write to <file>, keep input files
  -q, --quiet                    suppress all messages
  -s, --dictionary-size=<bytes>  set dictionary size limit in bytes [8 MiB]
  -S, --volume-size=<bytes>      set volume size limit in bytes
  -t, --test                     test compressed file integrity
  -v, --verbose                  be verbose (a 2nd -v gives more)
  -0 .. -9                       set compression level [default 6]
      --fast                     alias for -0
      --best                     alias for -9
      --loose-trailing           allow trailing data seeming corrupt header

If no file names are given, or if a file is '-', lzip compresses or
decompresses from standard input to standard output.
Numbers may be followed by a multiplier: k = kB = 10^3 = 1000,
Ki = KiB = 2^10 = 1024, M = 10^6, Mi = 2^20, G = 10^9, Gi = 2^30, etc...
Dictionary sizes 12 to 29 are interpreted as powers of two, meaning 2^12
to 2^29 bytes.

The bidimensional parameter space of LZMA can't be mapped to a linear
scale optimal for all files. If your files are large, very repetitive,
etc, you may need to use the options --dictionary-size and --match-length
directly to achieve optimal performance.

To extract all the files from archive 'foo.tar.lz', use the commands
'tar -xf foo.tar.lz' or 'lzip -cd foo.tar.lz | tar -xf -'.

Exit status: 0 for a normal exit, 1 for environmental problems (file
not found, invalid flags, I/O errors, etc), 2 to indicate a corrupt or
invalid input file, 3 for an internal consistency error (e.g., bug) which
caused lzip to panic.

The ideas embodied in lzip are due to (at least) the following people:
Abraham Lempel and Jacob Ziv (for the LZ algorithm), Andrey Markov (for the
definition of Markov chains), G.N.N. Martin (for the definition of range
encoding), Igor Pavlov (for putting all the above together in LZMA), and
Julian Seward (for bzip2's CLI).

Report bugs to lzip-bug@nongnu.org
Lzip home page: http://www.nongnu.org/lzip/lzip.html
 root  …  picoctf  writeups  picoCTF-2022  lzip -d flag.out
 root  …  picoctf  writeups  picoCTF-2022  lzip -d flag.out
 root  …  picoctf  writeups  picoCTF-2022  ls -al
total 44
drwxr-xr-x 5 root users 4096 Feb  9 00:35 .
drwxr-xr-x 3 root users 4096 Feb  8 23:30 ..
drwxr-xr-x 2 root users 4096 Feb  9 00:00 basic-file-exploit
-rw-r--r-- 1 root users 1024 Feb  9 00:26 cpio.arch
drwxr-xr-x 2 root users 4096 Feb  9 00:05 file-run
-rw-r--r-- 1 root users  283 Feb  9 00:27 flag.out.out
-rw-r--r-- 1 root users 5161 Feb  9 00:15 Flag.pdf
-rwxr-xr-x 1 root users 5161 Feb  9 00:17 Flag.sh
drwxr-xr-x 2 root users 4096 Feb  9 00:14 GDBTestDrive
 root  …  picoctf  writeups  picoCTF-2022  file flag.out.out
flag.out.out: LZ4 compressed data (v1.4+)
 root  …  picoctf  writeups  picoCTF-2022  lz
lz        lz4c      lzcat     lzdiff    lzf       lzgrep    lzless    lzmadec   lzmore
lz4       lz4cat    lzcmp     lzegrep   lzfgrep   lzip      lzma      lzmainfo
 root  …  picoctf  writeups  picoCTF-2022  lz4
lz4     lz4c    lz4cat
 root  …  picoctf  writeups  picoCTF-2022  lz4 --help
 root  …  picoctf  writeups  picoCTF-2022  lz4 --help
*** LZ4 command line interface 64-bits v1.9.4, by Yann Collet ***
Usage :
      lz4 [arg] [input] [output]

input   : a filename
          with no FILE, or when FILE is - or stdin, read standard input
Arguments :
 -1     : Fast compression (default)
 -9     : High compression
 -d     : decompression (default for .lz4 extension)
 -z     : force compression
 -D FILE: use FILE as dictionary
 -f     : overwrite output without prompting
 -k     : preserve source files(s)  (default)
--rm    : remove source file(s) after successful de/compression
 -h/-H  : display help/long help and exit

Advanced arguments :
 -V     : display Version number and exit
 -v     : verbose mode
 -q     : suppress warnings; specify twice to suppress errors too
 -c     : force write to standard output, even if it is the console
 -t     : test compressed file integrity
 -m     : multiple input files (implies automatic output filenames)
 -r     : operate recursively on directories (sets also -m)
 -l     : compress using Legacy format (Linux kernel compression)
 -B#    : cut file into blocks of size # bytes [32+]
                     or predefined block size [4-7] (default: 7)
 -BI    : Block Independence (default)
 -BD    : Block dependency (improves compression ratio)
 -BX    : enable block checksum (default:disabled)
--no-frame-crc : disable stream checksum (default:enabled)
--content-size : compressed frame includes original size (default:not present)
--list FILE : lists information about .lz4 files (useful for files compressed with --content-size flag)
--[no-]sparse  : sparse mode (default:enabled on file, disabled on stdout)
--favor-decSpeed: compressed files decompress faster, but are less compressed
--fast[=#]: switch to ultra fast compression level (default: 1)
--best  : same as -12
Benchmark arguments :
 -b#    : benchmark file(s), using # compression level (default : 1)
 -e#    : test all compression levels from -bX to # (default : 1)
 -i#    : minimum evaluation time in seconds (default : 3s)
 root  …  picoctf  writeups  picoCTF-2022  lz4 -d flag.out.out
 root  …  picoctf  writeups  picoCTF-2022  lz4 -d flag.out.out
Cannot determine an output filename
Incorrect parameters
Usage :
      lz4 [arg] [input] [output]

input   : a filename
          with no FILE, or when FILE is - or stdin, read standard input
Arguments :
 -1     : Fast compression (default)
 -9     : High compression
 -d     : decompression (default for .lz4 extension)
 -z     : force compression
 -D FILE: use FILE as dictionary
 -f     : overwrite output without prompting
 -k     : preserve source files(s)  (default)
--rm    : remove source file(s) after successful de/compression
 -h/-H  : display help/long help and exit
 root  …  picoctf  writeups  picoCTF-2022  lz4 -d flag.out.out flag                                                                              1 
flag.out.out         : decoded 266 bytes
 root  …  picoctf  writeups  picoCTF-2022  ls -al
 root  …  picoctf  writeups  picoCTF-2022  ls -al
total 48
drwxr-xr-x 5 root users 4096 Feb  9 00:36 .
drwxr-xr-x 3 root users 4096 Feb  8 23:30 ..
drwxr-xr-x 2 root users 4096 Feb  9 00:00 basic-file-exploit
-rw-r--r-- 1 root users 1024 Feb  9 00:26 cpio.arch
drwxr-xr-x 2 root users 4096 Feb  9 00:05 file-run
-rw-r--r-- 1 root users  266 Feb  9 00:27 flag
-rw-r--r-- 1 root users  283 Feb  9 00:27 flag.out.out
-rw-r--r-- 1 root users 5161 Feb  9 00:15 Flag.pdf
-rwxr-xr-x 1 root users 5161 Feb  9 00:17 Flag.sh
drwxr-xr-x 2 root users 4096 Feb  9 00:14 GDBTestDrive
 root  …  picoctf  writeups  picoCTF-2022  file flag
flag: LZMA compressed data, non-streamed, size 255
 root  …  picoctf  writeups  picoCTF-2022  lzm
lzma      lzmadec   lzmainfo  lzmore
 root  …  picoctf  writeups  picoCTF-2022  lzm
lzma      lzmadec   lzmainfo  lzmore
 root  …  picoctf  writeups  picoCTF-2022  lzma
lzma      lzmadec   lzmainfo
 root  …  picoctf  writeups  picoCTF-2022  lzma --help
Usage: lzma [OPTION]... [FILE]...
Compress or decompress FILEs in the .xz format.

  -z, --compress      force compression
  -d, --decompress    force decompression
  -t, --test          test compressed file integrity
  -l, --list          list information about .xz files
  -k, --keep          keep (don't delete) input files
  -f, --force         force overwrite of output file and (de)compress links
  -c, --stdout        write to standard output and don't delete input files
  -0 ... -9           compression preset; default is 6; take compressor *and*
                      decompressor memory usage into account before using 7-9!
  -e, --extreme       try to improve compression ratio by using more CPU time;
                      does not affect decompressor memory requirements
  -T, --threads=NUM   use at most NUM threads; the default is 1; set to 0
                      to use as many threads as there are processor cores
  -q, --quiet         suppress warnings; specify twice to suppress errors too
  -v, --verbose       be verbose; specify twice for even more verbose
  -h, --help          display this short help and exit
  -H, --long-help     display the long help (lists also the advanced options)
  -V, --version       display the version number and exit

With no FILE, or when FILE is -, read standard input.

Report bugs to <xz@tukaani.org> (in English or Finnish).
XZ Utils home page: <https://tukaani.org/xz/>
 root  …  picoctf  writeups  picoCTF-2022  lzma -d flag
 root  …  picoctf  writeups  picoCTF-2022  lzma -d flag
lzma: flag: Filename has an unknown suffix, skipping
 root  …  picoctf  writeups  picoCTF-2022  file flag                                                                                             2 
flag: LZMA compressed data, non-streamed, size 255
 root  …  picoctf  writeups  picoCTF-2022  lzma
lzma      lzmadec   lzmainfo
 root  …  picoctf  writeups  picoCTF-2022  lzma --help
Usage: lzma [OPTION]... [FILE]...
Compress or decompress FILEs in the .xz format.

  -z, --compress      force compression
  -d, --decompress    force decompression
  -t, --test          test compressed file integrity
  -l, --list          list information about .xz files
  -k, --keep          keep (don't delete) input files
  -f, --force         force overwrite of output file and (de)compress links
  -c, --stdout        write to standard output and don't delete input files
  -0 ... -9           compression preset; default is 6; take compressor *and*
                      decompressor memory usage into account before using 7-9!
  -e, --extreme       try to improve compression ratio by using more CPU time;
                      does not affect decompressor memory requirements
  -T, --threads=NUM   use at most NUM threads; the default is 1; set to 0
                      to use as many threads as there are processor cores
  -q, --quiet         suppress warnings; specify twice to suppress errors too
  -v, --verbose       be verbose; specify twice for even more verbose
  -h, --help          display this short help and exit
  -H, --long-help     display the long help (lists also the advanced options)
  -V, --version       display the version number and exit

With no FILE, or when FILE is -, read standard input.

Report bugs to <xz@tukaani.org> (in English or Finnish).
XZ Utils home page: <https://tukaani.org/xz/>
 root  …  picoctf  writeups  picoCTF-2022  lzmainfo flag

flag
Uncompressed size:             0 MB (255 bytes)
Dictionary size:               8 MB (2^23 bytes)
Literal context bits (lc):     3
Literal pos bits (lp):         0
Number of pos bits (pb):       2

 root  …  picoctf  writeups  picoCTF-2022  mv flag flag.xz
 root  …  picoctf  writeups  picoCTF-2022  lzma -d flag
 root  …  picoctf  writeups  picoCTF-2022  lzma -d flag
lzma: flag: No such file or directory
 root  …  picoctf  writeups  picoCTF-2022  lzma -d flag.                                                                                         1 
flag.out.out  flag.xz
 root  …  picoctf  writeups  picoCTF-2022  lzma -d flag.xz                                                                                       1 
 root  …  picoctf  writeups  picoCTF-2022  ls -al
total 48
drwxr-xr-x 5 root users 4096 Feb  9 00:37 .
drwxr-xr-x 3 root users 4096 Feb  8 23:30 ..
drwxr-xr-x 2 root users 4096 Feb  9 00:00 basic-file-exploit
-rw-r--r-- 1 root users 1024 Feb  9 00:26 cpio.arch
drwxr-xr-x 2 root users 4096 Feb  9 00:05 file-run
-rw-r--r-- 1 root users  255 Feb  9 00:27 flag
-rw-r--r-- 1 root users  283 Feb  9 00:27 flag.out.out
-rw-r--r-- 1 root users 5161 Feb  9 00:15 Flag.pdf
-rwxr-xr-x 1 root users 5161 Feb  9 00:17 Flag.sh
drwxr-xr-x 2 root users 4096 Feb  9 00:14 GDBTestDrive
 root  …  picoctf  writeups  picoCTF-2022  file flag
flag: lzop compressed data - version 1.040, LZO1X-1, os: Unix
 root  …  picoctf  writeups  picoCTF-2022  pacman -Ss lzop
extra/lzop 1.04-3
    File compressor using lzo lib
 root  …  picoctf  writeups  picoCTF-2022  sudo pacman -S lzop
resolving dependencies...
looking for conflicting packages...

Packages (1) lzop-1.04-3

Total Download Size:   0.07 MiB
Total Installed Size:  0.20 MiB

:: Proceed with installation? [Y/n] y
:: Retrieving packages...
 lzop-1.04-3-x86_64                                                 70.2 KiB   780 KiB/s 00:00 [########################################################] 100%
(1/1) checking keys in keyring                                                                 [########################################################] 100%
(1/1) checking package integrity                                                               [########################################################] 100%
(1/1) loading package files                                                                    [########################################################] 100%
(1/1) checking for file conflicts                                                              [########################################################] 100%
(1/1) checking available disk space                                                            [########################################################] 100%
:: Processing package changes...
(1/1) installing lzop                                                                          [########################################################] 100%
:: Running post-transaction hooks...
(1/1) Arming ConditionNeedsUpdate...
 root  …  picoctf  writeups  picoCTF-2022  lzop --help
                          Lempel-Ziv-Oberhumer Packer
                           Copyright (C) 1996 - 2017
lzop v1.04         Markus Franz Xaver Johannes Oberhumer         Aug 10th 2017

Usage: lzop [-dxlthIVL19] [-qvcfFnNPkUp] [-o file] [-S suffix] [file..]

Commands:
  -1     compress faster                   -9    compress better
  -d     decompress                        -x    extract (same as -dPp)
  -l     list compressed file              -I    display system information
  -t     test compressed file              -V    display version number
  -h     give this help                    -L    display software license
Options:
  -q     be quiet                          -v       be verbose
  -c     write on standard output          -oFILE   write output to 'FILE'
  -p     write output to current dir       -pDIR    write to path 'DIR'
  -f     force overwrite of output files
  -n     do not restore the original file name (default)
  -N     restore the original file name
  -P     restore or save the original path and file name
  -S.suf use suffix .suf on compressed files
  -U     delete input files after successful operation (like gzip and bzip2)
  file.. files to (de)compress. If none given, try standard input.
 root  …  picoctf  writeups  picoCTF-2022  lzop -d flag
 root  …  picoctf  writeups  picoCTF-2022  lzop -d flag
lzop: flag: unknown suffix -- ignored
skipping flag [flag.raw]
 root  …  picoctf  writeups  picoCTF-2022  lzop --help                                                                                  1 
                          Lempel-Ziv-Oberhumer Packer
                           Copyright (C) 1996 - 2017
lzop v1.04         Markus Franz Xaver Johannes Oberhumer         Aug 10th 2017

Usage: lzop [-dxlthIVL19] [-qvcfFnNPkUp] [-o file] [-S suffix] [file..]

Commands:
  -1     compress faster                   -9    compress better
  -d     decompress                        -x    extract (same as -dPp)
  -l     list compressed file              -I    display system information
  -t     test compressed file              -V    display version number
  -h     give this help                    -L    display software license
Options:
  -q     be quiet                          -v       be verbose
  -c     write on standard output          -oFILE   write output to 'FILE'
  -p     write output to current dir       -pDIR    write to path 'DIR'
  -f     force overwrite of output files
  -n     do not restore the original file name (default)
  -N     restore the original file name
  -P     restore or save the original path and file name
  -S.suf use suffix .suf on compressed files
  -U     delete input files after successful operation (like gzip and bzip2)
  file.. files to (de)compress. If none given, try standard input.
 root  …  picoctf  writeups  picoCTF-2022  ls -al
total 48
drwxr-xr-x 5 root users 4096 Feb  9 00:37 .
drwxr-xr-x 3 root users 4096 Feb  8 23:30 ..
drwxr-xr-x 2 root users 4096 Feb  9 00:00 basic-file-exploit
-rw-r--r-- 1 root users 1024 Feb  9 00:26 cpio.arch
drwxr-xr-x 2 root users 4096 Feb  9 00:05 file-run
-rw-r--r-- 1 root users  255 Feb  9 00:27 flag
-rw-r--r-- 1 root users  283 Feb  9 00:27 flag.out.out
-rw-r--r-- 1 root users 5161 Feb  9 00:15 Flag.pdf
-rwxr-xr-x 1 root users 5161 Feb  9 00:17 Flag.sh
drwxr-xr-x 2 root users 4096 Feb  9 00:14 GDBTestDrive
 root  …  picoctf  writeups  picoCTF-2022  mv flag flag.lzop
 root  …  picoctf  writeups  picoCTF-2022  lzop -d flag.lzop
 root  …  picoctf  writeups  picoCTF-2022  ls -al
 root  …  picoctf  writeups  picoCTF-2022  ls -al
total 52
drwxr-xr-x 5 root users 4096 Feb  9 00:38 .
drwxr-xr-x 3 root users 4096 Feb  8 23:30 ..
drwxr-xr-x 2 root users 4096 Feb  9 00:00 basic-file-exploit
-rw-r--r-- 1 root users 1024 Feb  9 00:26 cpio.arch
drwxr-xr-x 2 root users 4096 Feb  9 00:05 file-run
-rw-r--r-- 1 root users  197 Mar 15  2022 flag
-rw-r--r-- 1 root users  255 Feb  9 00:27 flag.lzop
-rw-r--r-- 1 root users  283 Feb  9 00:27 flag.out.out
-rw-r--r-- 1 root users 5161 Feb  9 00:15 Flag.pdf
-rwxr-xr-x 1 root users 5161 Feb  9 00:17 Flag.sh
drwxr-xr-x 2 root users 4096 Feb  9 00:14 GDBTestDrive
 root  …  picoctf  writeups  picoCTF-2022  file flag
flag: lzip compressed data, version: 1
 root  …  picoctf  writeups  picoCTF-2022  file flag.
flag.: cannot open `flag.' (No such file or directory)
 root  …  picoctf  writeups  picoCTF-2022  file flag.lzop
flag.lzop: lzop compressed data - version 1.040, LZO1X-1, os: Unix
 root  …  picoctf  writeups  picoCTF-2022  file flag
flag: lzip compressed data, version: 1
 root  …  picoctf  writeups  picoCTF-2022  lzip -d flag
 root  …  picoctf  writeups  picoCTF-2022  ls -al
total 52
drwxr-xr-x 5 root users 4096 Feb  9 00:39 .
drwxr-xr-x 3 root users 4096 Feb  8 23:30 ..
drwxr-xr-x 2 root users 4096 Feb  9 00:00 basic-file-exploit
-rw-r--r-- 1 root users 1024 Feb  9 00:26 cpio.arch
drwxr-xr-x 2 root users 4096 Feb  9 00:05 file-run
-rw-r--r-- 1 root users  255 Feb  9 00:27 flag.lzop
-rw-r--r-- 1 root users  156 Mar 15  2022 flag.out
-rw-r--r-- 1 root users  283 Feb  9 00:27 flag.out.out
-rw-r--r-- 1 root users 5161 Feb  9 00:15 Flag.pdf
-rwxr-xr-x 1 root users 5161 Feb  9 00:17 Flag.sh
drwxr-xr-x 2 root users 4096 Feb  9 00:14 GDBTestDrive
 root  …  picoctf  writeups  picoCTF-2022  file flag.out
 root  …  picoctf  writeups  picoCTF-2022  file flag.out
flag.out: XZ compressed data, checksum CRC64
 root  …  picoctf  writeups  picoCTF-2022  xz
xz       xzcat    xzcmp    xzdec    xzdiff   xzegrep  xzfgrep  xzgrep   xzless   xzmore
 root  …  picoctf  writeups  picoCTF-2022  xz --help
Usage: xz [OPTION]... [FILE]...
Compress or decompress FILEs in the .xz format.

  -z, --compress      force compression
  -d, --decompress    force decompression
  -t, --test          test compressed file integrity
  -l, --list          list information about .xz files
  -k, --keep          keep (don't delete) input files
  -f, --force         force overwrite of output file and (de)compress links
  -c, --stdout        write to standard output and don't delete input files
  -0 ... -9           compression preset; default is 6; take compressor *and*
                      decompressor memory usage into account before using 7-9!
  -e, --extreme       try to improve compression ratio by using more CPU time;
                      does not affect decompressor memory requirements
  -T, --threads=NUM   use at most NUM threads; the default is 1; set to 0
                      to use as many threads as there are processor cores
  -q, --quiet         suppress warnings; specify twice to suppress errors too
  -v, --verbose       be verbose; specify twice for even more verbose
  -h, --help          display this short help and exit
  -H, --long-help     display the long help (lists also the advanced options)
  -V, --version       display the version number and exit

With no FILE, or when FILE is -, read standard input.

Report bugs to <xz@tukaani.org> (in English or Finnish).
XZ Utils home page: <https://tukaani.org/xz/>
 root  …  picoctf  writeups  picoCTF-2022  xz -d flag.out
xz: flag.out: Filename has an unknown suffix, skipping
 root  …  picoctf  writeups  picoCTF-2022  mv flag.out flag.xz
 root  …  picoctf  writeups  picoCTF-2022  xz -d flag.xz
 root  …  picoctf  writeups  picoCTF-2022  xz -d flag.xz
 root  …  picoctf  writeups  picoCTF-2022  ls -al
total 52
drwxr-xr-x 5 root users 4096 Feb  9 00:39 .
drwxr-xr-x 3 root users 4096 Feb  8 23:30 ..
drwxr-xr-x 2 root users 4096 Feb  9 00:00 basic-file-exploit
-rw-r--r-- 1 root users 1024 Feb  9 00:26 cpio.arch
drwxr-xr-x 2 root users 4096 Feb  9 00:05 file-run
-rw-r--r-- 1 root users  110 Mar 15  2022 flag
-rw-r--r-- 1 root users  255 Feb  9 00:27 flag.lzop
-rw-r--r-- 1 root users  283 Feb  9 00:27 flag.out.out
-rw-r--r-- 1 root users 5161 Feb  9 00:15 Flag.pdf
-rwxr-xr-x 1 root users 5161 Feb  9 00:17 Flag.sh
drwxr-xr-x 2 root users 4096 Feb  9 00:14 GDBTestDrive
 root  …  picoctf  writeups  picoCTF-2022  file flag
flag: ASCII text
 root  …  picoctf  writeups  picoCTF-2022  cat flag
7069636f4354467b66316c656e406d335f6d406e3170756c407431306e5f
6630725f3062326375723137795f33633739633562617d0a
 root  …  picoctf  writeups  picoCTF-2022  strings flag
7069636f4354467b66316c656e406d335f6d406e3170756c407431306e5f
6630725f3062326375723137795f33633739633562617d0a
 root  …  picoctf  writeups  picoCTF-2022  echo "picoCTF{f1len@m3_m@n1pul@t10n_"
picoCTF{f1len@m3_m@n1pul@t10n_
 root  …  picoctf  writeups  picoCTF-2022  echo "f0r_0b2cur17y_3c79c5ba}"
f0r_0b2cur17y_3c79c5ba}
 root  …  picoctf  writeups  picoCTF-2022  
```
