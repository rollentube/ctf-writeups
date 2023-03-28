# Ready Gladiator 1
Can you make a CoreWars warrior that wins? (200 Points)
Your opponent is the Imp. The source is available here. If you wanted to pit the Imp against himself, you could download the Imp and connect to the CoreWars server like this:
nc saturn.picoctf.net 56057 < imp.red
To get the flag, you must beat the Imp at least once out of the many rounds.

## Data
imp.red

## Solution
Our enemy is again the Imp
```asm
;redcode
;name Imp Ex
;assert 1
mov 0, 1
end
```

But now we have to beat him at least in one round.

The Dwarf drops at every 4th place a bomb. If the Imp reaches such a bomb, his process will be terminated. So with some luck the Dwarf reaches a place before the Imp and can beat him. Otherwise the Dwarf will be overwritten by the Imp and become an Imp aswell. So the round draw out.

So lets use the following Dwarf:
```asm
;asstert 1
add #4, 3
mov 2, @2
jmp -2
dat #0, #0
```

In the match we can see, that the dwarf wins 25 round and the rest is tied up. Enough for this challenge:
```
[root@picoctf Ready_Gladiator_0]$ nc saturn.picoctf.net 56057
Submit your warrior: (enter 'end' when done)

;assert 1
;assert 1
add #4, 3
add #4, 3
mov 2, @2
mov 2, @2
jmp -2
jmp -2
dat #0, #0
dat #0, #0
end
end
Warrior1:
;assert 1
add #4, 3
mov 2, @2
jmp -2
dat #0, #0
end

Rounds: 100
Warrior 1 wins: 25
Warrior 2 wins: 0
Ties: 75
You did it!
picoCTF{1mp_1n_7h3_cr055h41r5_441be1fc}
[root@picoctf Ready_Gladiator_0]$
```
