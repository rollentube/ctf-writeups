# Stealth Invasion
Memory dump. Newest version of Volatility 3 needed.

https://blog.onfvp.com/post/volatility-cheatsheet/

## 1. What is the PID of the Original (First) Google Chrome process:
`4080`

```
┌──(venv)─(kali㉿kali)-[~/Desktop/volatility3]
└─$ vol -f ../htb/cyberapocolapse/memdump.elf windows.pslist | grep -i chrome
4080ress529600.0chrome.exe      0xa708c729e0c0  48      -       1       False   2025-03-13 17:01:04.000000 UTC  N/A     Disabled
2736    4080    chrome.exe      0xa708c74560c0  11      -       1       False   2025-03-13 17:01:04.000000 UTC  N/A     Disabled
5688    4080    chrome.exe      0xa708c6cf4080  18      -       1       False   2025-03-13 17:01:04.000000 UTC  N/A     Disabled
7504    4080    chrome.exe      0xa708c6b19080  24      -       1       False   2025-03-13 17:01:04.000000 UTC  N/A     Disabled
1220    4080    chrome.exe      0xa708c7514080  9       -       1       False   2025-03-13 17:01:04.000000 UTC  N/A     Disabled
4612    4080    chrome.exe      0xa708c7230080  15      -       1       False   2025-03-13 17:01:05.000000 UTC  N/A     Disabled
8036    4080    chrome.exe      0xa708caec6080  13      -       1       False   2025-03-13 17:01:08.000000 UTC  N/A     Disabled
1368    4080    chrome.exe      0xa708c6594080  14      -       1       False   2025-03-13 17:01:11.000000 UTC  N/A     Disabled

┌──(venv)─(kali㉿kali)-[~/Desktop/volatility3]
└─$ 
```
  
## 2. What is the only Folder on the Desktop
`malext`

```
┌──(venv)─(kali㉿kali)-[~/Desktop/volatility3]
└─$ vol -f ../htb/cyberapocolapse/memdump.elf windows.filescan > ../htb/cyberapocolapse/memdump_filescan

┌──(venv)─(kali㉿kali)-[~/Desktop/volatility3]
└─$ grep -i users ../htb/cyberapocolapse/memdump_filescan | grep Desktop
0xa708c7697e20  \Users\Public\Desktop\desktop.ini
0xa708c769d410  \Users\selene\Desktop\Microsoft Edge.lnk
0xa708c76a4c60  \Users\Public\Desktop
0xa708c76a52a0  \Users\Public\Desktop
0xa708c76b5790  \Users\selene\Desktop\desktop.ini
0xa708c76d38d0  \Users\Public\Desktop\Google Chrome.lnk
0xa708c81304b0  \Users\selene\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Accessibility\Desktop.ini
0xa708c8134c90  \Users\selene\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\System Tools\Desktop.ini
0xa708c8b39dd0  \Users\selene\AppData\Roaming\Microsoft\Windows\SendTo\Desktop.ini
0xa708c8d9ec30  \Users\selene\Desktop\malext\background.js
0xa708c8d9fef0  \Users\selene\Desktop\malext\manifest.json
0xa708c8da14d0  \Users\selene\Desktop\malext\rules.json
0xa708c8da1e30  \Users\selene\Desktop\malext\content-script.js
0xa708c8dac3d0  \Users\selene\Desktop
0xa708c8dad820  \Users\selene\Desktop
0xa708ca379980  \Users\selene\Desktop\malext\_metadata\generated_indexed_rulesets\_ruleset1

┌──(venv)─(kali㉿kali)-[~/Desktop/volatility3]
└─$ 

```

## 3. What is the Extention's ID (ex: hlkenndednhfkekhgcdicdfddnkalmdm)
`nnjofihdjilebhiiemfmdlpbdkbjcpae`

```
┌──(venv)─(kali㉿kali)-[~/Desktop/volatility3]
└─$ grep -i chrome ../htb/cyberapocolapse/memdump_filescan | grep -i extension
0xa708c79892d0  \Users\selene\AppData\Local\Google\Chrome\User Data\Default\Extension Rules\000003.log
0xa708c79aa930  \Users\selene\AppData\Local\Google\Chrome\User Data\Default\Extension Scripts\LOG
0xa708c79b11e0  \Users\selene\AppData\Local\Google\Chrome\User Data\Default\Extension Scripts\LOCK
0xa708c79b19b0  \Users\selene\AppData\Local\Google\Chrome\User Data\Default\Extension Rules\MANIFEST-000001
0xa708c79bcbd0  \Users\selene\AppData\Local\Google\Chrome\User Data\Default\Extension Rules\000003.log
0xa708c79bdb70  \Users\selene\AppData\Local\Google\Chrome\User Data\Default\Extension Scripts\MANIFEST-000001
0xa708c8828170  \Users\selene\AppData\Local\Google\Chrome\User Data\Default\Extensions\nmmhkkegccagdldgiimedpiccmgmieda\1.0.0.6_0\_metadata\computed_hashes.json
0xa708c8828300  \Users\selene\AppData\Local\Google\Chrome\User Data\Default\Extensions\nmmhkkegccagdldgiimedpiccmgmieda\1.0.0.6_0\_metadata\verified_contents.json
0xa708c8830c80  \Users\selene\AppData\Local\Google\Chrome\User Data\Default\Local Extension Settings\nnjofihdjilebhiiemfmdlpbdkbjcpae\LOG
0xa708c8836720  \Program Files\Google\Chrome\Application\134.0.6998.89\default_apps\external_extensions.json
0xa708c8943e20  \Users\selene\AppData\Local\Google\Chrome\User Data\Default\Extension State\000008.log
0xa708c89463a0  \Users\selene\AppData\Local\Google\Chrome\User Data\Default\Extension State\CURRENT
0xa708c8981810  \Users\selene\AppData\Local\Google\Chrome\User Data\Default\Extension State\MANIFEST-000007
0xa708c8b03460  \Users\selene\AppData\Local\Google\Chrome\User Data\Default\Extension Scripts\000003.log
0xa708c8b07150  \Users\selene\AppData\Local\Google\Chrome\User Data\Default\Extension Rules\000003.log
0xa708c8daf120  \Users\selene\AppData\Local\Google\Chrome\User Data\Default\Extension Rules\CURRENT
0xa708c8daf2b0  \Users\selene\AppData\Local\Google\Chrome\User Data\Default\Extension Rules\MANIFEST-000001
0xa708c8db4260  \Users\selene\AppData\Local\Google\Chrome\User Data\Default\Extension Scripts\CURRENT
0xa708c8db4710  \Users\selene\AppData\Local\Google\Chrome\User Data\Default\Extension Scripts\MANIFEST-000001
0xa708c8dca380  \Users\selene\AppData\Local\Google\Chrome\User Data\Default\Extension Cookies
0xa708c8dd5be0  \Users\selene\AppData\Local\Google\Chrome\User Data\Default\Local Extension Settings\nnjofihdjilebhiiemfmdlpbdkbjcpae\MANIFEST-000001
0xa708c8dda230  \Users\selene\AppData\Local\Google\Chrome\User Data\Default\Local Extension Settings\nnjofihdjilebhiiemfmdlpbdkbjcpae\CURRENTdbtmp
0xa708c8f2b500  \Users\selene\AppData\Local\Google\Chrome\User Data\Default\Local Extension Settings\nnjofihdjilebhiiemfmdlpbdkbjcpae
0xa708c8f2d760  \Users\selene\AppData\Local\Google\Chrome\User Data\Default\Local Extension Settings\nnjofihdjilebhiiemfmdlpbdkbjcpae
0xa708ca363090  \Users\selene\AppData\Local\Google\Chrome\User Data\Default\Extension Rules\LOCK
0xa708ca36c820  \Users\selene\AppData\Local\Google\Chrome\User Data\Default\Extension Rules\LOG
0xa708cab98380  \Users\selene\AppData\Local\Google\Chrome\User Data\Default\Extension State\000008.log
0xa708cab99c80  \Users\selene\AppData\Local\Google\Chrome\User Data\Default\Extension Rules\LOG
0xa708cab9a2c0  \Users\selene\AppData\Local\Google\Chrome\User Data\Default\Local Extension Settings\nnjofihdjilebhiiemfmdlpbdkbjcpae\LOG
0xa708cab9a5e0  \Users\selene\AppData\Local\Google\Chrome\User Data\Default\Extension State\LOCK
0xa708cab9de20  \Users\selene\AppData\Local\Google\Chrome\User Data\Default\Extension Scripts\LOG
0xa708cab9eaa0  \Users\selene\AppData\Local\Google\Chrome\User Data\Default\Extension State\LOG
0xa708caba14d0  \Users\selene\AppData\Local\Google\Chrome\User Data\Default\Local Extension Settings\nnjofihdjilebhiiemfmdlpbdkbjcpae\000003.log
0xa708caba2dd0  \Users\selene\AppData\Local\Google\Chrome\User Data\Default\Extension State\MANIFEST-000007
0xa708caba6480  \Users\selene\AppData\Local\Google\Chrome\User Data\Default\Extension State\LOG
0xa708cabba4d0  \Users\selene\AppData\Local\Google\Chrome\User Data\Default\Extension Scripts\000003.log
0xa708cabba660  \Users\selene\AppData\Local\Google\Chrome\User Data\Default\Extension Scripts\000003.log

┌──(venv)─(kali㉿kali)-[~/Desktop/volatility3]
└─$ 
```

## 4. After examining the malicious extention's code, what is the log filename in which the datais stored
`000003.log`

```
┌──(venv)─(kali㉿kali)-[~/Desktop/volatility3]
└─$ grep nnjofihdjilebhiiemfmdlpbdkbjcpae ../htb/cyberapocolapse/memdump_filescan
0xa708c8830c80  \Users\selene\AppData\Local\Google\Chrome\User Data\Default\Local Extension Settings\nnjofihdjilebhiiemfmdlpbdkbjcpae\LOG
0xa708c8dd5be0  \Users\selene\AppData\Local\Google\Chrome\User Data\Default\Local Extension Settings\nnjofihdjilebhiiemfmdlpbdkbjcpae\MANIFEST-000001
0xa708c8dda230  \Users\selene\AppData\Local\Google\Chrome\User Data\Default\Local Extension Settings\nnjofihdjilebhiiemfmdlpbdkbjcpae\CURRENTdbtmp
0xa708c8f2b500  \Users\selene\AppData\Local\Google\Chrome\User Data\Default\Local Extension Settings\nnjofihdjilebhiiemfmdlpbdkbjcpae
0xa708c8f2d760  \Users\selene\AppData\Local\Google\Chrome\User Data\Default\Local Extension Settings\nnjofihdjilebhiiemfmdlpbdkbjcpae
0xa708cab9a2c0  \Users\selene\AppData\Local\Google\Chrome\User Data\Default\Local Extension Settings\nnjofihdjilebhiiemfmdlpbdkbjcpae\LOG
0xa708caba14d0  \Users\selene\AppData\Local\Google\Chrome\User Data\Default\Local Extension Settings\nnjofihdjilebhiiemfmdlpbdkbjcpae\000003.log

┌──(venv)─(kali㉿kali)-[~/Desktop/volatility3]
└─$
```

## 5. What is the URL the user navigated to
`drive.google.com`

```
┌──(venv)─(kali㉿kali)-[~/Desktop/volatility3]
└─$ grep nnjofihdjilebhiiemfmdlpbdkbjcpae ../htb/cyberapocolapse/memdump_filescan
0xa708c8830c80  \Users\selene\AppData\Local\Google\Chrome\User Data\Default\Local Extension Settings\nnjofihdjilebhiiemfmdlpbdkbjcpae\LOG
0xa708c8dd5be0  \Users\selene\AppData\Local\Google\Chrome\User Data\Default\Local Extension Settings\nnjofihdjilebhiiemfmdlpbdkbjcpae\MANIFEST-000001
0xa708c8dda230  \Users\selene\AppData\Local\Google\Chrome\User Data\Default\Local Extension Settings\nnjofihdjilebhiiemfmdlpbdkbjcpae\CURRENTdbtmp
0xa708c8f2b500  \Users\selene\AppData\Local\Google\Chrome\User Data\Default\Local Extension Settings\nnjofihdjilebhiiemfmdlpbdkbjcpae
0xa708c8f2d760  \Users\selene\AppData\Local\Google\Chrome\User Data\Default\Local Extension Settings\nnjofihdjilebhiiemfmdlpbdkbjcpae
0xa708cab9a2c0  \Users\selene\AppData\Local\Google\Chrome\User Data\Default\Local Extension Settings\nnjofihdjilebhiiemfmdlpbdkbjcpae\LOG
0xa708caba14d0  \Users\selene\AppData\Local\Google\Chrome\User Data\Default\Local Extension Settings\nnjofihdjilebhiiemfmdlpbdkbjcpae\000003.log

┌──(venv)─(kali㉿kali)-[~/Desktop/volatility3]
└─$ vol -f ../htb/cyberapocolapse/memdump.elf -o ../htb/cyberapocolapse/dump windows.dumpfiles --virtaddr 0xa708caba14d0
Volatility 3 Framework 2.25.0
Progress:  100.00               PDB scanning finished                        
Cache   FileObject      FileName        Result

DataSectionObject       0xa708caba14d0  000003.log      file.0xa708caba14d0.0xa708c9d90d00.DataSectionObject.000003.log.dat

┌──(venv)─(kali㉿kali)-[~/Desktop/volatility3]
└─$ strings ../htb/cyberapocolapse/dump/file.0xa708caba14d0.0xa708c9d90d00.DataSectionObject.000003.log.dat       
"dr"
"dri"\+
"driv"?W
"drive""
"drive."@:
log     "drive.g"
"drive.go"
"drive.goo"
"drive.goog"
"drive.googl"
"drive.google"
"drive.google."
"drive.google.c"
"drive.google.co"
"drive.google.com"IN
"drive.google.comEnter\r\n"
"drive.google.comEnter\r\ns"
"drive.google.comEnter\r\nse"
"drive.google.comEnter\r\nsel"
"drive.google.comEnter\r\nsele"
log "drive.google.comEnter\r\nselen"*   o
log!"drive.google.comEnter\r\nselene"
log("drive.google.comEnter\r\nselene|Shift|"Xu@<;
log)"drive.google.comEnter\r\nselene|Shift|@"
log*"drive.google.comEnter\r\nselene|Shift|@r"
log+"drive.google.comEnter\r\nselene|Shift|@ra"
log,"drive.google.comEnter\r\nselene|Shift|@ran"
log-"drive.google.comEnter\r\nselene|Shift|@rang"
log."drive.google.comEnter\r\nselene|Shift|@range"
log/"drive.google.comEnter\r\nselene|Shift|@ranger"y
log0"drive.google.comEnter\r\nselene|Shift|@rangers"(&
log1"drive.google.comEnter\r\nselene|Shift|@rangers."d
log2"drive.google.comEnter\r\nselene|Shift|@rangers.e"D
log3"drive.google.comEnter\r\nselene|Shift|@rangers.el"
log4"drive.google.comEnter\r\nselene|Shift|@rangers.eld"
log5"drive.google.comEnter\r\nselene|Shift|@rangers.eldo"
log6"drive.google.comEnter\r\nselene|Shift|@rangers.eldor"
log7"drive.google.comEnter\r\nselene|Shift|@rangers.eldori"
log8"drive.google.comEnter\r\nselene|Shift|@rangers.eldoria"N
log9"drive.google.comEnter\r\nselene|Shift|@rangers.eldoria."
log:"drive.google.comEnter\r\nselene|Shift|@rangers.eldoria.c"
log;"drive.google.comEnter\r\nselene|Shift|@rangers.eldoria.co";
log<"drive.google.comEnter\r\nselene|Shift|@rangers.eldoria.com"
logE"drive.google.comEnter\r\nselene|Shift|@rangers.eldoria.comEnter\r\n"
logF"drive.google.comEnter\r\nselene|Shift|@rangers.eldoria.comEnter\r\nc"n
logG"drive.google.comEnter\r\nselene|Shift|@rangers.eldoria.comEnter\r\ncl"
logH"drive.google.comEnter\r\nselene|Shift|@rangers.eldoria.comEnter\r\ncli"C
logI"drive.google.comEnter\r\nselene|Shift|@rangers.eldoria.comEnter\r\nclip"!
logJ"drive.google.comEnter\r\nselene|Shift|@rangers.eldoria.comEnter\r\nclip-"
logK"drive.google.comEnter\r\nselene|Shift|@rangers.eldoria.comEnter\r\nclip-m"Fe"
logL"drive.google.comEnter\r\nselene|Shift|@rangers.eldoria.comEnter\r\nclip-mu"
logM"drive.google.comEnter\r\nselene|Shift|@rangers.eldoria.comEnter\r\nclip-mum"
logN"drive.google.comEnter\r\nselene|Shift|@rangers.eldoria.comEnter\r\nclip-mumm"
logO"drive.google.comEnter\r\nselene|Shift|@rangers.eldoria.comEnter\r\nclip-mummi"=
logP"drive.google.comEnter\r\nselene|Shift|@rangers.eldoria.comEnter\r\nclip-mummif"
logQ"drive.google.comEnter\r\nselene|Shift|@rangers.eldoria.comEnter\r\nclip-mummify"`
logR"drive.google.comEnter\r\nselene|Shift|@rangers.eldoria.comEnter\r\nclip-mummify-"
logS"drive.google.comEnter\r\nselene|Shift|@rangers.eldoria.comEnter\r\nclip-mummify-p",t|ff
logT"drive.google.comEnter\r\nselene|Shift|@rangers.eldoria.comEnter\r\nclip-mummify-pr"
logU"drive.google.comEnter\r\nselene|Shift|@rangers.eldoria.comEnter\r\nclip-mummify-pro"
logV"drive.google.comEnter\r\nselene|Shift|@rangers.eldoria.comEnter\r\nclip-mummify-proo"7^
logW"drive.google.comEnter\r\nselene|Shift|@rangers.eldoria.comEnter\r\nclip-mummify-proof"
logX"drive.google.comEnter\r\nselene|Shift|@rangers.eldoria.comEnter\r\nclip-mummify-proofs"
loga"drive.google.comEnter\r\nselene|Shift|@rangers.eldoria.comEnter\r\nclip-mummify-proofsEnter\r\n"

┌──(venv)─(kali㉿kali)-[~/Desktop/volatility3]
└─$ 
```

## 6. What is the password of selene@rangers.eldoria.com
`clip-mummify-proofs`

See output from the `000003.log` file in 5.