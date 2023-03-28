# FindAndOpen
Someone might have hidden the password in the trace file.
Find the key to unlock this file. This tracefile might be good to analyze.

## Files
- flag.zip
- dump.pcap

## Solution
Looking at the packages you can find the following five differen Ethernet packages, that seems interesting:
```
1	2022-10-22 07:33:08.916764	20:6f:6e:20:45:74	46:6c:79:69:6e:67	0x6865	43	Ethernet II
0000   46 6c 79 69 6e 67 20 6f 6e 20 45 74 68 65 72 6e   Flying on Ethern
0010   65 74 20 73 65 63 72 65 74 3a 20 49 73 20 74 68   et secret: Is th
0020   69 73 20 74 68 65 20 66 6c 61 67                  is the flag

23	2022-10-22 07:33:19.159572	76:51:31:52:47:65	69:42:77:61:57:4e	0x3143	47	Ethernet II
0000   69 42 77 61 57 4e 76 51 31 52 47 65 31 43 6f 75   iBwaWNvQ1RGe1Cou
0010   6c 64 20 74 68 65 20 66 6c 61 67 20 68 61 76 65   ld the flag have
0020   20 62 65 65 6e 20 73 70 6c 69 74 74 65 64 3f       been splitted?

48	2022-10-22 07:33:33.157638	50:4a:47:54:46:52	41:41:42:42:48:48	0x4c4b	70	Ethernet II
0000   41 41 42 42 48 48 50 4a 47 54 46 52 4c 4b 56 47   AABBHHPJGTFRLKVG
0010   68 70 63 79 42 70 63 79 42 30 61 47 55 67 63 32   hpcyBpcyB0aGUgc2
0020   56 6a 63 6d 56 30 4f 69 42 77 61 57 4e 76 51 31   VjcmV0OiBwaWNvQ1
0030   52 47 65 31 49 7a 4e 45 52 4a 54 6b 64 66 54 45   RGe1IzNERJTkdfTE
0040   39 4c 5a 46 38 3d                                 9LZF8=

49	2022-10-22 07:33:57.376525	76:51:31:52:47:65	50:42:77:61:57:55	0x7361	49	Ethernet II
0000   50 42 77 61 57 55 76 51 31 52 47 65 73 61 62 61   PBwaWUvQ1RGesaba
0010   62 61 62 6b 6a 61 41 53 4b 42 4b 53 42 41 43 56   babkjaASKBKSBACV
0020   56 41 56 53 44 44 53 53 53 53 44 53 4b 4a 42 4a   VAVSDDSSSSDSKJBJ
0030   53                                                S

58	2022-10-22 07:34:03.044104	76:51:31:52:47:65	50:42:77:61:57:55	0x314d	46	Ethernet II
0000   50 42 77 61 57 55 76 51 31 52 47 65 31 4d 61 79   PBwaWUvQ1RGe1May
0010   62 65 20 74 72 79 20 63 68 65 63 6b 69 6e 67 20   be try checking 
0020   74 68 65 20 6f 74 68 65 72 20 66 69 6c 65         the other file
```

The content of the third package looks like base encoded content. So throw this into CyberCheck will reveal the following content
```
This is the secret: picoCTF{R34DING_LOKd_
```

Seems like password for the zip file. Try it out
```
[root@picoctf FindAndOpen]$ unzip flag.zip
Archive:  flag.zip
[flag.zip] flag password:
 extracting: flag
[root@picoctf FindAndOpen]$ cat flag
picoCTF{R34DING_LOKd_fil56_succ3ss_8ec01288}
[root@picoctf FindAndOpen]$
```

The flag is picoCTF{R34DING\_LOKd\_fil56\_succ3ss\_8ec01288}
