# Sign-In Investigation
## Mission Briefing
### Training Exercise

Welcome to your first investigation training exercise. Before you can handle real security incidents, you need to know your way around the Microsoft Entra ID sign-in logs — the single most important data source for identity-based investigations.

Your Security Operations lead has pulled 5 days of sign-in logs from the **Blue Comet Technologies** tenant. Your task is to explore the logs, click into individual entries, and answer questions about what you find in each tab of the detail panel.

### Your Objectives

1. **Filter and Navigate** — Use filters to isolate specific users and identify patterns in their sign-in activity
2. **Spot Suspicious Activity** — Analyze sign-in locations, times, and statuses to identify potential compromises
3. **Explore the Detail Panel** — Dig into Device Info, Authentication methods, and Conditional Access results
4. **Understand Policy Enforcement** — Learn the difference between enabled, disabled, and report-only Conditional Access policies and what their results mean
5. **Know Your Tools** — Understand practical limitations like log retention that impact real investigations


## Investigation Questions
### Q1. Where does it look like James Wilson usually signs in from? (Tip: Use Filters)

Filter for user `james.wilson@bluecomet.io`

| Date (UTC)             | Request ID                           | User                      | Application        | Status  | IP address    | Location       |
| ---------------------- | ------------------------------------ | ------------------------- | ------------------ | ------- | ------------- | -------------- |
| Feb 13, 2026, 16:45:20 | 9a1b2c3d-0001-4000-8000-000000000031 | james.wilson@bluecomet.io | Entra Admin Center | Success | 198.51.100.22 | Denver, CO, US |
| Feb 13, 2026, 08:10:22 | 9a1b2c3d-0001-4000-8000-000000000028 | james.wilson@bluecomet.io | Microsoft Teams    | Success | 198.51.100.22 | Denver, CO, US |
| Feb 13, 2026, 08:10:22 | 9a1b2c3d-0001-4000-8000-000000000028 | james.wilson@bluecomet.io | Microsoft Teams    | Success | 198.51.100.22 | Denver, CO, US |
| Feb 12, 2026, 16:55:30 | 9a1b2c3d-0001-4000-8000-000000000020 | james.wilson@bluecomet.io | Azure Portal       | Success | 198.51.100.22 | Denver, CO, US |
| Feb 11, 2026, 14:05:50 | 9a1b2c3d-0001-4000-8000-000000000014 | james.wilson@bluecomet.io | SharePoint Online  | Success | 198.51.100.22 | Denver, CO, US |
| Feb 11, 2026, 08:52:14 | 9a1b2c3d-0001-4000-8000-000000000010 | james.wilson@bluecomet.io | Entra Admin Center | Success | 198.51.100.22 | Denver, CO, US |
| Feb 10, 2026, 15:48:09 | 9a1b2c3d-0001-4000-8000-000000000007 | james.wilson@bluecomet.io | Microsoft Teams    | Success | 198.51.100.22 | Denver, CO, US |
| Feb 10, 2026, 08:45:10 | 9a1b2c3d-0001-4000-8000-000000000002 | james.wilson@bluecomet.io | Azure Portal       | Success | 198.51.100.22 | Denver, CO, US |

```
> Denver
```

### Q2. Review the sign in logs. Which user appears like they could potentially have been breached?

Filter for user `sarah.chen@bluecomet.io`:

|Date (UTC)|Request ID|User|Application|Status|IP address|Location|
|---|---|---|---|---|---|---|
|Feb 14, 2026, 11:55:05|9a1b2c3d-0001-4000-8000-000000000034|sarah.chen@bluecomet.io|Outlook Web App|Success|198.51.100.22|Denver, CO, US|
|Feb 14, 2026, 08:00:15|9a1b2c3d-0001-4000-8000-000000000032|sarah.chen@bluecomet.io|Microsoft Teams|Success|198.51.100.22|Denver, CO, US|
|Feb 13, 2026, 14:30:05|9a1b2c3d-0001-4000-8000-000000000030|sarah.chen@bluecomet.io|Outlook Web App|Success|198.51.100.22|Denver, CO, US|
|Feb 13, 2026, 02:55:18|9a1b2c3d-0001-4000-8000-000000000028|sarah.chen@bluecomet.io|Microsoft Teams|Success|198.51.100.22|Denver, CO, US|
|Feb 13, 2026, 02:41:55|9a1b2c3d-0001-4000-8000-000000000027|sarah.chen@bluecomet.io|Outlook Web App|Success|41.58.120.73|London, GB|
|Feb 13, 2026, 02:28:10|9a1b2c3d-0001-4000-8000-000000000026|sarah.chen@bluecomet.io|SharePoint Online|Success|41.58.120.73|London, GB|
|Feb 13, 2026, 02:15:22|9a1b2c3d-0001-4000-8000-000000000025|sarah.chen@bluecomet.io|Microsoft Graph API|Success|41.58.120.73|London, GB|
|Feb 13, 2026, 02:03:44|9a1b2c3d-0001-4000-8000-000000000024|sarah.chen@bluecomet.io|Outlook Web App|Success|41.58.120.73|London, GB|
|Feb 13, 2026, 01:58:55|9a1b2c3d-0001-4000-8000-000000000023|sarah.chen@bluecomet.io|Outlook Web App|Failure|41.58.120.73|London, GB|
|Feb 13, 2026, 01:52:38|9a1b2c3d-0001-4000-8000-000000000022|sarah.chen@bluecomet.io|Outlook Web App|Failure|41.58.120.73|London, GB|
|Feb 13, 2026, 01:47:12|9a1b2c3d-0001-4000-8000-000000000021|sarah.chen@bluecomet.io|Outlook Web App|Failure|41.58.120.73|London, GB|
|Feb 12, 2026, 13:20:38|9a1b2c3d-0001-4000-8000-000000000019|sarah.chen@bluecomet.io|SharePoint Online|Success|198.51.100.22|Denver, CO, US|
|Feb 12, 2026, 07:55:03|9a1b2c3d-0001-4000-8000-000000000016|sarah.chen@bluecomet.io|Outlook Web App|Success|198.51.100.22|Denver, CO, US|
|Feb 11, 2026, 16:30:12|9a1b2c3d-0001-4000-8000-000000000015|sarah.chen@bluecomet.io|Microsoft Teams|Success|198.51.100.22|Denver, CO, US|
|Feb 11, 2026, 10:15:33|9a1b2c3d-0001-4000-8000-000000000012|sarah.chen@bluecomet.io|Outlook Web App|Success|198.51.100.22|Denver, CO, US|
|Feb 11, 2026, 08:05:27|9a1b2c3d-0001-4000-8000-000000000009|sarah.chen@bluecomet.io|Microsoft Teams|Success|198.51.100.22|Denver, CO, US|
|Feb 10, 2026, 19:10:33|9a1b2c3d-0001-4000-8000-000000000008|sarah.chen@bluecomet.io|Outlook Web App|Success|76.25.112.4|Denver, CO, US|
|Feb 10, 2026, 13:22:41|9a1b2c3d-0001-4000-8000-000000000006|sarah.chen@bluecomet.io|SharePoint Online|Success|198.51.100.22|Denver, CO, US|
|Feb 10, 2026, 09:15:55|9a1b2c3d-0001-4000-8000-000000000003|sarah.chen@bluecomet.io|Outlook Web App|Success|198.51.100.22|Denver, CO, US|
|Feb 10, 2026, 08:12:33|9a1b2c3d-0001-4000-8000-000000000001|sarah.chen@bluecomet.io|Microsoft Teams|Success|198.51.100.22|Denver, CO, US|

We can see a location jump, as well some failed logins. Also GB is not matching the locations of all other logins. But this could be normal.

```
> sarah.chen@bluecomet.io
```

### Q3. Based on the sign-in logs, what type of indicator would lead you to believe a user is compromised?
```
> Impossible Travel
```

### Q4. What is the device name associated with david.kim@bluecomet.io's sign-ins?

Adding `DEVICE NAME` column:

|                        |                                      |                        |                 |         |            |                       |               |
| ---------------------- | ------------------------------------ | ---------------------- | --------------- | ------- | ---------- | --------------------- | ------------- |
| Feb 10, 2026, 11:05:18 | 9a1b2c3d-0001-4000-8000-000000000005 | david.kim@bluecomet.io | Microsoft Teams | Success | 192.0.2.88 | San Francisco, CA, US | BLUCOMET-DK04 |

```
> BLUCOMET-DK04
```

### Q5. What MFA method did user james.wilson use on Feb 10, 2026, 08:45:10?
Open up the `Authentication` info of the entry:

Authentication policies applied

| Date                   | Authentication method   | Authentication step | Succeeded | Result detail         | Requirement                |
| ---------------------- | ----------------------- | ------------------- | --------- | --------------------- | -------------------------- |
| Feb 10, 2026, 08:45:10 | Password                | Step 1              | Yes       | Password validated    | Multifactor authentication |
| Feb 10, 2026, 08:45:10 | Microsoft Authenticator | Step 2              | Yes       | Notification approved |                            |
```
> Microsoft Authenticator
```

### Q6. How many ENABLED Conditional Access policies are configured in the Blue Comet Technologies tenant?

Open the `Conditional Access` tab from an entry:

| Policy name                             | Grant controls                     | Session controls | Result      |
| --------------------------------------- | ---------------------------------- | ---------------- | ----------- |
| Require MFA for All Users               | Require multifactor authentication | —                | Success     |
| Block Legacy Authentication             | Block                              | —                | Not applied |
| Block Sign-ins from High Risk Countries | Block                              | —                | Disabled    |
| Require App Protection Policy           | Require app protection policy      | —                | Success     |

There are four policies, but one is disabled.
```
> 3
```

### Q7. What conditional access policy would have blocked a successful sign in from London?
The **Report-only** tab on successful London sign-ins shows that the **Require Compliant Device** policy has a result of "Report-Only: Failure". This means the policy matched the sign-in conditions and the user **failed** to meet the requirements, but because the policy is in report-only mode, it only logged the result without actually blocking access. If this policy were enforced, the sign-in would have been blocked. Report-only mode is commonly used to test policies before enabling them in production.

```
> Require Compliant Device
```

### Q8. As an investigator, knowing how far back you can search is critical. How long does Entra ID retain sign-in logs by default with a P1/P2 license?
Microsoft Entra ID retains sign-in logs for **30 days** by default with a P1 or P2 license (7 days for free tier). This is a critical limitation for investigators. If you need to look further back, you must export logs to a **Log Analytics workspace**, **SIEM**, or **storage account** before they age out. Knowing your retention window is essential for scoping any investigation.

```
> 30 days
```
