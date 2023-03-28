# Specialer
Reception of Special has been cool to say the least. That's why we made an exclusive version of Special, called Secure Comprehensive Interface for Affecting Linux Empirically Rad, or just 'Specialer'. With Specialer, we really tried to remove the distractions from using a shell. Yes, we took out spell checker because of everybody's complaining. But we think you will be excited about our new, reduced feature set for keeping you focused on what needs it the most. Please start an instance to test your very own copy of Specialer. (400 Points)

## Solution
Take a look at the shell, we see that we dont have commands like 'ls', 'cat', etc., but if we double tab tab, we see our available commands. With a simple one liner shell script we can list the directory content. We see three files ('abra', 'ala', 'sim'). With echo we can print out the content. But we find out, that the files are directories with different text files in it. So inspecting those files will give us the flag from the file './ala/kazam.txt'
```
[root@picoctf ~]$ ssh -p 56759 ctf-player@saturn.picoctf.net
ctf-player@saturn.picoctf.net's password:
[...]
Specialer$
!          [[         bg         caller     compgen    coproc     do         else       exec       fc         function   history    kill       mapfile    pwd        return     shopt      then       true       umask      wait
./         ]]         bind       case       complete   declare    done       enable     exit       fg         getopts    if         let        popd       read       select     source     time       type       unalias    while
:          alias      break      cd         compopt    dirs       echo       esac       export     fi         hash       in         local      printf     readarray  set        suspend    times      typeset    unset      {
[          bash       builtin    command    continue   disown     elif       eval       false      for        help       jobs       logout     pushd      readonly   shift      test       trap       ulimit     until      }
Specialer$
Specialer$ for entry in ./*;do echo $entry;done
./abra
./ala
./sim
Specialer$ 
Specialer$ for entry in ./.*;do echo $entry;done
./.
./..
./.bash_history
./.hushlogin
./.profile
Specialer$ echo "$(<.hushlogin )"
Specialer$ echo "$(<./.hushlogin )"

Specialer$ echo "$(<./abra )"

Specialer$ echo "$(<./ala )"

Specialer$ echo "$(<./sim )"

Specialer$ 
Specialer$ ./abra
-bash: ./abra: Is a directory
Specialer$ ./ala
-bash: ./ala: Is a directory
Specialer$ ./sim
-bash: ./sim: Is a directory
Specialer$ for entry in ./abra/*;do echo $entry;done
./abra/cadabra.txt
./abra/cadaniel.txt
Specialer$ for entry in ./ala/*;do echo $entry;done
./ala/kazam.txt
./ala/mode.txt
Specialer$ for entry in ./sim/*;do echo $entry;done
./sim/city.txt
./sim/salabim.txt
Specialer$
Specialer$ echo "$(<./abra/cadabra.txt)"
Nothing up my sleeve!
Specialer$ echo "$(<./abra/cadaniel.txt)"
Yes, I did it! I really did it! I'm a true wizard!
Specialer$ echo "$(<./ala/kazam.txt)"
return 0 picoCTF{y0u_d0n7_4ppr3c1473_wh47_w3r3_d01ng_h3r3_c806dd0d}
Specialer$ echo "$(<./ala/mode.txt)"
Yummy! Ice cream!
Specialer$ echo "$(<./sim/city.txt)"
05ed181c-4aa0-4d4a-8505-2fe6ca9097d3
Specialer$ echo "$(<./sim/salabim.txt)"
#He was so kind, such a gentleman tied to the oceanside#
Specialer$ Connection to saturn.picoctf.net closed by remote host.
Connection to saturn.picoctf.net closed.
[root@picoctf ~]$
```

The flag is picoCTF{y0u\_d0n7\_4ppr3c1473\_wh47\_w3r3\_d01ng\_h3r3\_c806dd0d}
