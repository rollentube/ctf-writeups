# Custom encryption (100 points)
Can you get sense of this code file and write the function that will decode the given encrypted file content.

Find the encrypted file here _flag\_info_ and _code file_ might be good to analyze and get the flag.

## Data
* enc\_flag
* custom\_encryption.py

## Solution
We have got the following encryption code:
```python
from random import randint
import sys


def generator(g, x, p):
    return pow(g, x) % p


def encrypt(plaintext, key):
    cipher = []
    for char in plaintext:
        cipher.append(((ord(char) * key*311)))
    return cipher


def is_prime(p):
    v = 0
    for i in range(2, p + 1):
        if p % i == 0:
            v = v + 1
    if v > 1:
        return False
    else:
        return True


def dynamic_xor_encrypt(plaintext, text_key):
    cipher_text = ""
    key_length = len(text_key)
    for i, char in enumerate(plaintext[::-1]):
        key_char = text_key[i % key_length]
        encrypted_char = chr(ord(char) ^ ord(key_char))
        cipher_text += encrypted_char
    return cipher_text


def test(plain_text, text_key):
    p = 97
    g = 31
    if not is_prime(p) and not is_prime(g):
        print("Enter prime numbers")
        return
    a = randint(p-10, p)
    b = randint(g-10, g)
    print(f"a = {a}")
    print(f"b = {b}")
    u = generator(g, a, p)
    v = generator(g, b, p)
    key = generator(v, a, p)
    b_key = generator(u, b, p)
    shared_key = None
    if key == b_key:
        shared_key = key
    else:
        print("Invalid key")
        return
    semi_cipher = dynamic_xor_encrypt(plain_text, text_key)
    cipher = encrypt(semi_cipher, shared_key)
    print(f'cipher is: {cipher}')


if __name__ == "__main__":
    message = sys.argv[1]
    test(message, "trudeau")
```
We have got the following information of the encrypted text:
```
a = 95
b = 21
cipher is: [237915, 1850450, 1850450, 158610, 2458455, 2273410, 1744710, 1744710, 1797580, 1110270, 0, 2194105, 555135, 132175, 1797580, 0, 581570, 2273410, 26435, 1638970, 634440, 713745, 158610, 158610, 449395, 158610, 687310, 1348185, 845920, 1295315, 687310, 185045, 317220, 449395]
```

To decrypt out cipher we have to go through the reversed encryption process.

That mean this call as first:
```python
def encrypt(plaintext, key):
    cipher = []
    for char in plaintext:
        cipher.append(((ord(char) * key*311)))
    return cipher

[...]

cipher = encrypt(semi_cipher, shared_key)
```

So for every char we have to calculate `char / key / 311`.

Since we know the values for `a` and `b` we can easily calculate the key: `key = generator(v, a, p)`

That everything for the first step. The second step is the XOR:
```python
def dynamic_xor_encrypt(plaintext, text_key):
    cipher_text = ""
    key_length = len(text_key)
    for i, char in enumerate(plaintext[::-1]):
        key_char = text_key[i % key_length]
        encrypted_char = chr(ord(char) ^ ord(key_char))
        cipher_text += encrypted_char
    return cipher_text

[...]

semi_cipher = dynamic_xor_encrypt(plain_text, text_key)
```

If we use XOR again on an XOR encrypted cipher we get the initial value. That lies in the functionality of XOR. So we can just reuse the `dynamic_xor_encrypt` function. Except for the direction of the for loop. In the original function we iterate from the last to the first char. So to decrypt we have to iterate from the first to the last char: `enumerate(plaintext)`

Also the encryption direction affects the order of our ciphertext. The function XORs the last character and writes it on the first place of the ciphertext and so on. So in the last step we have to flip the order of our decrypted text.

Putting everythin together we got the following code for decryption:
```python
def generator(g, x, p):
    return pow(g, x) % p


def dynamic_xor_encrypt(plaintext, text_key):
    cipher_text = ""
    key_length = len(text_key)
    for i, char in enumerate(plaintext):
        key_char = text_key[i % key_length]
        encrypted_char = chr(ord(char) ^ ord(key_char))
        cipher_text += encrypted_char
    return cipher_text


# Encrypted text
a = 95
b = 21
ciphertext = [237915, 1850450, 1850450, 158610, 2458455, 2273410, 1744710, 1744710, 1797580, 1110270, 0, 2194105, 555135, 132175, 1797580, 0, 581570, 2273410, 26435, 1638970, 634440, 713745, 158610, 158610, 449395, 158610, 687310, 1348185, 845920, 1295315, 687310, 185045, 317220, 449395]

# Key generation
p = 97
g = 31
v = generator(g, b, p)
key = generator(v, a, p)

# Decrypt
decrypted_text = ""
for char in ciphertext:
    decrypted_char = chr(char // key // 311)
    decrypted_text += decrypted_char
decrypted_text = dynamic_xor_encrypt(decrypted_text, "trudeau")
print(decrypted_text[::-1])
```

If we run the code we get our flag:
```
$ python decrypt.py
picoCTF{custom_d2cr0pt6d_66778b34}
$
```
