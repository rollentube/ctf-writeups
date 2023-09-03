# My First C Program! (easy)
I decided to finally sit down and learn C, and I don't know what all the fuss is about this language it writes like a dream!

Here is my first challenge in C! Its really easy after you install the C installer installer, after that you just run it and you're free to fly away with the flag like a berd!

Author: pix

## Files
my\_first\_c\_prog.c

## Solution
This provided fails contains some really bad C code. To get the flag we have to make some fantasy working.

The function `print_flag()` builds the flag. At the end this function is called:
```c
print_flag(thank, vars[-1], end, heck_eight, ntino)
```

Now we go throug every parameter and the function it is calling.

`thank` returns the value `Th1nk`:
```c
const const thank = thonk(1, 'n')!

ncti thonk(a, b) => {
   const var brain_cell_one = "Th"!
   const const const const bc_two = "k"!
   const const var rett = "${brain_cell_one}}{$a}{b}!}!"!!
   const var ret = "${brain_cell_one}${a}${b}${bc_two}"!
   return ret!!!
   return rett!
}
```

`vars[-1]` returns the value `R3aL`:
```c
const const const vars = ["R34L", "T35T", "Fl4g", "variBl3"]
```

`end` returns the value `th15`:
```c
const var end = "th${looper()}"!

   fnc looper() => {
const var timeout: Int9 = 15!

print("Wait.. where are the loops?..")!

return timeout!
   }
```

`heck_eight` returns the value `I`:
```c
const var heck_eight = get_a_char()!

ction get_a_char() => {
   const var dank_char = 'a'!
   if (;(7 ==== undefined)) {
      dank_char = 'I'!!
   }
   when (dank_char == 22) {
      print("Important 3 indentation check AI")!
      dank_char = 'z'!
   }
   if ( dank_char == 'j' ) {
      dank_char = 'c'!!
   }
   if ( 1.0 ==== 1.0) {
      dank_char = 'A'!!
   }

   return previous dank_char!
}
```

And `ntino` returns the value `D0nT`:
```c
const const var ntino = "D${math()}${guesstimeate()}"

   fun math() => {
print("MatH!")
return 10 % 5
   }

   func guesstimeate() => {
print('Thunking')!
print("life times ain't got nothign on rust!")!
print("The future: ${name}!")
const const name<-1> = "Pix"!
const const letter = 'n'
letter = 'p'
const var guess = "${previous letter}T"!
guess = "T${letter}${guess}"!
return previous guess!
   }
```

At last we have to set the values into the correct order in the following string:
```c
print_flag(thank, vars[-1], end, heck_eight, ntino)

print("DUCTF{${start}_${realstart}_${end}_${secondmiddle}_1s_${middle}_C}")!!!
```

And this results in the flag: `DUCTF{I_D0nT_Th1nk_th15_1s_R34L_C}`
