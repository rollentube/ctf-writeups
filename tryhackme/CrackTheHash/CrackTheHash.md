# Crack the hash
Cracking hashes challenges

## Hashes Level 1
| Hash                                                                                                      | Algorithm    | Method                    | Cracked      |
| --------------------------------------------------------------------------------------------------------- | ------------ | ------------------------- | ------------ |
| 48bb6e862e54f2a795ffc4e541caed4d                                                                          | MD5          | https://crackstation.net/ | easy         |
| CBFDAC6008F9CAB4083784CBD1874F76618D2A97                                                                  | SHA1         | https://crackstation.net/ | password123  |
| 1C8BFE8F801D79745C4631D09FFF36C82AA37FC4CCE4FC946683D7B336B63032                                          | SHA256       | https://crackstation.net/ | letmein      |
| $2y$12$Dwt1BZj6pcyc3Dy1FWZ5ieeUznr71EeNkJkUlypTsgbX1H68wsRom                                              | bcrypt       | john the ripper           | bleh         |
| 279412f945939ba78ce0758d3fd83daa                                                                          | MD4          | https://crackstation.net/ | Eternity22   |

## Hashes Level 2
| Hash                                                                                                      | Algorithm    | Method                    | Cracked      |
| --------------------------------------------------------------------------------------------------------- | ------------ | ------------------------- | ------------ |
| F09EDCB1FCEFC6DFB23DC3505A882655FF77375ED8AA2D1C13F640FCCC2D0C85                                          | SHA256       | https://crackstation.net/ | paule        |
| 1DFECA0C002AE40B8619ECF94819CC1B                                                                          | NTLM         | https://crackstation.net/ | n63umy8lkf4i |
| $6$aReallyHardSalt$6WKUTqzq.UQQmrm0p/T7MPpMbGNnzXPMAXi4bJMl9be.cfi3/qxIf.hsGpS41BqMhSrHVXgMpdjS6xeKZAs02. | SHA512CRYPT* | john the ripper           | waka99       |
| e5d8870e5bdd26602cab8dbe07a942c8669e56d6                                                                  | HMAC-SHA1*   | hashcat                   | 481616481616 |

\*salted
- SHA512CRYPT: aReallyHardSalt
- HMAC-SHA1: tryhackme

## John
```
john --format=Raw-MD5 hash rockyou.txt
john --format=Raw-MD5 --wordlist=rockyou.txt hash
john --show --format=Raw-MD5 hash
cat /home/root/.john/john.pot
john --format=Raw-MD5 hash
john --format=Raw-SHA1 --wordlist=rockyou.txt hash
john --format=Raw-SHA256 --wordlist=rockyou.txt hash
john --show --format=Raw-SHA256 hash
john --format=NT --wordlist=rockyou.txt hash
john --format=bcrypt --wordlist=rockyou.txt --max-length=4 hash
john --format=sha512crypt --wordlist=rockyou.txt hash
```

## Hashcat
```
hashcat -a 0 -m 160 e5d8870e5bdd26602cab8dbe07a942c8669e56d6:tryhackme /usr/share/wordlists/rockyou.txt
hashcat --show -a 0 -m 160 e5d8870e5bdd26602cab8dbe07a942c8669e56d6:tryhackme /usr/share/wordlists/rockyou.txt
```
