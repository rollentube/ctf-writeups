# Bad Policies
Looks like the attacker managed to access the rebels Domain Controller.

Can you figure out how they got access after pulling these artifacts from one of our Outpost machines?

## Data
* badpolicies.zip

## Solution
We were given some group policies. I looked into those with the Policy Analyzer, but didn't find anything interesting.

Afterwards I decided to check all the files manually:
```
┌──(kali㉿kali)-[~/Desktop/ductf/badpolicies/rebels.ductf]
└─$ find . -type f
./Policies/{31B2F340-016D-11D2-945F-00C04FB984F9}/GPT.INI
./Policies/{31B2F340-016D-11D2-945F-00C04FB984F9}/MACHINE/Registry.pol
./Policies/{31B2F340-016D-11D2-945F-00C04FB984F9}/MACHINE/comment.cmtx
./Policies/{31B2F340-016D-11D2-945F-00C04FB984F9}/MACHINE/Microsoft/Windows NT/SecEdit/GptTmpl.inf
./Policies/{6AC1786C-016F-11D2-945F-00C04fB984F9}/GPT.INI
./Policies/{6AC1786C-016F-11D2-945F-00C04fB984F9}/MACHINE/Microsoft/Windows NT/SecEdit/GptTmpl.inf
./Policies/{B6EF39A3-E84F-4C1D-A032-00F042BE99B5}/Machine/Preferences/Groups/Groups.xml
./Policies/{B6EF39A3-E84F-4C1D-A032-00F042BE99B5}/GPT.INI
./Policies/{EFF21FC3-F476-4AE0-9DDC-07BE32C98CE4}/Machine/Microsoft/Windows NT/SecEdit/GptTmpl.inf
./Policies/{EFF21FC3-F476-4AE0-9DDC-07BE32C98CE4}/GPT.INI
./Policies/{3EF191ED-9090-44C9-B436-C2766F6F0156}/Machine/Registry.pol
./Policies/{3EF191ED-9090-44C9-B436-C2766F6F0156}/Machine/comment.cmtx
./Policies/{3EF191ED-9090-44C9-B436-C2766F6F0156}/GPT.INI

┌──(kali㉿kali)-[~/Desktop/ductf/badpolicies/rebels.ductf]
└─$ 
```

The interesting file here, is `./Policies/{B6EF39A3-E84F-4C1D-A032-00F042BE99B5}/Machine/Preferences/Groups/Groups.xml`:
```xml
<?xml version="1.0" encoding="utf-8"?>
<Groups clsid="{3125E937-EB16-4b4c-9934-544FC6D24D26}"><User clsid="{DF5F1855-51E5-4d24-8B1A-D9BDE98BA1D1}" name="Backup" image="2" changed="2024-06-12 14:26:50" uid="{CE475804-94EA-4C12-8B2E-2B3FFF1A05C4}"><Properties action="U" newName="" fullName="" description="" cpassword="B+iL/dnbBHSlVf66R8HOuAiGHAtFOVLZwXu0FYf+jQ6553UUgGNwSZucgdz98klzBuFqKtTpO1bRZIsrF8b4Hu5n6KccA7SBWlbLBWnLXAkPquHFwdC70HXBcRlz38q2" changeLogon="0" noChange="1" neverExpires="1" acctDisabled="0" userName="Backup"/></User>
</Groups>
```

We got a password for the Backup user. With the tool `gpp-decrypt`, we can try to decrypt it:
```
┌──(kali㉿kali)-[~/Desktop/ductf/badpolicies/rebels.ductf]
└─$ gpp-decrypt B+iL/dnbBHSlVf66R8HOuAiGHAtFOVLZwXu0FYf+jQ6553UUgGNwSZucgdz98klzBuFqKtTpO1bRZIsrF8b4Hu5n6KccA7SBWlbLBWnLXAkPquHFwdC70HXBcRlz38q2
DUCTF{D0n7_Us3_P4s5w0rds_1n_Gr0up_P0l1cy}

┌──(kali㉿kali)-[~/Desktop/ductf/badpolicies/rebels.ductf]
└─$ 
```

And we were successful. The flag is `DUCTF{D0n7_Us3_P4s5w0rds_1n_Gr0up_P0l1cy}`.