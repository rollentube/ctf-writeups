0:  55                      push   ebp
1:  89 e5                   mov    ebp,esp
3:  89 ee                   mov    esi,ebp
5:  83 c6 08                add    esi,0x8
8:  8b 36                   mov    esi,DWORD PTR [esi]
a:  8a 06                   mov    al,BYTE PTR [esi]
c:  3c 43                   cmp    al,0x43
e:  75 39                   jne    0x49
10: 46                      inc    esi
11: 8a 06                   mov    al,BYTE PTR [esi]
13: 3c 53                   cmp    al,0x53
15: 75 32                   jne    0x49
17: 46                      inc    esi
18: 8a 06                   mov    al,BYTE PTR [esi]
1a: 3c 43                   cmp    al,0x43
1c: 75 2b                   jne    0x49
1e: 46                      inc    esi
1f: 8a 06                   mov    al,BYTE PTR [esi]
21: 3c 47                   cmp    al,0x47
23: 75 24                   jne    0x49
25: 46                      inc    esi
26: 8a 06                   mov    al,BYTE PTR [esi]
28: 3c 7b                   cmp    al,0x7b
2a: 75 1d                   jne    0x49
2c: 46                      inc    esi
2d: 31 c9                   xor    ecx,ecx
2f: 8a 04 0e                mov    al,BYTE PTR [esi+ecx*1]
32: 3c 7d                   cmp    al,0x7d
34: 74 13                   je     0x49
36: 3c 00                   cmp    al,0x0
38: 74 0f                   je     0x49
3a: ba 10 00 00 00          mov    edx,0x10
3f: 29 ca                   sub    edx,ecx
41: 00 d0                   add    al,dl
43: 88 04 0e                mov    BYTE PTR [esi+ecx*1],al
46: 41                      inc    ecx
47: eb e6                   jmp    0x2f
49: 83 ee 05                sub    esi,0x5
4c: 89 f0                   mov    eax,esi
4e: c9                      leave
4f: c3                      ret
