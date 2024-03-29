# endianness (200 points)
Know of little and big endian?

`nc titan.picoctf.net 61099`

## Data
* flag.c

## Solution
The endianess is the byte order of a system. Little endian means that the least significant byte is in the first place, then the secons least etc. One character is one byte, so we just have to turn around the order of the string.

Big endian means that the most significant byte comes first. So the string representation will stay the same.

In our example we got the string _eiymp_. Or in hex _6569796D70_. So the little endian representation is _pmyie_. In hex that would be _706D796965_. Big endian will stay in the same orientation:
```
$ nc titan.picoctf.net 61099
Welcome to the Endian CTF!
You need to find both the little endian and big endian representations of a word.
If you get both correct, you will receive the flag.
Word: eiymp
Enter the Little Endian representation: 706D796965
Correct Little Endian representation!
Enter the Big Endian representation: 6569796D70
Correct Big Endian representation!
Congratulations! You found both endian representations correctly!
Your Flag is: picoCTF{3ndi4n_sw4p_su33ess_25c5f083}

$
```

We can also use the given program the calculate the answer for us. We just have to edit this line
```c
    //char *challenge_word = generate_random_word();
    char *challenge_word = "eiymp";
```
and print out the return values of `find_little_endian` and `find_big_endian`:
```
$ ./flag
Word: eiymp
706D796965
Enter the Little Endian representation:

706D796965
Correct Little Endian representation!
6569796D70
Enter the Big Endian representation: 6569796D70
Correct Big Endian representation!
Flag not found. Please run this on the server
$ 
```
