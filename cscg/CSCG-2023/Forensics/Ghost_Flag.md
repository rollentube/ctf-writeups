# Ghost Flag
You got access to a secret flag server, but can you find the flag?

## Solution
Auf dem Server laeuft ein Nano Prozess, welcher die Datei 'flag' geoeffnet, allerdings nicht gespeichert hat:
```
ctf@ghost-flag-rudanecasn:/home/ctf$ ls -al
ls -al
total 1572
drwxr-x--- 1 ctf  ctf    4096 Mar  8 23:08 .
drwxr-xr-x 1 root root   4096 Mar  4 17:31 ..
-rw------- 1 ctf  ctf     378 Mar  8 23:09 .bash_history
-rw-r--r-- 1 ctf  ctf     220 Jan  6  2022 .bash_logout
-rw-r--r-- 1 ctf  ctf    3771 Jan  6  2022 .bashrc
-rw-r--r-- 1 ctf  ctf    1024 Mar  8 22:48 .flag.swp
drwxr-xr-x 3 ctf  ctf    4096 Mar  8 22:48 .local
-rw-r--r-- 1 ctf  ctf     807 Jan  6  2022 .profile
ctf@ghost-flag-rudanecasn:/home/ctf$
ctf@ghost-flag-rudanecasn:/home/ctf$ ps aux | grep nano
ps aux | grep nano
root           7  0.0  0.0  10288  2976 ?        S    22:48   0:00 socat EXEC:/usr/bin/nano /home/ctf/flag,SU=ctf,pty FILE:/dev/null,ignoreof
ctf           10  0.0  0.0   3996  2996 ?        S    22:48   0:00 /usr/bin/nano /home/ctf/flag
ctf          109  0.0  0.0   3468  1708 pts/1    S+   23:12   0:00 grep --color=auto nano
ctf@ghost-flag-rudanecasn:/home/ctf$
```

Wird ein Nano Prozess beendet, erstellt dieser eine Datei mit der Endung .save und sichert den ungeschriebenen Buffer (https://serverfault.com/questions/453703/can-i-recover-a-nano-process-from-a-previous-terminal). Allerdings funktioniert dies in diesem Fall nicht. Vermutlich da der Prozess gestoppt ist und keine TTY mehr vorhanden ist. Oder weil die Datei noch nicht erstellt wurde, sondern Nano nur mit dieser als Parameter gestartet wurde.

Da man mit den offenen Filedeskriptoren des Prozesses auch nicht weiter kommt, ist der naechste Anhaltspunkt den Prozessspeicher zu dumpen und zu analysieren. Auf dem System sind kaum Tools vorhanden, weshalb das folgende Skript verwendet werden kann:

```bash
procdump()
(
    cat /proc/$1/maps | grep -Fv ".so" | grep " 0 " | awk '{print $1}' | ( IFS="-"
    while read a b; do
        dd if=/proc/$1/mem bs=$( getconf PAGESIZE ) iflag=skip_bytes,count_bytes \
           skip=$(( 0x$a )) count=$(( 0x$b - 0x$a )) of="$1_mem_$a.bin"
    done )
    cat $1*.bin > $1.dump
    rm $1*.bin
)
# usage: procdump PID
procdump 10
```
(https://book.hacktricks.xyz/linux-hardening/privilege-escalation#processes oder auch https://serverfault.com/questions/173999/dump-a-linux-processs-memory-to-file)

Anschliessend kann man durch den Output greppen oder diesen anderweitig analysieren
```
ctf@ghost-flag-rudanecasn:/home/ctf$ ls -al
ls -al
total 1572
drwxr-x--- 1 ctf  ctf    4096 Mar  8 23:08 .
drwxr-xr-x 1 root root   4096 Mar  4 17:31 ..
-rw------- 1 ctf  ctf     378 Mar  8 23:09 .bash_history
-rw-r--r-- 1 ctf  ctf     220 Jan  6  2022 .bash_logout
-rw-r--r-- 1 ctf  ctf    3771 Jan  6  2022 .bashrc
-rw-r--r-- 1 ctf  ctf    1024 Mar  8 22:48 .flag.swp
drwxr-xr-x 3 ctf  ctf    4096 Mar  8 22:48 .local
-rw-r--r-- 1 ctf  ctf     807 Jan  6  2022 .profile
-rw-r--r-- 1 ctf  ctf    4096 Mar  8 22:51 10_mem_5635c7b66000.bin
-rw-r--r-- 1 ctf  ctf  675840 Mar  8 22:51 10_mem_5635c9276000.bin
-rw-r--r-- 1 ctf  ctf    8192 Mar  8 22:51 10_mem_7f7933185000.bin
-rw-r--r-- 1 ctf  ctf   53248 Mar  8 22:51 10_mem_7f79333a2000.bin
-rw-r--r-- 1 ctf  ctf    8192 Mar  8 22:51 10_mem_7f793341f000.bin
-rw-r--r-- 1 ctf  ctf  135168 Mar  8 22:51 10_mem_7ffeded30000.bin
-rw-r--r-- 1 ctf  ctf       0 Mar  8 22:51 10_mem_7ffeded92000.bin
-rw-r--r-- 1 ctf  ctf    8192 Mar  8 22:51 10_mem_7ffeded96000.bin
-rw-r--r-- 1 ctf  ctf       0 Mar  8 22:51 10_mem_ffffffffff600000.bin
-rw-r--r-- 1 ctf  ctf     299 Mar  8 22:51 dump
-rw-r--r-- 1 ctf  ctf  675840 Mar  8 23:08 out_mem
ctf@ghost-flag-rudanecasn:/home/ctf$ grep -a -i cscg 10*
grep -a -i cscg 10*
10_mem_5635c9276000.bin:I=3yQI=3yRI=3ySI=3yTI=3yU#I=3yV)I=3yW/I=3yX4I=3yY:I=3yZ?I=3y[XDI=3y\II=3y]NI=3y^|TI=3y_ZI=3y`_I=3yaeI=3yb[jI=3ycpI=3ydvI=3ye|I=3yfWI=3J=3y(J=3y)J=3y$J=3y%J=3y&J=3yJ=3yJ=3y*J=3y+J=3yJ=3yJ=3yJ=3yJ=3yJ=3yJ=3yJ=3yJ=3yJ=3y<J=3yyJ=3yJ=3yJ=3y!Qs0Vyk}rsP!/home/ctf/flag!CSCG{d3l3t3d_fl4g}!.5V!/r0V!/home/ctf/.flag.swpctfx1000:1000:/home/ctf//bin/bashn/nologin/nologinats/usr/sbin/nologin\cyk}rsP
ctf@ghost-flag-rudanecasn:/home/ctf$
```

Hier kann dann die Flag gefunden werden: CSCG{d3l3t3d\_fl4g}


Alternativ kann man den Heap auch per Hand dumpen
```
ctf@ghost-flag-rudanecasn:/home/ctf$ cd /proc/10
cd /proc/10
ctf@ghost-flag-rudanecasn:/proc/10$ cat maps
cat maps
5635c7b20000-5635c7b25000 r--p 00000000 08:03 3432028                    /usr/bin/nano
5635c7b25000-5635c7b57000 r-xp 00005000 08:03 3432028                    /usr/bin/nano
5635c7b57000-5635c7b63000 r--p 00037000 08:03 3432028                    /usr/bin/nano
5635c7b64000-5635c7b65000 r--p 00043000 08:03 3432028                    /usr/bin/nano
5635c7b65000-5635c7b66000 rw-p 00044000 08:03 3432028                    /usr/bin/nano
5635c7b66000-5635c7b67000 rw-p 00000000 00:00 0
5635c9276000-5635c931b000 rw-p 00000000 00:00 0                          [heap]
7f7933185000-7f7933187000 rw-p 00000000 00:00 0
7f7933187000-7f79331af000 r--p 00000000 08:03 3423724                    /usr/lib/x86_64-linux-gnu/libc.so.6
7f79331af000-7f7933344000 r-xp 00028000 08:03 3423724                    /usr/lib/x86_64-linux-gnu/libc.so.6
7f7933344000-7f793339c000 r--p 001bd000 08:03 3423724                    /usr/lib/x86_64-linux-gnu/libc.so.6
7f793339c000-7f79333a0000 r--p 00214000 08:03 3423724                    /usr/lib/x86_64-linux-gnu/libc.so.6
7f79333a0000-7f79333a2000 rw-p 00218000 08:03 3423724                    /usr/lib/x86_64-linux-gnu/libc.so.6
7f79333a2000-7f79333af000 rw-p 00000000 00:00 0
7f79333af000-7f79333bd000 r--p 00000000 08:03 3423842                    /usr/lib/x86_64-linux-gnu/libtinfo.so.6.3
7f79333bd000-7f79333ce000 r-xp 0000e000 08:03 3423842                    /usr/lib/x86_64-linux-gnu/libtinfo.so.6.3
7f79333ce000-7f79333dc000 r--p 0001f000 08:03 3423842                    /usr/lib/x86_64-linux-gnu/libtinfo.so.6.3
7f79333dc000-7f79333e0000 r--p 0002c000 08:03 3423842                    /usr/lib/x86_64-linux-gnu/libtinfo.so.6.3
7f79333e0000-7f79333e1000 rw-p 00030000 08:03 3423842                    /usr/lib/x86_64-linux-gnu/libtinfo.so.6.3
7f79333e1000-7f79333e9000 r--p 00000000 08:03 3423788                    /usr/lib/x86_64-linux-gnu/libncursesw.so.6.3
7f79333e9000-7f7933412000 r-xp 00008000 08:03 3423788                    /usr/lib/x86_64-linux-gnu/libncursesw.so.6.3
7f7933412000-7f793341a000 r--p 00031000 08:03 3423788                    /usr/lib/x86_64-linux-gnu/libncursesw.so.6.3
7f793341a000-7f793341b000 ---p 00039000 08:03 3423788                    /usr/lib/x86_64-linux-gnu/libncursesw.so.6.3
7f793341b000-7f793341c000 r--p 00039000 08:03 3423788                    /usr/lib/x86_64-linux-gnu/libncursesw.so.6.3
7f793341c000-7f793341d000 rw-p 0003a000 08:03 3423788                    /usr/lib/x86_64-linux-gnu/libncursesw.so.6.3
7f793341f000-7f7933421000 rw-p 00000000 00:00 0
7f7933421000-7f7933423000 r--p 00000000 08:03 3423706                    /usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2
7f7933423000-7f793344d000 r-xp 00002000 08:03 3423706                    /usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2
7f793344d000-7f7933458000 r--p 0002c000 08:03 3423706                    /usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2
7f7933459000-7f793345b000 r--p 00037000 08:03 3423706                    /usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2
7f793345b000-7f793345d000 rw-p 00039000 08:03 3423706                    /usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2
7ffeded30000-7ffeded51000 rw-p 00000000 00:00 0                          [stack]
7ffeded92000-7ffeded96000 r--p 00000000 00:00 0                          [vvar]
7ffeded96000-7ffeded98000 r-xp 00000000 00:00 0                          [vdso]
ffffffffff600000-ffffffffff601000 --xp 00000000 00:00 0                  [vsyscall]
ctf@ghost-flag-rudanecasn:/proc/10$ dd if=mem bs=1 of=/home/ctf/out_mem skip=$((0x5635c9276000)) count=$((0xa5000))
<out_mem skip=$((0x5635c9276000)) count=$((0xa5000))
dd: mem: cannot skip to specified offset
675840+0 records in
675840+0 records out
675840 bytes (676 kB, 660 KiB) copied, 1.24522 s, 543 kB/s
ctf@ghost-flag-rudanecasn:/proc/10$ ls -al /home/ctf
ls -al /home/ctf
total 1572
drwxr-x--- 1 ctf  ctf    4096 Mar  8 23:08 .
drwxr-xr-x 1 root root   4096 Mar  4 17:31 ..
-rw------- 1 ctf  ctf     206 Mar  8 22:59 .bash_history
-rw-r--r-- 1 ctf  ctf     220 Jan  6  2022 .bash_logout
-rw-r--r-- 1 ctf  ctf    3771 Jan  6  2022 .bashrc
-rw-r--r-- 1 ctf  ctf    1024 Mar  8 22:48 .flag.swp
drwxr-xr-x 3 ctf  ctf    4096 Mar  8 22:48 .local
-rw-r--r-- 1 ctf  ctf     807 Jan  6  2022 .profile
-rw-r--r-- 1 ctf  ctf    4096 Mar  8 22:51 10_mem_5635c7b66000.bin
-rw-r--r-- 1 ctf  ctf  675840 Mar  8 22:51 10_mem_5635c9276000.bin
-rw-r--r-- 1 ctf  ctf    8192 Mar  8 22:51 10_mem_7f7933185000.bin
-rw-r--r-- 1 ctf  ctf   53248 Mar  8 22:51 10_mem_7f79333a2000.bin
-rw-r--r-- 1 ctf  ctf    8192 Mar  8 22:51 10_mem_7f793341f000.bin
-rw-r--r-- 1 ctf  ctf  135168 Mar  8 22:51 10_mem_7ffeded30000.bin
-rw-r--r-- 1 ctf  ctf       0 Mar  8 22:51 10_mem_7ffeded92000.bin
-rw-r--r-- 1 ctf  ctf    8192 Mar  8 22:51 10_mem_7ffeded96000.bin
-rw-r--r-- 1 ctf  ctf       0 Mar  8 22:51 10_mem_ffffffffff600000.bin
-rw-r--r-- 1 ctf  ctf     299 Mar  8 22:51 dump
-rw-r--r-- 1 ctf  ctf  675840 Mar  8 23:08 out_mem
ctf@ghost-flag-rudanecasn:/proc/10$ grep -a -i cscg /home/ctf/out_mem
grep -a -i cscg /home/ctf/out_mem
I=3yQI=3yRI=3ySI=3yTI=3yU#I=3yV)I=3yW/I=3yX4I=3yY:I=3yZ?I=3y[XDI=3y\II=3y]NI=3y^|TI=3y_ZI=3y`_I=3yaeI=3yb[jI=3ycpI=3ydvI=3ye|I=3yfWI=3ygI=3yhI=3yiI=3yjI=3ykI=J=3y(J=3y)J=3y$J=3y%J=3y&J=3yJ=3yJ=3y*J=3y+J=3yJ=3yJ=3yJ=3yJ=3yJ=3yJ=3yJ=3yJ=3yJ=3y<J=3yyJ=3yJ=3yJ=3y!Qs0Vyk}rsP!/home/ctf/flag!CSCG{d3l3t3d_fl4g}!.5V!/r0V!/home/ctf/.flag.swpctfx1000:1000:/home/ctf//bin/bashn/nologin/nologinats/usr/sbin/nologin\cyk}rsP
ctf@ghost-flag-rudanecasn:/proc/10$
```

In dem Skript wird die Flag ebenfalls durch den Dump von dem Heap gefunden.
