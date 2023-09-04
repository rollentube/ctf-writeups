# Post-Engagement
Much like there is considerable legwork before an engagement officially starts (when testing begins), we must perform many activities (many of them contractually binding) after our scans, exploitation, lateral movement, and post-exploitation activities are complete. No two engagements are the same, so these activities may differ slightly but generally must be performed to close out an engagement fully.

## Cleanup
Once testing is complete, we should perform any necessary cleanup, such as deleting tools/scripts uploaded to target systems, reverting any (minor) configuration changes we may have made, etc. We should have detailed notes of all of our activities, making any cleanup activities easy and efficient. If we don't have access to a system anymore, we have to contact the client. Also we should document all cleanup changes.

## Documentation and Reporting
Before we finally stop all our activities and inform the client, we have to make sure that we have a documentation for all findings (including command output, screenshots, listing of hosts, scan and log output, etc.).

* The report should consist of the following:
* An attack chain with detailed steps taken to achieve compromise
* A strong executive summary that a non-technical audience can understand
* Detailed findings specific to the client's environment (including risk rating, finding impact, remediation recommendations, high-quality external references related to the issue)
* Adequate steps to reproduce each finding for the team responsible for remediation
* Near, medium, and long-term recommendations specific to the environment
* Appendices which include information such as
    * the target scope
    * OSINT data
    * password cracking analysis
    * discovered ports/services
    * compromised hosts
    * compromised accounts
    * files transferred to client-owned systems
    * any account creation/system modifications
    * an Active Directory security analysis
    * relevant scan data/supplementary documentation
    * any other information necessary to explain a specific finding

## Report Review Meeting
Once the draft report is delivered, and the client has had a chance to distribute it internally and review it in-depth, it is customary to hold a report review meeting to walk through the assessment results. Typically we will go through each finding briefly and give an explanation from our own perspective/experience. The client will have the opportunity to ask questions about anything in the report.

## Deliverable Acceptance
The Scope of Work should clearly define the acceptance of any project deliverables. In penetration test assessments, generally, we deliver a report marked DRAFT and give the client a chance to review and comment. Once the client has submitted feedback (i.e., management responses, requests for clarification/changes, additional evidence, etc.) either by email or (ideally) during a report review meeting, we can issue them a new version of the report marked FINAL.

## Post-Remediation Testing
Most engagements include post-remediation testing as part of the project's total cost. In this phase, we will review any documentation provided by the client showing evidence of remediation or just a list of remediated findings. We will need to reaccess the target environment, test each issue to ensure it was appropriately remediated and issue a post-remediation report including evidences.

For example we can create a table like the following:
| #   | Finding Severity | Finding Title                       | Status         |
| --- | ---------------- | ----------------------------------- | -------------- |
| 1	  | High             | SQL Injection                       | Remediated     |
| 2	  | High             | Broken Authentication               | Remediated     |
| 3	  | High             | Unrestricted File Upload            | Remediated     |
| 4	  | High             | Inadequate Web and Egress Filtering | Not Remediated |
| 5	  | Medium           | SMB Signing Not Enabled             | Not Remediated |
| 6	  | Low              | Directory Listing Enabled           | Not Remediated |

## Role of the Pentester in Remediation
We not perform remediation on our findings (such as fixing code, patching systems, making changes in Active Directory), implement changes or giving precise remmediation advice. We can serve as trusted advisors by giving general remediation advice on how a specific issue could be fixed.

## Data Retention
After a penetration test concludes, we will have a considerable amount of client-specific data such as scan results, log output, credentials, screenshots, and more. Data retention and destruction requirements may differ from country to country and firm to firm, and procedures surrounding each should be outlined clearly in the contract language of the Scope of Work and the Rules of Engagement.

## Close Out
Once we have delivered the final report, assisted the client with questions regarding remediation, and performed post-remediation testing/issued a new report, we can finally close the project. we should ensure that any systems used to connect to the client's systems or process data have been wiped or destroyed and that any artifacts leftover from the engagement are stored securely (encrypted) per our firm's policy and per contractual obligations to our client.

The final steps would be invoicing the client and collecting payment for services rendered. Finally, it is always good to follow up with a post-assessment client satisfaction survey so the team and management.

## Questions
What designation do we typically give a report when it is first delivered to a client for a chance to review and comment? (One word)
```
> Draft
```
