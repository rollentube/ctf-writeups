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

## Resetting user passwords
* users forget passwords, normal to reset them
* alternative methods to make sure that the real user is resetting the password
* few different ways to implement this feature

### Sending passwords by email
* sending the current password to the user shouldn't be possible
* some websites generate new passwords and send them to the user via email
* persistent password over insecure channel -> should be avoided
  * password should expire, or the user should be forced to change it
* email not secure
  * mailbox is persistent and no secure storage
  * often automatic synched across insecure channels

### Resetting passwords using a URL
* more robust method of resetting passwords
* URL to password reset page
* if not good configured that account name is in the URL:
```
http://vulnerable-website.com/reset-password?user=victim-user
```
* can be changed to every username to reset the password
* better to use tokens:
```
http://vulnerable-website.com/reset-password?token=a0ba0d1cb3b63d13822572fcff1a241895d893f659164d4cc550b421ebdd48a8
```
* system should be able to check
  * if the token exists
  * which password it resets
  * token should expire after a short period
  * token should be deleted after the password was reset
* sometimes the token isn't validated again when the reset form is submitted
  * attack could visit the reset form from his user
  * delete the token
  * leverage the page to the reset of another user's password

Lab: [Password reset broken logic](../labs/Password_reset_broken_logic.md)

* another problem can be if the URL is generated dynamically
  * could be vulnerable to [password reset poisoning](./Password_reset_poisoning.md)
    * the attacker can steal the token from another user
    * can reset the password of the user

Lab: [Password reset poisoning via middleware](../labs/Password_reset_poisoning_via_middleware.md)

### Changing user passwords
* typically current password needed to change to a new one
* pages rely on process for checking username and password match (like login page)
  * vulnerable to the same techniques
* dangerous if it allows to access it directly without being logged in as a specific user
* example: username is provided in a hidden field -> attacker can change it to another user
  * can be lead to password brute-forcing

Lab: [Password brute-force via password change](../labs/Password_brute-force_via_password_change.md)
