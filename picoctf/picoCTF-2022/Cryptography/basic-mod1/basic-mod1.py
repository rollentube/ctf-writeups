numbers = [54,396,131,198,225,258,87,258,128,211,57,235,114,258,144,220,39,175,330,338,297,288]
chars = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

print("picoCTF{", end='')
for number in numbers:
    mod = number % 37

    if mod == 36:
        #print('Number:', number, '\t Mod:', mod, '\tChar:', '_')
        print('_', end='')
    else:
        #print('Number:', number, '\t Mod:', mod, '\tChar:', chars[mod])
        print(chars[mod], end='')
print('}')
