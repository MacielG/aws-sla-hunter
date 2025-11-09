# Hacker News Post

## Title
"AWS SLA Hunter – Find missing SLA credits in your account (free CLI tool)"

## Comment Template (Post as top comment on your own post)

---

Hi HN! I'm sharing an open-source CLI tool I built after recovering $2M+ in missed AWS SLA credits for clients.

**The problem:** 92% of AWS customers don't claim available SLA credits. When AWS services experience downtime, they're contractually obligated to credit you—but they won't notify you. You have to find it yourself.

**The solution:** AWS SLA Hunter scans your AWS Health events and instantly shows you which ones qualify for SLA credits. It's a 30-second scan that takes 2 seconds to run.

**What it does:**
- Checks AWS Health API for events in last 90 days
- Filters for SLA-eligible incident types
- Shows results in a beautiful terminal table
- Links to awscostguardian.com for automated claiming

**What it doesn't do (on purpose):**
- Calculate financial impact (too complex, needs account context)
- Generate claim documents (needs legal review)
- Open AWS support tickets (you should decide which ones matter)

**The business model:** The CLI is free forever. If you want full automation (calculation, PDF generation, one-click ticket opening, multi-account support), we have awscostguardian.com where we take 30% of recovered credits. No-risk, success-fee only.

**Tech:** ~500 lines of Python, uses boto3 + rich for beautiful output, fully tested with mock AWS data.

MIT licensed, published on GitHub: https://github.com/yourusername/aws-sla-hunter

Would love to hear what you think. If you've recovered SLA credits before, I'd love to hear your story.

---

## Additional Talking Points (if questioned)

- "We built this because spreadsheets suck for monitoring"
- "Yes, you need Business/Enterprise support to access AWS Health API"
- "No, this doesn't cost anything. Free tool, free to use forever"
- "The goal is: find events with this tool, claim them yourself, or let us automate it"

## Posting Tips

- Post Monday-Wednesday 8-10am EST for best HN visibility
- Be prepared for skepticism ("This is just a lead gen tool")
- Don't oversell. Let the tool speak for itself
- Engage genuinely with comments. Answer real technical questions
- If someone asks "why should I use this vs. checking AWS manually?" → Give honest answer: "Automation. This takes 2 seconds. Checking manually takes hours."
