# Vulnerabilities in multi-factor authentication
* some websites use another authentication factor next to the password
  * mandatory or optional
  * **something you know + something you have**
    * e.g. password + temp. verification code from out-of-band physical device
  * biometric factors is impractical for websites
* second factor unlikely to get for an attacker
* only as secure as its implementation
* "something you know" used twice isn't real 2FA
  * e.g. password + verification code per mail (password and credentials for email are both knowledge)

## Two-factor authentication tokens
* verifications codes read from a physical device
* e.g. RSA token, keypad device, mobile apps, text message
  * last one is open to abuse:
    * send via SMS and not generated -> interceptable
    * SIM swapping (attacker gets a SIM with the victims number)

## Bypassing two-factor authentication
* "only as secure as its implementation"

Scenario: User enters a password and is then prompted to enter a verification code on a separate page
* user is in a "logged in" state
* worth to try to get to a "logged-in only" page

Lab: [2FA simple bypass](../labs/2FA_simple_bypass.md)

## Flawed two-factor verification logic
* user completed initial login
* website doesn't verify correctly that the **same** user completing the second step

### Example
Initial login:
```
POST /login-steps/first HTTP/1.1
Host: vulnerable-website.com
...
username=carlos&password=qwerty
```

Cookie assigned before the second step:
```
HTTP/1.1 200 OK
Set-Cookie: account=carlos

GET /login-steps/second HTTP/1.1
Cookie: account=carlos
```

In the next step a verification code will be used (2FA). The earlier cookie is used to determine the account:
```
POST /login-steps/second HTTP/1.1
Host: vulnerable-website.com
Cookie: account=carlos
...
verification-code=123456
```

Attacker can change the account cookie to another username:
```
POST /login-steps/second HTTP/1.1
Host: vulnerable-website.com
Cookie: account=victim-user
...
verification-code=123456
```

* attacker is as the `victim-user` authenticated
* no password needed
* verification code can be brute-forced

Lab: [2FA broken logic](../labs/2FA_broken_logic.md)

## Brute-forcing 2FA verification codes
* website must prevent brute forcing for the 2FA (especially with 4/6-digit codes)
* some website log a user out if he enters too many wrong codes
  * not a good solution
  * macros (Burp Intruder) can be created to automate this process
  * Turbo Intruder can also be used

Lab: [2FA bypass using a brute-force attack](../labs/2FA_bypass_using_a_brute-force_attack.md)
