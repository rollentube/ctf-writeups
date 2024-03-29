# Time Machine (50 points)
What was I last working on? I remember writing a note to help me remember...

## Data
* challenge.zip

## Solution
If we extract the zip, we find again a git repository:
```
$ ls -al
total 4
drwxr-xr-x  3 root      root   80 Mar 12 01:07 .
drwxrwxrwt 16 root      root  440 Mar 12 23:51 ..
drwxr-xr-x  8 root      root  260 Mar 12 01:07 .git
-rw-r--r--  1 root      root   87 Mar 12 01:07 message.txt
$
```

The content of the txt file tells us that their could be some information in the git history:
```
$ cat message.txt
This is what I was working on, but I'd need to look at my commit history to know why...$
$
```

Taking a look into the `git log` gives us the flag:
```
$ git log
commit 712314f105348e295f8cadd7d7dc4e9fa871e9a2 (HEAD -> master)
Author: picoCTF <ops@picoctf.com>
Date:   Tue Mar 12 00:07:26 2024 +0000

    picoCTF{t1m3m@ch1n3_e8c98b3a}
$
```
