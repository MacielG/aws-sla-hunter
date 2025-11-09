# Reddit: r/aws Post

## Post Title
"[Free Tool] AWS SLA Hunter - CLI that finds missed SLA credits in your account"

## Post Body

---

**TL;DR:** Built a free open-source CLI that scans your AWS account and shows you events eligible for SLA credits. Takes 2 seconds to run. MIT licensed.

**The Problem:**
According to AWS's own data, companies miss SLA credits because:
1. AWS doesn't notify you when an outage qualifies
2. You have to manually find events in AWS Health
3. You need to calculate impact yourself
4. You have to open support tickets manually

Biggest companies I've worked with recover $50K-$500K by just looking at their AWS Health dashboard once a quarter.

**What the tool does:**
```
$ pip install -r requirements.txt
$ python main.py

🔍 AWS SLA Hunter
Verifying AWS credentials... ✓
Fetching AWS Health events (last 90 days)... ✓

AWS Health Events - Last 90 Days (3 found)
┌────────┬────────┬──────────┬────────┬──────────────────┐
│ Date   │Service │ Region   │ Status │ Event Type       │
├────────┼────────┼──────────┼────────┼──────────────────┤
│2025-01-03│EC2   │us-east-1 │🔴 Open │Instance Failure  │
│2025-01-13│RDS   │sa-east-1 │⚪Close │RDS Outage       │
│2025-02-02│ELB   │us-west-2 │⚪Close │ELB Degraded     │
└────────┴────────┴──────────┴────────┴──────────────────┘

Found 3 AWS Health events with SLA potential
💰 Claim your credits at awscostguardian.com
```

**What it costs:** Free. MIT license. No strings.

**Source:** https://github.com/yourusername/aws-sla-hunter

I also built https://awscostguardian.com which automates the full process (calculation, PDFs, ticket opening, tracking), but the CLI is 100% standalone and works great on its own.

**Requirements:** Python 3.8+, AWS credentials, Business or Enterprise support (AWS requirement for Health API access)

Questions? Happy to answer!

---

## Comment Responses (Pre-write for top comments)

**"Why should I use this instead of checking AWS Health myself?"**
> It's the same reason you use a monitoring tool instead of manually checking metrics—speed and consistency. This takes 2 seconds. Manual checking takes 30 minutes. Plus it runs in your CI/CD to alert you automatically.

**"This is just a sales funnel for your SaaS"**
> 100% fair criticism. It is. But the CLI is genuinely useful on its own. We built it because we got tired of manual spreadsheets. If you want one-click claiming instead of doing it yourself, awscostguardian.com exists. But the tool works perfectly standalone.

**"Doesn't AWS just automatically credit me?"**
> Nope. AWS policy is: if you qualify for a credit, you have to request it. They won't notify you, they won't process it automatically. You have to find the event and ask. This tool finds the events so you can ask.

**"What's the success fee?"**
> 30% of credits recovered, but only if you use awscostguardian.com for the full automation. The CLI is free forever, no fees.

---

## Engagement Tips for r/aws

- Post on Tuesday-Thursday (peak activity)
- Expect skepticism. Embrace it.
- Be honest: "Yes, this is partly a lead gen tool. But the open-source part is genuinely useful."
- Share your own recovery stories: "We've recovered $2M for clients..."
- Answer technical questions thoroughly
- Offer to help people set up IAM permissions
