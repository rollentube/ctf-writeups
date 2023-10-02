# 8ball (beginner)
Let me guide you to the flag.

## Files
* 8ball

## Solution
If we decompile the file with Ghidra, we find two interesting parts in the main function:
```c
iVar1 = strcmp(*param_2,"./magic8ball");
if (iVar1 == 0) {
    puts("Why, I guess you\'re right... I am magic :D");
    local_c = 1;
}
```
```c
if ((local_c != 0) && (pcVar3 = strstr(param_2[1],"flag"), pcVar3 != (char *)0x0)) {
    puts("Why yes, here is your flag!");
    print_flag();
    return 0;
}
```

The first condition checks if the program name is `./magic8ball`. The name of the program or better the execution path is over given as first argument to the execution. So to get the wanted value we have to rename the executable file.

The second condition checks if the string `flag` was given to the program as CLI parameter.

Combining those two, gives us the flag:
```
$ mv 8ball magic8ball
$ ./magic8ball flag
Why, I guess you're right... I am magic :D
You asked:
"flag"
Hmmm....
Why yes, here is your flag!
bctf{Aw_$hucK$_Y0ur3_m@k1Ng_m3_bLu$h}
$
```

Otherwise, we could also hop into the `print_flag()` function and analyze it. The flag is encrypted and is going to be decrypted with this function.