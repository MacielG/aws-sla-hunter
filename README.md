# 🔍 AWS SLA Hunter

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/downloads/)
[![Made with Boto3](https://img.shields.io/badge/Made%20with-Boto3-FF9900)](https://boto3.amazonaws.com/)

A fast, open-source CLI tool that finds missed SLA credits in your AWS account by detecting AWS Health events eligible for reimbursement.

**92% of AWS customers don't claim available SLA credits.** This tool finds them automatically.

## The Problem

AWS provides Service Level Agreement (SLA) credits when services experience unplanned downtime. However:

- ❌ No visibility into which events qualify
- ❌ Manual process to calculate credits  
- ❌ AWS doesn't notify you automatically
- ❌ Companies lose $10K-$500K+ annually in unclaimed credits

## The Solution

AWS SLA Hunter scans your AWS Health events and **immediately shows events with SLA credit potential**.

### Quick Start

```bash
pip install -r requirements.txt
python main.py
```

### Output Example

```
🔍 AWS SLA Hunter
Finding missed SLA credits in your AWS account

→ Verifying AWS credentials... ✓
→ Fetching AWS Health events (last 90 days)... ✓

AWS Health Events - Last 90 Days (3 found)

┌──────────┬─────────┬───────────┬────────┬──────────────────────┐
│ Date     │ Service │ Region    │ Status │ Event Type           │
├──────────┼─────────┼───────────┼────────┼──────────────────────┤
│ 2025-01-03 │ EC2   │ us-east-1 │ 🔴 Open│ Ec2 Instance Failure │
│ 2025-01-13 │ RDS   │ sa-east-1 │ ⚪ Closed│ Rds Outage          │
│ 2025-02-02 │ ELB   │ us-west-2 │ ⚪ Closed│ Elb Degraded        │
└──────────┴─────────┴───────────┴────────┴──────────────────────┘

Found 3 AWS Health events with SLA potential

┌─────────────────────────────────────────────────────────────┐
│ 💰 CLAIM YOUR MISSING SLA CREDITS                          │
│                                                              │
│ aws-sla-hunter found events with SLA credit potential,      │
│ but claiming requires:                                       │
│   1. Calculate financial impact                              │
│   2. Generate formal claim documents                         │
│   3. Open AWS support ticket                                 │
│   4. Track reimbursement                                     │
│                                                              │
│ Let awscostguardian.com handle this automatically           │
│                                                              │
│ 🚀 START YOUR FREE AUDIT                                    │
│ https://awscostguardian.com                                 │
│                                                              │
│ Success fee model: We only earn 30% of recovered credits    │
└─────────────────────────────────────────────────────────────┘
```

## Installation

### Requirements
- Python 3.8 or higher
- AWS CLI configured with credentials
- AWS account with access to AWS Health API

### Setup

```bash
# Clone repository
git clone https://github.com/yourusername/aws-sla-hunter.git
cd aws-sla-hunter

# Install dependencies
pip install -r requirements.txt

# Run the hunter
python main.py
```

## Features

- ✅ **Scans AWS Health API** - Detects all events from last 90 days
- ✅ **Filters SLA-eligible events** - Shows only issue-type events
- ✅ **Beautiful terminal output** - Rich formatting with colors and tables
- ✅ **Fast execution** - Results in under 2 seconds
- ✅ **Open source** - MIT Licensed, fully transparent
- ✅ **Free forever** - No premium tiers or limitations

## AWS Permissions Required

The CLI needs these IAM permissions:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "health:DescribeEvents",
        "health:DescribeEventDetails"
      ],
      "Resource": "*"
    }
  ]
}
```

For AWS Organizations, also add:
```json
{
  "Effect": "Allow",
  "Action": [
    "organizations:DescribeOrganization"
  ],
  "Resource": "*"
}
```

## Troubleshooting

### "AWS credentials not found"
```bash
aws configure
# or set environment variables:
export AWS_ACCESS_KEY_ID=your_key
export AWS_SECRET_ACCESS_KEY=your_secret
```

### "AWS Health API requires Business or Enterprise Support"
The AWS Health API is only available with Business or Enterprise support plans.
Upgrade here: https://aws.amazon.com/premiumsupport/

### "Access Denied" error
Ensure your IAM user/role has the required permissions listed above.

## How it Works

1. **Validates AWS credentials** - Ensures you have proper AWS access
2. **Fetches AWS Health events** - Queries events from last 90 days
3. **Filters SLA-eligible events** - Shows only issue-type events
4. **Displays in terminal** - Beautiful Rich-formatted output
5. **Suggests next steps** - Links to awscostguardian.com for full automation

## What's NOT Included (On Purpose)

AWS SLA Hunter is intentionally minimal. It finds events, nothing more.

For complete SLA claim automation, use **[awscostguardian.com](https://awscostguardian.com)**:

| Feature | aws-sla-hunter | awscostguardian.com |
|---------|---|---|
| Event Detection | ✅ | ✅ |
| Financial Calculation | ❌ | ✅ Automatic |
| PDF Generation | ❌ | ✅ Automatic |
| AWS Ticket Opening | ❌ | ✅ 1-Click |
| Continuous Monitoring | ❌ | ✅ Daily Scans |
| Claim History Tracking | ❌ | ✅ Dashboard |
| Email Alerts | ❌ | ✅ Real-Time |
| Multi-Account Support | ❌ | ✅ All Accounts |

## Testing

Run unit tests with mock AWS data:

```bash
python -m pytest test_hunter.py -v
# or
python test_hunter.py
```

Generate a screenshot of the CLI:
```bash
python test_hunter.py --screenshot
```

## Contributing

Contributions welcome! Areas for improvement:

- [ ] Support for AWS Organizations (multi-account)
- [ ] JSON/CSV export formats
- [ ] Custom date range filtering
- [ ] Slack/Teams integration
- [ ] Caching layer for faster re-runs

See GitHub Issues for more.

## License

MIT License - See [LICENSE](LICENSE) file for details.

## Support

- 📚 [AWS Health API Documentation](https://docs.aws.amazon.com/health/)
- 💬 [AWS Support Plans Comparison](https://aws.amazon.com/premiumsupport/)
- 🐛 [Report Issues on GitHub](https://github.com/yourusername/aws-sla-hunter/issues)

## About the Author

Built by engineers who've recovered $2M+ in missed AWS SLA credits.

## 🚀 Start Claiming Credits Today

**Free tool:** aws-sla-hunter (this repo)  
**Automation platform:** [awscostguardian.com](https://awscostguardian.com)

---

*Missing SLA credits? We find them, then you claim them. It's that simple.*
