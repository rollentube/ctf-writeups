# file-run1
A program has been provided to you, what happens if you try to run it on the command line?

## Loesung
Die Datei kann ausfuehrbar gemacht werden und ausgefuehrt werden. Sie gibt anschliessen die Flag aus:
```
 root  …  writeups  picoCTF-2022  file-run1  ./run
The flag is: picoCTF{U51N6_Y0Ur_F1r57_F113_9bc52b6b} root  …  writeups  picoCTF-2022  file-run1  
 root  …  writeups  picoCTF-2022  file-run1  
```

# file-run2
Another program, but this time, it seems to want some input. What happens if you try to run it on the command line with input "Hello!"?

## Loesung 
Die Datei braucht einen bestimmten String beim Aufruf und gibt dann die Flag aus:
```
 root  …  writeups  picoCTF-2022  file-run  ./run2
Run this file with only one argument.
 root  …  writeups  picoCTF-2022  file-run  ./run2 hallo
Won't you say 'Hello!' to me first?
 root  …  writeups  picoCTF-2022  file-run  ./run2 Hello!
The flag is: picoCTF{F1r57_4rgum3n7_be0714da} root  …  writeups  picoCTF-2022  file-run  
 root  …  writeups  picoCTF-2022  file-run  
```
