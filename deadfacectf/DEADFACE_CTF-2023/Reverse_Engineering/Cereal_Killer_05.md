# Cereal Killer 05 (10 points)
We think Dr. Geschichter of Lytton Labs likes to use his favorite monster cereal as a password for ALL of his accounts! See if you can figure out what it is, and keep it handy! Choose one of the binaries to work with.

Enter the answer as `flag{WHATEVER-IT-IS}`.

[Download Linux Binary](https://tinyurl.com/2mex44jv)
SHA1: 44a4753f896e06175bd6bb14eca2e662813867df

[Download Windows Binary](https://tinyurl.com/5n75wsjv)
SHA1: a5a6277516e19b8a3adc724f6dfcf9e11545feb1

## Solution
I downloaded the Linux binary and took a look at it with strings. In here we find the following text:
```
$ strings re05.bin | less

[...]

Dr. Geschichter, just because he is evil, doesn't mean he doesn't have a favorite cereal.
Please enter the passphrase, which is based off his favorite cereal and entity:
notf1aq{you-guessed-it---this-is-not-the-f1aq}
Xen0M0rphMell0wz

[...]

```

The word under the text looks like a password. So running the binary and entering the strings reveals the flag:
```
$ ./re05.bin
Dr. Geschichter, just because he is evil, doesn't mean he doesn't have a favorite cereal.
Please enter the passphrase, which is based off his favorite cereal and entity: Xen0M0rphMell0wz
flag{XENO-DO-DO-DO-DO-DO-DOOOOO}
$
```