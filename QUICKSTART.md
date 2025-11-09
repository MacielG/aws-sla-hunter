# AWS SLA Hunter - Quick Start

## 60 Seconds to First Run

### 1. Install
```bash
pip install -r requirements.txt
```

### 2. Configure AWS
```bash
aws configure
# Enter your credentials when prompted
```

### 3. Run
```bash
python main.py
```

### 4. See Results
```
🔍 AWS SLA Hunter
→ Verifying AWS credentials... ✓
→ Fetching AWS Health events (last 90 days)... ✓

AWS Health Events - Last 90 Days (3 found)
[Beautiful table with events]

💰 CLAIM YOUR MISSING SLA CREDITS
Visit https://awscostguardian.com
```

---

## That's It!

The CLI found events eligible for SLA credits.

### Next Steps:
1. **Manual:** Open AWS support tickets yourself
2. **Automated:** Visit https://awscostguardian.com for one-click claiming

---

## Troubleshooting

| Error | Solution |
|-------|----------|
| `ModuleNotFoundError: No module named 'boto3'` | Run: `pip install -r requirements.txt` |
| `NoCredentialsError` | Run: `aws configure` or set AWS_ACCESS_KEY_ID env var |
| `SubscriptionRequiredException` | Upgrade to Business support: https://aws.amazon.com/premiumsupport/ |
| `AccessDenied` | Ask admin to grant IAM permissions (see README.md) |

---

## Common Questions

**Q: Is this free?**  
A: Yes. MIT license. No fees.

**Q: What's the catch?**  
A: No catch on the CLI. We offer a SaaS platform (awscostguardian.com) that automates the whole process for a success fee.

**Q: Does it steal my data?**  
A: No. It's open source. You can read every line of code. No tracking, no calls home.

**Q: How accurate are the results?**  
A: 100% from AWS Health API. We just display what AWS tells us.

**Q: Can I integrate with X?**  
A: CLI outputs text. JSON/CSV export coming soon. See GitHub issues for feature requests.

---

## Full Documentation

- **Installation:** See `SETUP.md`
- **Features:** See `README.md`
- **Testing:** Run `python test_hunter.py`
- **Launching to GitHub:** See `LAUNCH_PLAN.md`

---

**Happy hunting!** 🔍💰
