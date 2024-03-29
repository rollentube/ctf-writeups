# Collaborative Development (75 points)
My team has been working very hard on new features for our flag printing program! I wonder how they'll work together?

## Data
* challenge.zip

## Solution
We have our git repository, but this time there is no flag directly in the git log:
```
$ ls -al
total 4
drwxr-xr-x  3 root      root   80 Mar 12 01:07 .
drwxrwxrwt 21 root      root  600 Mar 13 22:37 ..
-rw-r--r--  1 root      root   30 Mar 12 01:07 flag.py
drwxr-xr-x  8 root      root  260 Mar 12 01:07 .git
$ cat flag.py
print("Printing the flag...")
$ git log
commit 2258a0f267d57e8b6025e2a020b77fac7a553c92 (HEAD -> main)
Author: picoCTF <ops@picoctf.com>
Date:   Tue Mar 12 00:07:54 2024 +0000

    init flag printer
$
```

But can find out that there are several branches in this repo:
```
$ git branch
  feature/part-1
  feature/part-2
  feature/part-3
* main
$
```

With `git log --all` we can get all commits of all branches:
```
$ git log --all
commit 8eea0627726fc363246015cb4c7e927e70286e87 (feature/part-1)
Author: picoCTF <ops@picoctf.com>
Date:   Tue Mar 12 00:07:54 2024 +0000

    add part 1

commit 05db9e274ff691e0f9fb492403b570629eb80aa9 (feature/part-2)
Author: picoCTF <ops@picoctf.com>
Date:   Tue Mar 12 00:07:54 2024 +0000

    add part 2

commit 655c7bfebe9c221369ab00ac7374d0d4bd4d62a9 (HEAD -> feature/part-3)
Author: picoCTF <ops@picoctf.com>
Date:   Tue Mar 12 00:07:54 2024 +0000

    add part 3

commit 2258a0f267d57e8b6025e2a020b77fac7a553c92 (main)
Author: picoCTF <ops@picoctf.com>
Date:   Tue Mar 12 00:07:54 2024 +0000

    init flag printer
$
```

Seems like there could be some information in the branches. So lets check them out:
```
$ git checkout feature/part-1
Switched to branch 'feature/part-1'
$ cat flag.py
print("Printing the flag...")
print("picoCTF{t3@mw0rk_", end='')
$ git checkout feature/part-2
Switched to branch 'feature/part-2'
$ cat flag.py
print("Printing the flag...")

print("m@k3s_th3_dr3@m_", end='')
$ git checkout feature/part-3
Switched to branch 'feature/part-3'
$ cat flag.py
print("Printing the flag...")

print("w0rk_6c06cec1}")
$
```

We found in every branch a part of the flag. If we set them together we got it: `picoCTF{t3@mw0rk_m@k3s_th3_dr3@m_w0rk_6c06cec1}`
