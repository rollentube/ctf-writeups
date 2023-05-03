# Intro to Web 2
Now that you have a rough grasp on the things you can do with just your browser, let's take a closer look at how to utilize HTTP request manipulation with ZAP.

## Solution
Flag: CSCG{l9jj550KUaT0BVvkQ9Z39J9AW4at6R2B}

### Part 1
Die Seite vergleicht das User-Agent Feld in dem GET Request. Hierbei erwartet der Server scheinbar einen User-Agent von dem Betriebssystem Windows 95. Unter https://user-agents.net/platforms/win95/user-agents findet man hierfuer valide Agents.

Manipuliert man den Agent entsprechend (Resend, siehe Part 2 oder Break, sehe Part 4) wird man zu der gesuchten Seite weitergeleitet. Der erste Teil der Flag lautet:  **Flag part 1/4: CSCG{l9jj550K**

Die Flag wird durch ein Skript erst nach einiger Zeit generiert. Betrachtet man allerdings den Code der Seite, findet man die Flag direkt.

### Part 2
Verfolgt man den Aufruf mit ZAP, sieht man einen POST Request.

Open/Resend with Request Editor -> In der Payload die Variable filename auf 'flag.txt' anpassen

Im Response erhaelt man den zweiten Teil der Flag: **Flag part 2/4: UaT0BVvk**

### Part 3
In der URL kann der Filename einfach angepasst werden: https://90fef2d58c4d6ab86adfa2c3-intro-web-2.challenge.master.cscg.live:31337/read-file.php?filename=flag.txt

Alternativ kann die URL auch in dem GET Request angepasst werden.

Als Response erhaelt man den dritten Teil der Flag: **Flag part 3/4: Q9Z39J9A**

### Part 4
Fuer diesen Teil muss in ZAP die Break Funktion aktiviert werden (gruener Punkt). Hierdurch wird die HTTP Verbindung immer unterbrochen wenn der Browser ein Request oder der Server ein Response sendet.

Der Client fragt eine Datei namens 'enter-security-gate.php' an. Diese sendet einen redirect zurueck auf 'burn-after-reading-xxxxxx.php' und loescht die Flag. Auch zusehen ist, dass bei dem Redirect '?authorized=false' in der URL steht.

Unterbricht man den austausch nun und geht schrittweise bis zu dem Redirect vor, kann man diesen manipulieren und '?authorized=true' einsetzen. Anschliessend erhaelt man dann die Flag: **Flag part 4/4: W4at6R2B}**
