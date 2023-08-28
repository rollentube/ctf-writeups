# Exatlon
Can you find the password?

## Solution
### Packer
```
$ file exatlon_v1
exatlon_v1: ELF 64-bit LSB executable, x86-64, version 1 (GNU/Linux), statically linked, no section header
$
```

Taking a look with strings we can only see some kind of random data:
```
UPX!<
!E&8
C}Rn
_[a/J(kb<
uY-|o
m0xI
WB}?,E?
Y"eI
MBBL
E_)q
<$I9
X@H9

[...]
```
But the first line gives a hind, that the file is packed with UPX. Binary packers alter the original binary data, and restore it (more or less) before execution. This is for example used to obfuscate or compress a binary.

From the [UPX Homepage](https://upx.github.io/): _"UPX is an advanced executable file compressor. UPX will typically reduce the file size of programs and DLLs by around 50%-70%, thus reducing disk space, network load times, download times and other distribution and storage costs."_

We can also verify this as follows:
```
$ strings exatlon_v1 | grep UPX
UPX!<
$Info: This file is packed with the UPX executable packer http://upx.sf.net $
$Id: UPX 3.95 Copyright (C) 1996-2018 the UPX Team. All Rights Reserved. $
UPX!u
UPX!
UPX!
```

_(Keep in mind: Packing and obfuscation is a common technique to prevent malware from analysis. So the UPX strings can also be dropped in the file to fool the analyst. But in this CTF it is rather unlikely.)_

Other packers and there identification strings are for example:
* UPX - UPX0, UPX1, UPX2
* Aspack - aspack, adata
* NSPack - NSP0, NSP1, NSP2
* NTKrnl - NTKrnl Security Suite
* PECompact - PEC2, PECompact2
* Themida - Themida, aPa2Wa

Tools like [Detect It Easy](https://github.com/horsicq/Detect-It-Easy) can automatically detect the packer:
```
$ diec -rd exatlon_v1
ELF64
    Operation system: Unix(-)[EXEC AMD64-64]
    Packer: UPX(3.95)[NRV,brute]

$
```

Further information can be found [here](https://intezer.com/blog/malware-analysis/elf-malware-analysis-101-initial-analysis/)

### Decompress
```
$ upx -l exatlon_v1
                       Ultimate Packer for eXecutables
                          Copyright (C) 1996 - 2020
UPX 3.96        Markus Oberhumer, Laszlo Molnar & John Reiser   Jan 23rd 2020

        File size         Ratio      Format      Name
   --------------------   ------   -----------   -----------
   2202568 ->    709524   32.21%   linux/amd64   exatlon_v1
$ upx -d -o exatlon_uncomp exatlon_v1
                       Ultimate Packer for eXecutables
                          Copyright (C) 1996 - 2020
UPX 3.96        Markus Oberhumer, Laszlo Molnar & John Reiser   Jan 23rd 2020

        File size         Ratio      Format      Name
   --------------------   ------   -----------   -----------
   2202568 <-    709524   32.21%   linux/amd64   exatlon_uncomp

Unpacked 1 file.
$ file exatlon_uncomp
exatlon_uncomp: ELF 64-bit LSB executable, x86-64, version 1 (GNU/Linux), statically linked, BuildID[sha1]=99364060f1420e00a780745abcfa419af0
b8b0d8, for GNU/Linux 3.2.0, not stripped
$
```

### Reversing
If we reverse the decompressed file, we find now the main function, which generates the console output and take the user input. Also it sends our input into the function _exatlon_. This function seems to manipulate the input.

After the call, the program compares the changed input with the string _"1152 1344 1056 1968 1728 816 1648 784 1584 8 16 1728 1520 1840 1664 784 1632 1856 1520 172 8 816 1632 1856 1520 784 1760 1840 1824 816 1 584 1856 784 1776 1760 528 528 2000"_. This seems to be the password.
```c
{
    int64_t var_10 = arg1;
    int32_t rbx_2;
    do
    {
        std::operator<<<std::char_traits<char> >(&std::cout, &data_54b00f);
        std::operator<<<std::char_traits<char> >(&std::cout, &data_54b018);
        std::operator<<<std::char_traits<char> >(&std::cout, &data_54b0d8);
        sleep(1);
        std::operator<<<std::char_traits<char> >(&std::cout, &data_54b1a8);
        std::operator<<<std::char_traits<char> >(&std::cout, &data_54b260);
        sleep(1);
        std::operator<<<std::char_traits<char> >(&std::cout, &data_54b320);
        sleep(1);
        std::operator<<<std::char_traits<char> >(&std::cout, &data_54b400);
        sleep(1);
        void var_58;
        std::string::string(&var_58);
        std::operator<<<std::char_traits<char> >(&std::cout, "[+] Enter Exatlon Password  : ");
        std::operator>><char, st..._traits<char>, std::allocator<char> >(&std::cin, &var_58);
        void input;
        exatlon(&input, &var_58);
        char rax_1 = std::operator==<char, st..._traits<char>, std::allocator<char> >(&input, "1152 1344 1056 1968 1728 816 164…");
        std::string::~string(&input);
        if (rax_1 != 0)
        {
            int64_t* rax_2 = std::operator<<<std::char_traits<char> >(&std::cout, "[+] Looks Good ^_^ \n\n\n");
            std::ostream::operator<<(rax_2, 0x467e20, rax_2);
            arg1 = 0;
            rbx_2 = 0;
        }
        else if (std::operator==<char, st..._traits<char>, std::allocator<char> >(&var_58, &data_54b5b2) == 0)
        {
            int64_t* rax_4 = std::operator<<<std::char_traits<char> >(&std::cout, "[-] ;(\n");
            std::ostream::operator<<(rax_4, 0x467e20, rax_4);
            rbx_2 = 1;
        }
        else
        {
            arg1 = 0;
            rbx_2 = 0;
        }
        std::string::~string(&var_58);
    } while (rbx_2 == 1);
    return ((uint64_t)arg1);
}
```

If we take a look at the exatlon function, we find that the program does a left shift to the characters we gave as input:
```c
{
    std::string::string(arg1, &data_54b00c);
    int64_t var_78 = std::string::begin(arg2);
    int64_t var_80 = std::string::end(arg2);
    while (true)
    {
        if (operator!=<char const*, std::string>(&var_78, &var_80) == 0)
        {
            break;
        }
         void var_48;
        std::to_string(&var_48, (((int32_t)*(int8_t*)__normal_iterator<char const*, std::string>::operator*(&var_78)) << 4));
        void var_68;
        std::operator+<char, std..._traits<char>, std::allocator<char> >(&var_68, &var_48, &data_54b00d);
        std::string::operator+=(arg1, &var_68);
        std::string::~string(&var_68);
        std::string::~string(&var_48);
        __normal_iterator<char const*, std::string>::operator++(&var_78);
    }
    return arg1;
}
```

### Decrypt
So to get the flag we can just right shift the "decrypted" password and convert the numbers back to the corresponding ASCII letters. For that we can write a python script:
```python
enc = "1152 1344 1056 1968 1728 816 1648 784 1584 816 1728 1520 1840 1664 784 1632 1856 1520 1728 816 1632 1856 1520 784 1760 1840 1824 816 1584 1856 784 1776 1760 528 528 2000".split()

dec = ""
for i in enc:
    dec += chr(int(i) >> 4)
print(dec)
```

If we run the scirpt, we find the password and with that the flag.
```
$ python3 dec.py
HTB{l3g1c3l_sh1ft_l3ft_1nsr3ct1on!!}
$ ./exatlon_v1

███████╗██╗  ██╗ █████╗ ████████╗██╗      ██████╗ ███╗   ██╗       ██╗   ██╗ ██╗
██╔════╝╚██╗██╔╝██╔══██╗╚══██╔══╝██║     ██╔═══██╗████╗  ██║       ██║   ██║███║
█████╗   ╚███╔╝ ███████║   ██║   ██║     ██║   ██║██╔██╗ ██║       ██║   ██║╚██║
██╔══╝   ██╔██╗ ██╔══██║   ██║   ██║     ██║   ██║██║╚██╗██║       ╚██╗ ██╔╝ ██║
███████╗██╔╝ ██╗██║  ██║   ██║   ███████╗╚██████╔╝██║ ╚████║███████╗╚████╔╝  ██║
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝ ╚═══╝   ╚═╝


[+] Enter Exatlon Password  : HTB{l3g1c3l_sh1ft_l3ft_1nsr3ct1on!!}
[+] Looks Good ^_^



$
```
