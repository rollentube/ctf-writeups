# SAM I AM
The attacker managed to gain Domain Admin on our rebels Domain Controller! Looks like they managed to log on with an account using WMI and dumped some files.

Can you reproduce how they got the Administrator's Password with the artifacts provided?

Place the Administrator Account's Password in DUCTF{}, e.g. DUCTF{password123!}

## Data
* samiam.zip
  * sam.bak
  * system.bak

## Solution
Provided is the SAM database of the Windows system. We can extract the NTML hashes from it:
```
┌──(kali㉿kali)-[~/Desktop/ductf/samiam]
└─$ samdump2 system.bak sam.bak
Administrator:500:aad3b435b51404eeaad3b435b51404ee:476b4dddbbffde29e739b618580adb1e:::
*disabled* Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::

┌──(kali㉿kali)-[~/Desktop/ductf/samiam]
└─$ 
```

The hash can easily be cracked with hashcat to get the administrator password:
```
┌──(kali㉿kali)-[~/Desktop/ductf/samiam]
└─$ hashcat -a 0 -m 1000 hashes /home/kali/Desktop/tools/rockyou.txt
hashcat (v6.2.6) starting

[...]

476b4dddbbffde29e739b618580adb1e:!checkerboard1           
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 1000 (NTLM)
Hash.Target......: hashes
Time.Started.....: Sat Jul  6 07:54:03 2024 (7 secs)
Time.Estimated...: Sat Jul  6 07:54:10 2024 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (/home/kali/Desktop/tools/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:  2261.7 kH/s (0.05ms) @ Accel:256 Loops:1 Thr:1 Vec:8
Recovered........: 2/2 (100.00%) Digests (total), 2/2 (100.00%) Digests (new)
Progress.........: 14340096/14344386 (99.97%)
Rejected.........: 0/14340096 (0.00%)
Restore.Point....: 14339584/14344386 (99.97%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#1....: !g0tt1986 -> !carrie!
Hardware.Mon.#1..: Util: 63%

Started: Sat Jul  6 07:53:40 2024
Stopped: Sat Jul  6 07:54:12 2024

┌──(kali㉿kali)-[~/Desktop/ductf/samiam]
└─$
```

So the flag is `DUCTF{!checkerboard1}`.
