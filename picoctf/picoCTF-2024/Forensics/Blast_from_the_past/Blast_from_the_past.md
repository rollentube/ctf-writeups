# Blast from the past (300 points)
The judge for these pictures is a real fan of antiques. Can you age this photo to the specifications?

Set the timestamps on this picture to `1970:01:01 00:00:00.001+00:00` with as much precision as possible for each timestamp. In this example, `+00:00` is a timezone adjustment. Any timezone is acceptable as long as the time is equivalent. As an example, this timestamp is acceptable as well: `1969:12:31 19:00:00.001-05:00`. For timestamps without a timezone adjustment, put them in GMT time (+00:00). The checker program provides the timestamp needed for each.

Use this [picture]().

Submit your modified picture here:
`nc -w 2 mimas.picoctf.net 55193 < original_modified.jpg`

Check your modified picture here:
`nc -d mimas.picoctf.net 64151`

## Data
* original.png

## Solution
We find the following metadata with `exiftool`:
```
$ exiftool original.jpg
ExifTool Version Number         : 12.76
File Name                       : original.jpg
Directory                       : .
File Size                       : 2.9 MB
File Modification Date/Time     : 2024:03:26 11:58:39+01:00
File Access Date/Time           : 2024:03:26 11:59:01+01:00
File Inode Change Date/Time     : 2024:03:26 11:58:39+01:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
Exif Byte Order                 : Little-endian (Intel, II)
Image Description               :
Make                            : samsung
Camera Model Name               : SM-A326U
Orientation                     : Rotate 90 CW
X Resolution                    : 72
Y Resolution                    : 72
Resolution Unit                 : inches
Software                        : MediaTek Camera Application
Modify Date                     : 2023:11:20 15:46:23
Y Cb Cr Positioning             : Co-sited
Exposure Time                   : 1/24
F Number                        : 1.8
Exposure Program                : Program AE
ISO                             : 500
Sensitivity Type                : Unknown
Recommended Exposure Index      : 0
Exif Version                    : 0220
Date/Time Original              : 2023:11:20 15:46:23
Create Date                     : 2023:11:20 15:46:23
Components Configuration        : Y, Cb, Cr, -
Shutter Speed Value             : 1/24
Aperture Value                  : 1.9
Brightness Value                : 3
Exposure Compensation           : 0
Max Aperture Value              : 1.8
Metering Mode                   : Center-weighted average
Light Source                    : Other
Flash                           : On, Fired
Focal Length                    : 4.6 mm
Sub Sec Time                    : 703
Sub Sec Time Original           : 703
Sub Sec Time Digitized          : 703
Flashpix Version                : 0100
Color Space                     : sRGB
Exif Image Width                : 4000
Exif Image Height               : 3000
Interoperability Index          : R98 - DCF basic file (sRGB)
Interoperability Version        : 0100
Exposure Mode                   : Auto
White Balance                   : Auto
Digital Zoom Ratio              : 1
Focal Length In 35mm Format     : 25 mm
Scene Capture Type              : Standard
Compression                     : JPEG (old-style)
Thumbnail Offset                : 1408
Thumbnail Length                : 64000
Image Width                     : 4000
Image Height                    : 3000
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Time Stamp                      : 2023:11:20 21:46:21.420+01:00
MCC Data                        : United States / Guam (310)
Aperture                        : 1.8
Image Size                      : 4000x3000
Megapixels                      : 12.0
Scale Factor To 35 mm Equivalent: 5.4
Shutter Speed                   : 1/24
Create Date                     : 2023:11:20 15:46:23.703
Date/Time Original              : 2023:11:20 15:46:23.703
Modify Date                     : 2023:11:20 15:46:23.703
Thumbnail Image                 : (Binary data 64000 bytes, use -b option to extract)
Circle Of Confusion             : 0.006 mm
Field Of View                   : 71.5 deg
Focal Length                    : 4.6 mm (35 mm equivalent: 25.0 mm)
Hyperfocal Distance             : 2.13 m
Light Value                     : 4.0
```

We have to change the following ones:
```
$ exiftool original.jpg | egrep "202."
egrep: warning: egrep is obsolescent; using grep -E

[FILE TIMESTAMPS]

Modify Date                     : 2023:11:20 15:46:23
Date/Time Original              : 2023:11:20 15:46:23
Create Date                     : 2023:11:20 15:46:23
Time Stamp                      : 2023:11:20 21:46:21.420+01:00
Create Date                     : 2023:11:20 15:46:23.703
Date/Time Original              : 2023:11:20 15:46:23.703
Modify Date                     : 2023:11:20 15:46:23.703
$
```

To change the first few is pretty simple. We can also use `exiftool`:
```
$ exiftool "-ModifyDate=1970:01:01 00:00:00.001+00:00" _original.jpg

    1 image files updated
$ exiftool "-DateTimeOriginal=1970:01:01 00:00:00.001+00:00" _original.jpg

    1 image files updated
$ exiftool "-CreateDate=1970:01:01 00:00:00.001+00:00" _original.jpg

    1 image files updated
$ exiftool "-TimeStamp=1970:01:01 00:00:00.001+00:00" _original.jpg

Warning: Not an integer for XMP-apple-fi:TimeStamp
    0 image files updated
    1 image files unchanged
$ exiftool "-CreateDate=1970:01:01 00:00:00.001+00:00" _original.jpg

    1 image files updated
$ exiftool "-DateTimeOriginal=1970:01:01 00:00:00.001+00:00" _original.jpg

    1 image files updated
$ exiftool "-ModifyDate=1970:01:01 00:00:00.001+00:00" _original.jpg

    1 image files updated
$
```
`Time Stamp` is in epoch format, which is an integer. Our Timestamp corresponds to the value `1`. So we can set it as followed:
```
$ exiftool "-TimeStamp=1" _original.jpg

    1 image files updated
$
```
_(`0` or 1970:01:01 00:00:00.000+00:00 was the beginning of the time counting in computer science.)_

You can also convert your timestamps [here](https://www.epochconverter.com/)


Then we have to set also the following ones:
```
Sub Sec Time                    : 703
Sub Sec Time Original           : 703
Sub Sec Time Digitized          : 703
```
with
```
$ exiftool "-SubSecTime=001" _original.jpg
    1 image files updated
$ exiftool "-SubSecTimeOriginal=001" _original.jpg
    1 image files updated
$ exiftool "-SubSecTimeDigitized=001" _original.jpg
    1 image files updated
$
```
This is because some timestamps doesn't support subseconds and uses another data field.

The last one is a bit more tricky, because it's not shown directly. See the error from the checking tool of picoCTF:
```
Checking tag 7/7
Timezones do not have to match, as long as it's the equivalent time.
Looking at Samsung: TimeStamp
Looking for '1970:01:01 00:00:00.001+00:00'
Found: 2023:11:20 20:46:21.420+00:00
Oops! That tag isn't right. Please try again.
Total received bytes: 1199
Total sent bytes: 0
```

We can find this value only with the verbose information:
```
$ exiftool -v _original.jpg | less

[...]

Samsung trailer (143 bytes at offset 0x2b8e71):
  SamsungTrailer_0x0a01Name = Image_UTC_Data
  TimeStamp = 1700513181420
  SamsungTrailer_0x0aa1Name = MCC_Data
  MCCData = 310
  SamsungTrailer_0x0c61Name = Camera_Capture_Mode_Info
  SamsungTrailer_0x0c61 = 1
```
It's again in epoch format and we cannot change it with `exiftool`. But we have the offset `0x2b8e71`. With a hexeditor we can find the value:
```
002b8e70  d9 00 00 01 0a 0e 00 00  00 49 6d 61 67 65 5f 55  |.........Image_U|
002b8e80  54 43 5f 44 61 74 61 31  37 30 30 35 31 33 31 38  |TC_Data170051318|
002b8e90  31 34 32 30 00 00 a1 0a  08 00 00 00 4d 43 43 5f  |1420........MCC_|
002b8ea0  44 61 74 61 33 31 30 00  00 61 0c 18 00 00 00 43  |Data310..a.....C|
002b8eb0  61 6d 65 72 61 5f 43 61  70 74 75 72 65 5f 4d 6f  |amera_Capture_Mo|
002b8ec0  64 65 5f 49 6e 66 6f 31  53 45 46 48 6b 00 00 00  |de_Info1SEFHk...|
```
We now have to change it from  the above to the following (representation for `1`):
```
002b8e80  54 43 5f 44 61 74 61 31  00 00 00 00 00 00 00 00  |TC_Data1........|
002b8e90  00 00 00 00 00 00 a1 0a  08 00 00 00 4d 43 43 5f  |............MCC_|
```

If we know check the file again, we receive our flag:
```
$ nc -w 2 mimas.picoctf.net 60617 < _original.jpg


^C$ nc -d mimas.picoctf.net 50579
Warning: Debugging support not compiled, option `-d' discarded. Using maximum verbosity.
Notice: Real hostname for mimas.picoctf.net [52.15.88.75] is ec2-52-15-88-75.us-east-2.compute.amazonaws.com
mimas.picoctf.net [52.15.88.75] 50579 open
MD5 of your picture:
e0a294985d9766a73ae00014efaef3fa  test.out

Checking tag 1/7
Looking at IFD0: ModifyDate
Looking for '1970:01:01 00:00:00'
Found: 1970:01:01 00:00:00
Great job, you got that one!

Checking tag 2/7
Looking at ExifIFD: DateTimeOriginal
Looking for '1970:01:01 00:00:00'
Found: 1970:01:01 00:00:00
Great job, you got that one!

Checking tag 3/7
Looking at ExifIFD: CreateDate
Looking for '1970:01:01 00:00:00'
Found: 1970:01:01 00:00:00
Great job, you got that one!

Checking tag 4/7
Looking at Composite: SubSecCreateDate
Looking for '1970:01:01 00:00:00.001'
Found: 1970:01:01 00:00:00.001
Great job, you got that one!

Checking tag 5/7
Looking at Composite: SubSecDateTimeOriginal
Looking for '1970:01:01 00:00:00.001'
Found: 1970:01:01 00:00:00.001
Great job, you got that one!

Checking tag 6/7
Looking at Composite: SubSecModifyDate
Looking for '1970:01:01 00:00:00.001'
Found: 1970:01:01 00:00:00.001
Great job, you got that one!

Checking tag 7/7
Timezones do not have to match, as long as it's the equivalent time.
Looking at Samsung: TimeStamp
Looking for '1970:01:01 00:00:00.001+00:00'
Found: 1970:01:01 00:00:00.001+00:00
Great job, you got that one!

You did it!
picoCTF{71m3_7r4v311ng_p1c7ur3_ed953b57}
Total received bytes: 1236
Total sent bytes: 0
$
```
