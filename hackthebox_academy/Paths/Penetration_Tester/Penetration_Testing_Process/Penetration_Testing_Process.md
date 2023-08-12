# Penetration Testing Process
A Penetration Test (Pentest) is an **organized, targeted, and authorized attack** attempt to test IT infrastructure and its defenders to determine their susceptibility to IT security vulnerabilities. A pentest uses methods and techniques that real attackers use. As penetration testers, we apply various techniques and analyses to gauge the impact that a particular vulnerability or chain of vulnerabilities may have on the confidentiality, integrity, and availability of an organization's IT systems and data.

A pentest aims to uncover and identify all vulnerabilities in the systems under investigation and improve the security for the tested systems.

During a pentest, we prepare detailed documentation on the steps taken and the results achieved. However, it is the client's responsibility or the operator of their systems under investigation to rectify the vulnerabilities found. Our role is as trusted advisors to report vulnerabilities, detailed reproduction steps, and provide appropriate remediation recommendations, but we do not go in and apply patches or make code changes, etc. It is important to note that a pentest is not monitoring the IT infrastructure or systems but a momentary snapshot of the security status. A statement to this regard should be reflected in our penetration test report deliverable.

## Penetration Testing Stages
![PT Process](images/PT-Process.png)

### Pre-Engagement
The pre-engagement stage is where the **main commitments, tasks, scope, limitations, and related agreements** are documented in writing. During this stage, contractual documents are drawn up, and essential information is exchanged that is relevant for penetration testers and the client, depending on the type of assessment.

### Information Gathering
Information gathering is an essential part of any assessment. Because information, the knowledge gained from it, the conclusions we draw, and the steps we take are based on the information available. This information must be obtained from somewhere, so it is critical to know **how to retrieve it and best leverage it** based on our assessment goals.

The information we gather in advance will influence the results of the Exploitation stage. From this, we can see if we have collected enough or dived deep enough. Time, patience, and personal commitment all play a significant role in information gathering. This is when many penetration testers tend to jump straight into exploiting a potential vulnerability. This often fails and can lead, among other things, to a significant loss of time. Before attempting to exploit anything, we should have completed thorough information gathering, keeping detailed notes along the way, focusing on things to hone in on once we get to the exploitation stage. Most assessments are time-based, so we don't want to waste time bouncing around, which could lead to us missing something critical. Organization and patience are vital while being as thorough as possible.

### Vulnerability Assessment
The vulnerability assessment stage is divided into two areas. On the one hand, it is an approach to scan for known vulnerabilities using **automated tools** (like Nessus, Qualys or OpenVAS). On the other hand, it is **analyzing for potential vulnerabilities** through the information found. Many companies conduct regular vulnerability assessment audits to check their infrastructure for new known vulnerabilities and compare them with the latest entries in these tools' databases.

An analysis is more about thinking outside the box. We try to discover gaps and opportunities to trick the systems and applications to our advantage and gain unintended access or privileges. This requires creativity and a deep technical understanding. We must connect the various information points we obtain and understand its processes.

### Exploitation
Exploitation is the **attack performed against a system or application** based on the potential vulnerability discovered during our information gathering and enumeration. We use the information from the Information Gathering stage, analyze it in the Vulnerability Assessment stage, and prepare the potential attacks. Often many companies and systems use the same applications but make different decisions about their configuration. This is because the same application can often be used for various purposes, and each organization will have different objectives.

This stage is so comprehensive that it has been divided into two distinct areas. The first category is **general network protocols** often used and present in almost every network. The actual exploitation of the potential and existing vulnerabilities is based on the adaptability and knowledge of the different network protocols we will be dealing with. In addition, we need to be able to create an overview of the existing network to understand its individual components' purposes. In most cases, web servers and applications contain a great deal of information that can be used against them. As stated previously, since web is a vast technical area in its own right, it will be treated separately. We are also interested in the remotely exposed services running on the target hosts, as these may have misconfigurations or known public vulnerabilities that we can leverage for initial access. Finally, existing users also play a significant role in the overall network.

**Web exploitation** is the second part of the exploitation stage. Many different technologies, improvements, features, and enhancements have been developed in this area over the last few years, and things are constantly evolving. As a result, many different components come into play when dealing with web applications. This includes many kinds of databases that require differing command syntax to interact with. Due to the diversity of web applications available to companies and their prevalence worldwide, we must deal with this area separately and focus intently on it. Web applications present a vast attack surface and are often the main accessible targets during external penetration testing engagements, so strong web enumeration and exploitation skills are paramount.

### Post-Exploitation
In most cases, when we exploit certain services for our purposes to gain access to the system, we usually do not obtain the highest possible privileges. Because services are typically configured in a certain way "isolated" to stop potential attackers, bypassing these restrictions is the next step we take in this stage. However, it is not always easy to escalate the privileges. After gaining in-depth knowledge about how these operating systems function, we must adapt our techniques to the particular operating system and carefully study how **Linux Privilege Escalation and Windows Privilege Escalation** work.

After we have gained access to a system, we must be able to take further steps from within the system. During a penetration test, customers often want to find out how far an attacker could go in their network. There are many different versions of operating systems. For example, we may run into Windows XP, Windows 7, 8, 10, 11, and Windows Server 2008, 2012, 2016, and 2019. There are also different distributions for Linux-based operating systems, such as Ubuntu, Debian, Parrot OS, Arch, Deepin, Redhat, Pop!\_OS, and many others. **No matter which of these systems we get into, we have to find our way around it and understand the individual weak points** that a system can have from within.

### Lateral Movement
Lateral movement is one of the essential components for **moving through a corporate network**. We can use it to overlap with other internal hosts and further escalate our privileges within the current subnet or another part of the network. However, just like Pillaging, the Lateral Movement stage requires access to at least one of the systems in the corporate network. In the Exploitation stage, the privileges gained do not play a critical role in the first instance since we can also move through the network without administrator rights.

### Proof-of-Concept
The Proof-Of-Concept (POC) is merely **proof that a vulnerability found exists**. As soon as the administrators receive our report, they will try to confirm the vulnerabilities found by reproducing them. After all, no administrator will change business-critical processes without confirming the existence of a given vulnerability. A large network may have many interoperating systems and dependencies that must be checked after making a change, which can take a considerable amount of time and money. Just because a pentester found a given flaw, it doesn't mean that the organization can easily remediate it by just changing one system, as this could negatively affect the business. Administrators must carefully test fixes to ensure no other system is negatively impacted when a change is introduced. PoCs are sent along with the documentation as part of a high-quality penetration test, allowing administrators to use them to confirm the issues themselves.

### Post-Engagement
The Post-Engagement stage also includes **cleaning up the systems we exploit** so that none of these systems can be exploited using our tools. For example, leaving a bind shell on a web server that does not require authentication and is easy to find will do the opposite of what we are trying to do. In this way, we endanger the network through our carelessness. Therefore, it is essential to remove all content that we have transferred to the systems during our penetration test so that the corporate network is left in the same state as before our penetration test. We also should **note down any system changes, successful exploitation attempts, captured credentials, and uploaded files** in the appendices of our report so our clients can cross-check this against any alerts they receive to prove that they were a result of our testing actions and not an actual attacker in the network.

In addition, we have to **reconcile all our notes with the documentation** we have written in the meantime to make sure we have not skipped any steps and can provide a comprehensive, well-formatted and neat report to our clients.

## Testing Methods
### External Penetration Test
Many pentests are performed from an **external perspective or as an anonymous user on the Internet**. Most customers want to ensure that they are as **protected** as possible **against attacks on their external network perimeter**. We can perform testing from our own host (hopefully using a VPN connection to avoid our ISP blocking us) or from a VPS. Some clients will not care about stealth, while others will request that we proceed as quietly as possible and approach the target systems to avoid being banned by the firewalls and IDS/IPS systems and avoid triggering an alarm. They may ask for a stealthy or "hybrid" approach where we gradually become "noisier" to test their detection capabilities. Ultimately our goal here is to access external-facing hosts, obtain sensitive data, or gain access to the internal network.

### Internal Penetration Test
In contrast to an external pentest, an internal pentest is when we perform **testing from within the corporate network**. This stage may be executed after successfully penetrating the corporate network via the external pentest or starting from an assumed breach scenario. Internal pentests may also access isolated systems with no internet access whatsoever, which usually requires our physical presence at the client's facility.

## Types of Penetration Testing
| Type           | Information Provided |
| -------------- | -------------------- |
| Blackbox       | Minimal. Only the essential information, such as IP addresses and domains, is provided. |
| Greybox        | Extended. In this case, we are provided with additional information, such as specific URLs, hostnames, subnets, and similar. |
| Whitebox       | Maximum. Here everything is disclosed to us. This gives us an internal view of the entire structure, which allows us to prepare an attack using internal information. We may be given detailed configurations, admin credentials, web application source code, etc. |
| Red-Teaming    | May include physical testing and social engineering, among other things. Can be combined with any of the above types. |
| Purple-Teaming | It can be combined with any of the above types. However, it focuses on working closely with the defenders. |

## Laws and Regulations
Each country has specific federal laws which **regulate computer-related activities, copyright protection, interception of electronic communications, use and disclosure of protected health information, and collection of personal information** from children, respectively.

It is essential to follow these laws to protect individuals from unauthorized access and exploitation of their data and to ensure their privacy. We must be aware of these laws to ensure our research activities are compliant and do not violate any of the provisions of the law. Failure to comply with these laws can result in civil or criminal penalties, making it essential for individuals to familiarize themselves with the law and understand the potential implications of their activities. Furthermore, it is crucial to ensure that research activities adhere to these laws' requirements to protect individuals' privacy and guard against the potential misuse of their data. By following these laws and exercising caution when conducting research activities, security researchers can help ensure that individuals' data is kept secure and their rights are protected.

### Precautionary Measures during Penetration Tests
We have prepared a list of precautions we highly recommend following during each penetration test to avoid violating most laws. In addition, we should also be aware that some countries have additional regulations that apply to specific cases, and we should either inform ourselves or ask our lawyer:

* Obtain written consent from the owner or authorized representative of the computer or network being tested
* Conduct the testing within the scope of the consent obtained only and respect any limitations specified
* Take measures to prevent causing damage to the systems or networks being tested
* Do not access, use or disclose personal data or any other information obtained during the testing without permission
* Do not intercept electronic communications without the consent of one of the parties to the communication
* Do not conduct testing on systems or networks that are covered by the Health Insurance Portability and Accountability Act (HIPAA) without proper authorization
