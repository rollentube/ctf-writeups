numbers = [268,413,110,190,426,419,108,229,310,379,323,373,385,236,92,96,169,321,284,185,154,137,186]
chars = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

print("picoCTF{", end='')
for number in numbers:
    mod_inv = pow(number, -1, 41)
    mod_inv -= 1

    if mod_inv == 36:
        #print('Number:', number, '\t Mod:', mod_inv, '\tChar:', '_')
        print('_', end='')
    else:
        #print('Number:', number, '\t Mod:', mod_inv, '\tChar:', chars[mod_inv])
        print(chars[mod_inv], end='')
print('}')
