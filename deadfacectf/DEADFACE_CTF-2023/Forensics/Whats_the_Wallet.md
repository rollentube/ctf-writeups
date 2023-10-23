# What's the Wallet (20 points)
Ransomware was recently discovered on a system within De Monne’s network courtesy of a DEADFACE member. Luckily, they were able to restore from backups. You have been tasked with finding the Bitcoin wallet address from the provided sample so that it can be reported to the authorities. Locate the wallet address in the code sample and submit the flag as `flag{wallet_address}`.

[Download File](https://tinyurl.com/4ep6etk7)
SHA1: 69c2fd859d7f3666349b41106bef348ce51ca0da

## Solution
In the source code we find the following function:
```php
function Store-BtcWalletAddress {
    `$global:BtcWalletAddress = [System.Convert]::FromBase64String([System.Text.Encoding]::UTF8.GetBytes('bjMzaGE1bm96aXhlNnJyZzcxa2d3eWlubWt1c3gy'))
}
```

The string `bjMzaGE1bm96aXhlNnJyZzcxa2d3eWlubWt1c3gy` is Base64 encoded. If we decode it we get the wallet address:
```
$ echo 'bjMzaGE1bm96aXhlNnJyZzcxa2d3eWlubWt1c3gy' | base64 -d
n33ha5nozixe6rrg71kgwyinmkusx2
```

So the flag is `flag{n33ha5nozixe6rrg71kgwyinmkusx2}`.