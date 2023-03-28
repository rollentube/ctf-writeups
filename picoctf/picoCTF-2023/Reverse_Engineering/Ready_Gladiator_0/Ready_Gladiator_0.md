# Ready Gladiator 0
Can you make a CoreWars warrior that always loses, no ties? (100 Points)
Your opponent is the Imp. The source is available here. If you wanted to pit the Imp against himself, you could download the Imp and connect to the CoreWars server like this:
nc saturn.picoctf.net 55843 < imp.red

## Data
imp.red

## Solution
The description says, that our enemy is the 'Imp' and that we have to loose against him. The Imp is the simplest Warrior in the game and is programmed like this
```asm
;redcode
;name Imp Ex
;assert 1
mov 0, 1
end
```

The important part is the `mov 0, 1`. The adress '0' is the current instruction. '1' is the next instruction. So this is copying the mov instruction itself into the next instruction. Causing that this instruction will crawling forward through the whole memory.

To get the flag, we have to loose against the Imp. So if we just do nothing, we will loose:
```
[root@picoctf Ready_Gladiator_0]$ nc saturn.picoctf.net 49446
Submit your warrior: (enter 'end' when done)

;assert 1
;assert 1
end
end
Warrior1:
;assert 1
end

Warning:
        No instructions
Number of warnings: 1

Rounds: 100
Warrior 1 wins: 0
Warrior 2 wins: 100
Ties: 0
You did it!
picoCTF{h3r0_t0_z3r0_4m1r1gh7_e1610ed2}
[root@picoctf Ready_Gladiator_0]$
```

## Further reading
There are many tutorials. Some that helped me were:
- https://corewar.co.uk/guides.htm
- https://corewar.co.uk/zapf/Handbuch.pdf
- https://vyznev.net/corewar/guide.html
- https://corewar.co.uk/strategy.htm

