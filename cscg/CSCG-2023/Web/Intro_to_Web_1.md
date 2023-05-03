# Intro to Web 1
You've never touched web hacking before? You want to know what actually happens when you hit Enter in your browser's address bar? You want to learn about all the things that happen in the background while you're seeing this rather boring bit of text on your screen?

## Solution
Erster Teil der Flag kann gefunden werden in einem HTML Kommentar
```
Here's the first part of the flag:
CSCG{ImgAvH8w5
```

Der Zweite Teil kann gefunden werden indem hier die Funktion _showFlag()_ aus der Konsole aufgerufen wird (Inspect -> Console -> showFlag()).
```js
function countDown() {
    countDownTime--;
    if (countDownTime > 0) {
        document.getElementById("flag-timer").innerHTML = countDownTime;
    } else {
        clearInterval(countDownIntervalId);
        document.getElementById("flag-button").innerHTML = ""+
            '<a href="." onClick="showFlag();return false;">Show flag!</a>';
    }
}

function showFlag() {
    // You don't need to understand how this part of the flag is generated.
    // All you need to know is the result of what happens here.
    const randomGenerator = mulberry32(0x5eed);
    const flag = Math.floor(randomGenerator() * 10000000000).toString(16);

    alert(`Here's the second part of your flag: ${flag}`);
}
```

Ein Popup zeigt den zweiten Teil: 
```
Here's the second part of your flag: 1a7364a71
```

Den dritten Teil der Flag erhaelt man indem man sich den Response Header anschaut. Dies kann bspw. mit ZAP erfolgen oder auch einfach nur mit der integrierten Funktion im Browser (Inspect -> Network -> F5 -> Headers). In dem Header steht dann ein entsprechendes Feld:
```
FlagPart3: VdGb98br}
```

Die zusammengesetzte Flag lautet also: CSCG{ImgAvH8w51a7364a71VdGb98br}
