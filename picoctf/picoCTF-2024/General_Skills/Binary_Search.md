# Binary Search (100 points)
Want to play a game? As you use more of the shell, you might be interested in how they work! Binary search is a classic algorithm used to quickly find an item in a sorted list. Can you find the flag? You'll have 1000 possibilities and only 10 guesses.

Cyber security often has a huge amount of data to look through - from logs, vulnerability reports, and forensics. Practicing the fundamentals manually might help you in the future when you have to write your own tools!

`ssh -p 54088 ctf-player@atlas.picoctf.net`

Using the password `1db87a14`. Accept the fingerprint with `yes`, and `ls` once connected to begin. Remember, in a shell, passwords are hidden!


## Data
* challenge.zip

## Solution
Binary search is a algorithm where we compare the target with the middle element of our array. If we do so we can narrow down the correct answer. I did so and found the random number:
```
$ ssh -p 54088 ctf-player@atlas.picoctf.net
ctf-player@atlas.picoctf.net's password:
Welcome to the Binary Search Game!
I'm thinking of a number between 1 and 1000.
Enter your guess: 500
Lower! Try again.
Enter your guess: 250
Higher! Try again.
Enter your guess: 350
Higher! Try again.
Enter your guess: 450
Lower! Try again.
Enter your guess: 400
Lower! Try again.
Enter your guess: 375
Lower! Try again.
Enter your guess: 360
Higher! Try again.
Enter your guess: 370
Higher! Try again.
Enter your guess: 372
Congratulations! You guessed the correct number: 372
Here's your flag: picoCTF{g00d_gu355_1597707f}
Connection to atlas.picoctf.net closed.
$
```
