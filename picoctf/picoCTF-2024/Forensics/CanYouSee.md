# CanYouSee (100 points)
How about some hide and seek?

## Data
* unknown.zip

## Solution
We got a JPG image that hides a flag somewhere. So as first I analysed the metadata:
```
$ hexdump -C ukn_reality.jpg | less
$ strings ukn_reality.jpg | grep -i pico
$ exiftool ukn_reality.jpg
ExifTool Version Number         : 12.76
File Name                       : ukn_reality.jpg
Directory                       : .
File Size                       : 2.3 MB
File Modification Date/Time     : 2024:03:12 01:05:55+01:00
File Access Date/Time           : 2024:03:16 16:30:08+01:00
File Inode Change Date/Time     : 2024:03:16 16:29:30+01:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 72
Y Resolution                    : 72
XMP Toolkit                     : Image::ExifTool 11.88
Attribution URL                 : cGljb0NURntNRTc0RDQ3QV9ISUREM05fNmE5ZjVhYzR9Cg==
Image Width                     : 4308
Image Height                    : 2875
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 4308x2875
Megapixels                      : 12.4
$
```

`exiftool` show a data field called _Attribution URL_. The value seems like Base64. Might be worth a try:
```
$ echo "cGljb0NURntNRTc0RDQ3QV9ISUREM05fNmE5ZjVhYzR9Cg==" | base64 -d
picoCTF{ME74D47A_HIDD3N_6a9f5ac4}
$
```

We already found the flag!
