# interencdec (50 points)
Can you get the real meaning from this file.

## Data
* enc\_flag

## Solution
The file contains a string that looks like Base64 encoded:
```
$ cat enc_flag
YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclh6ZzJhMnd6TW1zeWZRPT0nCg==
$
```

If we decode it, we get another Base64 string. If we decode this again we get a string that looks like a ROT encoded flag:
```
$ cat enc_flag | base64 -d
b'd3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrXzg2a2wzMmsyfQ=='
$ echo "d3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrXzg2a2wzMmsyfQ==" | base64 -d
wpjvJAM{jhlzhy_k3jy9wa3k_86kl32k2}
$
```

With CyberChef we can adjust the rotations pretty simple and just try out the correct amount. I found that ROT19 is the one we was looking for:
```
picoCTF{caesar_d3cr9pt3d_86de32d2}
```
