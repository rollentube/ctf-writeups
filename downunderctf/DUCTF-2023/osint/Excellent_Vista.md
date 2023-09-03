# Excellent Vista! (beginner)
What a nice spot to stop,lookout and watch time go by, EXAMINE the image and discover where this was taken.

NOTE: Flag is case-insensitive and requires placing inside DUCTF{} wrapper! e.g DUCTF{Osint\_Lookout}

Author: Yo\_Yo\_Bro

## Files
ExcellentVista.jpg

## Solution
To get GPS information of the picture we can use _exiftool_:
```
$ exiftool ExcellentVista.jpg
ExifTool Version Number         : 12.60
File Name                       : ExcellentVista.jpg
Directory                       : .
File Size                       : 2.7 MB
File Modification Date/Time     : 2023:09:02 14:39:11+02:00
File Access Date/Time           : 2023:09:02 14:39:20+02:00
File Inode Change Date/Time     : 2023:09:02 14:39:16+02:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
Exif Byte Order                 : Big-endian (Motorola, MM)
X Resolution                    : 72
Y Resolution                    : 72
Resolution Unit                 : inches
Y Cb Cr Positioning             : Centered
Date/Time Original              : 2023:08:31 22:58:56
Create Date                     : 2023:08:31 22:58:56
Sub Sec Time Original           : 00
Sub Sec Time Digitized          : 00
GPS Version ID                  : 2.3.0.0
GPS Latitude Ref                : South
GPS Longitude Ref               : East
GPS Altitude Ref                : Above Sea Level
GPS Speed Ref                   : km/h
GPS Speed                       : 0
GPS Img Direction Ref           : True North
GPS Img Direction               : 122.5013812
GPS Dest Bearing Ref            : True North
GPS Dest Bearing                : 122.5013812
GPS Horizontal Positioning Error: 6.055886243 m
Padding                         : (Binary data 2060 bytes, use -b option to extract)
About                           : uuid:faf5bdd5-ba3d-11da-ad31-d33d75182f1b
Image Width                     : 4032
Image Height                    : 3024
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 4032x3024
Megapixels                      : 12.2
Create Date                     : 2023:08:31 22:58:56.00
Date/Time Original              : 2023:08:31 22:58:56.00
GPS Altitude                    : 70.5 m Above Sea Level
GPS Latitude                    : 29 deg 30' 34.33" S
GPS Longitude                   : 153 deg 21' 34.46" E
GPS Position                    : 29 deg 30' 34.33" S, 153 deg 21' 34.46" E
$
```

Espacially
```
GPS Position                    : 29 deg 30' 34.33" S, 153 deg 21' 34.46" E
```

If we throw this coordinates into for example Google Maps, we find the _Durrangan Lookout_ next to the location (the ccordinates has to be in format `29°30'34.3"S 153°21'34.5"E` for Google Maps).

So our flag is: `DUCTF{Durrangan_Lookout}`
