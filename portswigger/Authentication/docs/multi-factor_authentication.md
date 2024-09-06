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