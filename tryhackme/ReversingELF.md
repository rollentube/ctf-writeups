# Reversing ELF
## Task1
Ausfuehren der Datei gibt Flag. Iteriert ueber einen Encoded String und fuegt jedem Char 0x41 hinzu.
```
 root  …  tryhackme  writeups  ReversingELF  ./crackme1
flag{not_that_kind_of_elf}
 root  …  tryhackme  writeups  ReversingELF  
```

## Task 2
Mit Strings oder Ghidra kann das Kennwort gefunden werden: _super\_secret\_password_

Dieses kann dann eingegeben werden und man erhaelt die Flag
```
 root  …  tryhackme  writeups  ReversingELF  strings crackme2 | less
 root  …  tryhackme  writeups  ReversingELF  ./crackme2 super_secret_password
Access granted.
flag{if_i_submit_this_flag_then_i_will_get_points}
 root  …  tryhackme  writeups  ReversingELF  
```

## Task 3
Mit Strings oder Ghidra kann des Kennwort gefunden werden. Dieses ist Base64 encoded, decoded man dieses hat man die Flag bereits gefunden.
```
 root  …  tryhackme  writeups  ReversingELF  strings crackme3 | less
 root  …  tryhackme  writeups  ReversingELF  ./crackme3 f0r_y0ur_5ec0nd_le55on_unbase64_4ll_7h3_7h1ng5
Correct password!
 root  …  tryhackme  writeups  ReversingELF  
```

## Task 4
In Ghidra sieht man, dass eine Funktion aufgerufen wird, welche einen Encoded String Zeichenweise XOR 0x24 decoded. Anschliessend wird das Ergebnis mit der Eingabe verglichen. Betrachtet man diese Stelle in gdb sieht man das Kennwort: _my\_m0r3\_secur3\_pwd_

Hierbei handelt es sich auch um die Flag:
```
 root  …  tryhackme  writeups  ReversingELF  ./crackme4 my_m0r3_secur3_pwd
password OK
 root  …  tryhackme  writeups  ReversingELF  
```

## Task 5
Betrachtet man das Programm in Ghidra sieht man, dass die Eingabe mit einem String verglichen wird (ueber Umwege, allerdings macht dies kein Unterschied). Dieser ist auch die Flag. In gdb kann dies auch nachvollzogen werden:

Peda
```
Guessed arguments:
arg[0]: 0x7fffffffe1a0 ('A' <repeats 17 times>)
arg[1]: 0x7fffffffe1c0 ("OfdlDSA|3tXb32~X3tX@sX`4tXtz\377\177")
arg[2]: 0x7fffffffe1c0 ("OfdlDSA|3tXb32~X3tX@sX`4tXtz\377\177")
```

pwndbg
```
 ► 0x40082f <main+188>    call   strcmp_                      <strcmp_>
        rdi: 0x7fffffffe1a0 ◂— 'AAAAAAAAAAAAAAAAAAAAAAAAA'
        rsi: 0x7fffffffe1c0 ◂— 0x7c4153446c64664f ('OfdlDSA|')
        rdx: 0x7fffffffe1c0 ◂— 0x7c4153446c64664f ('OfdlDSA|')
        rcx: 0x0
[...]
pwndbg> x/s 0x7fffffffe1c0
0x7fffffffe1c0: "OfdlDSA|3tXb32~X3tX@sX`4tXtz\377\177"
pwndbg>
```

Eingabe
```
 root  …  tryhackme  writeups  ReversingELF  ./crackme5
Enter your input:
OfdlDSA|3tXb32~X3tX@sX`4tXtz
Good game
 root  …  tryhackme  writeups  ReversingELF  
```

## Task 6
In Ghidra findet man eine Funktion, welche das Kennwort mit IF Bedingungen ueberprueft. Der Key wird hier Zeichenweise getestet. Aus den Befindungen kann man die Flag ablesen:
```
 root  …  tryhackme  writeups  ReversingELF  ./crackme6 1337_pwd
password OK
 root  …  tryhackme  writeups  ReversingELF  
```

## Task 7
In Ghidra findet man neben den geforderten Zahlen eine weitere Bedinungen, welche abgefragt wird:
```c
  else if (local_14 == 31337) {
    puts("Wow such h4x0r!");
    giveFlag();
  }
```

Gibt man also die Zahl ein, erhaelt man die Flag:
```
 root  …  tryhackme  writeups  ReversingELF  ./crackme7
Menu:

[1] Say hello
[2] Add numbers
[3] Quit

[>] 31337
Wow such h4x0r!
flag{much_reversing_very_ida_wow}
 root  …  tryhackme  writeups  ReversingELF  
```

## Task 8
Betrachtet man das Programm in Ghidara sieht man, dass dieses die Eingabe mit atoi in einen Int wandelt und diesen abgleicht:
```c
input_i = atoi((char *)argv[1]);
if (input_i == L'\xcafef00d') {
  puts("Access granted.");
  giveFlag();
  uVar1 = 0;
}
```

Der Ziel int ist _-889262067_ (konvertieren). Gibt man dies als Key ein, erhaelt man die Flag:
```
 root  …  tryhackme  writeups  ReversingELF  ./crackme8 -889262067
Access granted.
flag{at_least_this_cafe_wont_leak_your_credit_card_numbers}
 root  …  tryhackme  writeups  ReversingELF  
```
