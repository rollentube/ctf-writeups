# Information Gathering
Once the pre-engagement phase has been completed, and all parties have signed all contractual terms and conditions, the information gathering phase begins. Information gathering is an essential part of any security assessment. This is the phase in which we gather all available information about the company, its employees and infrastructure, and how they are organized. Information gathering is the most frequent and vital phase throughout the penetration testing process, to which we will return again and again.

To gather information about our targets, we can mention the following categories:
1. Open-Source Intelligence
2. Infrastructure Enumeration
3. Service Enumeration
4. Host Enumeration

## Open-Source Intelligence (OSINT)
OSINT is a process for finding publicly available information on a target company or individuals. We can often find security-relevant and sensitive information from companies and their employees.

For example can passwords, hashes, keys, tokens and much more be found on Github repositories if they are not set up correctly. Such information can also be found on StackOverflow or other platforms where source code is shared. The process of incident handling and reporting if such data is found, is written down in the RoE. Passwords or SSH-Keys could be a critical security gap.

## Infrastructure Enumeration
We try to overview the company's position on the internet and intranet. For that we use OSINT and first active scans (internal and external). Services like DNS can help to create a map of servers, hosts and the structure of the clients infrastructure. That includes for example name servers, mail servers, web servers or cloud instances. We create a list with the hosts/IPs and compare them to our scope.

Also we try to determine the company's security measures. This could be helpful to disguise the attacks (Evasive Testing), if requested.

## Service Enumeration
Here we identify services that allow us to interact with the host or server. For that we find out a services version, information that it provides and the purpose of it.

The version gives us information if the host is up to date or could tell us if there is a security vulnerabilities because of an older versions. 

## Host Enumeration
With a detailed list of the infrastructure, we can examine every host listed in the scoping document. We try to identify the operating system, running services and there versions and more. Again, active scans and OSINT could be helpful here.

The enumeration includes internal and external hosts. Internal hosts or services are not uncommon misconfigurated, because they "aren't connected to the internet" and administrators won't pay much attention to them.

If we got access to a host, this category also includes files, local services, scripts, applications and so on. This information could be found after the Post-Exploitation phase or could be helpful for it (keep in mind the back and forth between the stages).

## Pillaging
Like discussed in the earlier paragraph Host Enumeration, after the Post-Exploitation stage we collect sensitive information locally on already exploited hosts. This process is also called Pillaging and could be used to escalate our privileges or move laterally in the network.

Pillaging itself is not a stage or a subcategory, but an integral part of information gathering and privelege escalation.
