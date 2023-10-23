# Coin Code (10 points)
We found this image of a coin that belongs to a member of DEADFACE. The image has something to do with the encoded message. We believe the message indicates who this DEADFACE actor wants to target next. Figure out who the target is.

Submit the flag as `flag{Target Name}` (e.g., `flag{Bob's Auto}`)

The encoded message reads: `Fwpl lsjywl xgj ew oadd tw Smjgjs Hzsjes.`

[Download Image](https://tinyurl.com/2k239ux9)
SHA1: 03e101c4c177ecc477e024366958f25ae595b124

## Solution
The image shows a coin with to rings of letters on it. The outer ring shows A B C ... The inner ring as well, but moved to the right. This is the ROT chiffre.

So the encrypted message are the letters in the inner ring. The decrypted letters are those letters from the outer ring, that are above the inner ones. The alphabet is rotated. If count the steps from the outer to the inner A, we count 8. So the encoding is probably ROT 8.

With a tool like CyberChef we can decode this and get the following message: `Next target for me will be Aurora Pharma`

So the flag is: `flag{Aurora Pharma}`