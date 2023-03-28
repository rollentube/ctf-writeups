# Reverse
Try reversing this file? Can ya?
I forgot the password to this file. Please find it for me? (100 Points)

## Files
- ret

## Solution
### Overview
```
[root@picoctf Reverse]$ file ret
ret: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=1e3b1266f41d7ea7d00d3a35a1dff916c75c07f5, for GNU/Linux 3.2.0, not stripped
[root@picoctf Reverse]$ ./ret
-bash: ./ret: Permission denied
[root@picoctf Reverse]$ chmod 755 ./ret
[root@picoctf Reverse]$ ./ret
Enter the password to unlock this file: password
You entered: password
Access denied
[root@picoctf Reverse]$
```

### Reversing with Ghidra
The main showed up the following code
```c
  pass._0_8_ = 0x7b4654436f636970;
  pass._8_8_ = 0x337633725f666c33;
  pass._16_8_ = 0x75735f676e693572;
  pass._24_8_ = 0x6c75663535656363;
  pass._32_8_ = 0x313633333765665f;
  printf("Enter the password to unlock this file: ");
  __isoc99_scanf(&fmt_str,input);
  printf("You entered: %s\n",input);
  cmp = strcmp(input,pass);
  if (cmp == 0) {
    puts("Password correct, please see flag: picoCTF{3lf_r3v3r5ing_succe55ful_fe733618}");
    puts(pass);
  }
  else {
    puts("Access denied");
  }
```

So we can see the flag in clear text without the right password. But the password is hardcoded in the string 'pass': picoCTF{3lf\_r3v3r5ing\_succe55ful\_fe73361 (same as the flag, but without '}')

```
[root@picoctf Reverse]$ ./ret
Enter the password to unlock this file: picoCTF{3lf_r3v3r5ing_succe55ful_fe73361
You entered: picoCTF{3lf_r3v3r5ing_succe55ful_fe73361
Password correct, please see flag: picoCTF{3lf_r3v3r5ing_succe55ful_fe733618}
picoCTF{3lf_r3v3r5ing_succe55ful_fe73361
[root@picoctf Reverse]$
```

Alternative you simple can use strings
```
[root@picoctf Reverse]$ strings ret | grep pico
picoCTF{H
Password correct, please see flag: picoCTF{3lf_r3v3r5ing_succe55ful_fe733618}
[root@picoctf Reverse]$
```

The flag is: picoCTF{3lf\_r3v3r5ing\_succe55ful\_fe733618}
