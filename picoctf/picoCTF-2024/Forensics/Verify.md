# Verify (50 points)
People keep trying to trick my players with imitation flags. I want to make sure they get the real thing! I'm going to provide the SHA-256 hash and a decrypt script to help you know that my flags are legitimate.

The same files are accessible via SSH here: `ssh -p 61308 ctf-player@rhea.picoctf.net`

Using the password `1db87a14`. Accept the fingerprint with yes, and ls once connected to begin. Remember, in a shell, passwords are hidden!

Checksum: 55b983afdd9d10718f1db3983459efc5cc3f5a66841e2651041e25dec3efd46a

To decrypt the file once you've verified the hash, run `./decrypt.sh files/<file>`.

## Data
* challenge.zip

## Solution
We have the following files:
```
$ ls -al
total 12
drwxr-xr-x 3 root      root   120 Mar 16 16:19 .
drwxr-xr-x 3 root      root    60 Mar 16 16:09 ..
-rw-r--r-- 1 root      root    65 Mar 12 01:09 checksum.txt
-rwxr-xr-x 1 root      root   856 Mar 12 01:09 decrypt.sh
drwxr-xr-x 2 root      root  6060 Mar 12 01:09 files
$ 
```
* `checksum.txt` contains the same SHA-256 Hash like in the description
* `files/` contains a lot of encrypted files with random names
* `decrypt.sh` is a script to decrypt a files in `files/`

Our goal is now to find the file inside `files/` with the given checksum.

To do so we can use a short python script:
```python
import os
import hashlib

directory = "files"
to_find = "55b983afdd9d10718f1db3983459efc5cc3f5a66841e2651041e25dec3efd46a"

for file in os.listdir(directory):
    f = os.path.join(directory, file)
    if not os.path.isfile(f):
        continue
    sha256_hash = hashlib.sha256(open(f, "rb").read()).hexdigest()
    if sha256_hash == to_find:
        print(f)
```
The script iterates over all files, create their SHA-256 hash and compares it to the given one. If it matches we will print out the filename.

Let's run it:
```
$ python validate.py
files/2cdcb2de
$
```

Now we can decrypt this file:
```
$ ./decrypt.sh files/2cdcb2de
picoCTF{trust_but_verify_2cdcb2de}
$ 
```

Aaand we got our flag.
