# Cereal Killer 01 (50 points)
How well do you know your DEADFACE hackers? Test your trivia knowledge of our beloved friends at our favorite hactivist collective! We’ll start with `bumpyhassan`. Even though he grates on `TheZeal0t` a bit, we find him to be absolutely ADORKABLE!!!

Choose one of the binaries below to test your BH trivia knowlege.

Enter the flag in the format: `flag{Ch33ri0z_R_his_FAV}`.

[Download Linux Binary](https://tinyurl.com/5bwpcw7p)
SHA1: a4df763d093295a02f23c641d268c417bd32ee69

[Download Windows Binary](https://tinyurl.com/5az73h9w)
SHA1: 7976bf7051b0295f84a80e12d9d1a17e654fa178

## Solution
We can get the flag at two points if we reverse the binary.

As first, the program takes the user input, increases the character values for each one by 7, and compare it to a data section:
```c
fgets(input,4095,_stdin);
for (i = input; *i != '\0'; i = i + 1) {
  *i = *i + 7;
}
*i = '\0';
cmp = memcmp(&DAT_00012039,input,14);
if (cmp == 0) {
  puts("You are correct!");
```

The data section has stored the following values:
```
00012039 4d              ??         4Dh    M
0001203a 79              ??         79h    y
0001203b 7c              ??         7Ch    |
0001203c 70              ??         70h    p
0001203d 7b              ??         7Bh    {
0001203e 80              ??         80h
0001203f 47              ??         47h    G
00012040 52              ??         52h    R
00012041 59              ??         59h    Y
00012042 5c              ??         5Ch    \
00012043 4c              ??         4Ch    L
00012044 4e              ??         4Eh    N
00012045 4c              ??         4Ch    L
00012046 59              ??         59h    Y
```

We can now use a simple python script to decrease those values by 7 again:
```python
hex = [0x4d,0x79,0x7c,0x70,0x7b,0x80,0x47,0x52,0x59,0x5c,0x4c,0x4e,0x4c,0x59]

for num in hex:
    new = num - 7
    print(chr(new), end='')
print()
```

Resulting in the following input:
```
$ python mov.py
Fruity@KRUEGER
```

And we can get the flag:
```
$ ./re01
Bumpyhassan loves Halloween, so naturally, he LOVES SPOOKY CEREALS!
He also happens to be a fan of horror movies from the 1970's to the 1990's.
What is bumpyhassan's favorite breakfast cereal? Fruity@KRUEGER
You are correct!
flag{I_am_REDDY_for_FREDDY!!!}
```

The second way is on hay the flag is created. We have the following string in the program:
```c
flag = "I&_9a%mx_tRmE4D3DmYw_9fbo6rd_aFcRbE,D.D>Y[!]!\'!q";
```
(the backslash is no character)

If the user input is correct, the program iterates over this string and only stores the first and after that only every 2nd character:
```c
for (; *flag != '\0'; flag = flag + 2) {
  *buffer = *flag;
  buffer = buffer + 1;
}
```

So if we remove the character 1, 3, 5, etc. we get from the string `I&_9a%mx_tRmE4D3DmYw_9fbo6rd_aFcRbE,D.D>Y[!]!'!q` to `I_am_REDDY_for_FREDDY!!!` and got our flag as well.