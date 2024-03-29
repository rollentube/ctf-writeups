# Intro to Forensics 2
We were able to capture a hidden service. Could you recover the secret order?

Fuer Analysen mit Tshark ist die Doku sehr hilfreich: https://tshark.dev/

## Solution
In dem pcap Verlauf sind mehrere http Anfragen an YouTube Videos zu erkennen. Diese koennen mit tshark uebersichtlich extrahiert werden:
```
$ tshark -r intro-forensics-2.pcapng -Y 'http.request.method == GET' -T fields -e http.request.full_uri
http://www.youtube.com/watch?v=lDHMHyA5qqI
http://www.youtube.com/watch?v=97DySuuHhOw
http://www.youtube.com/watch?v=DujEvJIW_9I
http://www.youtube.com/watch?v=hTpqWkFw7bg
http://www.youtube.com/watch?v=vCxJAKntgAw
http://www.youtube.com/watch?v=G7GERh0sQzY
http://www.youtube.com/watch?v=bx3L1mzbxHU
http://www.youtube.com/watch?v=Q2hLFoFcVi8
http://www.youtube.com/watch?v=MnrWkcL85hw
http://www.youtube.com/watch?v=NJmH7vhy-1c
http://www.youtube.com/watch?v=b38_IhIJils
http://www.youtube.com/watch?v=f8OHybVhQwc
[...]
http://www.youtube.com/watch?v=cWlAduQ9v2A
$ 
```

Das erste Video hat den Titel '60 seconds' und alle anderen 'Knock Knock' oder einen aequivalenten Namen.

Hieraus laesst sich schliessen, dass es sich um Port Knocking handelt. Hierbei wird an bestimmten Ports geklopft ein gewuenschtes Verhalten auszuloesen. Die 60 Sekunden deuten darauf, dass man Pakete erst ab 60 Sekunden betrachten soll.

Da das Port Knocking vermutlich nicht bei Youtube als Ziel angewendet werden soll, sollte klar sein. Man betrachtet also nur die Pakete die nicht Youtube als Ziel haben. Beispielsweise mit folgendem filter:
```
tshark -r intro-forensics-2.pcapng -Y ip.addr!=142.250.186.46 -x
```

Schaut man sich hier ein wenig die Daten an, findet man am Ende ein Paket mit '..Welcome home!.cscg@cscg-server'. An dieser Stelle war das Port Knocking also abgeschlossen.

Geht man die Pakete so durch erkennt man in den Destination Ports schon Teile der Flag im ASCII Code. Allerdings findet man auch Pakete mit den ASCII Daten '|<|\|0<|<|<|\|0<|<'. Dies soll eine ASCII Darstellung von 'Klopfen' sein.

Man kann also nun nach diesen Paketen Filtern und dann die Ports betrachten:
```
$ tshark -r intro-forensics-2.pcapng -Y 'ip.addr!=142.250.186.46 && data==f0:9f:9a:aa:7c:3c:7c:5c:7c:30:3c:7c:3c:7c:3c:7c:5c:7c:30:3c:7c:3c:f0:9f:9a:aa:0a' -T fields -e tcp.dstport
17235
17223
31595
28208
25451
24427
28208
25451
24427
28208
25451
12654
26463
12398
24424
13108
30259
28213
24432
12402
29749
8573
$
```
Hexwerte muessen im Filter bspw. durch ':' getrennt werden. Der Hexwert kann bswp. aus Wireshark kopiert werden.

Alternativ
```
tshark -r intro-forensics-2.pcapng -Y 'ip.addr!=142.250.186.46 && data==f0:9f:9a:aa:7c:3c:7c:5c:7c:30:3c:7c:3c:7c:3c:7c:5c:7c:30:3c:7c:3c:f0:9f:9a:aa:0a' -o 'gui.column.format:"Dest port", "%D"'
```
Parameter fuer das Column Format koennen mit `tshark -G column-formats` gefunden werden.

Um diese Ports in ASCII Character zu konverieren kann ein Python Skript verwendet werden (Dec -> Hex -> Bytewise ASCII):
```python
ports = [17235,
17223,
31595,
28208,
25451,
24427,
28208,
25451,
24427,
28208,
25451,
12654,
26463,
12398,
24424,
13108,
30259,
28213,
24432,
12402,
29749,
8573]

for port in ports:
    char1 = hex(port)[2:4]
    char2 = hex(port)[4:6]
    print(bytes.fromhex(char1).decode("ascii"), end='')
    print(bytes.fromhex(char2).decode("ascii"), end='')
print()
```

```
$ cat port_to_ascii.py 
ports = [17235, ..., 8573]

for port in ports:
    char1 = hex(port)[2:4]
    char2 = hex(port)[4:6]
    print(bytes.fromhex(char1).decode("ascii"), end='')
    print(bytes.fromhex(char2).decode("ascii"), end='')
print()
$ 
```

Fuhrt man das Skript aus erhaelt man die Flag:
```
$ python port_to_ascii.py 
CSCG{kn0ck_kn0ck_kn0ck1ng_0n_h34v3n5_p0rt5!}
$
```
