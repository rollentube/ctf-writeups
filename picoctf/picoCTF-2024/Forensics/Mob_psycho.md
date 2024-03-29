# Mob psycho (200 points)
Can you handle APKs?

## Data
* mobpsycho.apk

## Solution
At first a ran a bit down the rabbit hole and analysed the APK with JADX, but I didn't found anythin useful here.

Then I unzipped the APK and searched a bit inside:
```
$ unzip -l mobpsycho.apk

[...]

$ grep -r picoCTF *
$ hexdump -C classes.dex | less
$ strings classes* | grep -i pico
$ strings classes* | grep picoCTF
$ find . | grep -i flag
./res/color/flag.txt
$
```

And my last guess brougth me the flag:
```
$ cat ./res/color/flag.txt
7069636f4354467b6178386d433052553676655f4e5838356c346178386d436c5f37343664666133397d
$
```

Decoding it from hex with CyberChef reveals it: `picoCTF{ax8mC0RU6ve_NX85l4ax8mCl_746dfa39}`
