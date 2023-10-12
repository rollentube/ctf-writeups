# Web Enumeration
When performing service scanning, we will often run into web servers running on ports 80 and 443. Webservers host web applications (sometimes more than 1) which often provide a considerable attack surface and a very high-value target during a penetration test. Proper web enumeration is critical, especially when an organization is not exposing many services or those services are appropriately patched.

## Gobuster
[Gobuster](https://github.com/OJ/gobuster) is a tool that can enumerate web directories, DNS names or vhosts with brute force.

### Directory enumeration
To run Gobuster with a wordlist to enumerate directories, we can use the following command:
```
gobuster dir -u http://10.10.10.121/ -w /usr/share/dirb/wordlists/common.txt
```
* `dir` uses directory enumeration mode
* `-u` specifies the url
* `-w` gives a wordlist

### Status codes
* `2xx` succes
* `3xx` redirection
* `4xx` client error

### DNS enumeration
Like already said, Gobuster can enumerate DNS names, especially subdomains, aswell. For that we can use the following command:
```
gobuster dns -d inlanefreight.com -w /usr/share/SecLists/Discovery/DNS/namelist.txt
```
* `dns` uses DNS enumeration mode
* `-d` specifies the domain

[SecLists](https://github.com/danielmiessler/SecLists) is an excellent collection of wordlists for different scenarios. Also, it contains a list for domain names.

## Web Enumeration Tips
### Banner Grabbing / Web Server Headers
#### cURL
With `cURL` we can retrieve the header information of the web server:
```
curl -IL https://www.inlanefreight.com
```
* `-I` shows only headers
* `-L` follows redirection (`3xx`)

#### EyeWitness
[EyeWitness](https://github.com/RedSiege/EyeWitness) is a tool, that can take a screenshot of the web application, fingerprint them, and identify possible default credentials. A command example:
```
eyewitness --single data.analytical.htb --web
```

#### Whatweb
With Whatweb we can easily extract the version of web servers, supporting frameworks and applications:
```
whatweb 10.10.10.121
```

As well we can scan whole networks:
```
whatweb --no-errors 10.10.10.0/24
```

### Certificates
The SSL/TLS certificates of a web servers contains many information, including the email address and company name. Those can be used for example for phishing. The certificate can be views in the browser.

### Robots.txt
The `robots.txt` file instructs search engine web crawlers which resource can or cannot be accessed for indexing. In here could also be information of private files and admin pages.

### Source Code
The source code of a website can be inspected in the browser. For example with the shortcut `CTRL + U`. Often we can find useful information or comments from the developer that weren't removed.

## Questions
Answer the question(s) below to complete this Section and earn cubes!

```
Target: 94.237.59.185:47807 
Life Left: 89 minutes
```

Try running some of the web enumeration techniques you learned in this section on the server above, and use the info you get to get the flag.
```
> HTB{w3b_3num3r4710n_r3v34l5_53cr375}
```

### Solution
Check `robots.txt`:
```
$ curl 94.237.59.185:47807/robots.txt
User-agent: *
Disallow: /admin-login-page.php
```

Inspect `/admin-login-page.php`:
```
$ curl 94.237.59.185:47807/admin-login-page.php

<!DOCTYPE html>
<html>

[...]

<body>
                <form name='login' autocomplete='off' class='form' action='' method='post'>
            <div class='control'>
                <h1>
                    Admin Panel
                </h1>
            </div>
            <div class="container">
                <label for="username"><b>Username</b></label>
                <input name='username' placeholder='Username' type='text'>

                <label for="password"><b>Password</b></label>
                <input name='password' placeholder='Password' type='password'>

                <!-- TODO: remove test credentials admin:password123 -->

                <button type="submit" formmethod='post'>Login</button>
            </div>
        </form>
    </body>

</html>
```

In a comment we find the credentials for the login:
```html
<!-- TODO: remove test credentials admin:password123 -->
```

If we try to login with those credentials, we get the flag:
```
$ curl -X POST 94.237.59.185:47807/admin-login-page.php --data "username=admin&password=password123"

<!DOCTYPE html>
<html>

[...]

<body>
            <form name='logout' autocomplete='off' class='form' action='?logout=1' method='post'>

            <button type='submit' formmethod='post'>
                <div class='text'>
                    Logout
                </div>
            </button>
            <br><br>
            <center><strong>HTB{w3b_3num3r4710n_r3v34l5_53cr375}</strong></center>
        </form>
        </body>

</html>
```