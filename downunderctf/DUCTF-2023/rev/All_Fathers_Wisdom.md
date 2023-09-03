# All Father's Wisdom (beginner)
We found this binary in the backroom, its been marked as "The All Fathers Wisdom" - See hex for further details. Not sure if its just old and hex should be text, or they mean the literal hex.

Anyway can you get this 'wisdom' out of the binary for us?

Author: pix

## Files
the-all-fathers-wisdom

## Solution
Running the file won't give any result. Also there is no easy to grab flag in the strings of the file.

If we analyze the file a bit, we can find that there is a function called `main.print_flag`:
```
$ file the-all-fathers-wisdom
the-all-fathers-wisdom: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=01eec917a381d4efe62ed137f1349127f4faeeaa, for GNU/Linux 4.4.0, not stripped
$
```
```
$ strings the-all-fathers-wisdom | grep main
__libc_start_main
/home/pix/chal/main.odin
main.print_flag
main.main
__libc_start_main@GLIBC_2.34
$
```

Reversing this function with Ghidra shows the following:
```
[...]
  local_140 = 0x77;
  local_148 = 0x25;
  local_150 = 0x31;
  local_158 = 0x73;
  local_160 = 0x26;
  local_168 = 0x31;
  local_170 = 0x27;
  local_178 = 0x25;
  local_180 = 0x31;
  local_188 = 0x25;
  local_190 = 0x24;
  local_198 = 0x31;
  local_1a0 = 0x22;
  local_1a8 = 0x25;
  local_1b0 = 0x31;
  local_1b8 = 0x24;
  local_1c0 = 0x24;
  local_1c8 = 0x31;
  local_1d0 = 0x25;
  local_1d8 = 0x25;
  local_1e8 = &local_1d8;
  len = 59;
  for (i = 0; string = local_1e8, place = i, i < len; i = i + 1) {
    runtime.bounds_check_error("/home/pix/chal/main.odin",0x18,0x47,0x24,i,len);
    xor = *(uint *)(string + place) ^ 17;
    local_228._8_8_ = 0x4200000000000001;
    local_228._0_8_ = &xor;
    local_218._8_8_ = 0x4200000000000001;
    local_218._0_8_ = &xor;
    local_208._8_8_ = 1;
    local_208._0_8_ = local_218;
    fmt.printf("%c",2,local_218,1,param_1);
  }
  return;
```
At first we have an array. Probably it's a string and 59 characters long.

After that, we can see a for loop iterating over that string, XOR every character with 17 and printing that character.

With that information we can write a script which also does this transformation for us:
```python
hex_string = [0x75,0x26,0x31,0x22,0x25,0x31,0x77,0x24,0x31,0x25,0x26,0x31,0x21,0x22,0x31,0x74,0x25,0x31,0x75,0x23,0x31,0x22,0x24,0x31,0x20,0x22,0x31,0x77,0x24,0x31,0x74,0x27,0x31,0x20,0x22,0x31,0x25,0x27,0x31,0x77,0x25,0x31,0x73,0x26,0x31,0x27,0x25,0x31,0x25,0x24,0x31,0x22,0x25,0x31,0x24,0x24,0x31,0x25,0x25]

string = ""
for char in hex_string:
    xor = char ^ 17
    string += chr(xor)
print(string)
```
This will give us the following string: `d7 34 f5 47 03 e4 d2 35 13 f5 e6 13 46 f4 b7 64 45 34 55 44`

Now we have ASCII characters that represent another string. But it seems to be in little endian, because the hex values are no valid ASCII symbols and the first character seems to be _0x7d_ which is _}_ (typical for CTF flags).

So we have to invert the string character and byte wise. This will lead us to the string: `44 55 43 54 46 7b 4f 64 31 6e 5f 31 53 2d 4e 30 74 5f 43 7d`

Know we can convert this hex string into the real ASCII. Either with another few lines or with tools like CyberChef.

A script for all tasks could look like this:
```python
hex_string = [0x75,0x26,0x31,0x22,0x25,0x31,0x77,0x24,0x31,0x25,0x26,0x31,0x21,0x22,0x31,0x74,0x25,0x31,0x75,0x23,0x31,0x22,0x24,0x31,0x20,0x22,0x31,0x77,0x24,0x31,0x74,0x27,0x31,0x20,0x22,0x31,0x25,0x27,0x31,0x77,0x25,0x31,0x73,0x26,0x31,0x27,0x25,0x31,0x25,0x24,0x31,0x22,0x25,0x31,0x24,0x24,0x31,0x25,0x25]

# xor characters
string = ""
for char in hex_string:
    xor = char ^ 17
    string += chr(xor)

# turn bytewise
string = string.split(" ")
for i, char in enumerate(string):
    string[i] = char[::-1]

# turn string, convert hex to char
string = string[::-1]

conv_string = bytes.fromhex("".join(string)).decode("ASCII")
print(conv_string)
```

Running the script will give us the flag:
```
$ python dec.py
DUCTF{Od1n_1S-N0t_C}
$
```
