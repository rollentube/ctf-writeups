# packer
Reverse this linux executable?

## Data
* out

## Solution
The given binary takes a password input and tries to validate it:
```
$ ./out
Enter the password to unlock this file: AAAA
You entered: AAAA

Access denied
$
```

But if we analyse the file we can see an UPX header:
```
$ file out
out: ELF 64-bit LSB executable, x86-64, version 1 (GNU/Linux), statically linked, no section header
$ strings out | head
UPX!<
P/PI
}_PzH
F^lx/
Bf/P
@/ j
ME=n
[GSd2
t>d4
8%'u
$
```

We can also open the binary in Ghidra and search for strings. Here we can find the following ones:
```
"$Info: This file is packed with the UPX executable packer http://upx.sf.net $\n"
"$Id: UPX 3.95 Copyright (C) 1996-2018 the UPX Team. All Rights Reserved. $\n"
```

UPX is a packer for executable files. Means that it compresses a binary if we pack it.

So the next step is to decompress the file. We can do this with the `upx` utility:
```
$ upx -d out
                       Ultimate Packer for eXecutables
                          Copyright (C) 1996 - 2024
UPX 4.2.2       Markus Oberhumer, Laszlo Molnar & John Reiser    Jan 3rd 2024

        File size         Ratio      Format      Name
   --------------------   ------   -----------   -----------
    877724 <-    336520   38.34%   linux/amd64   out

Unpacked 1 file.
$
```

If we compare the file sizes before and after, we can clearly see the decompression:
```
$ ls -al out
-rwxr-xr-x  1 root      root  336520 Mar 16 01:01 out
$

[...]

$ ls -al out
-rwxr-xr-x  1 root      root  872088 Mar 16 01:01 out
$ 
```

We get now more information about the binary:
```
$ file out
out: ELF 64-bit LSB executable, x86-64, version 1 (GNU/Linux), statically linked, BuildID[sha1]=36bf0fdfd791fee2c1cc45dff9ddb2a4f48f6d53, for GNU/Linux 3.2.0, not stripped
$
```

It's time to decompile it again with Ghidra. If we open the main function, we find the output if our entered password is correct:
```c
  if (iVar3 == 0) {
    *(undefined8 *)(puVar4 + -0x78) = 0x401f57;
    puts(
        "Password correct, please see flag: 7069636f4354467b5539585f556e5034636b314e365f42316e34526933535f39343130343638327d"
        );
    *(undefined8 *)(puVar4 + -0x78) = 0x401f63;
    puts((char *)&pass);
  }
```
`7069636f4354467b5539585f556e5034636b314e365f42316e34526933535f39343130343638327d` seems to be the flag in some kind.

If we throw this into CyberChef end decode it from hex we get our flag: `picoCTF{U9X_UnP4ck1N6_B1n4Ri3S_94104682}`
