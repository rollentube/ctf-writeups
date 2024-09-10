# Vulnerabilities in other authentication mechanisms
* supplementary functionality for users to manage their account
  * e.g. change/reset password
* login pages often good secured
* forgotten to secure functionalities as well
* relevant if the attacker can create his own account

## Keeping users logged in
* common feature: stay logged in after closing the browser ("Remember me")
* implemented with a "remember me" token, that is stored in a cookie
* the cookie bypasses the login process
* some websites generate the token with predictable static values (e.g. username + timestamp)
* can be found out with an own account
* try to brute force users' cookie
* some just encrypt the static values
  * Base64 adds no protection
  * other encryptions are not always safe (e.g. attacker finds out the algorithm + no salt)

Lab: [Brute-forcing a stay-logged-in cookie](../labs/Brute-forcing_a_stay-logged-in_cookie.md)

* attackers without an account can also exploit this vulnerability
* with XSS such a cookie could also be stolen and analyzed
* open source websites reveal their cookie construction publicly
* clear text can be extracted from hashed cookies
  * hashed versions of password lists
  * salt is important

Lab: [Offline password cracking](../labs/Offline_password_cracking.md)