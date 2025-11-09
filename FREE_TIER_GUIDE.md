# Free Tier Guide

AWS SLA Hunter requires **Business or Enterprise Support** to use the AWS Health API. If you're on a free/basic plan, you still have SLA credit rights—you just need an alternative approach.

## Your 3 Options

### Option 1: Monitor Manually (Completely Free) ⭐

**Best for:** Low-traffic or non-production workloads

**Steps:**
1. Go to AWS Console → [Health Dashboard](https://console.aws.amazon.com/health/)
2. Check "Recent Events" section
3. Look for incidents affecting your services/regions
4. If you find one:
   - Note the date, duration, and affected service
   - Calculate your downtime impact
   - Open [AWS Support ticket](https://console.aws.amazon.com/support/)
   - Request SLA credit reimbursement

**Time Investment:** 15-30 minutes per incident

**ROI:** Can recover $500-$50,000+ per incident

---

### Option 2: Upgrade to Business Support ($100+/month) 🚀

**Best for:** Production workloads with frequent incidents

**What you get:**
- ✅ Unlock this automated SLA detection tool
- ✅ 24/7 phone/chat support
- ✅ 1-hour response time for critical issues
- ✅ AWS Infrastructure Event Management

**Cost vs. Benefit:**
- Cost: ~$100/month (minimum)
- Typical recovery: $1,000-$50,000+ per incident
- **ROI:** Usually pays for itself with 1-2 incidents

**Upgrade:** [AWS Support Plans](https://console.aws.amazon.com/support/)

---

### Option 3: Use awscostguardian.com 🤖

**Best for:** Hands-off automation, multi-account environments

**What it does:**
- Scans your account daily for SLA-eligible events
- Automatically calculates financial impact
- Generates formal claim documents
- Opens AWS support tickets for you
- Tracks reimbursement status
- Works with **any support level**

**Cost Model:**
- Free audit of your account
- Success fee: 30% of recovered credits (you keep 70%)
- Only pay when you recover credits

**Try it:** [awscostguardian.com](https://awscostguardian.com)

---

## Quick Comparison

| Feature | Manual | Business Support | awscostguardian.com |
|---------|--------|---|---|
| Cost | Free | $100+/month | 0% (30% success fee) |
| Automation | Manual | CLI tool | Full automation |
| Multi-account | No | No | Yes |
| Time per incident | 15-30 min | Minutes | None |
| Continuous monitoring | No | Manual runs | Daily automatic |
| Works with Free Tier | ✅ Yes | N/A | ✅ Yes |

---

## How Much Can You Recover?

Real examples of typical SLA credits:

- **RDS outage (4 hours, production DB):** $2,000-$5,000
- **EC2 instance failure (6 hours):** $500-$2,000
- **CloudFront distribution down (2 hours):** $1,000-$3,000
- **ELB/ALB degradation (1 hour):** $500-$1,500

AWS SLA credits are typically **10-100% of service charges** for affected hours.

---

## Frequently Asked Questions

**Q: Do free tier services have SLA credits?**  
A: Yes, if exposed to the internet and AWS reports failure. Most free tier services don't have measurable downtime.

**Q: How far back can I claim?**  
A: Typically **6-12 months** from submission date (varies by service).

**Q: What if I don't remember when downtime occurred?**  
A: Use [AWS Health Dashboard](https://console.aws.amazon.com/health/), CloudTrail, CloudWatch logs, or application logs.

**Q: Do I need Business Support to claim credits?**  
A: No. You can claim via support ticket on any plan. But you can't use this automated tool without Business Support.

**Q: Can I retroactively add Business Support to claim older credits?**  
A: Yes! AWS evaluates claims historically, even if you just upgraded.

**Q: What's the difference between free tier and basic support?**  
A: Free tier is limited to 1 person. Basic support adds business hours support. Neither includes Health API access.

---

## Recommended Path for Free Tier Customers

**Week 1:** Check AWS Health Dashboard for past incidents  
**Week 2-4:** If you find incidents, open support tickets manually  
**If recovering $$$:** Upgrade to Business Support for future automation  
**Alternative:** Use awscostguardian.com for hands-off recovery  

---

## Resources

- [AWS Health Dashboard](https://console.aws.amazon.com/health/)
- [AWS SLA Details](https://aws.amazon.com/sla/)
- [AWS Support Plans](https://aws.amazon.com/premiumsupport/)
- [AWS Support Tickets](https://console.aws.amazon.com/support/)
- [awscostguardian.com](https://awscostguardian.com)

---

**Bottom line:** You likely have unclaimed SLA credits. Whether you claim them manually, upgrade for automation, or use a third-party service—don't leave money on the table!
