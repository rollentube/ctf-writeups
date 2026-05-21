# Mailbox Forwarding Audit (Easy)
The security team at Contoso Ltd has received an alert about potential data exfiltration. An employee in the Finance department reported that emails seem to be "leaking" to external parties.

Your task is to investigate the inbox rules and mailbox settings to identify any unauthorized forwarding configurations. Review the evidence below to find the suspicious rule and answer the investigation questions.

## Q1.Which user has a suspicious inbox forwarding rule configured
See the `Inbox Rules`:

| #   | Display Name         | User                      | Conditions                            | Actions                                                     | Enabled | Stop Rules |
| --- | -------------------- | ------------------------- | ------------------------------------- | ----------------------------------------------------------- | ------- | ---------- |
| 3   | Client Notifications | Sarah.Johnson@contoso.com | Subject contains "invoice", "payment" | Forward to sjohnson.backup@gmail.com; Stop processing rules | true    | true       |

## Q2.What external email address is receiving the forwarded emails?
See Q1.

## Q3.What keywords trigger the forwarding rule?
See Q1.

## Q4.From which IP address was the malicious rule created?
Details for the corresponding entry in the `Unified Audit Log` tab:
```
Date (UTC)
2025-11-14T13:19:42Z

IP Address
185.220.101.45

Users
Sarah.Johnson@contoso.com

Activity
Created new inbox rule in Outlook web app

Item
Client Notifications

Details
Admin Units

RuleName
Client Notifications

Parameters
[
    {
        "Name": "SubjectContains",
        "Value": "invoice;payment"
    },
    {
        "Name": "ForwardTo",
        "Value": "sjohnson.backup@gmail.com"
    },
    {
        "Name": "StopProcessingRules",
        "Value": "True"
    },
    {
        "Name": "Name",
        "Value": "Client Notifications"
    }
]

CreationTime
2025-11-14T13:19:42Z

Id
a1b2c3d4-0006-0000-0000-000000000006

Operation
New-InboxRule

OrganizationId
a8d4e21f-3b92-4c71-9f6a-1c2d3e4f5a6b

RecordType
1

UserKey
Sarah.Johnson@contoso.com

UserType
0

Version
1

Workload
Exchange

ClientIP
185.220.101.45

UserId
Sarah.Johnson@contoso.com

ResultStatus
True

ObjectId
Client Notifications
```

Differs from other IPs, matches to the suspicious inbox rule.

## Q5.Which Anti-spam policy setting should be configured to prevent unauthorized external forwarding?
```
> Automatic forwarding = Off
```

The **Anti-Spam Policies** tab reveals that the **Executives Outbound Policy** (Priority 1) and **Marketing Outbound Policy** (Priority 3) both have "Automatic forwarding" explicitly set to **"On - Forwarding is enabled"**. In Microsoft 365, lower priority numbers are evaluated first and take precedence. Since the Executives policy (Priority 1) is evaluated before the default policy (Priority "Lowest"), users covered by it can forward emails externally regardless of the default policy's "Automatic - System-controlled" setting, which blocks forwarding by default. Setting "Automatic forwarding" to **"Off"** on all outbound anti-spam policies blocks forwarding at the transport level, regardless of inbox rules. The other options address different concerns: sending limits control volume, over-limit actions handle existing blocks, and bulk email thresholds filter inbound spam.