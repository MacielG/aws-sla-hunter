# AWS SLA Hunter - Setup Guide

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure AWS Credentials
```bash
# Option A: Using AWS CLI
aws configure

# Option B: Using environment variables
export AWS_ACCESS_KEY_ID=your_key
export AWS_SECRET_ACCESS_KEY=your_secret
export AWS_DEFAULT_REGION=us-east-1
```

### 3. Run the Hunter
```bash
python main.py
```

### 4. (Optional) Generate Screenshot
```bash
python test_hunter.py --screenshot
```

### 5. (Optional) Run Tests
```bash
python test_hunter.py
```

## Requirements

### AWS Account
- Business or Enterprise support plan (required by AWS for Health API access)
- IAM credentials with these permissions:
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

### System Requirements
- Python 3.8 or higher
- pip package manager
- Internet connection (to reach AWS API)

## Troubleshooting

### "ModuleNotFoundError: No module named 'boto3'"
```bash
pip install -r requirements.txt
```

### "NoCredentialsError: Unable to locate credentials"
```bash
aws configure
# or set environment variables
```

### "SubscriptionRequiredException: AWS Health API requires Business or Enterprise Support"
- Upgrade your AWS support plan at: https://aws.amazon.com/premiumsupport/
- Or contact AWS support to enable Health API

### "AccessDenied: User is not authorized to perform: health:DescribeEvents"
- Ask your AWS administrator to add the IAM permissions listed above
- See: https://docs.aws.amazon.com/health/latest/ug/security_iam_service-with-iam.html

## Next Steps

1. **Run aws-sla-hunter** to find events
2. **Review results** in the table output
3. **Claim credits** through AWS support (manual) or awscostguardian.com (automated)

## Support

- GitHub Issues: https://github.com/yourusername/aws-sla-hunter/issues
- AWS Health Docs: https://docs.aws.amazon.com/health/
- AWS SLA Info: https://aws.amazon.com/service-level-agreement/

## More Information

See README.md for full documentation.
