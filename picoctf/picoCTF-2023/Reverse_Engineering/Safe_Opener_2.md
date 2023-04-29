# Safe Opener 2
What can you do with this file?
I forgot the key to my safe but this file is supposed to help me with retrieving the lost key. Can you help me unlock my safe? (100 Points)

## Files
- SafeOpener.class

## Solution
With 'strings' you can find the flag pretty easy
```
[root@picoctf Safe_Opener_2]$ strings SafeOpener.class | grep pico
,picoCTF{SAf3_0p3n3rr_y0u_solv3d_it_d6afee27}
[root@picoctf Safe_Opener_2]$
```
