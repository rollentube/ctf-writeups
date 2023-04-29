# rotation
You will find the flag after decrypting this file (100 Points)
Download the encrypted flag here.

## Files
- encrypted.txt

## Solution
```
[root@picoctf rotation]$ cat encrypted.txt
xqkwKBN{z0bib1wv_l3kzgxb3l_7mkl1k61}
[root@picoctf rotation]$
```

The challange name could be a hint for the encryption. So we try ROT13, a classic rotation cipher. Its not the right one, so we increase the ROT Cipher in CyberChef. ROT13 with amount '18' decrypted it: picoCTF{r0tat1on\_d3crypt3d\_7ecd1c61}
