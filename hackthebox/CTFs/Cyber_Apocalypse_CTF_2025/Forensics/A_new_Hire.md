# A new Hire
```
┌──(kali㉿kali)-[~/Desktop/htb/cyberapocolapse]
└─$ less email.eml

You can review his resume here:
`storage.microsoftcloudservices.com:[PORT]/index.php`
[...]
```

```
┌──(kali㉿kali)-[~/Desktop/htb/cyberapocolapse]
└─$ curl 83.136.253.44:46737/index.php                                                       

    function getResume() {
      window.location.href=`search:displayname=Downloads&subquery=\\\\${window.location.hostname}@${window.location.port}\\3fe1690d955e8fd2a0b282501570e1f4\\resumes\\`;
    }
[...]
```

This link runs into a ftp server where we can find this file:
```
┌──(kali㉿kali)-[~/Desktop/htb/cyberapocolapse]
└─$ curl http://83.136.253.44:46737/3fe1690d955e8fd2a0b282501570e1f4/configs/client.py
import base64

key = base64.decode("SFRCezRQVF8yOF80bmRfbTFjcjBzMGZ0X3MzNHJjaD0xbjF0MTRsXzRjYzNzISF9Cg==")

[...]
```

```
┌──(kali㉿kali)-[~/Desktop/htb/cyberapocolapse]
└─$ echo "SFRCezRQVF8yOF80bmRfbTFjcjBzMGZ0X3MzNHJjaD0xbjF0MTRsXzRjYzNzISF9Cg==" | base64 -d
HTB{4PT_28_4nd_m1cr0s0ft_s34rch=1n1t14l_4cc3s!!}

┌──(kali㉿kali)-[~/Desktop/htb/cyberapocolapse]
└─$ 
```
