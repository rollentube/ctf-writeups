# GDB Test Drive
Can you get the flag?

Here's the test drive instructions:
```
$ chmod +x gdbme
$ gdb gdbme
(gdb) layout asm
(gdb) break *(main+99)
(gdb) run
(gdb) jump *(main+104)
```

## Loesung
Setzt man einen Breakpoint in der Main und geht die Funktion durch, sieht man einen Aufruf von 'sleep' mit einer sehr hohen Zeit. Mit einem 'jump' kann man diese Funktion ueberspringen. Danach wird die Flag ausgeben.
```
──────────────────────────────────────────────────────────────────────────[ DISASM ]──────────────────────────────────────────────────────────────────────────
   0x55555555530f <main+72>     movabs rdx, 0x4e32676662346668
   0x555555555319 <main+82>     mov    qword ptr [rbp - 0x20], rax
   0x55555555531d <main+86>     mov    qword ptr [rbp - 0x18], rdx
   0x555555555321 <main+90>     mov    byte ptr [rbp - 0x10], 0
   0x555555555325 <main+94>     mov    edi, 0x186a0
 ► 0x55555555532a <main+99>     call   sleep@plt                <sleep@plt>
        seconds: 0x186a0

   0x55555555532f <main+104>    lea    rax, [rbp - 0x30]
   0x555555555333 <main+108>    mov    rsi, rax
   0x555555555336 <main+111>    mov    edi, 0
   0x55555555533b <main+116>    call   rotate_encrypt                <rotate_encrypt>

   0x555555555340 <main+121>    mov    qword ptr [rbp - 0x38], rax
──────────────────────────────────────────────────────────────────────────[ STACK ]───────────────────────────────────────────────────────────────────────────
00:0000│ rsp 0x7fffffffe350 —▸ 0x7fffffffe4b8 —▸ 0x7fffffffe802 ◂— '/home/root/ctf/picoctf/writeups/picoCTF-2022/GDBTestDrive/gdbme'
01:0008│     0x7fffffffe358 ◂— 0x100000000
02:0010│     0x7fffffffe360 ◂— 0x0
03:0018│     0x7fffffffe368 ◂— 0x0
04:0020│     0x7fffffffe370 ◂— 'A:4@r%uL5b3F88bC05C`Gb0`hf4bfg2N'
05:0028│     0x7fffffffe378 ◂— '5b3F88bC05C`Gb0`hf4bfg2N'
06:0030│     0x7fffffffe380 ◂— '05C`Gb0`hf4bfg2N'
07:0038│     0x7fffffffe388 ◂— 'hf4bfg2N'
────────────────────────────────────────────────────────────────────────[ BACKTRACE ]─────────────────────────────────────────────────────────────────────────
 ► f 0   0x55555555532a main+99
   f 1   0x7ffff7dc8290
   f 2   0x7ffff7dc834a __libc_start_main+138
   f 3   0x55555555514e _start+46
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
pwndbg> jump 0x55555555532f
Function "0x55555555532f" not defined.
pwndbg> jump *0x55555555532f
Continuing at 0x55555555532f.
picoCTF{d3bugg3r_dr1v3_197c378a}
[Inferior 1 (process 45249) exited normally]
pwndbg>
```
