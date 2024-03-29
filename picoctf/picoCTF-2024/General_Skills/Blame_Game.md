# Blame Game (75 points)
Someone's commits seems to be preventing the program from working. Who is it?

## Data
* challenge.zip

## Solution
Like in the challenges before, we have again our git repository. But this time there is a bracket missing:
```
$ ls -al
total 4
drwxr-xr-x  3 root      root   80 Mar 12 01:07 .
drwxrwxrwt 22 root      root  600 Mar 13 22:27 ..
drwxr-xr-x  8 root      root  260 Mar 12 01:07 .git
-rw-r--r--  1 root      root   22 Mar 12 01:07 message.py
$ cat message.py
print("Hello, World!"
$
```

Since the challenge is called _Blame Game_ we probably have to `git blame` the user who made this mistake:
```
$ git blame message.py
8c83358c (picoCTF{@sk_th3_1nt3rn_2c6bf174} 2024-03-12 00:07:11 +0000 1) print("Hello, World!"
$
```
Yep, here we got our flag.

We can also find this information in the git log. There are many commits, but the penultimate entry brings us also the flag:
```
$ git log -p

[...]

commit 8c83358c32daee3f8b597d2b853c1d1966b23f0a
Author: picoCTF{@sk_th3_1nt3rn_2c6bf174} <ops@picoctf.com>
Date:   Tue Mar 12 00:07:11 2024 +0000

    optimize file size of prod code

diff --git a/message.py b/message.py
index 7df869a..326544a 100644
--- a/message.py
+++ b/message.py
@@ -1 +1 @@
-print("Hello, World!")
+print("Hello, World!"

commit caa945839a2fc0fb52584b559b4e89ac7c46bf54
Author: picoCTF <ops@picoctf.com>
Date:   Tue Mar 12 00:07:11 2024 +0000

    create top secret project

diff --git a/message.py b/message.py
new file mode 100644
index 0000000..7df869a
--- /dev/null
+++ b/message.py
@@ -0,0 +1 @@
+print("Hello, World!")
```


