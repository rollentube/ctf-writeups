# Password reset poisoning
* attacker manipulates a vulnerable website into generating a password reset link pointing to a arbitrary domain
  * stealing tokens for resetting their passwords

## How does a password reset work?
* websites allow their users to reset their passwords
* several ways with different degrees of security

Most common approach:
1. User enters username/email and submits a reset request
2. Website checks the user and generates a temporary, unique, high-entropy token associated to the user.
3. Website sends an email to the user with a link containing the query with the token to reset the password (e.g. `https://normal-website.com/reset?token=0a1b2c3d4e5f6g7h8i9j`).
4. If accessed, the website checks if the token is valid and connects it to the account. If everything is fine, the password can be reset and the token is deleted.

* simple and pretty secure
* relies on the access of the user to the email and their unique token
* Password reset poisoning: stealing this token and change the users password

## How to construct a password reset poisoning attack
* if the token is generated based on controllable input (e.g. host header)
* possible to construct the attack:

1. Attacker needs victims username/email and submits a password request for them.
  * intercepting the HTTP request while submitting the form
  * modify the host header
    * changing to the attacker's domain (e.g. `evil-user.net`)
2. Victim receives a password reset email with the link containing the valid token. 
  * but the domain points to the attacker: `https://evil-user.net/reset?token=0a1b2c3d4e5f6g7h8i9j`
3. If the victim clicks the link, the token will be sent to the attacker's server.
4. Attacker can now visit the real URL, supply the stolen token and can change the user's password.

* sometimes possible to inject HTML into sensitive emails if you can't control the reset link
* email clients typically don't execute JavaScript, but something like dangling markup injection may work

Lab: [Basic password reset poisoning](../labs/Basic_password_reset_poisoning.md)

Lab: [Password reset poisoning via middleware](../labs/Password_reset_poisoning_via_middleware.md)

Lab: [Password reset poisoning via dangling markup]()