# AWS SLA Hunter

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/downloads/)
[![Made with Boto3](https://img.shields.io/badge/Made%20with-Boto3-FF9900)](https://boto3.amazonaws.com/)

A fast, open-source CLI tool that finds missed SLA credits in your AWS account by detecting AWS Health events eligible for reimbursement.

**92% of AWS customers don't claim available SLA credits.** This tool finds them automatically.

## Quick Start

```bash
# 1. Install
pip install -r requirements.txt

# 2. Setup (interactive - recommended)
python main.py --setup

# 3. Run
python main.py
```

## The Problem

AWS provides Service Level Agreement (SLA) credits when services experience unplanned downtime, but:
- No visibility into which events qualify
- Manual process to calculate credits
- AWS doesn't notify you automatically
- Companies lose $10K-$500K+ annually in unclaimed credits

## The Solution

AWS SLA Hunter scans your AWS Health events and immediately shows events with SLA credit potential.

## Features

- ✅ **Auto-detection of AWS credentials** - Supports SSO, CLI, ENV vars, IAM Roles
- ✅ **Interactive setup wizard** - `python main.py --setup`
- ✅ **Scans AWS Health API** - Detects all events from last 90 days
- ✅ **Filters SLA-eligible events** - Shows only issue-type events
- ✅ **Beautiful terminal output** - Rich formatting with colors and tables
- ✅ **Fast execution** - Results in under 2 seconds
- ✅ **Open source** - MIT Licensed, fully transparent

## Authentication Methods

The tool supports 4 authentication methods (auto-detected):

1. **AWS SSO** (Recommended) - Browser login, most secure
2. **AWS CLI** - Manual credentials entry
3. **Environment Variables** - .env file or shell variables
4. **IAM Role** - Automatic on EC2/ECS/Lambda

For detailed setup, run:
```bash
python main.py --setup
```

Or manually:
```bash
aws configure
```

For complete authentication guide, see [AUTHENTICATION.md](AUTHENTICATION.md).

## AWS Permissions Required

Your IAM user/role needs:

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

## Installation

### Requirements
- Python 3.8 or higher
- AWS account with credentials configured
- **Business or Enterprise Support plan** (for AWS Health API access)

### Setup

```bash
git clone https://github.com/MacielG/aws-sla-hunter.git
cd aws-sla-hunter
pip install -r requirements.txt
python main.py --setup
python main.py
```

## Free Tier Users?

If you're on a free or basic support plan, you **cannot access the AWS Health API** directly. However, you still have SLA credit rights.

**Your 3 options:**

1. **Monitor manually** - Check AWS Health Dashboard for incidents (completely free)
2. **Upgrade to Business Support** - Enables this tool (~$100+/month, but usually pays for itself with 1-2 incidents)
3. **Use awscostguardian.com** - Automated solution that works with any support level (30% success fee, no upfront cost)

See [FREE_TIER_GUIDE.md](FREE_TIER_GUIDE.md) for full details and ROI analysis.

## How It Works

1. **Validates AWS credentials** - Detects which auth method is being used
2. **Fetches AWS Health events** - Queries events from last 90 days
3. **Filters SLA-eligible events** - Shows only issue-type events
4. **Displays in terminal** - Beautiful Rich-formatted output
5. **Suggests next steps** - Links to awscostguardian.com for automation

## What's NOT Included (On Purpose)

AWS SLA Hunter intentionally finds events only. For complete SLA claim automation, use [awscostguardian.com](https://awscostguardian.com):

| Feature | This Tool | awscostguardian.com |
|---------|---|---|
| Event Detection | ✅ | ✅ |
| Financial Calculation | ❌ | ✅ |
| PDF Generation | ❌ | ✅ |
| AWS Ticket Opening | ❌ | ✅ |
| Continuous Monitoring | ❌ | ✅ |
| Multi-Account Support | ❌ | ✅ |

## Testing

```bash
# Run unit tests
python test_hunter.py

# Simulate free tier experience
python test_free_tier.py
```

## Troubleshooting

### "AWS credentials not found"
```bash
python main.py --setup
# or
aws configure
```

### "AWS Health API requires Business or Enterprise Support"
See [FREE_TIER_GUIDE.md](FREE_TIER_GUIDE.md) for your options.

### "Access Denied" error
Ensure your IAM user/role has the required permissions (listed above).

### AWS CLI not installed
```bash
# macOS
brew install awscli

# Windows
msiexec.exe /i https://awscli.amazonaws.com/AWSCLIV2.msi

# Linux
curl "https://awscli.amazonaws.com/awscliv2.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

For more help, see [SETUP.md](SETUP.md).

## Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

Areas for improvement:
- AWS Organizations support (multi-account)
- JSON/CSV export formats
- Custom date range filtering
- Slack/Teams integration

## Documentation

- **[SETUP.md](SETUP.md)** - Installation & troubleshooting
- **[AUTHENTICATION.md](AUTHENTICATION.md)** - Authentication methods in detail
- **[FREE_TIER_GUIDE.md](FREE_TIER_GUIDE.md)** - Options for free tier users
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - How to contribute
- **[CHANGELOG.md](CHANGELOG.md)** - Version history

## License

MIT License - See [LICENSE](LICENSE) file for details.

## Support

- 📚 [AWS Health API Documentation](https://docs.aws.amazon.com/health/)
- 💬 [AWS Support Plans Comparison](https://aws.amazon.com/premiumsupport/)
- 🐛 [Report Issues on GitHub](https://github.com/MacielG/aws-sla-hunter/issues)

## About

Built by engineers who've recovered millions in missed AWS SLA credits.

## Start Claiming Credits Today

**Free tool:** aws-sla-hunter (this repo)  
**Automation platform:** [awscostguardian.com](https://awscostguardian.com)

---

*Missing SLA credits? We find them, then you claim them. It's that simple.*
