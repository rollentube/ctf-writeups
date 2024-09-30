# fu (50 points)
"There is just news. There is no good or bad. Except for the news that you can sign up for classes today at https://fu.challs.pwnoh.io and become the dragon warrior for a few dollars a month, that is GREAT news!" - Master Oogway

## Solution
The flag is located in a comment in the source code of the website. Since we are not able to inspect the source code via the browser, we can fetch it for example with curl:
```
$ curl https://fu.challs.pwnoh.io/ | grep -i bctf
        <!-- Sign up within the next hour and get the flag free too! bctf{1n5p3c7_3l3m3n7_w0rk4r0und_f0und_88b73569618bcb6a} -->
$
```
