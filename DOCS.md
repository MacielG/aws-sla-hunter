# Documentation Map

Quick reference to find what you need.

## I Want To...

| Goal | File |
|------|------|
| **Understand the project** | [README.md](README.md) |
| **Get started quickly** | [SETUP.md](SETUP.md) |
| **Setup authentication** | [AUTHENTICATION.md](AUTHENTICATION.md) |
| **Use on free tier** | [FREE_TIER_GUIDE.md](FREE_TIER_GUIDE.md) |
| **Contribute code** | [CONTRIBUTING.md](CONTRIBUTING.md) |
| **Check version history** | [CHANGELOG.md](CHANGELOG.md) |

---

## Core Files

```
aws-sla-hunter/
├── main.py                 # CLI application
├── auth_handler.py         # Authentication module
├── test_hunter.py          # Unit tests
├── test_free_tier.py       # Free tier tests
├── requirements.txt        # Python dependencies
├── README.md              # Start here
├── SETUP.md               # Installation guide
├── AUTHENTICATION.md      # Auth methods
├── FREE_TIER_GUIDE.md     # Free tier options
├── CONTRIBUTING.md        # How to contribute
├── CHANGELOG.md           # Version history
├── LICENSE                # MIT License
├── .gitignore             # Git ignore rules
└── posts/                 # Marketing posts
```

---

## Quick Commands

```bash
# Install and setup
pip install -r requirements.txt
python main.py --setup

# Run the tool
python main.py

# Run tests
python test_hunter.py
python test_free_tier.py
```

---

## Documentation Structure

This project uses **7 core documentation files** to keep things concise and avoid duplication.

### Level 1: Start Here
- **README.md** - Project overview, features, and quick start
- **SETUP.md** - Installation steps and troubleshooting

### Level 2: Configuration
- **AUTHENTICATION.md** - AWS credential setup and auth methods
- **FREE_TIER_GUIDE.md** - Options for users without Business Support

### Level 3: Development
- **CONTRIBUTING.md** - Contributing guidelines and development setup
- **CHANGELOG.md** - Version history and project statistics

### Other
- **DOCS.md** - This file (navigation guide)

---

## What Changed?

**Consolidated from 12 to 7 documentation files:**

| Removed | Merged Into |
|---------|-------------|
| `00_START_HERE.md` | README.md |
| `QUICKSTART.md` | SETUP.md |
| `PROJECT_SUMMARY.md` | README.md + CHANGELOG.md |
| `INDEX.md` | DOCS.md |
| `DEVELOPMENT.md` | CHANGELOG.md |

**Benefits:**
- ✅ No duplicate information
- ✅ Easier to maintain
- ✅ Clearer navigation
- ✅ More concise

---

## Still Need Help?

1. Check the relevant file above
2. Review code comments in main.py
3. Open an issue on GitHub
4. See [CONTRIBUTING.md](CONTRIBUTING.md) for support

---

**Ready to find those missed SLA credits?**

Start with [README.md](README.md) → [SETUP.md](SETUP.md) → `python main.py --setup`
