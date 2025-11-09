# Reddit: r/devops Post

## Post Title
"Built a DevOps tool to find missed AWS SLA credits (open-source CLI)"

## Post Body

---

**Context:** As a DevOps engineer, you're probably responsible for monitoring cloud costs and service reliability. This tool bridges a gap I noticed: no one's checking AWS SLA credits automatically.

**What's the use case?**
When AWS services go down, you get:
- CloudWatch alerts (for monitoring)
- AWS Health events (for SLA eligibility)
- But no automatic way to connect them → "which outages should we claim credits for?"

This CLI solves that. It scans AWS Health and shows you in 2 seconds which events might qualify for SLA credits.

**The tool:**
```bash
$ python main.py
→ Verifying AWS credentials... ✓
→ Fetching AWS Health events... ✓

AWS Health Events (3 found)
- EC2 instance failure in us-east-1 (Open)
- RDS outage in sa-east-1 (Closed)
- ELB degradation in us-west-2 (Closed)

Found 3 SLA-eligible events
→ Claim at awscostguardian.com
```

**Why DevOps needs this:**
1. **Incident correlation** - Link outages in your monitoring to SLA events
2. **Cost recovery** - Automate credit recovery to reduce cloud spend
3. **Compliance** - Track which SLA events were claimed/missed
4. **Automation** - Run in CI/CD to get daily alerts

**Tech stack:**
- Python 3.8+ (simple, dependency-light)
- boto3 (AWS SDK)
- rich (beautiful terminal output)
- fully tested with mock AWS data

**Release:** MIT license, GitHub: https://github.com/yourusername/aws-sla-hunter

For full DevOps automation (calculation, PDF, ticket opening, tracking), we have https://awscostguardian.com, but the CLI works standalone.

---

## Expected Objections & Responses

**"This feels like a sales funnel"**
> 100% transparent: it is. But the open-source tool is genuinely useful on its own. We built it because we needed it internally. The SaaS version is for teams who want full automation.

**"Can I integrate this into Terraform/Ansible?"**
> Absolutely! The CLI outputs clean data. We're working on JSON/CSV export. Add to your monitoring pipeline.

**"Does this work with multiple AWS accounts?"**
> Not yet in the CLI (scope creep risk). The SaaS version does multi-account automatically.

**"How often should I run this?"**
> Once a month is good for finding recent events. Integrate into your monitoring to check daily.

**"What if we already claimed these credits?"**
> The tool just shows events from AWS Health. AWS Health is the source of truth. If you already claimed them, they'll still show (no state tracking in the CLI).

---

## Posting Strategy for r/devops

- Post on Tuesday-Wednesday (peak activity)
- Lead with the **DevOps problem**, not the sales pitch
- Show the **simplicity** of the tool
- Highlight **integration potential** with existing DevOps workflows
- Be honest about the business model
- Offer to help with **IAM permissions** and **setup troubleshooting**
- Share **real recovery stories** (anonymized)

---

## Potential Follow-Up Posts (1-2 weeks later)

1. "AWS SLA Hunting in CI/CD - Automate credit detection"
   - How to integrate aws-sla-hunter into GitHub Actions
   - Slack/email alerting when new events found
   - Cost tracking over time

2. "Multi-cloud SLA monitoring - how to handle Azure/GCP"
   - AWS SLA Hunter for AWS
   - Azure Service Health for Azure
   - Google Cloud Status for GCP
   - Unified monitoring approach

3. "Case study: How we recovered $500K in missed AWS credits"
   - Real numbers (anonymized)
   - Timeline of discovery
   - Process improvements made
   - Tools used (including aws-sla-hunter)
