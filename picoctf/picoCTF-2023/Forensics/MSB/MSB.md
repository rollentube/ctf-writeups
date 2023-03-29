# MSB
This image passes LSB statistical analysis, but we can't help but think there must be something to the visual artifacts present in this image... Download the image here (200 Points)

## Data
Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png

## Solution
If we take a look at the picture we can see that is clearly corrupted somehow. Basic checking tools like https://www.nayuki.io/page/png-file-chunk-inspector or 'pngcheck' doesnt show any errors in the file sectors:
```
[root@picoctf MSB]$ pngcheck -v Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png 
File: Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png (3354311 bytes)
  chunk IHDR at offset 0x0000c, length 13
    1074 x 1500 image, 24-bit RGB, non-interlaced
  chunk IDAT at offset 0x00025, length 65536
    zlib: deflated, 32K window, default compression
  chunk IDAT at offset 0x10031, length 65536
  chunk IDAT at offset 0x2003d, length 65536
  chunk IDAT at offset 0x30049, length 65536
  chunk IDAT at offset 0x40055, length 65536
  chunk IDAT at offset 0x50061, length 65536
  chunk IDAT at offset 0x6006d, length 65536
  chunk IDAT at offset 0x70079, length 65536
  chunk IDAT at offset 0x80085, length 65536
  chunk IDAT at offset 0x90091, length 65536
  chunk IDAT at offset 0xa009d, length 65536
  chunk IDAT at offset 0xb00a9, length 65536
  chunk IDAT at offset 0xc00b5, length 65536
  chunk IDAT at offset 0xd00c1, length 65536
  chunk IDAT at offset 0xe00cd, length 65536
  chunk IDAT at offset 0xf00d9, length 65536
  chunk IDAT at offset 0x1000e5, length 65536
  chunk IDAT at offset 0x1100f1, length 65536
  chunk IDAT at offset 0x1200fd, length 65536
  chunk IDAT at offset 0x130109, length 65536
  chunk IDAT at offset 0x140115, length 65536
  chunk IDAT at offset 0x150121, length 65536
  chunk IDAT at offset 0x16012d, length 65536
  chunk IDAT at offset 0x170139, length 65536
  chunk IDAT at offset 0x180145, length 65536
  chunk IDAT at offset 0x190151, length 65536
  chunk IDAT at offset 0x1a015d, length 65536
  chunk IDAT at offset 0x1b0169, length 65536
  chunk IDAT at offset 0x1c0175, length 65536
  chunk IDAT at offset 0x1d0181, length 65536
  chunk IDAT at offset 0x1e018d, length 65536
  chunk IDAT at offset 0x1f0199, length 65536
  chunk IDAT at offset 0x2001a5, length 65536
  chunk IDAT at offset 0x2101b1, length 65536
  chunk IDAT at offset 0x2201bd, length 65536
  chunk IDAT at offset 0x2301c9, length 65536
  chunk IDAT at offset 0x2401d5, length 65536
  chunk IDAT at offset 0x2501e1, length 65536
  chunk IDAT at offset 0x2601ed, length 65536
  chunk IDAT at offset 0x2701f9, length 65536
  chunk IDAT at offset 0x280205, length 65536
  chunk IDAT at offset 0x290211, length 65536
  chunk IDAT at offset 0x2a021d, length 65536
  chunk IDAT at offset 0x2b0229, length 65536
  chunk IDAT at offset 0x2c0235, length 65536
  chunk IDAT at offset 0x2d0241, length 65536
  chunk IDAT at offset 0x2e024d, length 65536
  chunk IDAT at offset 0x2f0259, length 65536
  chunk IDAT at offset 0x300265, length 65536
  chunk IDAT at offset 0x310271, length 65536
  chunk IDAT at offset 0x32027d, length 65536
  chunk IDAT at offset 0x330289, length 11306
  chunk IEND at offset 0x332ebf, length 0
No errors detected in Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png (54 chunks, 30.6% compression).
```

So the description of the challenge is talking about a LSB check. Hiding data in the least significant bits of the pixels of an image is typical technique to stego data in pictures. The LSBs are manipulated to the bits of the data. So all LSBs will represent together the hidden data.

Since the name of the challange is MSB (most significant bit) and the fact that the description says that there are no LSB errors, there is probably data hidden in the MSBs of the pixels of the image. Changing those bits is more likely a corruption that is viewable on the image than LSBs.

Searching a bit, I found the following GitHub project for extracting LSB/MSB stego data: https://github.com/Larkteryny/MSB-LSB-steganography

The script does nothing else than iterating through every pixel of the image and extract the LSB/MSB. Running it for hopefully extracting the MSB data:
```
[root@picoctf MSB-LSB-steganography]$ python msb.py
MSB steganography. Hide files within most significant bits of images.

Usage:
  msb.py hide <img_file> <payload_file> <password>
  msb.py extract <stego_file> <out_file> <password>
  msb.py analyse <stego_file>
[root@picoctf MSB-LSB-steganography]$
[root@picoctf MSB-LSB-steganography]$ python msb.py extract ../Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png ../out password
[+] Image size: 1074x1500 pixels.
[+] Written extracted data to ../out.
[root@picoctf MSB-LSB-steganography]$
```
(Note that the 'password' functionality isnt implemented yet in the script, so there can be just a random password. Otherwise you can remove the argv parsing from the script.)

If we take a look at the output we can find the following:
```
[root@picoctf MSB-LSB-steganography]$ file ../out
../out: ASCII text
[root@picoctf MSB-LSB-steganography]$ head ../out
The Project Gutenberg eBook of The History of Don Quixote, by Miguel de Cervantes

This eBook is for the use of anyone anywhere in the United States and
most other parts of the world at no cost and with almost no restrictions
whatsoever. You may copy it, give it away or re-use it under the terms
of the Project Gutenberg License included with this eBook or online at
www.gutenberg.org. If you are not located in the United States, you
will have to check the laws of the country where you are located before
using this eBook.

[root@picoctf MSB-LSB-steganography]$
```

So there were data hidden in the MSBs of the image, but is there also a flag?
```
[root@picoctf MSB-LSB-steganography]$ grep pico ../out
picoCTF{15_y0ur_que57_qu1x071c_0r_h3r01c_b5e03bc5}
[root@picoctf MSB-LSB-steganography]$ 
```

Yes it is. Solved this one.
