# Ready Gladiator 2
Can you make a CoreWars warrior that wins every single round? (400 Points)
Your opponent is the Imp. The source is available here. If you wanted to pit the Imp against himself, you could download the Imp and connect to the CoreWars server like this:
nc saturn.picoctf.net 63915 < imp.red
To get the flag, you must beat the Imp all 100 rounds.

## Data
imp.red

## Again we have the classic Imp as enemy. But now we have to win all rounds. I just researched a bit and found the D-Clear Warrior (https://corewar.co.uk/clearimp.htm) and tested him out. In the first run he won 99 of the rounds. So i gave him a few tries in hope he can also get the 100. And he did:
```
[root@picoctf Ready_Gladiator_0]$ nc saturn.picoctf.net 63915
Submit your warrior: (enter 'end' when done)

;assert 1
        org    start

gate    dat    4000,       1700
bomb    dat    >2667,      11

        for    4
        dat    0,0
        rof

        spl    #4000,      >gate
clear   mov    bomb,       >gate
        djn.f  clear,      >gate

        for    23
        dat    0,0
        rof

        istep  equ 1143           ; (CORESIZE+1)/7

start   spl    clear-1
        mov    imp,        *launch
        spl    1                  ; 32 parallel processes
        spl    1
        spl    1
        spl    1
        spl    1
        spl    nxpoint
launch  djn.f  3600,       <4000

        for    2
        dat    0,0
        rof

nxpoint add.f  #istep,     launch
        djn.f  clear-1,    <3000

imp     mov.i  #1,         istep
end
;assert 1
        org    start

gate    dat    4000,       1700
bomb    dat    >2667,      11

        for    4

        for    4
        dat    0,0
        rof

        spl    #4000,      >gate
clear   mov    bomb,       >gate
        djn.f  clear,      >gate

        for    23
        dat    0,0
        rof

        istep  equ 1143           ; (CORESIZE+1)/7

start   spl    clear-1
        mov    imp,        *launch
        spl    1                  ; 32 parallel processes
        spl    1
        spl    1
        spl    1
        spl    1
        spl    nxpoint
launch  djn.f  3600,       <4000

        for    2
        dat    0,0
        rof

nxpoint add.f  #istep,     launch
        djn.f  clear-1,    <3000

imp     mov.i  #1,         istep
end
Warrior1:
;assert 1
        org    start

gate    dat    4000,       1700
bomb    dat    >2667,      11

        for    4
        dat    0,0
        rof

        spl    #4000,      >gate
clear   mov    bomb,       >gate
        djn.f  clear,      >gate

        for    23
        dat    0,0
        rof

        istep  equ 1143           ; (CORESIZE+1)/7

start   spl    clear-1
        mov    imp,        *launch
        spl    1                  ; 32 parallel processes
        spl    1
        spl    1
        spl    1
        spl    1
        spl    nxpoint
launch  djn.f  3600,       <4000

        for    2
        dat    0,0
        rof

nxpoint add.f  #istep,     launch
        djn.f  clear-1,    <3000

imp     mov.i  #1,         istep
end

Rounds: 100
Warrior 1 wins: 100
Warrior 2 wins: 0
Ties: 0
You did it!
picoCTF{d3m0n_3xpung3r_9a074a57}
[root@picoctf Ready_Gladiator_0]$
```

Since i dont want to go deeper in the Core War meterial, i wont analyse the warrior any furhter. Im fine to understand the basics at this point. Also if this is kinda script kiddy thinking.
