# Cereal Killer 02 (100 points)
`luciafer` can be a bit of trouble sometimes, but she can put away the sugary monster cereals with the best of them! She has a favorite, too, and it is based on her favorite monster. See if you can figure it out! Select the binary for your preferred platform.

[Download Linux Binary](https://tinyurl.com/588fpsn6)
SHA1: ddaefcd54e3b608ce37f92cca36ebe060f7fc2e6

[Download Windows Binary](https://tinyurl.com/4v3cern9)
SHA1: 9cf6fb48d83c819ed731302bca0d03f3c42bca39

## Solution
If we reverse the binary we see that the input is thrown into a function `decode_str`. The output of this function is compared to the string `CORRECT!!!!!`. If it matches, the flag will give out:
```c
decode_str(input,63,&DAT_00012094,decoded);
cmp = strncmp(decoded,"CORRECT!!!!!",12);
if (cmp == 0) {
  puts(decoded);
}
```

`decode_str` takes four arguments. The input, a length of 63, a data section and the buffer for the output. The data is defined as follows:
```
00012094 08              ??         08h
00012095 3d              ??         3Dh    =
00012096 33              ??         33h    3
00012097 3f              ??         3Fh    ?
00012098 15              ??         15h
00012099 36              ??         36h    6
0001209a 32              ??         32h    2
0001209b 47              ??         47h    G
0001209c 52              ??         52h    R
0001209d 12              ??         12h
0001209e 1b              ??         1Bh
0001209f 65              ??         65h    e
000120a0 6b              ??         6Bh    k
000120a1 48              ??         48h    H
000120a2 41              ??         41h    A
000120a3 0b              ??         0Bh
000120a4 3c              ??         3Ch    <
000120a5 14              ??         14h
000120a6 01              ??         01h
000120a7 1d              ??         1Dh
000120a8 34              ??         34h    4
000120a9 41              ??         41h    A
000120aa 5b              ??         5Bh    [
000120ab 29              ??         29h    )
000120ac 1b              ??         1Bh
000120ad 13              ??         13h
000120ae 4c              ??         4Ch    L
000120af 26              ??         26h    &
000120b0 02              ??         02h
000120b1 34              ??         34h    4
000120b2 2b              ??         2Bh    +
000120b3 16              ??         16h
000120b4 06              ??         06h
000120b5 40              ??         40h    @
000120b6 17              ??         17h
000120b7 0d              ??         0Dh
000120b8 38              ??         38h    8
000120b9 5f              ??         5Fh    _
000120ba 22              ??         22h    "
000120bb 02              ??         02h
000120bc 3d              ??         3Dh    =
000120bd 1c              ??         1Ch
000120be 08              ??         08h
000120bf 4b              ??         4Bh    K
000120c0 35              ??         35h    5
000120c1 5c              ??         5Ch    \
000120c2 48              ??         48h    H
000120c3 69              ??         69h    i
000120c4 0f              ??         0Fh
000120c5 13              ??         13h
000120c6 4c              ??         4Ch    L
000120c7 2f              ??         2Fh    /
000120c8 31              ??         31h    1
000120c9 11              ??         11h
000120ca 4b              ??         4Bh    K
000120cb 2d              ??         2Dh    -
000120cc 1a              ??         1Ah
000120cd 57              ??         57h    W
000120ce 49              ??         49h    I
000120cf 65              ??         65h    e
000120d0 6a              ??         6Ah    j
000120d1 53              ??         53h    S
000120d2 1c              ??         1Ch
000120d3 00              ??         00h
```

The function itself iterates over the data and xor every byte with the user input. But only for the first 12 character of the input. If the 13th character is reached, it starts again at the beginning of the input. The result is written to the output:
```c
j = 0;
i = 0;
while (i < len) {
  *(byte *)(output + i) = *(byte *)(data + i) ^ *(byte *)(input + j);
  i = i + 1;
  j = j + 1;
  if (11 < j) {
    j = 0;
  }
}
```

Remembering the compare function of the main, it compares the first 12 characters of the output with `CORRECT!!!!!`. So our input xor the data should result in this string. At least for the first 12 characters.

To get the correct input I wrote this python script:
```python
chars = ['C','O','R','R','E','C','T','!','!','!','!','!']
data = [0x08,0x3d,0x33,0x3f,0x15,0x36,0x32,0x47,0x52,0x12,0x1b,0x65,0x6b,0x48,0x41,0x0b,0x3c,0x14,0x01,0x1d,0x34,0x41,0x5b,0x29,0x1b,0x13,0x4c,0x26,0x02,0x34,0x2b,0x16,0x06,0x40,0x17,0x0d,0x38,0x5f,0x22,0x02,0x3d,0x1c,0x08,0x4b,0x35,0x5c,0x48,0x69,0x0f,0x13,0x4c,0x2f,0x31,0x11,0x4b,0x2d,0x1a,0x57,0x49,0x65,0x6a,0x53,0x1c,0x00]

i = 0
for value in data:
    print(chr(value ^ ord(chars[i])), end='')
    if i == 11:
        i = 0
        print()
    else:
        i += 1
print()
```

If we xor our string with the data, we get our searched input.

So if we run the script we get the input that solves the program:
```
$ python re02.py
KramPuffs3:D
(YyWU<`z
X\tGw7'a6,
{pPx_\j}iH
L\}tR
     ;vhD
)NR
```

And we can generate our flag:
```
$ ./re02.bin
Luciafer also loves Halloween, so she, too, LOVES SPOOKY CEREALS!
She has different favorite villain from 70-80's horror movies.
What is Luciafer's favorite breakfast cereal? KramPuffs3:D
CORRECT!!!!! : flag{GramPa-KRAMpus-Is-Comin-For-Da-Bad-Kids!!!}
dface
```