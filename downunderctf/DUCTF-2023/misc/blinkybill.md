# blinkybill (beginner)
Hey hey it's Blinky Bill!

NOTE: Flag is case-insensitive and requires placing inside DUCTF{} wrapper!

Author: Yo\_Yo\_Bro

## Files 
blinkybill.wav

## Solution
Listening to the audio file, we can hear blinky bill with something in the background that is listening like morse code. Opening the file in Audacity, changing to spectogram and playing around with the rate and the colors give us this picture:
[Blinkybill](images/blinkybill.png)

We can see pretty clearly a morse code with long and short signals.

Throwing the code into a converter like https://morsecode.world/international/translator.html gets us the string `SRINGBACKTHETREES`. But the first word doesn't seem to be correct. So we did some trial and error to find out that the correct string is `BRINGBACKTHETREES`. There is missing one long signal at the beginning in the audio file. Not sure why.

Bute the correct morse code is: `-... .-. .. -. --. -... .- -.-. -.- - .... . - .-. . . ...`

And the flag is: `DUCTF{BRINGBACKTHETREES}`
