# hideme
Every file gets a flag.
The SOC analyst saw one image been sent back and forth between two people. They decided to investigate and found out that there was more than what meets the eye here.

## Files
- flag.png

## Solution
Getting an overview with tools like strings and hexdump. Here we can see, that there is content after the end of the png file. So we run binwalk.
```
[root@picoctf hideme]$ binwalk -e flag.png

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 512 x 504, 8-bit/color RGBA, non-interlaced
41            0x29            Zlib compressed data, compressed
39739         0x9B3B          Zip archive data, at least v1.0 to extract, name: secret/
39804         0x9B7C          Zip archive data, at least v2.0 to extract, compressed size: 3004, uncompressed size: 3162, name: secret/flag.png
43043         0xA823          End of Zip archive, footer length: 22

[root@picoctf hideme]$ ls -al
total 56
drwxr-xr-x 3 root users  4096 Mar 15 22:38 .
drwxr-xr-x 3 root users  4096 Mar 15 22:35 ..
-rw-r--r-- 1 root users 43065 Mar 15 22:36 flag.png
drwxr-xr-x 3 root users  4096 Mar 15 22:38 _flag.png.extracted
[root@picoctf hideme]$ cd _flag.png.extracted/
[root@picoctf _flag.png.extracted]$ ls -al
total 60
drwxr-xr-x 3 root users  4096 Mar 15 22:38 .
drwxr-xr-x 3 root users  4096 Mar 15 22:38 ..
-rw-r--r-- 1 root users     0 Mar 15 22:38 29
-rw-r--r-- 1 root users 43024 Mar 15 22:38 29.zlib
-rw-r--r-- 1 root users  3326 Mar 15 22:38 9B3B.zip
drwxr-xr-x 2 root users  4096 Mar 15 03:30 secret
[root@picoctf _flag.png.extracted]$ cd secret/
[root@picoctf secret]$ ls -al
total 12
drwxr-xr-x 2 root users 4096 Mar 15 03:30 .
drwxr-xr-x 3 root users 4096 Mar 15 22:38 ..
-rw-r--r-- 1 root users 3162 Mar 15 03:30 flag.png
[root@picoctf secret]$
```
With binwalk we can extract a folder called 'secret/', containing another flag.png file. This image file contains the flag.

The flag is: picoCTF{Hiddinng\_An\_imag3\_within\_@n\_ima9e\_683e597b}}
