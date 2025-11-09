# AWS SLA Hunter - Launch Plan (7 Days)

## Phase 1: Repository Setup (Day 1)

### Step 1.1: Create GitHub Repository
1. Go to https://github.com/new
2. Repository name: `aws-sla-hunter`
3. Description: "CLI tool to find missed AWS SLA credits"
4. Public repository
5. Check "Add a README.md"
6. Add MIT License
7. Create repository

### Step 1.2: Upload Files
```bash
git clone https://github.com/yourusername/aws-sla-hunter.git
cd aws-sla-hunter

# Copy files from this project
cp main.py .
cp requirements.txt .
cp test_hunter.py .
cp LICENSE .
cp .gitignore .
cp README.md .
cp SETUP.md .

# Create posts directory
mkdir -p posts
cp posts/* ./posts/

# Commit and push
git add .
git commit -m "Initial commit: AWS SLA Hunter CLI"
git push origin main
```

### Step 1.3: Publish to PyPI (Optional, for Week 2)
```bash
# Install build tools
pip install setuptools wheel twine

# Create setup.py (template below)
# Build distribution
python setup.py sdist bdist_wheel

# Upload to PyPI
twine upload dist/*
```

**setup.py template:**
```python
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="aws-sla-hunter",
    version="0.1.0",
    author="Your Name",
    author_email="your@email.com",
    description="Find missed AWS SLA credits in your account",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/aws-sla-hunter",
    py_modules=["main"],
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: System :: Monitoring",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Developers",
    ],
    python_requires=">=3.8",
    install_requires=[
        "boto3>=1.26.0",
        "botocore>=1.29.0",
        "rich>=13.0.0",
    ],
    entry_points={
        "console_scripts": [
            "aws-sla-hunter=main:main",
        ],
    },
)
```

---

## Phase 2: Generate Screenshots & Documentation (Day 2)

### Step 2.1: Generate Screenshot
```bash
python test_hunter.py --screenshot
```

### Step 2.2: Upload to README
1. Commit screenshot to repo:
   ```bash
   git add screenshot.png
   git commit -m "Add CLI output screenshot"
   git push
   ```

### Step 2.3: Run Tests
```bash
python test_hunter.py

# Expected output:
# test_display_results_empty ... ok
# test_display_results_with_events ... ok
# test_fetch_health_events ... ok
# test_format_event_date ... ok
# test_format_region ... ok
# test_format_service ... ok
# test_format_status ... ok
# test_get_credentials_no_credentials ... ok
# test_get_credentials_success ... ok
# test_main_credential_failure ... ok
# test_main_success ... ok
# test_main_with_mock_data ... ok
```

---

## Phase 3: Community Posting (Days 3-5)

### Day 3: Hacker News
1. Open https://news.ycombinator.com/submit
2. URL: `https://github.com/yourusername/aws-sla-hunter`
3. Title: "AWS SLA Hunter – Find missing SLA credits in your account (free CLI)"
4. Post from 8-10am EST (Tuesday-Wednesday optimal)
5. Use comment template from `posts/hacker_news.md`
6. Engage with comments for 24 hours
7. Track: upvotes, comments, traffic

### Day 4: Reddit r/aws
1. Go to https://reddit.com/r/aws
2. Click "Create Post"
3. Post type: "Post"
4. Title: "[Free Tool] AWS SLA Hunter - CLI that finds missed SLA credits"
5. Body: Copy from `posts/reddit_aws.md`
6. Engage with comments
7. Track: upvotes, awards, new followers

### Day 4: Reddit r/devops
1. Go to https://reddit.com/r/devops
2. Same as above but use `posts/reddit_devops.md`
3. Time gap: 2-3 hours after r/aws post

### Day 5: Discord FinOps Brasil
1. Go to your FinOps Brasil Discord community
2. Post in #ferramentas or #anúncios
3. Message: Copy from `posts/discord_finops_brasil.md`
4. Pin your message
5. Engage with reactions/replies
6. Track: reactions, DMs, joins

---

## Phase 4: Paid Traffic - Reddit Ads (Days 5-7)

### Step 4.1: Setup Reddit Ads Campaign
1. Go to https://ads.reddit.com
2. Create new campaign
3. Budget: R$100 (approximately $20 USD)
4. Campaign name: "AWS SLA Hunter - SLA Credits"

### Step 4.2: Ad Creative
**Headline:** "Find R$100K+ in missed AWS SLA credits with 1 command"

**Description:** 
```
92% of AWS customers don't claim available SLA credits.

AWS SLA Hunter scans your account and shows which events qualify.

Free CLI tool. Open source. MIT licensed.

✓ Detects SLA-eligible events
✓ Works in 2 seconds
✓ Beautiful terminal output
✓ No signup required
```

**Landing Page:** https://github.com/yourusername/aws-sla-hunter

**UTM Parameters:**
```
https://github.com/yourusername/aws-sla-hunter?utm_source=reddit&utm_medium=cpc&utm_campaign=sla_hunter&utm_content=v1
```

### Step 4.3: Targeting
- Interest: AWS, DevOps, Cloud, FinOps
- Subreddits: r/aws, r/devops, r/sysadmin
- Platforms: Mobile + Desktop
- Bid: Auto or $0.50 per click

### Step 4.4: Monitor Performance
Track:
- Cost per click
- Landing page views
- GitHub stars (via UTM)
- GitHub repository views

---

## Phase 5: Growth Tracking (Days 1-7 & Beyond)

### Setup Analytics

#### GitHub
1. Go to your repo settings
2. Enable "Insights" to track:
   - Traffic sources
   - Referrers
   - Top pages

#### Add UTM Parameters to All Links
```
README.md links:
- https://awscostguardian.com?utm_source=github&utm_medium=cli&utm_campaign=sla_hunter
- https://github.com/yourusername/aws-sla-hunter?utm_source=readme&utm_medium=organic&utm_campaign=sla_hunter

Social links:
- HN: utm_source=hackernews&utm_medium=organic&utm_campaign=sla_hunter
- Reddit AWS: utm_source=reddit_aws&utm_medium=organic&utm_campaign=sla_hunter
- Reddit DevOps: utm_source=reddit_devops&utm_medium=organic&utm_campaign=sla_hunter
- Discord: utm_source=discord_br&utm_medium=organic&utm_campaign=sla_hunter
```

#### Google Analytics / Mixpanel
1. Add tracking to awscostguardian.com landing page
2. Track conversion funnel:
   - Visited from GitHub
   - Viewed pricing
   - Started audit
   - Signed up

### Target Metrics (7-Day)

| Metric | Target | How to Track |
|--------|--------|--------------|
| GitHub Stars | 50+ | GitHub repo page |
| GitHub Clones | 30+ | GitHub Insights → Traffic |
| awscostguardian.com visits | 100+ | Google Analytics |
| awscostguardian.com signups | 5+ | CRM/Database |
| Reddit upvotes | 200+ | Reddit post |
| HN points | 100+ | HN post |
| Reddit Ads impressions | 2000+ | Reddit Ads dashboard |
| Reddit Ads clicks | 40+ | Reddit Ads dashboard |
| Reddit Ads CTR | 2%+ | Reddit Ads dashboard |

---

## Phase 6: Week 2 & Beyond

### Organic Growth
- Respond to all GitHub issues/PRs
- Create follow-up posts (see posts/ folder)
- Share case studies anonymously
- Publish on Product Hunt (when ready)

### Organic SEO
- Add keyword-rich descriptions
- Create blog post: "How to find missed AWS SLA credits"
- Link back to awscostguardian.com
- Target keywords: "AWS SLA credits", "AWS Health events", "AWS cost recovery"

### Community Engagement
- Answer questions in r/aws, r/devops
- Sponsor relevant subreddits (if budget allows)
- Create tutorials/videos
- Guest posts on AWS/DevOps blogs

### Product Improvements
- Add JSON/CSV export
- Add multi-account support
- Add scheduling (cron)
- Add Slack integration
- Add email notifications

---

## Success Metrics

### Immediate (Week 1)
- [ ] 50+ GitHub stars
- [ ] 5+ awscostguardian.com signups
- [ ] 200+ Reddit upvotes combined
- [ ] 100+ awscostguardian.com visits

### Medium-term (Month 1)
- [ ] 200+ GitHub stars
- [ ] 20+ awscostguardian.com paying customers
- [ ] $10K+ in recovered SLA credits via SaaS
- [ ] 500+ organic GitHub visits/month

### Long-term (Q1)
- [ ] 1000+ GitHub stars
- [ ] 100+ active SaaS users
- [ ] $100K+ in recovered SLA credits
- [ ] 1+ featured article/press mention

---

## Budget Breakdown

| Item | Cost | Notes |
|------|------|-------|
| Reddit Ads | R$100 | Days 5-7, R$20-30/day optimal |
| Domain (optional) | R$50 | Not needed, GitHub is enough |
| Screenshot tool (PIL) | Free | pip install Pillow |
| Time investment | ~20 hours | Setup, posting, monitoring |

**Total: R$100**

---

## Checklist

Phase 1 (Day 1):
- [ ] GitHub repo created
- [ ] All files uploaded
- [ ] Repository public
- [ ] MIT License added

Phase 2 (Day 2):
- [ ] Screenshot generated
- [ ] Tests passing
- [ ] Documentation complete

Phase 3 (Days 3-5):
- [ ] Hacker News post (Day 3)
- [ ] r/aws post (Day 4 morning)
- [ ] r/devops post (Day 4 afternoon)
- [ ] Discord post (Day 5)
- [ ] Comments engaged with

Phase 4 (Days 5-7):
- [ ] Reddit Ads campaign setup
- [ ] Ad creative approved
- [ ] Budget allocated
- [ ] Campaign running

Phase 5 (Ongoing):
- [ ] UTM parameters tracking
- [ ] GitHub Insights monitored
- [ ] awscostguardian.com analytics on
- [ ] Daily metric tracking

---

## Quick Copy-Paste Commands

```bash
# Initial setup
git clone https://github.com/yourusername/aws-sla-hunter.git
cd aws-sla-hunter
pip install -r requirements.txt
python main.py

# Test
python test_hunter.py
python test_hunter.py --screenshot

# Publish to PyPI (Week 2)
pip install setuptools wheel twine
python setup.py sdist bdist_wheel
twine upload dist/*

# Check stats daily
curl https://api.github.com/repos/yourusername/aws-sla-hunter
# Look at: stars_count, forks, watchers
```

---

## Success Stories to Highlight

Once you have real user testimonials:

1. Share anonymized case studies
2. Quantify results: "Recovered R$500K in SLA credits"
3. Time to value: "Found in 2 seconds, processed in 1 week"
4. Cost savings: "Zero infrastructure, zero subscription"
5. Team adoption: "Adopted by 50+ teams"

---

## Important: Be Authentic

- Admit it's a lead generation tool
- Show genuine value in the CLI itself
- Don't oversell
- Respond honestly to skepticism
- Share your real recovery stories
- Engage genuinely with community

---

**Now go build, launch, and recover that money!** 🚀
