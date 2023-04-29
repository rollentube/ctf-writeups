# Virtual Machin 0
Can you crack this black box? (100 Points)
We grabbed this design doc from enemy servers: Download. We know that the rotation of the red axle is input and the rotation of the blue axle is output. The following input gives the flag as output: Download.

## Data
- Virtual-Machine-0.zip
- input.txt

## Solution
Using https://3dviewer.net/ we can see a black box out of Lego stone. If we tear them down we see two axles with gears inside. A big red one and smaller purple (should be blue as you can see with other 3D viewers) one. The red has 40 and the blue has 8 teeth. So rotate the red one time causes in 5 rotations for the blue one.

So with the input of `39722847074734820757600524178581224432297292490103996085769154356559546905` we will get the output `198614235373674103788002620892906122161486462450519980428845771782797734525` (input * 5).

But what can we do with this number. Its no ASCII or something "easy" alphabetical approach. Searching a bit for crypto and CTF brought me to <https://captainmich.github.io/programming_language/CTF/Challenge/CryptoHack/general.html>. Especially the _Bytes and Big Integers_ section.

Using the following pyhton snippet brings us the correct flag:
```python
>>> from Crypto.Util.number import bytes_to_long
>>> from Crypto.Util.number import long_to_bytes
>>>
>>> data = 198614235373674103788002620892906122161486462450519980428845771782797734525
>>> bytes = long_to_bytes(data)
>>> print(bytes)
b'picoCTF{g34r5_0f_m0r3_c133eae2}'
>>>
```

The string was converted to the hex ASCII representation. This hex values were concatenated and converted to a decimal number. So you could also just convert it back to hex and get the ASCII values with CyberChef or something else.
```python
>>> hex(198614235373674103788002620892906122161486462450519980428845771782797734525)
'0x7069636f4354467b67333472355f30665f6d3072335f63313333656165327d'
>>> bytearray.fromhex("7069636f4354467b67333472355f30665f6d3072335f63313333656165327d").decode()
'picoCTF{g34r5_0f_m0r3_c133eae2}'
>>>
```
