# Pre-Engagement
Pre-engagement is the stage of preparation for the actual penetration test. During this stage, many questions are asked, and some contractual agreements are made. The client informs us about what they want to be tested, and we explain in detail how to make the test as efficient as possible.

The pre-engagemnt process consists of three essential components:
1. Scoping questionnaire
2. Pre-engagement meeting
3. Kick-off meeting

## Non-Disclosure Agreement (NDA)
A Non-Disclosure Agreement (NDA) must be signed by all parties, before the Pre-Engagement can roll on. There are several types of NDAs:
1. **Unilateral**: Only one party maintains confidentiality and the other party is allowed to share the information received with third parties.
2. **Bilateral**: Both parties are obligated to keep the resulting and acquired information confidential (most common).
3. **Multilateral**: Commitment to confidentiality by more than two parties (e.g. penetration test for a cooperative network -> all responsible and involved parties must sign this document).

Exceptions can also be made in urgent cases. Also it is essential to know who in the company is permitted to contract us for a penetration test (CEO, CTO, CISO, etc.).

The NDA is one of several documents, that are required before a penetration test and has to be signed by our client and us. This ensures, that we are not get in conflice with the Computer Misuse Act. The documents are:
1. **Non-Disclosure Agreement (NDA)**: After Initial Contact
2. **Scoping Questionnaire**: Before the Pre-Engagement Meeting
3. **Scoping Document**: During the Pre-Engagement Meeting
4. **Penetration Testing Proposal (Contract/Scope of Work (SoW))**: During the Pre-engagement Meeting
5. **Rules of Engagement (RoE)**: Before the Kick-Off Meeting
6. **Contractors Agreement (Physical Assessments)**: Before the Kick-Off Meeting
7. **Reports**: During and after the conducted Penetration Test

## Scoping Questionnaire
After initial contact is made with the client, we typically send them a Scoping Questionnaire to better understand the services they are seeking. This scoping questionnaire should clearly explain our services and may typically ask them to choose one or more from the our list.

The services could be for example: Internal/External Penetration Test, Web Application Security Assessment, Physical Security Assessment, etc.

The questionnaire should allow the client to be more specific about the required assessment and give more information like:
* How many expected live hosts?	
* How many IPs/CIDR ranges in scope?	
* How many Domains/Subdomains are in scope?	
* How many wireless SSIDs in scope?	
* How many web/mobile applications? If testing is authenticated, how many roles (standard user, admin, etc.)?	
* For a phishing assessment, how many users will be targeted? Will the client provide a list, or we will be required to gather this list via OSINT?	
* If the client is requesting a Physical Assessment, how many locations? If multiple sites are in-scope, are they geographically dispersed?	
* What is the objective of the Red Team Assessment? Are any activities (such as phishing or physical security attacks) out of scope?	
* Is a separate Active Directory Security Assessment desired?	
* Will network testing be conducted from an anonymous user on the network or a standard domain user?	
* Do we need to bypass Network Access Control (NAC)?

* Is the Penetration Test black box (no information provided), grey box (only IP address/CIDR ranges/URLs provided), white box (detailed information provided)
* Would they like us to test from a non-evasive, hybrid-evasive (start quiet and gradually become "louder" to assess at what level the client's security personnel detect our activities), or fully evasive.

Based on those informations we can assign the resources and create a proposal with a project timeline. Finally we can an overview and summarize all information in the **Scoping Document**.

## Pre-Engagement Meeting
This meeting gives the customer a detailed presentation of the penetration test and discusses all relevant and essential components with him. The results will be combined with the scoping questionnaire and serves as inputs for the Penetration Testing Proposal (Contract/Scope of Work (SoW)).

The **Contract Checklist** contains the following:
* NDA
* Goals and milestones
* Scope
* Penetration Testing Type
* Methodologies
* Penetration Testing Locations
* Time Estimation
* Third Parties
* Evasive Testing
* Risks
* Scope Limitations & Restrictions
* Information Handling
* Contact Information
* Lines of Communication
* Reporting
* Payment Terms

Based on the Contract Checklist and the scoping information, the Penetration Testing Proposal (Contract) and the **Rules of Engagement (RoE)** are created. The checklist contains:
* Introduction
* Contractor
* Penetration Testers
* Contact Information
* Purpose
* Goals
* Scope
* Lines of Communication
* Time Estimation
* Time of the Day to Test
* Penetration Testing Type
* Penetration Testing Locations
* Methodologies
* Objectives / Flags
* Evidence Handling
* System Backups
* Information Handling
* Incident Handling and Reporting
* Status Meetings
* Reporting
* Retesting
* Disclaimers and Limitation of Liability
* Permission to Test

## Kick-Off Meeting
Occurs after signing all contracual documents includes the relevant persons from the client (POCs, technical support) and the penetration testing team (management, pentester). We will go over the nature of the penetration test and how it will take place. For example is the reporting of critical vulnerabilities e.g. RCE or SQLi discussed. In such a case the testing will be paused and the emergency contact informed. A report will be generated aswell.

Also we inform the customer about potential risks like log entries, alarms, locked users or negatively impacts to their network.

With the meeting we explain on a professional way the entire process for the customer. For technical stuff and apart from them.

## Questions
How many documents must be prepared in total for a penetration test?

The answer can be found under the NDA paragraph.
