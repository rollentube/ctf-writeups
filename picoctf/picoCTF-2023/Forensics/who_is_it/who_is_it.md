# who is it
Someone just sent you an email claiming to be Google's co-founder Larry Page but you suspect a scam.
Can you help us identify whose mail server the email actually originated from?
Download the email file here. Flag: picoCTF{FirstnameLastname} (100 Points)

## Files
- email-export.eml

## Solution
The file contains the full mail, included content and headers. In the headers you can see the domain and the mail server of the domain
```
Received-SPF: pass (google.com: domain of lpage@onionmail.org designates 173.249.33.206 as permitted sender) client-ip=173.249.33.206;
```

If you check the domain and the ip with a tool like 'whois', you can find the name Wilhelm Zwalina
```
[root@picoctf who_is_it]$ whois 173.249.33.206

#
# ARIN WHOIS data and services are subject to the Terms of Use
# available at: https://www.arin.net/resources/registry/whois/tou/
#
# If you see inaccuracies in the results, please report at
# https://www.arin.net/resources/registry/whois/inaccuracy_reporting/
#
# Copyright 1997-2023, American Registry for Internet Numbers, Ltd.
#

[...]

person:         Wilhelm Zwalina
address:        Contabo GmbH
address:        Aschauer Str. 32a

[...]

[root@picoctf who_is_it]$
```

So the flag is: picoCTF{WilhelmZwalina}
