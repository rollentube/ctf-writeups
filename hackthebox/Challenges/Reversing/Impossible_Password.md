# Impossible Password
Are you able to cheat me and get the flag?

## Solution
If we take a look into the program with strings we directly find a some kind of key:
```
$ strings impossible_password.bin | less
[...]
SuperSeKretKey
$
```

We can run the program and use the key. It seems correct, but the program wants antoher one:
```
$ ./impossible_password.bin
* afdsa
[afdsa]
$ ./impossible_password.bin
* SuperSeKretKey
[SuperSeKretKey]
** fdas
$
```

Taking a look into the program with Ghidra reveals a second key and a second check:
```
key = "SuperSeKretKey";
second_key[0] = 'A';
second_key[1] = ']';
second_key[2] = 'K';
second_key[3] = 'r';
second_key[4] = '=';
second_key[5] = '9';
second_key[6] = 'k';
second_key[7] = '0';
second_key[8] = '=';
second_key[9] = '0';
second_key[10] = 'o';
second_key[11] = '0';
second_key[12] = ';';
second_key[13] = 'k';
second_key[14] = '1';
second_key[15] = '?';
second_key[16] = 'k';
second_key[17] = '8';
second_key[18] = '1';
second_key[19] = 't';

[...]

printf("** ");
__isoc99_scanf(&fmt,input);
rand_key = (char *)random_key(20);
iVar1 = strcmp(input,rand_key);
if (iVar1 == 0) {
    generating_flag(second_key);
}
```

So the second key is used to generate the flag in the function `generating_flag`. But to reach this function, we have to give an input matching to the output of the `rand_key` function. This function uses some `rand()` functions to generate a string. So it's pretty unpossible to give the matching input.

But since the `generating_flag` function just generates the flag with the second key, we can just convert it into a valid program:
```
void generating_flag(byte *key)

{
  int local_14;
  byte *local_10;
  
  local_14 = 0;
  local_10 = key;
  while ((*local_10 != 9 && (local_14 < 20))) {
    putchar((int)(char)(*local_10 ^ 9));
    local_10 = local_10 + 1;
    local_14 = local_14 + 1;
  }
  putchar(10);
  return;
}
```
```c
int main() {
  int local_14 = 0;
  char* local_10 = "A]Kr=9k0=0o0;k1?k81t";
  while ((*local_10 != 9 && (local_14 < 20))) {
    putchar((int)(char)(*local_10 ^ 9));
    local_10 = local_10 + 1;
    local_14 = local_14 + 1;
  }
  putchar(10);
  return 0;
}
```
Alternative we could just debug the program and skip the matching process or jump into the generate function.

But if we run the function, we found the flag:
```
$ ./decr
HTB{40b949f92b86b18}
$
```
