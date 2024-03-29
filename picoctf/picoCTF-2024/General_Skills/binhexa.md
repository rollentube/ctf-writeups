# binhexa (100 points)
How well can you perfom basic binary operations?

Start searching for the flag here `nc titan.picoctf.net 49964`

## Solution
If we connect to the system, we get two binary numbers and have to make several operations with them. If we give the right answer, we reach the next question.

I'm a bit lazy and solved the questions with python:
```
>>> a = 0b01001110
>>> b = 0b10100111
>>> a
78
>>> b
167
>>>
>>>
>>> a&b
6
>>> bin(a&b)
'0b110'
>>> bin(a+b)
'0b11110101'
>>> bin(b>>1)
'0b1010011'
>>> bin(a|b)
'0b11101111'
>>> bin(a<<1)
'0b10011100'
>>> bin(a*b)
'0b11001011100010'
>>> bin(a*b)
'0b11001011100010'
>>> hex(a*b)
'0x32e2'
>>>
```

Here is the output if we enter the correct answers:
```
$ nc titan.picoctf.net 49964

Welcome to the Binary Challenge!"
Your task is to perform the unique operations in the given order and find the final result in hexadecimal that yields the flag.

Binary Number 1: 01001110
Binary Number 2: 10100111


Question 1/6:
Operation 1: '&'
Perform the operation on Binary Number 1&2.
Enter the binary result: 110
Correct!

Question 2/6:
Operation 2: '+'
Perform the operation on Binary Number 1&2.
Enter the binary result: 11110101
Correct!

Question 3/6:
Operation 3: '>>'
Perform a right shift of Binary Number 2 by 1 bits .
Enter the binary result: 1010011
Correct!

Question 4/6:
Operation 4: '|'
Perform the operation on Binary Number 1&2.
Enter the binary result: 11101111
Correct!

Question 5/6:
Operation 5: '<<'
Perform a left shift of Binary Number 1 by 1 bits.
Enter the binary result: 10011100
Correct!

Question 6/6:
Operation 6: '*'
Perform the operation on Binary Number 1&2.
Enter the binary result: 11001011100010
Correct!

Enter the results of the last operation in hexadecimal: 32e2

Correct answer!
The flag is: picoCTF{b1tw^3se_0p3eR@tI0n_su33essFuL_d6f8047e}
$
```

And in the last step we got our flag!
