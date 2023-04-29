# Burp Suite: The Basics
An introduction to using Burp Suite for Web Application pentesting.

This rooms contains mainly theoretical parts, that are just reading and filling in the solution based on the read text. I wont give the answers for that parts here. I will summarize the different topics instead.

## Task 1: Outline
Nothing interesting here

## Task 2: What is Burp Suie?
1. Burp Suite Community Edition
- free to use
- less features

2. Burp Suite Professional
- An automated vulnerability scanner
- A fuzzer/bruteforcer that isn't rate limited
- Saving projects for future use; report generation
- A built-in API to allow integration with other tools
- Unrestricted access to add new extensions for greater functionality
- Access to the Burp Suite Collaborator (effectively providing a unique request catcher self-hosted or running on a Portswigger owned server)

3. Burp Suite Enterpirse
- used for continous scanning (automated)
- runs server side

## Task 3: Features of Burp Community
Modules of the CE
1. Proxy
- intercept and modify requests/responses of web applications

2. Repeater
- capture, modify and resend the same request numerous times
- good for trail and error payloads

3. Intruder
- spray an endpoint with request
- used for bruteforce or fuzzing

4. Decoder
- decoding captured information
- endoding payload

5. Comparer
- compare data on word or byte level

6. Sequencer
- used for randomness of tokens
- for example session cookies or random generated data

## Task 4: Installation
Nothing interesting here

## Task 5: The Dashboard
1. Tasks
- define and manage background tasks

2. Event log
- logs
- e.g. starting proxy, starting connections

3. Issue activity
- Burp Pro only
- shows found vulnerabilities by the automated scanner

4. Advisory
- more information for the found vulnerabilities

## Task 6: Navigation
- modules as tabs in the overview
- shortcuts to switch between the tabs:
    - Ctrl + Shift + D -> switch to dashboard
    - Ctrl + Shift + T -> switch to target
    - Ctrl + Shift + P -> switch to proxy
    - Ctrl + Shift + I -> switch to intruder
    - Ctrl + Shift + R -> switch to repeater

## Task 7: Options
- **Global settings** can be found in the User options tab along the top menu bar
- **Project-specific settings** can be found in the Project options tab
- In current versions the two has been moved to one 'Settings' menu, with the tabs 'All', 'User' and 'Project'

### User options
Also in newer Versions the options are move and renamed
- Connections: Network -> Connections
    - control how Burp make connections to targets
- TLS: Network -> TLS
    - enable/disable TLS options
    - upload client certificates
- Display: User interface -> Display
    - appearance
- Misc: Probably splitted up
    - for example: User interface -> Hotkeys

### Project options
Also in newer Versions the options are move and renamed
- Connections: Network -> Connections
    - same options as in the user options, but overrides them for a project
    - Hostname Resolution: map domains to IPs
    - Out-of-Scope Requests: control requests to anything that is not targeted
- HTTP: Network -> HTTP
    - control handle with HTTP protocol (for example follow redirects)
- TLS: Network -> TLS
    - same options as in the user options, but overrides them for a project
    - list of publice server certificates
- Sessions
    - control handle with sessions
    - behavior of cookies
    - macros for automating tasks (logging into web applications with credentials)
- Misc: Probably splitted up
    - logging, embedded browser


## Task 8: Introduction to the Burp Proxy
Intercept, capture and manipulate requests and responses between client and target. Like ZAP. Every request can be send to the other modules of Burp.

- Intercept: intercept the requests (Forward, Drop)
- HTTP history: loggings of the requests
- WebScokets history: loggings of the web sockets

The proxy options gives for example the ability to configure rule on that to intercept.

Forward Shortcut: Ctrl + F

## Task 9: Connecting through the Proxy (FoxyProxy)
Two options using the proxy:
1. embedded Burp browser
2. configure local browser
    - plugins like FoxyProxy
    - configure network settings

Firefox
- Settings -> General -> Network Settings (bottom) -> Manual proxy configuration -> localhost : 8080

## Task 10: Proxying HTTPS
Import Burp CA
- connect to http://burp/cert (Proxy enabled) and download the 'cacert.der' File
- activate in Firefox: Settings -> Privacy & Security -> Certificates (bottom) -> View Certificates -> Import

## Task 11: The Burp Suite Browser
Using the embedded browser doesn't need any proxy configuration (pre configured). Both options are commonly used.

## Task 12: Scoping and Targeting
Scoping specific domain
- Target tab -> right click targeted URL -> Add to scope
- in the scope settings we can see all target scopes (Settings -> Project -> Scope)

Intercept only scoped URLs
- Proxy settings (Settings -> Tools -> Proxy)
- Request interception rules -> activate the rule "And URL Is in target scope"

## Task 13: Site map and Issue Definitions
Sub tabs under the Target tab
- Site map: Tree structure of the visited apps (folders etc. of web app)
    - Burp Pro would spider through everything and look for links between pages etc.
- Issue definitions: List of vulnerabilities that Burp Pro can look up for (with a lot of description)

### Flag
Iterating through the subpages of the target machine will give us the site page "http://10.10.241.61/5yjR2GLcoGoij2ZK". Looking at the Response of this URL will reveal the flag: `THM{NmNlZTliNGE1MWU1ZTQzMzgzNmFiNWVk}`

## Task 14: Example Attack
Try typing: `<script>alert("Succ3ssful XSS")</script>`, into the "Contact Email" field. You should find that there is a client-side filter in place which prevents you from adding any special characters that aren't allowed in email addresses.

Fortunately for us, client-side filters are absurdly easy to bypass. There are a variety of ways we could disable the script or just prevent it from loading in the first place.

Let's focus on simply bypassing the filter for now.

First, make sure that your Burp Proxy is active and that the intercept is on.

Now, enter some legitimate data into the support form. For example: "pentester@example.thm" as an email address, and "Test Attack" as a query.

Submit the form -- the request should be intercepted by the proxy.

With the request captured in the proxy, we can now change the email field to be our very simple payload from above: `<script>alert("Succ3ssful XSS")</script>`. After pasting in the payload, we need to select it, then URL encode it with the Ctrl + U shortcut to make it safe to send.

The last line of the request should look like this: `email=<script>alert("Succ3ssful XSS")</script>&content=test`

Finally, press the "Forward" button to send the request.

You should find that you get an alert box from the site indicating a successful XSS attack!

## Task 15: Room Conclusion
Nothing to note here. The room is done!
