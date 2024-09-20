# Password reset broken logic
This lab's password reset functionality is vulnerable. To solve the lab, reset Carlos's password then log in and access his "My account" page.
* Your credentials: `wiener:peter`
* Victim's username: `carlos`

## Solution
In the login page, we got a _Forgot password?_ button:

![Forgot password](../images/Password_reset_broken_logic_0.png)

Inhere, we can enter a username or email to get a change password link:

![Forgot password](../images/Password_reset_broken_logic_1.png)

If we do so with the username `wiener`, we get an email with a link to reset our password:

![Reset link](../images/Password_reset_broken_logic_2.png)

Clicking that link, we can reset the password and the process is done:

![Reset form](../images/Password_reset_broken_logic_3.png)

We can now inspect the POST request of this form:

![POST reset](../images/Password_reset_broken_logic_4.png)

The token `temp-forgot-password-token=pf0gdf3awexh5bknmaplpz4fabvgd1kb` is submitted as well. But the flaw is that it's not checked again by the backend. Neither is the username checked to see if they have made a request to reset their password.

So can simply manipulate the POST request and change the username to `carlos` with a password that we want:

![Manipulated password reset](../images/Password_reset_broken_logic_5.png)

After the request, we are redirected to the main page.

And now we can log in as `carlos` with our new password. If we do so, the lab is solved:

![Solved](../images/Password_reset_broken_logic_6.png)