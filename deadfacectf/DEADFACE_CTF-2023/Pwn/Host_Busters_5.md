#  Host Busters 5 (100 points)
See if you can crack `gh0st404`’s password. Based on Ghost Town conversations, we suspect the password is found in common wordlists.

Submit the flag as `flag{password}`.

`vim@gh0st404.deadface.io`

Password: `letmevim`

## Solution
As already mentioned in [Host Busters 5](./Host_Busters_5.md) with the privileged rights we are able to read out the /etc/shadow and crack the password. The password of the user `gh0st404` is `zaq12wsx`.

So the flag is: `flag{zaq12wsx}`
