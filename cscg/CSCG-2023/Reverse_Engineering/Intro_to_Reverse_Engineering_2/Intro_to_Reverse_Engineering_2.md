# Intro to Reverse Engineering 2
Somehow the password was encoded and can't be found in plaintext in the binary. Can you still figure out the right password?

## Solution
In Ghidra kann man sehen, dass bei der "Verschluesselung" lediglich -119 auf den Char gerechnet und anschliessend mit einer globalen Speicherstelle verglichen wird:
```c
  initialize_flag();
  puts("Give me your password: ");
  bytes = read(0,input,31);
  len = (int)bytes;
  input[(int)bytes + -1] = '\0';
  for (i = 0; i < len + -0x1; i = i + 1) {
    input[i] = input[i] + -119;
  }
  cmp = strcmp(input,&pass);
  if (cmp == 0) {
    puts("Thats the right password!");
    printf("Flag: %s",flagBuffer);
  }
  else {
    puts("Thats not the password!");
  }
```

An dieser Speicherstelle finde man also das Encrypted Password:
`0x02 0xEA 0x02 0xE8 0xFC 0xFD 0xBD 0xFD 0xF2 0xEC 0xE8 0xFD 0xFB 0xEA 0xF7 0xFC 0xEF 0xB9 0xFB 0xF6 0xEA 0xFD 0xF2 0xF8 0xF7 0x00`

Dieses kann man beispielsweise mit einem C Programm (_dec.c_) wieder decrypten und erhaelt dann das Kennwort.
```
 root  ~  ctf  cscg_23  reverse_2  clang -o dec dec.c
 root  ~  ctf  cscg_23  reverse_2  ./dec
yay_st4tic_transf0rmation
 root  ~  ctf  cscg_23  reverse_2  ncat --ssl 28f50730c72cd90d9451689f-intro-rev-2.challenge.master.cscg.live 31337
Give me your password:
yay_st4tic_transf0rmation
Thats the right password!
Flag: CSCG{y0u_just_r3versed_a_st4tic_transformation!}
^C
 root  ~  ctf  cscg_23  reverse_2  
```
