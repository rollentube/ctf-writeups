# PcapPoisoning
How about some hide and seek heh?
Download this file and find the flag.

## Files
- trace.pcap

## Solution
Inspecting some of the packages, contents, follow streams. Stream 1 brings the flag
```
4	2023-03-15 02:41:08.448477	172.16.0.2	10.253.0.6	FTP	74	Request:     username root    password toor
507	2023-03-15 02:41:08.548126	172.16.0.2	10.253.0.6	TCP	82	[TCP Retransmission] [TCP Port numbers reused] 20 → 21 [SYN] Seq=0 Win=8192 Len=42

0000   45 00 00 52 00 01 00 00 40 06 c3 90 ac 10 00 02   E..R....@.......
0010   0a fd 00 06 00 14 00 15 00 00 00 00 00 00 00 00   ................
0020   50 02 20 00 ba ea 00 00 70 69 63 6f 43 54 46 7b   P. .....picoCTF{
0030   50 36 34 50 5f 34 4e 34 4c 37 53 31 53 5f 53 55   P64P_4N4L7S1S_SU
0040   35 35 33 35 35 46 55 4c 5f 65 30 64 62 31 31 66   55355FUL_e0db11f
0050   31 7d                                             1}
```

The flag is: picoCTF{P64P\_4N4L7S1S\_SU55355FUL\_e0db11f1}
