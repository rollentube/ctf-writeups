# HideToSee
How about some hide and seek heh? (100 Points)
Look at this image here.

## Files
- atbash.jpg

## Solution
Used 'steghide' to extract stego data (no password, classic CTF variant)
```
[root@picoctf HideToSee]$ steghide extract -sf atbash.jpg
Enter passphrase:
wrote extracted data to "encrypted.txt".
[root@picoctf HideToSee]$ cat encrypted.txt
krxlXGU{zgyzhs_xizxp_7867098z}
[root@picoctf HideToSee]$
```

The picture shows the Atbash Cipher. So its obvious that the flag is encrypted with this cipher. CyberChef has a recipe for it and can decrypt it:
picoCTF{atbash\_crack\_7867098a}
