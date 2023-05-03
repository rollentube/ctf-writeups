# Intro to Reverse Engineering 3
Again, the password was encoded. But this time your input is transformed dynamically! Is it still possible to find the password?

## Solution
In Ghidra sieht man, dass nun die Character unter anderem mit XOR encypted wurden
```c
  initialize_flag();
  puts("Give me your password: ");
  bytes = read(0,input,0x1f);
  len = (int)bytes;
  input[(int)bytes + -1] = 0;
  for (i = 0; i < len + -1; i = i + 1) {
    input[i] = (char)i + 10U ^ input[i];
    input[i] = input[i] - 2;
  }
  cmp = strcmp((char *)input,"b9yPw:MwqcoHuFz^r-o*{>I\x10Y");
  if (cmp == 0) {
    puts("Thats the right password!");
    printf("Flag: %s",flagBuffer);
  }
  else {
    puts("Thats not the password!");
  }
```

Das Ganze kann nun beispielsweise mit angr geloest werden (_dec.py_). Hierdurch findet das gesuchte Passwort
```
 root  ~  ctf  cscg_23  reverse_3  python dec.py
[angr crap...]
Die Eingabe lautet:      b'n0w_w3_have_a_dyn4m1c_k3y!H\x00IP\x00'
 root  ~  ctf  cscg_23  reverse_3  ncat --ssl ac81bc8e510b6510abbb889f-intro-rev-3.challenge.master.cscg.live 31337
Give me your password:
n0w_w3_have_a_dyn4m1c_k3y!
Thats the right password!
Flag: CSCG{X0R_and_sub_is_a_n1ce_c0mbinati0n}
^C
 root  ~  ctf  cscg_23  reverse_3                                                                                                           SIGINT 
```
