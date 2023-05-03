# Intro to Forensics 3
There is a new variant of a ransomware, messing up my image files. Somebody told me a vital part of forensics is to understand files. Could you help me to recover my image file?

## Solution
Die PNG Datei laesst sich nicht oeffnen. Mit einem Hexeditor findet man Aufgenscheinlich keine Fehler an Header oder Footer.

Analysiert man das Bild mit Tools wie
- https://www.nayuki.io/page/png-file-chunk-inspector
- https://github.com/Hedroed/png-parser
- https://github.com/sherlly/PCRT

kann man sehen, dass die CRC Checksummen der einzelnen Chunks nichts stimmen:
```
 root  ~  ctf  cscg_23  forensic_3  png-parser --crc intro-forensics-3.png
[...]
Filename: intro-forensics-3.png | Size: 4658757

[00000000-00000032] (0)
IHDR:
CRC : 00000000 : Incorrect must be 1a3057f6
Data size : 13

[00000033-00194145] (1)
IDAT:
CRC : 00000005 : Incorrect must be bb03d15f
Data size : 194101

[00194146-00388258] (2)
IDAT:
CRC : 0000000b : Incorrect must be 4fcd95c6
Data size : 194101

[00388259-00582371] (3)
IDAT:
CRC : 00000010 : Incorrect must be fd3e7204
Data size : 194101
[...]
```

Korrigiert man diese fuehrt dies allerdings nicht zum gewuenschten Erfolg. Das Bild bleibt grau (`png-parser intro-forensics-3.png -o test.png`).

Schaut man genauer auf die manipulierten Checksummen, faellt auf, dass diese nummiert scheinen:
```
 root  ~  ctf  cscg_23  forensic_3  png-parser --crc intro-forensics-3.png | grep CRC                                                       SIGINT 
CRC : 00000000 : Incorrect must be 1a3057f6
CRC : 00000005 : Incorrect must be bb03d15f
CRC : 0000000b : Incorrect must be 4fcd95c6
CRC : 00000010 : Incorrect must be fd3e7204
CRC : 00000014 : Incorrect must be fce7782d
CRC : 00000018 : Incorrect must be 036c52b6
CRC : 00000012 : Incorrect must be 424003c5
CRC : 0000000d : Incorrect must be be6bb9d9
CRC : 00000009 : Incorrect must be aa2c749a
CRC : 00000006 : Incorrect must be 7b0333a4
CRC : 00000004 : Incorrect must be 7c4da485
CRC : 00000017 : Incorrect must be 165cd707
CRC : 00000011 : Incorrect must be 95111258
CRC : 0000000c : Incorrect must be f54aaa76
CRC : 00000008 : Incorrect must be 20d88e32
CRC : 00000003 : Incorrect must be e22bfc32
CRC : 00000016 : Incorrect must be bee5a9f7
CRC : 00000013 : Incorrect must be 65be2225
CRC : 0000000f : Incorrect must be 1c35533a
CRC : 00000015 : Incorrect must be 69c87f54
CRC : 0000000e : Incorrect must be dfe9be2e
CRC : 00000007 : Incorrect must be a0f387aa
CRC : 00000002 : Incorrect must be 227a7e2c
CRC : 0000000a : Incorrect must be 58078fb6
CRC : 00000001 : Incorrect must be 1a131490
CRC : 00000019 : Incorrect must be ae426082
 root  ~  ctf  cscg_23  forensic_3  
 root  ~  ctf  cscg_23  forensic_3  png-parser --crc intro-forensics-3.png | grep CRC | awk -F ':' '{print $ 2}' | sort
 00000000
 00000001
 00000002
 00000003
 00000004
 00000005
 00000006
 00000007
 00000008
 00000009
 0000000a
 0000000b
 0000000c
 0000000d
 0000000e
 0000000f
 00000010
 00000011
 00000012
 00000013
 00000014
 00000015
 00000016
 00000017
 00000018
 00000019
 root  ~  ctf  cscg_23  forensic_3  
```

Die Chunks muessen also in die Reihenfolge der falschen CRC Checksummen gebracht werden. Die Extrahierung der einzelnen Chunks kann beispielsweise mit 'dd' erfolgen. Die Offsets kann man https://www.nayuki.io/page/png-file-chunk-inspector entnehmen oder `binwalk -R "IDAT" intro-forensics-3.png`. Allerdings sind bei letzerem nicht die ersten 4 Byte fuer die Data Size eingerechnet.

Die folgenden Befehle extrahieren die einzelnen Chunks
```
dd if=intro-forensics-3.png of=dd_start bs=1 count=32
dd if=intro-forensics-3.png of=dd_05 bs=1 count=194113 skip=33
dd if=intro-forensics-3.png of=dd_0B bs=1 count=194113 skip=194146
dd if=intro-forensics-3.png of=dd_10 bs=1 count=194113 skip=388259
dd if=intro-forensics-3.png of=dd_14 bs=1 count=194113 skip=582372
dd if=intro-forensics-3.png of=dd_18 bs=1 count=194113 skip=776485
dd if=intro-forensics-3.png of=dd_12 bs=1 count=194113 skip=970598
dd if=intro-forensics-3.png of=dd_0D bs=1 count=194113 skip=1164711
dd if=intro-forensics-3.png of=dd_09 bs=1 count=194113 skip=1358824
dd if=intro-forensics-3.png of=dd_06 bs=1 count=194113 skip=1552937
dd if=intro-forensics-3.png of=dd_04 bs=1 count=194113 skip=1747050
dd if=intro-forensics-3.png of=dd_17 bs=1 count=194113 skip=1941163
dd if=intro-forensics-3.png of=dd_11 bs=1 count=194113 skip=2135276
dd if=intro-forensics-3.png of=dd_0C bs=1 count=194113 skip=2329389
dd if=intro-forensics-3.png of=dd_08 bs=1 count=194113 skip=2523502
dd if=intro-forensics-3.png of=dd_03 bs=1 count=194113 skip=2717615
dd if=intro-forensics-3.png of=dd_16 bs=1 count=194113 skip=2911728
dd if=intro-forensics-3.png of=dd_13 bs=1 count=194113 skip=3105841
dd if=intro-forensics-3.png of=dd_0F bs=1 count=194113 skip=3299954
dd if=intro-forensics-3.png of=dd_15 bs=1 count=194113 skip=3494067
dd if=intro-forensics-3.png of=dd_0E bs=1 count=194113 skip=3688180
dd if=intro-forensics-3.png of=dd_07 bs=1 count=194113 skip=3882293
dd if=intro-forensics-3.png of=dd_02 bs=1 count=194113 skip=4076406
dd if=intro-forensics-3.png of=dd_0A bs=1 count=194113 skip=4270519
dd if=intro-forensics-3.png of=dd_01 bs=1 count=194113 skip=4464632
dd if=intro-forensics-3.png of=dd_end bs=1 count=12 skip=4658745
```

Nun kann man diese mit einem Hex Editor wie bspw. Bless Hexeditor in der korrekten Reihenfolge zusammensetzen. Header (00) und Footer (19) scheinen bereits korrekt sortiert zu sein, weshalb man auf die Reihenfolge 01-09, 0a-0f, 10-18 schliessen kann.

Korrekt angeordnet koennen die Checksummen repariert werden und das Bild kann korrekt dargestellt werden
```
png-parser fixed.png solution.png
```

Das Bild zeigt einen Screenshot aus Borderlands. In dem Ingame Chat ist die Flag geschrieben: **CSCG{g1v3\_m3\_4\_sm1l3\_cl4ptr4p}**

![Solution](images/solution.png)

## Nice to know
Mit Wireshark koennen PNG File ebenfalls geoeffnet werden. Wireshark parsed dann entsprechend die Chunks und listet diese auf.
