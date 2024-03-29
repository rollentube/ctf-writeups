# Intro to Forensics 1
First we will learn a little bit about Wireshark. For the beginning just start play around with Wireshark and their filters, look into the protocols and getting familar with the tool. Besides Reverse Engineering skills, recording the network traffic is an important part in the analysis of malware.

## Solution
Betrachtet man den Traffic sieht man HTTP Traffic. Betrachtet man diesen ein wenig kann man sehen, dass es sich um eine Authentifizierung auf einer Webseite geht.

Filter man nach 'http' sieht man vor jeder POST Anfrage den html Code:
```html
Please provide a valid token: <form action='/login' method=POST><input name=token></input><button type='submit' value='send'>send</button></form>
```

Der Token ist also in den POST Anfragen zu finden. Mit 'http.request.method == POST' Filtert man nach diesen. Man sieht in diesen Paketen eine Cookie Struktur mit dem Feld 'token'. Es gibt drei POST Anfragen in welchen man jeweils die folgenden drei Token findet:
```
http.cookie_pair: token=Test
http.cookie_pair: token=NobodyCanSeeMySecretToken!!!
http.cookie_pair: token=8967e85a7301be8958b3ccafe1faad4d6dbea2154fbb2fdbcb5221c9cd6c607c877c67d36bd67c0e362a968a0d3522feed7e0d68a70796aa4682735608d7686b
```

Der letzte ist hierbei der gesuchte Token. Dies kann man entweder durch ausprobieren herausfinden oder indem man den Response betrachtet. Fuer die ersten beiden Token wird keine Antwort mit einer Flag zurueckgegeben. Fuer den letzten Token ist in dem Mitschnitt allerdings kein Response mitgeliefert.

Die Standardantwort ist
```
Thx for your request! Please go <a href='/'>home</a> now!
```
anschliessend wird man entweder zum Login Text geleitet oder zur Flag.

Gibt man den richtigen Token ein, erhaelt man die Flag:
```
Welcome to the CSCG Flag Service serving some flags: CSCG{w1235h42k_15_1n_th3_m1ddl3!}
```

## Tshark
Alternativ kann auch thsark zur Loesung verwendet werden um den Token zu finden:
```
$ tshark -r intro-forensics-1.pcapng -Y http
    6 0.808494508   172.17.0.1 → 172.17.0.2   HTTP 1678   GET /login HTTP/1.1 
   10 0.812648752   172.17.0.2 → 172.17.0.1   HTTP 211   HTTP/1.1 200 OK  (text/html)
   18 9.998801771   172.17.0.1 → 172.17.0.2   HTTP 1824   POST /login HTTP/1.1  (application/x-www-form-urlencoded)
   22 10.001065341   172.17.0.2 → 172.17.0.1   HTTP 123   HTTP/1.1 200 OK  (text/html)
   30 13.631885303   172.17.0.1 → 172.17.0.2   HTTP 1702   GET / HTTP/1.1 
   34 13.634325184   172.17.0.2 → 172.17.0.1   HTTP 112   HTTP/1.1 200 OK  (text/html)
   42 18.291162845   172.17.0.1 → 172.17.0.2   HTTP 1702   GET /login HTTP/1.1 
   46 18.293220497   172.17.0.2 → 172.17.0.1   HTTP 211   HTTP/1.1 200 OK  (text/html)
   54 25.782610775   172.17.0.1 → 172.17.0.2   HTTP 1943   POST /login HTTP/1.1  (application/x-www-form-urlencoded)
   58 25.784908779   172.17.0.2 → 172.17.0.1   HTTP 123   HTTP/1.1 200 OK  (text/html)
   66 27.361858760   172.17.0.1 → 172.17.0.2   HTTP 1802   GET /login HTTP/1.1 
   70 27.363634111   172.17.0.2 → 172.17.0.1   HTTP 211   HTTP/1.1 200 OK  (text/html)
   78 42.948569588   172.17.0.1 → 172.17.0.2   HTTP 1935   POST /login HTTP/1.1  (application/x-www-form-urlencoded)
   82 42.950862513   172.17.0.2 → 172.17.0.1   HTTP 123   HTTP/1.1 200 OK  (text/html)
$ tshark -r intro-forensics-1.pcapng -Y 'http.request.method == POST'
   18 9.998801771   172.17.0.1 → 172.17.0.2   HTTP 1824   POST /login HTTP/1.1  (application/x-www-form-urlencoded)
   54 25.782610775   172.17.0.1 → 172.17.0.2   HTTP 1943   POST /login HTTP/1.1  (application/x-www-form-urlencoded)
   78 42.948569588   172.17.0.1 → 172.17.0.2   HTTP 1935   POST /login HTTP/1.1  (application/x-www-form-urlencoded)
$ tshark -r intro-forensics-1.pcapng -Y 'http.request.method == POST' -T fields -e http.cookie | awk -F ';' '{ print $9 }'
 token=Test
 token=NobodyCanSeeMySecretToken!!!
 token=8967e85a7301be8958b3ccafe1faad4d6dbea2154fbb2fdbcb5221c9cd6c607c877c67d36bd67c0e362a968a0d3522feed7e0d68a70796aa4682735608d7686b
$ 
```
