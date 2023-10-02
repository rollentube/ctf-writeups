# Needle in the Wifi Stack (easy)
## Files
* frames.pcap

## Solution
The pcap shows WLAN management packages:
```
$ tshark -r frames.pcap | tail
100991  -0.042350 22:22:22:22:22:22 → Broadcast    802.11 96 Beacon frame, SN=0, FN=0, Flags=........, BI=100, SSID="bm90IGhlcmUgZWk3aGVyCg=="
100992  -0.053371 22:22:22:22:22:22 → Broadcast    802.11 84 Beacon frame, SN=0, FN=0, Flags=........, BI=100, SSID="bjB0IGgzcjMK"
100993   0.002501 22:22:22:22:22:22 → Broadcast    802.11 120 Beacon frame, SN=0, FN=0, Flags=........, BI=100, SSID="MW9vMDAwb28wMDBvbzAwMDc3YSB0cmFmZmljIDcwZDR5Cg=="
100994  -0.035372 22:22:22:22:22:22 → Broadcast    802.11 96 Beacon frame, SN=0, FN=0, Flags=........, BI=100, SSID="bm83IGhlcjMgM2l0aDNyCg=="
100995  -0.013123 22:22:22:22:22:22 → Broadcast    802.11 108 Beacon frame, SN=0, FN=0, Flags=........, BI=100, SSID="d2gzbiBpbiBkMHViNywgaGFjayBoYXJkM3IK"
100996  -0.045852 22:22:22:22:22:22 → Broadcast    802.11 84 Beacon frame, SN=0, FN=0, Flags=........, BI=100, SSID="bjB0IGhlcmUK"
100997  -0.020147 22:22:22:22:22:22 → Broadcast    802.11 136 Beacon frame, SN=0, FN=0, Flags=........, BI=100, SSID="eTB1IHByb2I0Ymx5IDVoMHUxZG4nNyA3cnkgN28gZDAgN2hpcyBtYW51NDExeQo="
100998   0.023733 22:22:22:22:22:22 → Broadcast    802.11 116 Beacon frame, SN=0, FN=0, Flags=........, BI=100, SSID="YmU0Y29uIGZyYW1lNSwgczAgaG90IHJpNmh0IG5vdwo="
100999   0.029637 22:22:22:22:22:22 → Broadcast    802.11 140 Beacon frame, SN=0, FN=0, Flags=........, BI=100, SSID="N2hpcyBpcyBub3QgdGgzIG5lN3dvcmsgbmFtMyB5b3UgYXJlIGwwb2tpbmcgZjByCg=="
101000   0.004824 22:22:22:22:22:22 → Broadcast    802.11 128 Beacon frame, SN=0, FN=0, Flags=........, BI=100, SSID="NGwxIHRoZSBjMDAxIGtpZDUgNHIzIHAxNHlpbjYgd2k3aCA4MDIuMTEK"
$
```

The SSIDs of the packages are Base encoded. Probably Base64, because it is pretty common.

With `thark` we can filter the SSIDs:
```
$ tshark -r frames.pcap -Tfields -e wlan.ssid | tail
626d39304947686c636d55675a576b336147567943673d3d
626a42304947677a636a4d4b
4d5739764d444177623238774d444276627a41774d44633359534230636d466d5a6d6c6a494463775a44523543673d3d
626d38334947686c636a4d674d326c3061444e7943673d3d
6432677a626942706269426b4d4856694e7977676147466a6179426f59584a6b4d33494b
626a42304947686c636d554b
655442314948427962324930596d78354944566f4d4855785a47346e4e794133636e6b674e3238675a4441674e32687063794274595735314e44457865516f3d
596d55305932397549475a795957316c4e537767637a41676147393049484a704e6d68304947357664776f3d
4e3268706379427063794275623351676447677a4947356c4e336476636d7367626d46744d7942356233556759584a6c4947777762327470626d63675a6a427943673d3d
4e4777784948526f5a53426a4d444178494774705a4455674e48497a494841784e486c70626a596764326b33614341344d4449754d54454b
$
```

Now we have to bring the raw data back into ASCII representation and decode the Base64. This can be done with the CLI tools `xxd` and `base64`:
```
$ tshark -r frames.pcap -Tfields -e wlan.ssid | xxd -r -p | base64 -d | tail
not here ei7her
n0t h3r3
1oo000oo000oo00077a traffic 70d4y
no7 her3 3ith3r
wh3n in d0ub7, hack hard3r
n0t here
y0u prob4bly 5h0u1dn'7 7ry 7o d0 7his manu411y
be4con frame5, s0 hot ri6ht now
7his is not th3 ne7work nam3 you are l0oking f0r
4l1 the c001 kid5 4r3 p14yin6 wi7h 802.11
$
```

The last thing, that we have to do, is to grep for our flag:
```
$ tshark -r frames.pcap -Tfields -e wlan.ssid | xxd -r -p | base64 -d | grep bctf | uniq
bctf{tw0_po1nt_4_g33_c0ng3s7i0n}
$
```