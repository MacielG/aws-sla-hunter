# Setup Guide

## Quick Start (60 seconds)

```bash
pip install -r requirements.txt
python main.py --setup
python main.py
```

## Step-by-Step Installation

### 1. Clone Repository
```bash
git clone https://github.com/MacielG/aws-sla-hunter.git
cd aws-sla-hunter
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure AWS Credentials

**Option A: Interactive Setup (Recommended)**
```bash
python main.py --setup
```
This wizard:
- Auto-detects existing credentials
- Offers setup for 4 auth methods
- Verifies credentials after setup

**Option B: Manual Setup**
```bash
aws configure
```

**Option C: Environment Variables**
```bash
export AWS_ACCESS_KEY_ID=your_key
export AWS_SECRET_ACCESS_KEY=your_secret
export AWS_DEFAULT_REGION=us-east-1
```

### 4. Run
```bash
python main.py
```

## System Requirements

- Python 3.8 or higher
- AWS account with credentials
- Internet connection
- **Business or Enterprise Support plan** (for AWS Health API)

## Troubleshooting

### "ModuleNotFoundError: No module named 'boto3'"
```bash
pip install -r requirements.txt
```

### "NoCredentialsError: Unable to locate credentials"
```bash
python main.py --setup
# or
aws configure
```

### "SubscriptionRequiredException"
This means you're on free/basic support. See [FREE_TIER_GUIDE.md](FREE_TIER_GUIDE.md).

### "AccessDenied: health:DescribeEvents"
Your IAM user needs these permissions:
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

### AWS CLI not installed

For interactive setup, install AWS CLI:

**macOS:**
```bash
brew install awscli
```

**Windows:**
```
Download: https://awscli.amazonaws.com/AWSCLIV2.msi
Run the installer
```

**Linux:**
```bash
curl "https://awscli.amazonaws.com/awscliv2.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

## Optional: Run Tests

```bash
python test_hunter.py
```

## Next Steps

1. Run `python main.py` to find SLA events
2. If found, visit [awscostguardian.com](https://awscostguardian.com) to automate claiming
3. If errors, check [FREE_TIER_GUIDE.md](FREE_TIER_GUIDE.md) or [AUTHENTICATION.md](AUTHENTICATION.md)

## Need More Help?

- **Authentication:** See [AUTHENTICATION.md](AUTHENTICATION.md)
- **Free Tier:** See [FREE_TIER_GUIDE.md](FREE_TIER_GUIDE.md)
- **General:** See [README.md](README.md)
- **Contributing:** See [CONTRIBUTING.md](CONTRIBUTING.md)
