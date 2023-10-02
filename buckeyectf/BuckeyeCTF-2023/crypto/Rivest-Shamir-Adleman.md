# Rivest-Shamir-Adleman (beginner)
Big numbers make big security

## Files
* dist.py

## Solution
The script uses the RSA algorithm to encrypt a message:
```python
message = b"[REDACTED]"

m = int.from_bytes(message, "big")

p = 3782335750369249076873452958462875461053 # prime
q = 9038904185905897571450655864282572131579 # prime
e = 65537 # exponent

n = p * q # public key
et = (p - 1) * (q - 1) # private key phi
d = pow(e, -1, et) # private key

c = pow(m, e, n) # encrypt with public key
```

Since the message is encrypted with the public key, we can simply decrypt it with the private key:
```python
dec = pow(c, d, n) # decrypt with private key
```

The script also shows the output of a different execution with an encrypted message:
```python
# OUTPUT:
# e = 65537
# n = 34188170446514129546929337540073894418598952490293570690399076531159358605892687
# c = 414434392594516328988574008345806048885100152020577370739169085961419826266692
```

So we have to decrypt `c`:
```python
# decrypt with private key
c = 414434392594516328988574008345806048885100152020577370739169085961419826266692
dec = pow(c, d, n)

dec_bytes = bytes.fromhex(f'{dec:x}')
dec_string = dec_bytes.decode('utf-8')

print(dec_string)
```

Running the script gives us the flag:
```
$ python dist.py
e = 65537
n = 34188170446514129546929337540073894418598952490293570690399076531159358605892687
c = 28757147278231593142695434919904858691582799419726779855729029505856861067181243
bctf{1_u53d_y0ur_k3y_7h4nk5}
$
```

https://www.geeksforgeeks.org/rsa-algorithm-cryptography/ shows more information relating to the RSA algorithm.