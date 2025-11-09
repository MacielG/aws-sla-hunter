# Authentication Guide

## Quick Start

```bash
python main.py --setup
```

This interactive wizard auto-detects credentials and guides you through setup.

## Authentication Methods

The tool supports 4 methods (auto-detected in order):

### 1. AWS SSO (Recommended) ⭐

Browser-based login with automatic token refresh. Most secure.

**Setup:**
```bash
aws configure sso
# Follow browser prompts
```

**Pros:** Most secure, MFA support, automatic refresh  
**Cons:** Requires AWS CLI installed, first login needs browser  
**Best for:** Production systems, teams, enterprise

---

### 2. AWS CLI Configuration

Manual credentials entry.

**Setup:**
```bash
aws configure
# Enter Access Key, Secret Key, Region, Format
```

**Pros:** Simple, widely compatible  
**Cons:** Credentials stored on disk  
**Best for:** Local development, testing

---

### 3. Environment Variables

Use .env file or shell environment.

**Option A - .env file:**
```bash
python main.py --setup
# Choose "Environment Variables"
```

Creates `.env`:
```
AWS_ACCESS_KEY_ID=your_key
AWS_SECRET_ACCESS_KEY=your_secret
AWS_DEFAULT_REGION=us-east-1
```

**Option B - Shell:**
```bash
export AWS_ACCESS_KEY_ID=your_key
export AWS_SECRET_ACCESS_KEY=your_secret
export AWS_DEFAULT_REGION=us-east-1
python main.py
```

**Pros:** Works everywhere, good for CI/CD  
**Cons:** Credentials visible in files/history  
**Best for:** Development, CI/CD pipelines

**⚠️ Security Warning:**
- Never commit `.env` with real credentials
- Add `.env` to `.gitignore`
- Use rotating/temporary credentials

---

### 4. IAM Role (EC2/ECS/Lambda)

Automatic credentials from AWS metadata service.

**Setup:**
Attach IAM role to EC2, task role to ECS, or execution role to Lambda. Then just run:

```bash
python main.py
# Credentials loaded automatically!
```

**Pros:** Most secure, automatic rotation, no setup needed  
**Cons:** Only works on AWS services, requires IAM configuration  
**Best for:** Production on AWS

---

## How Boto3 Searches for Credentials

The tool searches in this order:

1. Environment Variables (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`)
2. IAM Role (EC2/ECS/Lambda metadata)
3. Credentials File (`~/.aws/credentials`)
4. Config File (`~/.aws/config` for SSO)

The tool shows which method was detected:
```
→ Verifying AWS credentials... ✓ (AWS SSO)
→ Verifying AWS credentials... ✓ (Environment Variables)
→ Verifying AWS credentials... ✓ (IAM Role)
```

## Troubleshooting

### "No credentials found"
```bash
python main.py --setup
```

### "Access Denied: health:DescribeEvents"
Your IAM needs:
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

### "AWS Health API requires Business or Enterprise Support"
See [FREE_TIER_GUIDE.md](FREE_TIER_GUIDE.md).

### Credentials expired
**For SSO:**
```bash
aws sso login --profile your-profile-name
```

**For other methods:**
Update in AWS IAM Console and run:
```bash
aws configure
```

## Security Best Practices

### ✅ DO:
- Use AWS SSO for production
- Use IAM roles on AWS services
- Rotate credentials regularly (every 90 days)
- Use temporary/short-lived credentials
- Keep `.env` in `.gitignore`

### ❌ DON'T:
- Hardcode credentials in code
- Commit `.env` with credentials
- Use root AWS account credentials
- Share credentials between people
- Use long-lived access keys
- Store credentials in version control

## For Different Scenarios

### Local Development
```bash
aws configure sso
# or
python main.py --setup
```

### CI/CD Pipeline
```bash
export AWS_ACCESS_KEY_ID=${{ secrets.AWS_ACCESS_KEY_ID }}
export AWS_SECRET_ACCESS_KEY=${{ secrets.AWS_SECRET_ACCESS_KEY }}
python main.py
```

### EC2/Lambda/ECS Production
```bash
# Attach IAM role, then:
python main.py
```

### Docker
```dockerfile
FROM python:3.8
RUN pip install -r requirements.txt
VOLUME ["/root/.aws"]
CMD ["python", "main.py"]
```

Run with:
```bash
docker run -v ~/.aws:/root/.aws my-sla-hunter
```

## FAQs

**Q: Which method is most secure?**  
A: AWS SSO, then IAM Role. Avoid long-lived access keys.

**Q: Can I use temporary credentials?**  
A: Yes! Set `AWS_SESSION_TOKEN` env var.

**Q: Does it support multiple accounts?**  
A: Use cross-account IAM roles or SSO.

**Q: How often should I rotate credentials?**  
A: AWS recommends every 90 days minimum.

**Q: Can I use different profiles?**  
A: For SSO: `export AWS_PROFILE=profile-name`

## Next Steps

After setup:
```bash
python main.py
```

If you found SLA events:
- Visit [awscostguardian.com](https://awscostguardian.com) to automate claiming

If error about support plan:
- See [FREE_TIER_GUIDE.md](FREE_TIER_GUIDE.md)

Questions? Open an issue on GitHub: https://github.com/MacielG/aws-sla-hunter/issues
