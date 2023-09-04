# Lateral Movement
If everything went well and we were able to penetrate the corporate network (Exploitation) successfully, gather locally stored information, and escalate our privileges (Post-Exploitation), we next enter the Lateral Movement stage. The goal here is that we test what an attacker could do within the entire network.

After all, the main goal is not only to successfully exploit a publicly available system but also to get sensitive data or find all ways that an attacker could render the network unusable. One of the most common examples is ransomware. If a system in the corporate network is infected with ransomware, it can spread across the entire network. It locks down all the systems using various encryption methods, making them unusable for the whole company until a decryption key is entered.

In this stage, we want to test how far we can move manually in the entire network and what vulnerabilities we can find from the internal perspective that might be exploited. In doing so, we will again run through several phases:
1. Pivoting
2. Evasive Testing
3. Information Gathering
4. Vulnerability Assessment
5. (Privilege) Exploitation
6. Post-Exploitation

Also, we can move to this stage from the Exploitation and the Post-Exploitation stage. Sometimes we may not find a direct way to escalate our privileges on the target system itself, but we have ways to move around the network. This is where Lateral Movement comes into play.

## Pivoting
In most cases, the system we use will not have the tools to enumerate the internal network efficiently. Some techniques allow us to use the exploited host as a proxy and perform all the scans from our attack machine. So a non public network can be reached. This process is also known as Pivoting or Tunneling.

## Evasive Testing
Also, at this stage, we should consider whether evasive testing is part of the assessment scope. There are many ways to protect against lateral movement, including network (micro) segmentation, threat monitoring, IPS/IDS, EDR, etc. To bypass these efficiently, we need to understand how they work and what they respond to. Then we can apply methods to avoid detection.

## Information Gathering
Before we target the internal network, we must first get an overview of which systems can be reached from our system. So we return to the Information Gathering stage, but this time, we do it from inside the network with a different view of it. Once we have discovered all hosts and servers, we can enumerate them individually.

## Vulnerability Assessment
Vulnerability assessment from the inside of the network differs from the previous procedures. This is because far more errors occur inside a network than on hosts and servers exposed to the Internet. Here, the groups to which one has been assigned and the rights to different system components play an essential role. In addition, it is common for users to share information and documents and work on them together.

For example, if we compromise a user account assigned to a developer group, we may gain access to most of the resources used by company developers. This will likely provide us with crucial internal information about the systems and could help us to identify flaws or further our access.

## (Privilege) Exploitation
Once we have found and prioritized these paths, we can jump to the step where we use these to access the other systems. For example we find ways to crack passwords and hashes and gain higher privileges, can use our existing credentials or use tools like [Responder](https://github.com/lgandx/Responder) to intercept hashes and use the pass-the-hash technique.

## Post-Exploitation
Once we have reached one or more systems, we go through the steps of the post-exploitation stage again for each system and collect system information, data from created users or business information.
