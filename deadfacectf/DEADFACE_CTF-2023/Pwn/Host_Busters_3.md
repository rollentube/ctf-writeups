# Host Busters 3 (100 points)
Continue characterizing the machine. Is there any way you can escalate to a user that has permissions the vim user does not have? Find the flag associated with this user.

Submit the flag as `flag{flag_here}`.

`vim@gh0st404.deadface.io`

Password: `letmevim`

## Solution
As already mentioned in [Host Busters 1](./Host_Busters_1.md) we can use the private ssh key to log in as `gh0st404` and find the flag:
```
vim@25debd5e0e7b:/home/gh0st404$ ssh -i id_rsa gh0st404@localhost
Linux 25debd5e0e7b 5.10.0-26-amd64 #1 SMP Debian 5.10.197-1 (2023-09-29) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Sat Oct 21 11:08:12 2023 from 127.0.0.1
gh0st404@25debd5e0e7b:~$ cat hostbusters3.txt
flag{Embr4c3_th3_K3y_t0_5ucc355!}
gh0st404@25debd5e0e7b:~$
```