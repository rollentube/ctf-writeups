# Common Terms
## What is a Shell?
A shell is a program that takes user input as commands, which are performed and executed by the operating system: Linux terminal (Bash, Zsh, etc.), Windows command line, Windows PowerShell

Types of shell connections:
* Reverse shell: initiates a connection back to a listener
* Bind shell: binds to a port on the target
* Web shell: runs operating system commands via the web browser

## What is a Port?
_A port can be thought of as a window or door on a house._

Ports are virtual points for network connections. Software-based and managed by the operating system. Usually they are associated to a process and allows other systems to connect to a specific service. The system can differentiate with ports between different traffic types.

Port numbers range from 1 to 65,535, with the range of well-known ports 1 to 1,023 being reserved for privileged services. If anything attempts to bind to port 0 (such as a service), it will bind to the next available port above port 1,024 because port 0 is treated as a "wild card" port.

Two categories:
* TCP: connection-oriented with handshake
* UDP: connectionless without handshake

Ports are often related to specific protocols. Some of them are:
| Port(s)       | Protocol        |
| ------------- | --------------- |
| 20/21 (TCP)   | FTP             |
| 22 (TCP)      | SSH             |
| 23 (TCP)      | Telnet          |
| 25 (TCP)      | SMTP            |
| 80 (TCP)      | HTTP            |
| 161 (TCP/UDP)	| SNMP            |
| 389 (TCP/UDP)	| LDAP            |
| 443 (TCP)	    | SSL/TLS (HTTPS) |
| 445 (TCP)     | SMB             |
| 3389 (TCP)    | RDP             |

## What is a Web Server?
A web server is an application that runs on the back-end server, which handles all of the HTTP traffic from the client-side browser, routes it to the requests destination pages, and finally responds to the client-side browser.

OWASP Top 10 is a standardizes list of the top 10 web application vulnerabilities by the Open Web Application Security Project (OWASP):
1. Broken Access Control
2. Cryptographic Failures
3. Injection
4. Insecure Design
5. Security Misconfiguration
6. Vulnerable and Outdated Components
7. Identification and Authentication Failures
8. Software and Data Integrity Failures
9. Security Logging and Monitoring Failures
10. Server-Side Request Forgery