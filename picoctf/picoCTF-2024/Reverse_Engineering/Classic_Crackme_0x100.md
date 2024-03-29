# Classic Crackme 0x100 (300 points)
A classic Crackme. Find the password, get the flag!

Crack the Binary file locally and recover the password. Use the same password on the server to get the flag!

Access the server using `nc titan.picoctf.net 60838`

## Data
* crackme100

## Solution
If we open the executable with IDA we find the following main function:
```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  char input[51]; // [rsp+0h] [rbp-A0h] BYREF
  char output[51]; // [rsp+40h] [rbp-60h] BYREF
  int random2; // [rsp+7Ch] [rbp-24h]
  int random1; // [rsp+80h] [rbp-20h]
  char fix; // [rsp+87h] [rbp-19h]
  int secret3; // [rsp+88h] [rbp-18h]
  int secret2; // [rsp+8Ch] [rbp-14h]
  int secret1; // [rsp+90h] [rbp-10h]
  int len; // [rsp+94h] [rbp-Ch]
  int i_0; // [rsp+98h] [rbp-8h]
  int i; // [rsp+9Ch] [rbp-4h]

  strcpy(output, "qhcpgbpuwbaggepulhstxbwowawfgrkzjstccbnbshekpgllze");
  setvbuf(_bss_start, 0LL, 2, 0LL);
  printf("Enter the secret password: ");
  __isoc99_scanf("%50s", input);
  i = 0;
  len = strlen(output);
  secret1 = 85;
  secret2 = 51;
  secret3 = 15;
  fix = 97;
  while ( i <= 2 )
  {
    for ( i_0 = 0; i_0 < len; ++i_0 )
    {
      random1 = (secret1 & (i_0 % 255)) + (secret1 & ((i_0 % 255) >> 1));
      random2 = (random1 & secret2) + (secret2 & (random1 >> 2));
      input[i_0] = ((random2 & secret3) + input[i_0] - fix + (secret3 & (random2 >> 4))) % 26 + fix;
    }
    ++i;
  }
  if ( !memcmp(input, output, len) )
    printf("SUCCESS! Here is your flag: %s\n", "picoCTF{sample_flag}");
  else
    puts("FAILED!");
  return 0;
}
```

The important condition is this one:
```c
  if ( !memcmp(input, output, len) )
    printf("SUCCESS! Here is your flag: %s\n", "picoCTF{sample_flag}");
  else
    puts("FAILED!");
```

So if our input matches the output, we get the flag. The output is the following string: `qhcpgbpuwbaggepulhstxbwowawfgrkzjstccbnbshekpgllze`

The program operates on our input and manipulates it. After the manipulation it has to be the same as the output.

I took a look with gdb into the program. I set a brakepoint on to the call of `memcmp` (`0x0x40136a`) and gave the the input `aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa`.

We can know see the two parameters that `memcmp` is comparing:
```
arg[0]: 0x7fffffffe290 ("addgdggjdggjgjjmdggjgjjmgjjmjmmpdggjgjjmgjjmjmmpgj")
arg[1]: 0x7fffffffe2d0 ("qhcpgbpuwbaggepulhstxbwowawfgrkzjstccbnbshekpgllze")
```

The first one is our manipulated input, and the second one is the output that we want to match.

The calculation of the manipulation is static and depends only on the character of the current iteration. Meaning that each character manipulation don't rely on any other character. So we can guess or calculate each character individual until it matches the output.

I wrote a short python script to automate this:
```python
diff = "addgdggjdggjgjjmdggjgjjmgjjmjmmpdggjgjjmgjjmjmmpgj"
out  = "qhcpgbpuwbaggepulhstxbwowawfgrkzjstccbnbshekpgllze"
sol  = ""

for i, char in enumerate(diff):
        offset = ord(char) - 97
        sol += chr(ord(out[i]) - offset)
print(sol)
```

I gave the input `aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa` to the program and at the end it was manipulated to `addgdggjdggjgjjmdggjgjjmgjjmjmmpdggjgjjmgjjmjmmpgj`. So for each character we can calculate the offset to the original input `a`. In the next step we have to substract this offset from the char of our output `qhcpgbpuwbaggepulhstxbwowawfgrkzjstccbnbshekpgllze`. As result we get that character that we can input and that is manipulated into the searched output character.

If we run this script we get the following solution:
```
$ python crackme.py
qe`jd\jlt\[^a\giibmkrYncqXnZ^f_kgmnZ]YeVm_\_g[`]t\
$
```

We can know input this password to the program:
```
$ ./crackme100
Enter the secret password: qe`jd\jlt\[^a\giibmkrYncqXnZ^f_kgmnZ]YeVm_\_g[`]t\
SUCCESS! Here is your flag: picoCTF{sample_flag}
$ 
```
Seems good!

Finally we can enter it on the server application to get the flag:
```
$ nc titan.picoctf.net 61322
Enter the secret password: qe`jd\jlt\[^a\giibmkrYncqXnZ^f_kgmnZ]YeVm_\_g[`]t\
SUCCESS! Here is your flag: picoCTF{s0lv3_angry_symb0ls_4699696e}
$
```

## Problems
This challenge should also be doable with angr or z3. But my skills here are not that good and I failed several times in this challenge until I found the solution mentioned above. With angr I got the solution ```b'qe`jdvjltvu^{vgii|mkr\xbdncq\xbcn\xd8^fykgmnt\xa7se\xbamyv_guz]tv'```, which obviously has not only printable characters.

I also tried to limit the input to printable characters, but I was not successful. I'm looking forward to the writeups.
