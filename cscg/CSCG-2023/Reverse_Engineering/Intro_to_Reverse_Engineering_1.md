# Intro to Reverse Engineering 1
Let's have a gentle introduction to reverse engineering x86\_64 binaries on Linux. You can find a detailed writeup with many basics and solutions to this challenge attached :)

## Solution
Mit Strings das gesuchte Passwort gefunden
```
Give me your password:
m4gic_passw0rd
Thats the right password!
```

```
 root  ~  ctf  cscg_23  reverse_1  ncat --ssl fca9e5b9c6957c20501d449f-intro-rev-1.challenge.master.cscg.live 31337
Give me your password:
m4gic_passw0rd
Thats the right password!
Flag: CSCG{congrats_t0_y0ur_(maybe?)_f1rst_r3versing_task}
^C
 root  ~  ctf  cscg_23  reverse_1                                                                                                           SIGINT 
```
