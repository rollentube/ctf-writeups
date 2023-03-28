# ReadMyCert
How about we take you on an adventure on exploring certificate signing requests (100 Points)
Take a look at this CSR file here.

## Files
- readmycert.csr

## Solution
An CSR file can be read out with 'openssl' for example
```
[root@picoctf ReadMyCert]$ openssl req -in readmycert.csr -noout -text
Certificate Request:
    Data:
        Version: 1 (0x0)
        Subject: CN = picoCTF{read_mycert_7834c5f2}, name = ctfPlayer
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                Public-Key: (2048 bit)
                Modulus:
                    00:b3:42:ab:6e:fe:d7:47:5c:8b:f8:10:fd:b0:71:
                    ce:ab:44:3a:0a:20:69:a6:fa:cc:6e:76:f5:a2:2e:
                    2a:c2:3d:c3:59:b3:52:03:65:19:de:f4:56:37:3a:
                    48:d4:c6:44:01:16:6d:06:ac:33:cc:c2:37:d8:97:
                    eb:08:26:9a:8b:44:fa:6e:3f:d7:fe:fe:42:4c:6e:
                    17:1b:df:74:93:82:ca:03:5d:d2:bb:48:b0:97:6d:
                    cc:2e:d9:78:6d:d7:24:5d:e7:cb:e1:4e:1a:b3:f5:
                    c6:78:bb:c5:62:29:22:3c:1f:5e:d1:1c:a6:b3:ba:
                    e5:64:5e:54:81:65:68:71:06:4b:1f:ea:44:c0:56:
                    80:8d:34:05:17:06:58:4b:a4:d5:78:11:31:7a:1f:
                    eb:76:7b:d6:5d:2d:c8:08:8d:71:5b:a2:bd:24:ce:
                    7f:a3:87:1f:51:4d:6d:d3:b7:c0:a5:f2:d3:de:10:
                    08:8b:7c:cb:19:f9:38:02:a2:dc:40:22:01:26:93:
                    ea:16:0a:8d:cb:3a:7a:50:95:dd:84:e2:e2:ec:49:
                    33:0d:e6:09:94:3a:1b:cc:a1:46:17:6f:f7:61:f5:
                    03:9c:50:c2:d4:13:59:3a:4f:17:b0:80:d1:e2:72:
                    ae:67:2d:14:81:13:a4:1b:d6:4c:d5:9f:3f:9a:e8:
                    ac:15
                Exponent: 65537 (0x10001)
        Attributes:
            Requested Extensions:
                X509v3 Extended Key Usage:
                    TLS Web Client Authentication
    Signature Algorithm: sha256WithRSAEncryption
    Signature Value:
        68:48:19:de:fd:bb:89:54:0b:78:42:d2:2a:4f:3d:d5:5f:01:
        9a:61:f5:68:db:8e:7b:bd:76:87:e2:c4:c8:e1:78:7f:af:e3:
        e3:54:f3:15:ce:95:5c:34:b1:50:7a:fb:1c:81:ea:23:80:2b:
        eb:90:eb:0f:c5:d2:7e:2d:95:c1:76:02:41:d7:e3:26:3c:d6:
        03:78:76:94:1d:3c:3f:4a:3d:0c:0b:77:f6:b2:d9:86:b6:6b:
        9a:7f:fb:f4:95:c9:9b:68:d9:80:a7:40:31:b8:f1:e2:72:d2:
        dc:99:68:09:7c:5f:11:91:a4:00:ec:c9:75:c6:18:16:b1:08:
        5d:86:27:8c:bd:b4:01:de:f2:a7:aa:46:87:21:48:ac:d0:0a:
        45:80:0b:06:56:d2:9f:e6:c5:01:11:b1:3f:13:39:d9:15:8f:
        24:d1:4a:47:29:de:d3:fa:31:da:eb:7a:8b:57:52:33:56:15:
        ee:f5:8d:9b:43:a0:63:1c:b3:50:98:38:26:d4:99:39:77:c7:
        cf:e0:da:db:a6:64:8e:c5:1d:e0:b2:6d:91:dd:b2:39:bb:5d:
        ac:30:7f:ae:8b:81:a1:28:74:7e:0a:4f:c9:96:b5:9c:d4:72:
        b2:83:87:09:f9:e0:49:a7:7a:f3:21:50:5a:de:38:ea:de:65:
        98:7d:64:4f
[root@picoctf ReadMyCert]$
```

The flag is: picoCTF{read\_mycert\_7834c5f2}
