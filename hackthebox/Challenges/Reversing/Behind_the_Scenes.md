# Behind the Scenes
After struggling to secure our secret strings for a long time, we finally figured out the solution to our problem: Make decompilation harder. It should now be impossible to figure out how our programs work!

## Solution
The file needs a password to give the wanted output:
```
[root@arch rev_behindthescenes]$ ./behindthescenes
./challenge <password>
[root@arch rev_behindthescenes]$ ./behindthescenes test
[root@arch rev_behindthescenes]$
```

We can't find the password with strings. But we found probably the format string of the output:
```
[root@arch rev_behindthescenes]$ strings behindthescenes | less
[...]
./challenge <password>
> HTB{%s}
[...]
```

Let's take a look with hexdump:
```
[root@arch rev_behindthescenes]$ hexdump -C behindthescenes | less
[...]
00002000  01 00 02 00 2e 2f 63 68  61 6c 6c 65 6e 67 65 20  |...../challenge |
00002010  3c 70 61 73 73 77 6f 72  64 3e 00 49 74 7a 00 5f  |<password>.Itz._|
00002020  30 6e 00 4c 79 5f 00 55  44 32 00 3e 20 48 54 42  |0n.Ly_.UD2.> HTB|
00002030  7b 25 73 7d 0a 00 00 00  01 1b 03 3b 4c 00 00 00  |{%s}.......;L...|
[...]
```
Skipping the nullbytes, the password seems to be `Itz_0nLy_UD2`.

Let's try it out:
```
[root@arch rev_behindthescenes]$ ./behindthescenes Itz_0nLy_UD2
> HTB{Itz_0nLy_UD2}
[root@arch rev_behindthescenes]$
```

We found the flag and the challenge is solved.
