# Commitment Issues (50 points)
I accidentally wrote the flag down. Good thing I deleted it!

## Data
* challenge.zip

## Solution
If we extract the zip file, we get a folder with a txt file:
```
$ ls -al
total 4
drwxr-xr-x  3 root      root   80 Mar 12 01:06 .
drwxrwxrwt 16 root      root  420 Mar 12 23:43 ..
drwxr-xr-x  8 root      root  260 Mar 12 23:42 .git
-rw-r--r--  1 root      root   11 Mar 12 01:06 message.txt
$ cat message.txt
TOP SECRET
$
```

Since it seems to be a git repository, we can check the commits with `git log` and get some information if the content of the file was changed:
```
$ git log
commit 42942c9c605b30100f5d859ef6e172027447c0db (HEAD -> master)
Author: picoCTF <ops@picoctf.com>
Date:   Tue Mar 12 00:06:23 2024 +0000

    remove sensitive info

commit b562f0b425907789d11d2fe2793e67592dc6be93
Author: picoCTF <ops@picoctf.com>
Date:   Tue Mar 12 00:06:23 2024 +0000

    create flag
$
```

Seems like the intersting part was removed from the file. With `git log -p` we can get the difference in each commit:
```
$ git log -p
commit 42942c9c605b30100f5d859ef6e172027447c0db (HEAD -> master)
Author: picoCTF <ops@picoctf.com>
Date:   Tue Mar 12 00:06:23 2024 +0000

    remove sensitive info

diff --git a/message.txt b/message.txt
index 0e0fefc..d552d1e 100644
--- a/message.txt
+++ b/message.txt
@@ -1 +1 @@
-picoCTF{s@n1t1z3_c785c319}
+TOP SECRET

commit b562f0b425907789d11d2fe2793e67592dc6be93
Author: picoCTF <ops@picoctf.com>
Date:   Tue Mar 12 00:06:23 2024 +0000

    create flag

diff --git a/message.txt b/message.txt
new file mode 100644
index 0000000..0e0fefc
--- /dev/null
+++ b/message.txt
@@ -0,0 +1 @@
+picoCTF{s@n1t1z3_c785c319}
$
```

And here we found our flag.
